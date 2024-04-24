import allure
from locators.order_page_first_locators import OrderPageFirstLocators
from pages.main_page import BasePage


class OrderPageFirst(BasePage):
    @allure.step('Заполняем поле Имя')
    def send_first_name(self, first_name):
        self.set_field_argument(OrderPageFirstLocators.FIRST_NAME, first_name)

    @allure.step('Заполняем поле Фамилия')
    def send_second_name(self, second_name):
        self.set_field_argument(OrderPageFirstLocators.SECOND_NAME, second_name)

    @allure.step('Заполняем поле Адресс')
    def send_address(self, address):
        self.set_field_argument(OrderPageFirstLocators.ADDRESS, address)

    @allure.step('Заполняем поле Телефон')
    def send_telephone(self, telephone):
        self.set_field_argument(OrderPageFirstLocators.TELEPHONE, telephone)

    @allure.step('Вводим название метро')
    def click_and_send_metro_list(self, metro_name):
        open_element = self.wait_and_find_element(OrderPageFirstLocators.METRO_LIST)
        open_element.click()
        open_element.send_keys(metro_name)

    @allure.step('Выбираем метро из списка')
    def choose_metro_in_list(self, metro_locator):
        self.click_on_button_wait_of_visible(metro_locator)

    @allure.step('Нажимаем кнопку \'Далее\'')
    def click_button_next(self):
        self.click_on_button_wait_of_visible(OrderPageFirstLocators.BUTTON_NEXT)
