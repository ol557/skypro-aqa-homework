from selenium.webdriver.common.by import By

class Color:

    def __init__(self, browser):

        self._driver = browser

    def color_zip(self):
        color_zip = self._driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
        return color_zip

    def color_company(self):
        color_company = self._driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")
        return color_company

    def color_job_position(self):
        color_job_position = self._driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
        return color_job_position

    def color_phone_number(self):
        color_phone_number = self._driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
        return color_phone_number

    def color_e_mail(self):
        color_e_mail = self._driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
        print(color_e_mail)
        return color_e_mail

    def color_country(self):
        color_country = self._driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
        return color_country

    def color_city(self):
        color_city = self._driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
        return color_city

    def color_address(self):
        color_address = self._driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
        return color_address

    def color_last_name(self):
        color_last_name = self._driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
        return color_last_name

    def color_first_name(self):
        color_first_name = self._driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
        return color_first_name