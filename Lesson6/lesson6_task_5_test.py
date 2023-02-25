from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 46)
  
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys("45")
driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4)").click()
driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning").click()

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), "15")
)

fifteen = driver.find_element(By.CSS_SELECTOR, "#calculator > div.top > div").text

driver.quit()


def test_fifteen():
    assert fifteen == "15"