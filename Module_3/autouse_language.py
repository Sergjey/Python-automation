#автоопределение языка интерфейса в хром
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

#автоопределение языка интерфейса в мозилла
fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)