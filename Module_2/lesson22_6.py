from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #находим значение х 
    x_element = browser.find_element_by_css_selector("#input_value")
    #х теперь будет равен ( вносим этот текст в переменную х)
    x = x_element.text
    #считаем формулу функция def (x)
    y = calc(x)

    #проскроллить страницу вниз
    #browser.execute_script("window.scrollBy(0, 150);") - либо так , но тогда надо закомментить другой скролл

    #вписываем ответ в тектсовое поле
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    #альтернативный скролл - либо так либо как выше ( ВАЖНО, если так то именно такая последовательность!
    #если это будет перед вводом текста, то ввод текста собьет скролл
    button = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    #выставляем чекбокс
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    #выставляем радиокнопку
    radio = browser.find_element_by_css_selector("[id='robotsRule']")
    radio.click()

    #нажать кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
