import time
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_add_in_basket(browser):
    browser.get(link)
    button = browser.find_element_by_xpath("//button[text()='Добавить в корзину']")
    button.click()
    
    time.sleep(7)
     
    result = find_element_by_xpath("//button[text()=' был добавлен в вашу корзину. ']")