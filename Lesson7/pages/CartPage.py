from selenium.webdriver.common.by import By

class Cart:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()