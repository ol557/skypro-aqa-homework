from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


driver = webdriver.Chrome()
driver.implicitly_wait(5)
waiter = WebDriverWait(driver, 10)
  
driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Oleg')
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Proskurykov')
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('123456')

driver.find_element(By.CSS_SELECTOR, '#continue').click()

price = driver.find_element(By.CSS_SELECTOR, '#checkout_summary_container > div > div.summary_info > div.summary_total_label').text
driver.quit()

print(price)

def test_price():
    assert price == 'Total: $58.29'