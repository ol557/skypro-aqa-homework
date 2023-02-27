from selenium.webdriver.common.by import By

class Product:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(15)

    def sauce_labs_backpack(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    
    def sauce_labs_bolt_t_shirt(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

    def sauce_labs_onesie(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()



    