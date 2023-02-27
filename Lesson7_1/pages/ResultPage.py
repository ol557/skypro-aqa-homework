from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self, browser):
        self._driver = browser
        
    def switch_to_table(self):
        self._driver.find_element(By.CSS_SELECTOR, '#catalog-navigation > form > div.desktop-subnavigagions-block.only_desc > div:nth-child(1) > div > div > span.navisort-part.navisort-view.navisort-part-6.fright > span > a.radioitems-item.view-table').click()
        WebDriverWait(self._driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table')))

    def add_books(self):
        bay_battons = self._driver.find_elements(By.CSS_SELECTOR, '.btn.buy-link.btn-primary')
        counter = 0
        for btn in (bay_battons):
            btn.click()
            counter +=1
        return counter
    
    def get_empty_result_message(self):
        div = self._driver.find_element(By.CSS_SELECTOR, "div.search-error")
        h1 = div.find_element(By.CSS_SELECTOR, "h1")
        
        return h1.text
