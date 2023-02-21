from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

search_locator_add = 'button'
search_add_element = driver.find_element(By.CSS_SELECTOR, search_locator_add)
for click in range(1,6):
    search_add_element.click()

search_locator_delete = '.added-manually'
search_delete = driver.find_elements(By.CSS_SELECTOR, search_locator_add)

print(len(search_delete) - 1)

sleep(5)