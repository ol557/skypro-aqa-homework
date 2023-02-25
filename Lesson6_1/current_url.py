from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://ya.ru")
url = browser.current_url
print(url)
browser.quit()