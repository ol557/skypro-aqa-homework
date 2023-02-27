from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
my_cookie = {
    'name' : "cookie_policy",
    'value' : '1'
}

driver = webdriver.Chrome()

def open_labirint():
    #перейти на сайт лабиринт
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(5)
    driver.add_cookie(my_cookie)

def search(tern):
    #найти все книги python
    driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys(tern)
    driver.find_element(By.CSS_SELECTOR, '#searchform > div.b-search-e-input-wrapper > button').click()

def go_table():
    #изменить вид на таблицу
    driver.find_element(By.CSS_SELECTOR, '#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-view.navisort-part-6.fright > span > a.radioitems-item.view-table').click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))

def add_book():
    #выбрать все книги
    bay_battons = driver.find_elements(By.CSS_SELECTOR, '.btn.buy-link.btn-primary')
    counter = 0
    for btn in (bay_battons):
        btn.click()
        counter +=1
    return counter

def go_cart():
    #перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    #получить текущее значение книг в корзине
    a = driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]')
    txt = a.find_element(By.CSS_SELECTOR, 'b').text
    return int(txt)

def close():
    driver.quit()



def test_card_counter():
    open_labirint()
    search('python')
    go_table()
    added = add_book()
    go_cart()
    cart_counter = get_cart_counter()
    close()
    assert added == cart_counter



    
    
   
    
    
    
    

    
    
    
    
    

