from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage

def test_card_counter():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('python')

    result_page = ResultPage(browser)
    result_page.switch_to_table()
    to_be = result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.get()
    as_is = cart_page.get_counter()

    assert as_is == to_be

    browser.quit()

def test_empty_search_result():
    browser = webdriver.Chrome()

    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search('123 qwe asd')

    result_page = ResultPage(browser)
    msg = result_page.get_empty_result_message()

    assert msg == 'Мы ничего не нашли по вашему запросу! Что делать?'

    browser.quit()
    
   
    
    
    
    

    
    
    
    
    

