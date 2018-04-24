# Crypto Price Data scraper

Scrapes historical price data for a crypto currency from CoinMarketCap.

## Installation

Clone the repo onto your machine with the following command:

$ git checkout https://github.com/wyattshapiro/crypto_data.git


## Dependencies

We use Python 2.7 to create the scrapers.

See https://www.python.org/downloads/ for information on download.

We use virtualenv to manage dependencies, if you have it installed you can run
the following commands from the root code directory to create the environment and
activate it:

$ virtualenv venv
$ source venv/bin/activate

See https://virtualenv.pypa.io/en/stable/ for more information.

We use pip to install dependencies, which comes installed in a virtualenv.
You can run the following to install dependencies:

$ pip install -r requirements.txt

See https://pip.pypa.io/en/stable/installing/ for information.

We use ChromeDriver 2.38 to spin up a Chrome browser.

See https://sites.google.com/a/chromium.org/chromedriver/ for more information.


## Config

- BASE_DIR: base directory of program
- HEADERS: headers used in Chrome browser
- COIN: coin you want to scrape
- START_DATE: date you want to start scraping
- END_DATE: date you want to stop scraping
- OUTPUT_PATH: location of file you want to write out data


## Inputs
Configured in src/config.py file

- COIN: coin you want to scrape
- START_DATE: date you want to start scraping
- END_DATE: date you want to stop scraping

## Execution
You can run the following to execute program based on Inputs:

$ cd [path/to/crypto_scraper/dir]
$ python src/scrape.py
