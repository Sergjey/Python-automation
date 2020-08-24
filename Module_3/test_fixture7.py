import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

    #
    # @pytest.mark.parametrize('language', ["ru", "en-gb"])
    # class TestLogin:
    #     def test_guest_should_see_login_link(self, browser, language):
    #         link = f"http://selenium1py.pythonanywhere.com/{language}/"
    #         browser.get(link)
    #         browser.find_element_by_css_selector("#login_link")
    #         # этот тест запустится 2 раза
    #
    #     def test_guest_should_see_navbar_element(self, browser, language):
    # # этот тест тоже запустится дважды