from selenium import webdriver
import os

try: 
    link = "http://suninjuly.github.io/file_input.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    #находим поле first name и заполняем его
    fn = browser.find_element_by_css_selector("[name='firstname']")
    fnn = fn.send_keys("Petr")

    #находим поле last name и заполняем его
    sn = browser.find_element_by_css_selector("[name='lastname']")
    snn = sn.send_keys("Petrov")

    #находим поле email и заполняем его
    em = browser.find_element_by_css_selector("[name='email']")
    emm = em.send_keys("pochta@mail.ru")

    #находим кнопку Обзор для прикрепления файла и прикреепляем файл
    obzor = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson22_8.txt')     # добавляем к этому пути имя файла 
    obzor.send_keys(file_path)

    #нажать кнопку отправки анкеты
    button = browser.find_element_by_tag_name("button")
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
