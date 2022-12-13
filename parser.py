from selenium import webdriver
from bs4 import BeautifulSoup


def get_prise(url, tag, name, number=0):
    """"""
    browser = webdriver.Chrome()
    browser.get(url)
    browser.implicitly_wait(3)
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    quotes = soup.find_all(tag, class_=name)
    browser.quit()
    print(quotes[number].text)
    return quotes[number].text


def get_prise_in_int(string):
    """"""
    result = ""
    for char in string:
        if char.isdigit():
            result += char
    return int(result)
