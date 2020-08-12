from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажать кнопку отправки анкеты
    button = browser.find_element_by_tag_name("button")
    button.click()

    #принять confirm
    confirm = browser.switch_to.alert.accept()
    #confirm.accept()

    #находим цифру и считаем
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    #находим поле и вписываем ответ
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)

    #нажать кнопку отправки анкеты
    button = browser.find_element_by_tag_name(".btn")#через button не вышло
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
