from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

# переход на сайт
driver.get("http://the-internet.herokuapp.com/inputs")

search_locator_inputs = 'input[type="number"]'
# поиск элемента по локатору
search_inputs = driver.find_element(By.CSS_SELECTOR, search_locator_inputs)
# действия с элементом
search_inputs.send_keys("1000")

search_inputs.clear()

search_inputs.send_keys("SkyPro")

sleep(5)
