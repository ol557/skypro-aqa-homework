from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

search_locator_bly = '.btn.btn-primary'
search_bly = driver.find_element(By.CSS_SELECTOR, search_locator_bly)

search_bly.click()
driver.refresh()


sleep(5)