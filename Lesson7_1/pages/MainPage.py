from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.labirint.ru/")
        self.driver.implicitly_wait(5)



    def set_cookie_policy(self):
        cookie = {
        'name' : "cookie_policy",
        'value' : '1'
        }
        self.driver.add_cookie(cookie)

    def search(self, tern):
        self.driver.find_element(By.CSS_SELECTOR, '#search-field').send_keys(tern)
        self.driver.find_element(By.CSS_SELECTOR, '#searchform > div.b-search-e-input-wrapper > button').click()