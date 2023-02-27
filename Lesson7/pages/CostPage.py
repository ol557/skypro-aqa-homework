from selenium.webdriver.common.by import By

class Cost:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(5)

    def price(self):
        txt = self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
        return txt
