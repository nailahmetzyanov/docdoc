from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure

class BasePage:
    def __init__(self, browser, url=None):
        self.browser = browser
        self.base_url = url

    def open(self):
        with allure.step(f"Переходим на сайт: {self.base_url}"):
            self.browser.maximize_window()
            return self.browser.get(self.base_url)

    def find(self, locator, time=15):
        with allure.step(f"Поиск элемента, {locator}"):
            return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Элемент не найден: {locator}")

    def finds(self, locator, time=15):
        with allure.step(f"Поиск элементов, {locator}"):
            return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator), message=f"Элементы не найдены: {locator}")

    def is_element_present(self, locator, time=15):
        with allure.step(f"Поиск видимых элементов на странице, {locator}"):
            try:
                WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator), message=f"Элемент не найден: {locator}")
            except NoSuchElementException:
                return False
            return True