from selenium.webdriver.common.by import By

class Buyer:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def first_name(self, first_name):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)

    def last_name(self, last_name):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)

    def postal_code(self, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)

    def go_to_bay(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()