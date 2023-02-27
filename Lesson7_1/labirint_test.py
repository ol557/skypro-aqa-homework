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



def test_card_counter():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    #waiter = WebDriverWait(driver, 10)
    
    #перейти на сайт лабиринт
    driver.get("https://www.labirint.ru/")
    driver.add_cookie(my_cookie)

    #найти все книги python
    driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys('python')
    driver.find_element(By.CSS_SELECTOR, '#searchform > div.b-search-e-input-wrapper > button').click()

    #изменить вид на таблицу
    driver.find_element(By.CSS_SELECTOR, '#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-view.navisort-part-6.fright > span > a.radioitems-item.view-table').click()
    
    #выбрать все книги
    bay_battons = driver.find_elements(By.CSS_SELECTOR, '.btn.buy-link.btn-primary')
    print('кол-во книг на странице -',len(bay_battons))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))
    counter = 0
    for btn in (bay_battons):
        btn.click()
        counter +=1
    print('количество кликов -', counter)
    
    #перейти в корзину
    driver.get("https://www.labirint.ru/cart/")
    #получить текущее значение книг в корзине
    a = driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]')
    txt = a.find_element(By.CSS_SELECTOR, 'b').text

    #сверить число книг в корзине с числом выбранных книг
    assert counter == int(txt)
    
    driver.quit()
    
    

