from selenium.webdriver.common.by import By

class Authorization:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(15)

    def username(self, username):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)

    def password(self, password):
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
