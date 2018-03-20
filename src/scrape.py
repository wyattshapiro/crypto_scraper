import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from bs4 import BeautifulSoup
# import requests

COINMARKET_URL = "https://coinmarketcap.com/currencies/"
HEADERS = {'User-Agent': 'Mozilla/5.0'}
START_DATE = "20130428"
END_DATE = "20180319"

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
        url = COINMARKET_URL + coin + "/historical-data/?start=" + START_DATE + "&end=" + END_DATE
        driver = initChromeDriver()
        driver.get(url)
        table_soup = driver.find_element_by_xpath('//*[@id="historical-data"]//table')
        table_html = table_soup.get_attribute('outerHTML')
        table_df = pd.read_html(table_html)[0]
        print(len(table_df))
        driver.close()

        # response = requests.get(url, headers=HEADERS)
        # all_html = BeautifulSoup(response.content, 'lxml')
        # table_html = all_html.find('table')[1]
        # print(len(table_html))
        # table_df = pd.read_html(table_html)

        return True, table_df
    except Exception, e:
        print(e)
        table_df = None
        # driver.close()
        return False, table_df


def writeDF(coin, price_df):
    try:
        output_path = "/Users/wyattshapiro/projects/cloudburst/crypto_data/results/" + coin + "_" + START_DATE + "_" + END_DATE + ".csv"
        price_df.to_csv(output_path, index=False, index_label=False)
        return True
    except Exception, e:
        print(e)
        return False


def run():
    coin_list = ["ethereum", "ripple", "bitcoin"]
    for coin in coin_list:
        print(coin)
        scrape_success, table_df = getCoinHistory(coin)
        print("Scrape success %s" % scrape_success)
        if scrape_success:
            write_success = writeDF(coin, table_df)
            print("Write success %s" % write_success)
        print("-"*30)

if __name__ == "__main__":
    run()
