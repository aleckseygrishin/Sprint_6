import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажимаем на логотип \'Самокат\'')
    def click_on_main_logo_scooter(self):
        self.click_on_button_wait_of_visible(MainPageLocators.SCOOTER_LOGO_ON_MAIN_PAGE)

    @allure.step('Нажимаем на логотип \'Яндекс\'')
    def click_on_yandex_logo_on_main_page(self):
        self.click_on_button_wait_of_visible(MainPageLocators.YANDEX_LOGO_ON_DZEN)

    @allure.step('Открываем ответ вопрос на главной странице')
    def click_on_question_main_page(self, locator_question):
        self.scroll_to_end_page_and_find_element(locator_question)
