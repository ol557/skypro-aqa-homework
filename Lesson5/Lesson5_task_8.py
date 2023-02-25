from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

# переход на сайт
driver.get("http://the-internet.herokuapp.com/login")

search_locator_uername = '#username'
search_locator_password = '#password'
search_locator_login = '.radius'
# поиск элемента по локатору и действия с элементом
search_uername = driver.find_element(By.CSS_SELECTOR, search_locator_uername)
search_uername.send_keys("tomsmith")

search_password = driver.find_element(By.CSS_SELECTOR, search_locator_password)
search_password.send_keys("SuperSecretPassword!")

search_login = driver.find_element(By.CSS_SELECTOR, search_locator_login)
search_login.click()

sleep(5)