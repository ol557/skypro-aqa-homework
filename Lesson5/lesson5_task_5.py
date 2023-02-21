from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

search_locator_bly = '.btn-primary'
search_bly = driver.find_element(By.CSS_SELECTOR, search_locator_bly)

search_bly.click()
#нажать кнопку в выбранном URL
#search_bly.send_keys(Keys.RETURN)

# избавиться от выпавшего окна
Alert(driver).accept()

#перегрузить страницу
driver.refresh

search_bly.click()
Alert(driver).accept()
driver.refresh

search_bly.click()
Alert(driver).accept()
driver.refresh

sleep(5)