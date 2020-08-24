import pytest
from selenium import webdriver
import time
import math

#для передачи в тест список ссылок в качестве параметров
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    # включаем автоматическое ожидание перед каждой итерацией
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', links)
class TestAnsw():
    def test_input_answ(self, browser, link):
        #запускаем каждую линку и принтим для проверки, что используются разные линки
        browser.get(link)
        print(link)

    #def test_answ(self):
        # считаем формулу, которая должна применяться для каждого нового запуска, т.к. зависит от текущего времени
        answer = str(math.log(int(time.time() + 0.2)))
        #return answer
        print(answer)

        # вписываем текст в поле и принтим ответ который вписываем и ожидаем появление поля
        textarea = browser.find_element_by_css_selector("[class = 'textarea string-quiz__textarea ember-text-area ember-view']")
        textarea.send_keys(answer)
        print(answer)
        # этот тест запустится столько раз, сколько ссылок в links

        #browser.implicitly_wait(5)
        button = browser.find_element_by_class_name("submit-submission")
        button.click()

        message = browser.find_element_by_css_selector("[class='attempt-message_correct']")
        assert message.text

        message2 = browser.find_element_by_css_selector("[class='smart-hints__hint']")
        assert "Correct!" in message2.text

        #pytest -s -v test_lesson3_6_3.py
        # pytest -s test_lesson3_6_3.py