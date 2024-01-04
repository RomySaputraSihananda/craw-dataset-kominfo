import pytz
from datetime import datetime
class Datetime:
    def execute(self, text: str) -> str:
        try:
            return datetime.strptime(text, "%d %b %Y").strftime("%Y-%m-%dT%H:%M:%S");
        except Exception as e:
            return e;

    def now(self) -> str:
        tz = pytz.timezone("Asia/Jakarta")
        date = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S")
        return date
    
if(__name__ == '__main__'):
    datetime2: Datetime = Datetime()
    date: str = datetime2.execute("28 Jul 2023")
    print(date)