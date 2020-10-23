import pytest
from selenium import webdriver
import allure
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser(request):
    with allure.step("Запуск браузера"):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
    yield browser
    with allure.step("Закрываем браузер"):
        browser.quit()