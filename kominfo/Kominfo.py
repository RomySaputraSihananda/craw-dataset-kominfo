from time import perf_counter
from json import dumps
from pyquery import PyQuery
from requests import Session, Response
from itertools import groupby

from concurrent.futures import ThreadPoolExecutor, as_completed

from kominfo.helpers import Parser, Datetime, logging
from kominfo.helpers.Enums import Group, Organisasi

class Kominfo:
    def __init__(self) -> None:
        self.__parser: Parser = Parser()
        self.__datetime: Datetime = Datetime()
        self.__executor: ThreadPoolExecutor = ThreadPoolExecutor()
        self.__BASE_URL: str = 'https://data.kominfo.go.id'
        
        self.__result: dict = {} 
        self.__result['page']: int = None
        self.__result['next_page']: int = None
        self.__result['prev_page']: int = None
        self.__result['date_now']: str = None
        self.__result['data']: list = [] 
        
        self.__requests: Session = Session()
        self.__requests.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3" 
        })
    
    def __filter_data(self, url: str) -> dict:
        response: Response = self.__requests.get(url)
        body: PyQuery = self.__parser.execute(response.text, 'body')

        self.__result['data'].append({
            "judul": self.__parser.execute(body, 'h4.mb-3').text(),
            **{ self.__parser.execute(tr, 'th').text().lower().replace(' ', '_'): self.__datetime.execute(self.__parser.execute(tr, 'td').text()) if i == 3 or i == 4 else self.__parser.execute(tr, 'td').text() for i, tr in enumerate(self.__parser.execute(body, '.table.table-bordered tr'))},
            "datasets": {
                format: [
                    {
                        "judul": self.__parser.execute(dataset, 'div p').text(),
                        "url": self.__parser.execute(dataset, 'span a').attr('href')
                    } for dataset in datasets
                ] for format, datasets in groupby(
                    sorted(
                        self.__parser.execute(body, '.list-group-item.d-flex.justify-content-between.align-items-center'),
                        key=lambda dataset: self.__parser.execute(dataset, 'span:first-child').attr('data-format')
                    ),
                    key=lambda dataset: self.__parser.execute(dataset, 'span:first-child').attr('data-format')
                )
            }
        })

    def search(self, **kwargs) -> None:
        # page: int = 1
        # while(True):
        self.__result['data']: list = [] 
        response: Response = self.__requests.get(f'https://data.kominfo.go.id/opendata/dataset', params=kwargs)
        
        if(response.status_code != 200): return logging.warning(f'error to fetch with code [{response.status_code}]')
        cards: PyQuery = self.__parser.execute(response.text, '.d-flex.align-content-center.mb-3.list-wrap.p-3.cs-rounded-md.cs-bg-light')

        if(not cards): return logging.warning('page not contain datasets')

        logging.info(f'proccess page {kwargs.get("page")}')

        pagination: PyQuery = self.__parser.execute(response.text, '.pagination') 

        self.__result['date_now']: str = self.__datetime.now()
        self.__result['page']: int = kwargs.get('page')
        self.__result['prev_page']: int = int(self.__parser.execute(pagination, '.page-item:first-child a').attr('href').split('=')[-1]) if self.__parser.execute(pagination, '.page-item:first-child a') else None
        self.__result['next_page']: int = int(self.__parser.execute(pagination, '.page-item:last-child a').attr('href').split('=')[-1]) if self.__parser.execute(pagination, '.page-item:last-child a') else None

        # print(self.__parser.execute(pagination, 'li:first-child'))

        urls: list = [self.__BASE_URL + self.__parser.execute(card, 'a:first-child').attr('href') for card in cards] 

        futures: list = [self.__executor.submit(self.__filter_data, url) for url in urls]
        
        for future in as_completed(futures):
            future.result()

        return self.__result

            # page += 1

# testing
if(__name__ == '__main__'):
    start: float = perf_counter()
    kominfo: Kominfo = Kominfo()
    kominfo.search()
    kominfo.search(q='pendidikan')
    kominfo.search(groups=Group.ALAT_DAN_PERANGKAT.value)
    kominfo.search(org=Organisasi.BADAN_PENELITIAN_DAN_PENGEMBANGAN_SUMBER_DAYA_MANUSIA.value)
    logging.info(perf_counter() - start)