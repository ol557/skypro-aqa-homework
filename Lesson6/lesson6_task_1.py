from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")
driver.implicitly_wait(20)

driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
#content = driver.find_element(By.CSS_SELECTOR, "#content")
#txt = content.find_element(By.CSS_SELECTOR, '#content > p').text 

# второй вариант поиска текста
txt = driver.find_element(By.CSS_SELECTOR, '#content > p').text
print(txt)