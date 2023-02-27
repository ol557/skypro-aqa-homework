from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

from pages.AuthorizationPage import Authorization 
from pages.ProductPage import Product
from pages.CartPage import Cart
from pages.BuyerPage import Buyer
from pages.CostPage import Cost

def test_summa_():
    browser = webdriver.Chrome()
    authorization = Authorization(browser)
    authorization.username('standard_user')
    authorization.password('secret_sauce')
    authorization.login()

    product = Product(browser)
    product.sauce_labs_backpack()
    product.sauce_labs_bolt_t_shirt()
    product.sauce_labs_onesie()
    product.go_to_cart()

    cart = Cart(browser)
    cart.checkout()

    buyer = Buyer(browser)
    buyer.first_name("Oleg")
    buyer.last_name('Proskuryakov')
    buyer.postal_code('123456')
    buyer.go_to_bay()

    cost = Cost(browser)
    all = cost.price()

    assert all == 'Total: $58.29' 

    browser.quit()












