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

### Get all

```bash
python main.py --page=1 --output=data
```

### By Group

```bash
python main.py --group=DOMAIN --page=1 --output=data
```

### By Organisasi

```bash
python main.py --org=INSPEKTORAT_JENDERAL --page=1 --output=data
```

### Searching

```bash
# get all
python main.py --keyword=pendidikan --page=1 --output=data
# by group
python main.py --keyword=pendidikan --group=POS --page=1 --output=data
# by organisasi
python main.py --keyword=pendidikan --org=DIREKTORAT_JENDERAL_PENYELENGGARAAN_POS_DAN_INFORMATIKA --page=1 --output=data
```

### Flags

| Flag      | Alias |               Description               | Example                    | Default |
| :-------- | :---: | :-------------------------------------: | :------------------------- | :-----: |
| --keyword |  -k   |      keyword to search to the site      | --keyword=war              |  None   |
| --group   |  -g   |      [group](Group.md) of the site      | --group=DOMAIN             |  None   |
| --org     |  -or  | [organisasi](Organisasi.md) of the site | --org=INSPEKTORAT_JENDERAL |  None   |
| --page    |  -p   |         number page of the site         | --page=2                   |    1    |
| --output  |  -o   |          json file output path          | --output=data              |  data   |

## Sample Output

```json

```

## License

This project is licensed under the [MIT License](LICENSE).
