# election_scrapper

Election_scraper is a Python script designed to scrape the volby.cz website, especially to export the data of the 2017 elections to the Chamber of Deputies - territorial unit (selection of municipalities) to a csv file.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install modules from requirements.txt file eg:.

```bash
pip install requests
```

Copy election_scrapper files from GITHUB to your local folder.

## Usage

```python
py election_scrapper.py arg1 arg2

#arg1
URL to territorial unit from web https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
URL must be in quotes!!!

#arg2
File name.

# result
Script will generate a file to your current path with scrapped content.

#CSV header example
code,location,registered,envelopes,valid, .... party results ...

```

## Contributing

Please do not contribute.

## License

No license required.