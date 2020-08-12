import math

from selenium import webdriver

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"
browser.get(link)

formula = str(math.ceil(math.pow(math.pi, math.e)*10000))
link2 = browser.find_element_by_link_text(formula)
link2.click()

firstn = browser.find_element_by_name("first_name")
firstn.send_keys("Ivan")

lastn = browser.find_element_by_name("last_name")
lastn.send_keys("Ivanov")

city = browser.find_element_by_class_name("form-control.city")
city.send_keys("Vologda")

country = browser.find_element_by_id("country")
country.send_keys("Russia")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(10)
browser.quit()
