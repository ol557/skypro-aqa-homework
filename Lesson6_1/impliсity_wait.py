# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()

# driver.get("http://uitestingplayground.com/ajax")
# driver.implicitly_wait(20)

# driver.find_element(By.CSS_SELECTOR, '#ajaxButton').click()
# #content = driver.find_element(By.CSS_SELECTOR, "#content")
# #txt = content.find_element(By.CSS_SELECTOR, '#content > p').text 

# # второй вариант поиска текста
# txt = driver.find_element(By.CSS_SELECTOR, '#content > p').text
# print(txt)


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/progressbar")
driver.find_element(By.CSS_SELECTOR, '#startButton').click()

waiter = WebDriverWait(driver, 40, 0.1)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#progressBar'), '75%'))

driver.find_element(By.CSS_SELECTOR, '#stopButton').click()

print(driver.find_element(By.CSS_SELECTOR, "#result").text)