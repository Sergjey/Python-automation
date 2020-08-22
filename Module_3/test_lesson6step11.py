import unittest
from selenium import webdriver
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

def first(link1):
    browser = webdriver.Chrome()
    browser.get(link1)

    # Ваш код, который заполняет обязательные поля
    First_name = browser.find_element_by_css_selector("[placeholder = 'Input your first name']")
    First_name.send_keys("ivan")

    Second_name = browser.find_element_by_css_selector("[placeholder = 'Input your last name']")
    Second_name.send_keys("Ivanov")

    Email = browser.find_element_by_xpath("//input[contains(@class,'third') and @required]")
    Email.send_keys("emailovich@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt2
    welcome_text = welcome_text_elt.text

class TestFirst(unittest.TestCase):
    def test_first(self):
        first_link = first(link1)
        return first_link
        self.assertEqual(first_link, "Congratulations! You have successfully registered!", "something went wrong")

    def test_second(self):
        second_link = first(link2)
        return second_link
        self.assertEqual(second_link, "Congratulations! You have successfully registered!", 'something went wrong')

if __name__ == "__main__":
    unittest.main()