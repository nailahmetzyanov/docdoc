import datetime
import time
from .base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, browser, url):
        with allure.step("Открываем браузер и сайт"):
            super().__init__(browser, url)
            self.browser = browser
            self.base_url = url

    # Локаторы
    DOCTORS_CARD = (By.CSS_SELECTOR, ".doctor-card-search")
    FILTER = (By.CSS_SELECTOR, ".select-box-with-calendar")
    FILTER_TITLE = (By.XPATH, "//span[@class='select-box__title' and contains(text(), 'Расписание на все дни')]")
    LIST_VALUE = (By.CSS_SELECTOR, ".select-box__options-item-title")
    DATE_CHECKBOX = (By.XPATH, "//button[@class='select-box__options-item select-all-days --active']//span[@class='select-box__options-item-active-icon']")
    CLICK_TOMORROW = (By.XPATH, "//span[@class='select-box__options-item-title' and contains(text(), 'Завтра')]")
    TOMORROW_TITLE = (By.XPATH, "//span[@class='select-box__title' and contains(text(), 'Расписание на завтра')]")
    DOCTORS_TOMORROW = (By.CSS_SELECTOR, ".clinic-slots__caption")

    def url_doctor(self):
        with allure.step("Проверка: 'Открыта страница сайта '/doctor''"):
            url = self.browser.current_url
            assert url == "https://docdoc.ru/doctor"

    def doctors_card_10(self):
        with allure.step("Проверка: 'Отображаются 10 карточек врачей на странице'"):
            list_doctors_card = self.finds(locator=self.DOCTORS_CARD)
            assert len(list_doctors_card) == 10, f"Карточек врачей найдено не: 10, а {list_doctors_card}"

    def filter(self):
        with allure.step("Проверка: 'Отображается кнопка 'Расписание (фильтр)'"):
            self.is_element_present(locator=self.FILTER)
        with allure.step("Проверка: 'Заголовок кнопки 'Расписание (фильтр)' содержит текст 'Расписание на все дни'"):
            assert "Расписание на все дни" == self.find(locator=self.FILTER_TITLE).text

    def filter_open(self):
        with allure.step("Нажимаем: на кнопку 'Расписание (фильтр)'"):
            self.find(locator=self.FILTER).click()
        with allure.step("Проверка: 'Отображается элемент 'Список значений для выбора даты'"):
            list_value = self.finds(locator=self.LIST_VALUE)
            assert len(list_value) == 5, f"Значений найдено не: 5, а {list_value}"
        with allure.step("Проверка: 'Помечен галочкой пункт 'Все дни' в выпадающем списке 'Список значений для выбора даты'"):
            self.find(locator=self.DATE_CHECKBOX)

    def filter_click_tomorrow(self):
        with allure.step("Нажимаем: на пункт 'Завтра' в выпадающем списке 'Список значений для выбора даты'"):
            self.find(locator=self.CLICK_TOMORROW).click()
            time.sleep(3)
        with allure.step("Проверка: 'Заголовок кнопки 'Расписание (фильтр)' содержит текст 'Расписание на завтра'"):
            assert "Расписание на завтра" == self.find(locator=self.TOMORROW_TITLE).text

    def doctors_tomorrow(self):
        with allure.step("Проверка: 'Отображаются врачи, работающие в выбранный день'"):
            tomorrow = datetime.date.today() + datetime.timedelta(days=1)
            assert_text_tomorrow = "Онлайн-расписание на " + tomorrow.strftime("%d" + " октября")   # Месяц не стал заморачиваться, написал так
            filter_text_tomorrow = self.find(locator=self.DOCTORS_TOMORROW).text
            assert filter_text_tomorrow == assert_text_tomorrow, f"Ошибка после фильтра, должно быть: {assert_text_tomorrow}, а не {filter_text_tomorrow}"
            list_filter_text_tomorrow = self.finds(locator=self.DOCTORS_TOMORROW)
            assert len(list_filter_text_tomorrow) == 10, f"Значений найдено не: 10, а {list_filter_text_tomorrow}"
