from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys('Иван')
driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys('Петров')
driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys('Ленина, 55-3')
driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys('Москва')
driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys('Россия')
driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys('QA')
driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, "button.btn").click()
sleep(3)

first_name = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("color")
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('color')
address = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('color')
city = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('color')
country = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('color')
company = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('color')
job_position = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('color')
e_mail = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('color')
phone_number = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('color')
zip_code = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('color')

print(first_name, zip_code)
def test_red():
   assert zip_code == "rgba(132, 32, 41, 1)"

@pytest.mark.parametrize('per, color', [(company, "rgba(15, 81, 50, 1)"),
(job_position, "rgba(15, 81, 50, 1)"),
(first_name, "rgba(15, 81, 50, 1)"),
(last_name, "rgba(15, 81, 50, 1)"),
(address, "rgba(15, 81, 50, 1)"),
(city, "rgba(15, 81, 50, 1)"),
(country, "rgba(15, 81, 50, 1)")])

def test_green(per, color):
   assert per == color