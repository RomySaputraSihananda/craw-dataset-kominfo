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
{
  "page": 1,
  "next_page": 2,
  "prev_page": null,
  "date_now": "2024-01-04T15:13:12",
  "data": [
    {
      "judul": "Jumlah Pertukaran Data Stasiun Radio Periode November 2021 hingga September 2022",
      "topik": "Frekuensi Radio",
      "pemilik": "Direktorat Jenderal Sumber Daya dan Perangkat Pos dan Informatika",
      "email_pemilik": "-",
      "dataset_dibuat": "2023-07-28T00:00:00",
      "dataset_diperbarui": "2023-07-28T00:00:00",
      "versi": "-",
      "lisensi": "",
      "datasets": {
        "csv": [
          {
            "judul": "Jumlah Pertukaran Data Stasiun Radio Periode November 2021 hingga September 2022",
            "url": "https://data.kominfo.go.id/warehouse/dataset/f52ce392-cc58-4e4c-949e-c4b1d87fe5e9/resource/ec4bd640-5fd6-4696-b773-8742d8ceaf16/download/jumlah-pertukaran-data-stasiun-radio-periode-november-2021-hingga-september-2022.csv"
          }
        ],
        "xlsx": [
          {
            "judul": "Jumlah Pertukaran Data Stasiun Radio Periode November 2021 hingga September 2022",
            "url": "https://data.kominfo.go.id/warehouse/dataset/f52ce392-cc58-4e4c-949e-c4b1d87fe5e9/resource/230ccf5c-8d73-44dc-a481-62376915ef3a/download/jumlah-pertukaran-data-stasiun-radio-periode-november-2021-hingga-september-2022.xlsx"
          }
        ]
      }
    }
    // more datasets
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
