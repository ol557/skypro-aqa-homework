from time import sleep
from selenium import webdriver
browser = webdriver.Chrome()

my_cookie = {
    'name' : "cookie_policy",
    'value' : '1'
}
browser.get("https://labirint.ru")

browser.add_cookie(my_cookie)
browser.refresh()

browser.delete_all_cookies()
browser.refresh()

sleep(5)

browser.quit()