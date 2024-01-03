[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-dataset-kominfo

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GBnPRZmbgAABJA8.jpeg)

Program ini dirancang untuk melakukan web scraping pada situs kominfo dengan memanfaatkan </br>parameter seperti group, keyword, dan organisasi. </br>Tujuan utama dari program ini adalah untuk mengumpulkan informasi dataset dari kominfo sesuai </br>dengan kriteria yang diinputkan oleh pengguna.

## Requirements

- **Python >= 3.11.4**
- **pyquery >= 2.0.0**
- **pytz >= 2023.3.post1**
- **Requests >= 2.31.0**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-dataset-kominfo

# Change Directory
cd craw-dataset-kominfo

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

### By Group

```bash
python main.py --group=news --output=data
```

### By Organisasi

```bash
python main.py --org=news --output=data
```

### Searching

```bash
python main.py --keyword=pendidikan --output=data
python main.py --keyword=pendidikan --category=news --output=data
python main.py --keyword=pendidikan --org=news --output=data
```

### Flags

| Flag        | Alias |             Description             | Example                | Default |
| :---------- | :---: | :---------------------------------: | :--------------------- | :-----: |
| --category  |  -s   | [category](Category.md) of the site | --category=news        |  news   |
| --page      |  -p   |       number page of the site       | --page=2               |    1    |
| --keyword   |  -d   |    keyword to search to the site    | --keyword=war          |  None   |
| --from_date |  -d   |       start date of the site        | --from_date=2023-01-01 |  None   |
| --to_date   |  -d   |        end date of the site         | --to_date=2023-12-18   |  None   |
| --output    |  -o   |        json file output path        | --output=data          |  data   |

## Sample Output

```json

```

## License

This project is licensed under the [MIT License](LICENSE).
