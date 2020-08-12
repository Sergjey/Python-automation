from selenium import webdriver
import time

from selenium.webdriver.support.ui import Select

import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("#num1").text
    #x = ("#num1").int()

    y = browser.find_element_by_css_selector("#num2").text
    #y = ("#num2").int
    
    summa = str(int(x) + int(y))
    print(summa)
    
    dropdwn = Select(browser.find_element_by_tag_name("select"))
    dropdwn.select_by_value(summa)
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

