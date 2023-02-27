from selenium.webdriver.common.by import By

class Pole:
    def __init__(self, browser):

        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(5)
        

    def first_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(name)

    def last_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(name)

    def address(self, address):
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)

    def zip(self, zip):
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip)

    def city(self, city):
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)

    def country(self, country):
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)

    def mail(self, mail):
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(mail)

    def phone(self, phone):
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)

    def job(self, job):
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job)

    def company(self, company):
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)

    
        

    def click(self):
        self._driver.find_element(By.CSS_SELECTOR, "button.btn").click()