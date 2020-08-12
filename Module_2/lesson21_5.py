from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим значение х (156)
    x_element = browser.find_element_by_css_selector("#input_value")
    #х теперь будет равен 156 ( вносим этот текст в переменную х)
    x = x_element.text
    #считаем формулу функция def (x)
    y = calc(x)
    
    #вписываем ответ в тектсовое поле
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    #выставляем чекбокс
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    #выставляем радиокнопку
    radio = browser.find_element_by_css_selector("[id='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector(".btn")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
