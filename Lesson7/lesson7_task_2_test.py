from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.CalculatorPage import Calculator

def test_fifteen():
    browser = webdriver.Chrome()
    
    calculator = Calculator(browser)
    calculator.time(45)
    calculator.seven()
    calculator.plus()
    calculator.eigth()
    calculator.equally()

    displey = calculator.displey()

    assert displey =='15'


  




