from time import perf_counter
from json import dumps
from pyquery import PyQuery
from requests import Session, Response
from itertools import groupby

from concurrent.futures import ThreadPoolExecutor

from kominfo.helpers import Parser, logging

class Kominfo:
    def __init__(self) -> None:
        self.__parser: Parser = Parser()
        self.__BASE_URL: str = 'https://data.kominfo.go.id'
        
        self.__result: dict = {} 
        self.__result['page']: int = None
        self.__result['data']: list = [] 
        
        self.__request: Session = Session()
        self.__request.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3" 
        })
    
    def __filter_data(self, url: str) -> dict:
        response: Response = self.__request.get(url)
        self.__result['data'].append({
            'datasets': {
                format_: [
                    {
                        'title': self.__parser.execute(dataset, 'div p').text(),
                        'url': self.__parser.execute(dataset, 'span a').attr('href')
                    } for dataset in datasets
                ] for format_, datasets in groupby(
                    sorted(
                        self.__parser.execute(response.text, '.list-group-item.d-flex.justify-content-between.align-items-center'),
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

            self.__result['page']: int = page

            cards: PyQuery = self.__parser.execute(response.text, '.d-flex.align-content-center.mb-3.list-wrap.p-3.cs-rounded-md.cs-bg-light')

            if(not cards): break

            urls: list = [self.__BASE_URL + self.__parser.execute(card, 'a:first-child').attr('href') for card in cards] 

            with ThreadPoolExecutor() as executor:
                executor.map(self.__filter_data, urls)
            
            
            with open(f'page_{page}.json', 'w') as file:
                file.write(dumps(self.__result, indent=2))

            if(page == 2): break
            page += 1
        executor.shutdown(wait=True)




if(__name__ == '__main__'):
    start: float = perf_counter()
    kominfo: Kominfo = Kominfo()
    kominfo.get_all()
    logging.info(perf_counter() - start)

# search
# by_topik
# by_org
