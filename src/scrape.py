import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import config as config

COINMARKET_URL = "https://coinmarketcap.com/currencies/"


def initChromeDriver():
    driver = webdriver.Chrome()
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


def writeDF(coin, price_df):
    try:
        price_df.to_csv(path_or_buf=config.OUTPUT_PATH, index=False, index_label=False)
        return True
    except Exception, e:
        print(e)
        return False


def run():
    print("Scraping %s from CoinMarketCap" % config.COIN)
    scrape_success, table_df = getCoinHistory(config.COIN)
    print("Scrape success %s" % scrape_success)
    if scrape_success:
        write_success = writeDF(config.COIN, table_df)
        print("Write success %s" % write_success)
    print("-"*30)


if __name__ == "__main__":
    run()
