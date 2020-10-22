import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import allure
from webdriver_manager.chrome import ChromeDriverManager
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename="test.log")

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    with allure.step("Запуск браузера"):
        def fin():
            try:
                allure.attach(name=browser.session_id, body=str(browser.desired_capabilities), attachment_type=allure.attachment_type.JSON)
                allure.attach(name="chrome log", body=browser.get_log('browser'), attachment_type=allure.attachment_type.TEXT)
            except TypeError as e:
                logger.error(f'Ошибка: {e}')
            finally:
                with allure.step("Закрываем браузер"):
                    browser.quit()
        request.addfinalizer(fin)
    return browser