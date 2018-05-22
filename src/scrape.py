import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import config
import sys

COINMARKET_URL = "https://coinmarketcap.com/currencies/"


def initChromeDriver():
    chrome_options = Options()
    if config.HEADLESS:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.wait = WebDriverWait(driver, 10000)
    driver.set_page_load_timeout(100000)
    driver.set_window_size(1024, 1024)
    driver.switch_to_window(driver.current_window_handle)
    driver.implicitly_wait(10)
    return driver


def getCoinHistory(coin):
    try:
        url = COINMARKET_URL + coin + "/historical-data/?start=" + config.START_DATE + "&end=" + config.END_DATE
        driver = initChromeDriver()
        driver.get(url)
        table_soup = driver.find_element_by_xpath('//*[@id="historical-data"]//table')
        table_html = table_soup.get_attribute('outerHTML')
        table_df = pd.read_html(table_html)[0]
        print("Number of days scraped: %s" % len(table_df))
        driver.close()

        return True, table_df
    except Exception, e:
        print(e)
        table_df = None
        driver.close()

        return False, table_df


def writeDF(file_path, price_df):
    try:
        price_df.to_csv(path_or_buf=file_path, index=False, index_label=False)
        return True
    except Exception, e:
        print(e)
        return False


def run():
    args = sys.argv
    if len(args) == 2:
        coin_name = str(args[1]).lower().strip()
    else:
        print('')
        print('Please provide args in the following format:')
        print('python scrape.py [coin_name]')
        print('Where [coin_name] can be "bitcoin", "ripple" etc without quotes')
        print('')
        return

    print("Scraping %s from CoinMarketCap" % coin_name)
    scrape_success, table_df = getCoinHistory(coin_name)
    print("Scrape success? %s" % scrape_success)

    if scrape_success:
        file_path = config.OUTPUT_PATH.replace('[coin_name]', coin_name)
        write_success = writeDF(file_path, table_df)
        print("Write success? %s" % write_success)
    else:
        print('')
        print('Is the coin you provided to the scraper spelled correctly?')
        print('')

    print("-"*30)


if __name__ == "__main__":
    run()
