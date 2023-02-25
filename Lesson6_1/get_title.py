from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://vc.ru")
curent_title = browser.title
print(curent_title)
browser.quit()
