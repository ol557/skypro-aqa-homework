from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get("https://ya.ru")
element_search = browser.find_element(By.CSS_SELECTOR, '#text')
element_search.clear()
element_search.send_keys('skypro')
sleep(1)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
sleep(3)
browser.quit()