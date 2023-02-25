from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

#browser.get("https://ya.ru")
#tag = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').tag_name
#print(tag)
#txt = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').text
#print(txt)
#id = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').id
#print(id)
#href = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').get_attribute("href")
#print(href)
#ff = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("font-family")
#print(ff)
#color = browser.find_element(By.CSS_SELECTOR, 'a[title="USD MOEX"]').value_of_css_property("color")
#print(color)
#sleep(1)
#browser.quit()

# browser.get("http://uitestingplayground.com/visibility")
# is_displayed = browser.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# sleep(1)
# print(is_displayed)
# browser.find_element(By.CSS_SELECTOR, '#hideButton').click()
# sleep(1)
# is_displayed = browser.find_element(By.CSS_SELECTOR, '#transparentButton').is_displayed()
# sleep(1)
# print(is_displayed)


# sleep(1)
# browser.quit()

# browser.get("https://demoqa.com/radio-button")
# is_enabled = browser.find_element(By.CSS_SELECTOR, "#yesRadio").is_enabled()
# print(is_enabled)

# is_enabled = browser.find_element(By.CSS_SELECTOR, "#noRadio").is_enabled()
# print(is_enabled)

# browser.quit()

# browser.get("https://the-internet.herokuapp.com/checkboxes")
# cb = browser.find_element(By.CSS_SELECTOR,'input[type=checkbox')
# is_selected = cb.is_selected()
# print(is_selected)

# cb.click()

# is_selected = cb.is_selected()
# print(is_selected)


# browser.get("https://the-internet.herokuapp.com/checkboxes")
# div = browser.find_element(By.CSS_SELECTOR,'#page-footer')
# a = div.find_element(By.CSS_SELECTOR, 'a')
# print(a.get_attribute ("href"))

# browser.get("https://the-internet.herokuapp.com/checkboxes")
# divs = browser.find_elements(By.CSS_SELECTOR,'div')
# l = len(divs)
# print(l)
# div = divs[7]
# sleep(5)
# css_style = div.get_attribute("style")
# print(css_style)

browser.get("https://demoqa.com/browser-windows")
sleep(3)
browser.find_element(By.CSS_SELECTOR, '#tabButton').click()
sleep(3)
browser.close()
sleep(3)
browser.quit()
