import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    # Настройка опций Chrome
    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': user_language
    })

    print(f"\nstart chrome browser with {user_language} language..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
