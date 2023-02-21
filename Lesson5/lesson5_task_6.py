from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/entry_ad")

search_locator_close = '#modal > div.modal > div.modal-footer > p'
search_close = driver.find_element(By.CSS_SELECTOR, search_locator_close)
sleep(1)
search_close.click()