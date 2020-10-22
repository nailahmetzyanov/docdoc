import allure
from pages.main_page import MainPage

@allure.epic("Врачи")
@allure.feature("Страница выдачи врачей")
@allure.story("Фильтр 'Расписание' на выдаче врачей")
class Test_Doctor():
    @allure.title("Выбор дня")
    def test_select_day(self, browser):
        page = MainPage(browser, url="https://www.docdoc.ru/doctor/")
        page.open()
        page.url_doctor()
        page.doctors_card_10()
        page.filter()
        page.filter_open()
        page.filter_click_tomorrow()
        page.doctors_card_10()
        page.doctors_tomorrow()