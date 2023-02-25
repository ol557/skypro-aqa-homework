from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

def make_screen(browser):
    browser.get("https://ya.ru")
    browser.maximize_window
    sleep(5)
    browser.save_screenshot('./ya_'+browser.name+'.png')
    browser.quit()
    # сделать и положить скрин в необходимую папку 
    #browser.save_screenshot('/Users/oleg/Source/Learn/skypro-aqa-homework/Lesson6_1/ya_'+browser.name+'.png')

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
#safari= webdriver.Safari()

make_screen(chrome)
make_screen(firefox)
#make_screen(safari)



