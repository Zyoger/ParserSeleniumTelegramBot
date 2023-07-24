from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup


def make_driver() -> Chrome:
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        'source': '''
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
          '''
    })
    return driver


def get_prise(url, tag, name, number=0):
    """Return prise"""
    browser = make_driver()
    browser.get(url)
    #browser.implicitly_wait(3)
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.TAG_NAME, "html")))
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    print(soup)
    quotes = soup.find_all(tag, attrs=name)
    browser.quit()
    return quotes[number].text


def get_prise_in_int(string):
    """Convert str in int"""
    result = ""
    for char in string:
        if char.isdigit():
            result += char
    return int(result)


get_prise("https://www.auchan.ru/catalog/morozhenoe/plombir/", "p", {"class": "css-1bdovxp"})
# <p class="css-1bdovxp">Крем для лица дневной Nivea Care антивозрастной, 100 мл</p>