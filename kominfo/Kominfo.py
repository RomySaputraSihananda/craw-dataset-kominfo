from time import perf_counter
from json import dumps
from pyquery import PyQuery
from requests import Session, Response
from itertools import groupby

from concurrent.futures import ThreadPoolExecutor

from kominfo.helpers import Parser, Datetime, logging
from kominfo.helpers.Enums import Topik, Organisasi

class Kominfo:
    def __init__(self) -> None:
        self.__parser: Parser = Parser()
        self.__datetime: Datetime = Datetime()
        self.__BASE_URL: str = 'https://data.kominfo.go.id'
        
        self.__result: dict = {} 
        self.__result['page']: int = None
        self.__result['date_now']: str = None
        self.__result['data']: list = [] 
        
        self.__request: Session = Session()
        self.__request.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3" 
        })
    
    def __filter_data(self, url: str) -> dict:
        response: Response = self.__request.get(url)
        body: PyQuery = self.__parser.execute(response.text, 'body')

        self.__result['data'].append({
            "judul": self.__parser.execute(body, 'h4.mb-3').text(),
            **{ self.__parser.execute(tr, 'th').text().lower().replace(' ', '_'): self.__parser.execute(tr, 'td').text() for tr in self.__parser.execute(body, '.table.table-bordered tr')},
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

    def get_all(self) -> None:
        page: int = 1
        while(True):
            self.__result['data']: list = [] 
            response: Response = self.__request.get(f'https://data.kominfo.go.id/opendata/dataset?page={page}')
            
            if(response.status_code != 200): return
            cards: PyQuery = self.__parser.execute(response.text, '.d-flex.align-content-center.mb-3.list-wrap.p-3.cs-rounded-md.cs-bg-light')

            if(not cards): break
            
            logging.info(f'proccess page {page}')

            self.__result['date_now']: str = self.__datetime.now()
            self.__result['page']: int = page 

            urls: list = [self.__BASE_URL + self.__parser.execute(card, 'a:first-child').attr('href') for card in cards] 

            with ThreadPoolExecutor() as executor:
                executor.map(self.__filter_data, urls)
            
            
            with open(f'page_{page}.json', 'w') as file:
                file.write(dumps(self.__result, indent=2))

            # if(page == 2): break
            page += 1
        executor.shutdown(wait=True)

    def get_by_topik(self, topik: Topik) -> None:
        page: int = 1
        while(True):
            self.__result['data']: list = [] 
            response: Response = self.__request.get(f'https://data.kominfo.go.id/opendata/dataset?groups={topik.value}&page={page}')
            
            if(response.status_code != 200): return
            cards: PyQuery = self.__parser.execute(response.text, '.d-flex.align-content-center.mb-3.list-wrap.p-3.cs-rounded-md.cs-bg-light')

            if(not cards): break
            
            logging.info(f'proccess page {page}')

            self.__result['date_now']: str = self.__datetime.now()
            self.__result['page']: int = page 

            urls: list = [self.__BASE_URL + self.__parser.execute(card, 'a:first-child').attr('href') for card in cards] 

            with ThreadPoolExecutor() as executor:
                executor.map(self.__filter_data, urls)
            
            
            with open(f'page_{page}.json', 'w') as file:
                file.write(dumps(self.__result, indent=2))

            # if(page == 2): break
            page += 1
        executor.shutdown(wait=True)



if(__name__ == '__main__'):
    start: float = perf_counter()
    kominfo: Kominfo = Kominfo()
    # kominfo.get_all()
    kominfo.get_by_topik(Topik.FREKUENSI_RADIO)
    logging.info(perf_counter() - start)

# search
# by_topik
# by_org
