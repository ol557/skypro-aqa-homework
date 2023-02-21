from time import sleep
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window
driver.get("https://ya.ru")
#driver.get("https://vk.ru")
driver.fullscreen_window()
#for x in range(1, 5):
    #driver.back()
    #driver.forward()
driver.save_screenshot('/Users/oleg/Source/Learn/skypro-aqa-homework/Lesson5/yandex.png')
#driver.set_window_size(640, 360)

sleep(5)