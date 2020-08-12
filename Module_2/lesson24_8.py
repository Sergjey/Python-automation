from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    
    #чтобы убедиться что прайс находит верно и ошибка не здесь
    #print(price)
    
    button = browser.find_element_by_id("book")
    button.click()

    #alert = browser.switch_to.alert
    #alert.accept()

    #скролл вниз к кнопке
    scroll = browser.find_element_by_css_selector("#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", scroll)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #проверка считает ли "y"
    print(y)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
