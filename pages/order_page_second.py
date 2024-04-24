import allure
from locators.order_page_second_locators import OrderPageSecondLocators
from pages.base_page import BasePage


class OrderPageSecond(BasePage):
    @allure.step('Заполняем дату')
    def send_date(self, date):
        self.set_field_argument(OrderPageSecondLocators.DATE_SCOOTER_DELIVERY, date)

    @allure.step('Кликаем по полю период и выбираем необходимый из списка')
    def click_and_select_rental_period(self, period_locator):
        self.click_on_button_wait_of_visible(OrderPageSecondLocators.RENTAL_PERIOD_CLICKABLE_ELEMENT)
        self.click_on_button_wait_of_visible(period_locator)

    @allure.step('Выбираем цвет самоката')
    def choose_color_scooter(self, color_locator):
        self.click_on_button_wait_of_visible(color_locator)

    @allure.step('Заполняем комментарий для курьера')
    def write_comment_for_courier(self, comment):
        self.set_field_argument(OrderPageSecondLocators.COMMENT_FOR_COURIER, comment)

    @allure.step('Нажимаем кнопку \'Заказать\'')
    def click_on_finish_order_button(self):
        self.click_on_button_wait_of_visible(OrderPageSecondLocators.BUTTON_FINISH_ORDER)

    @allure.step('Подтверждаем заказ')
    def click_on_yes_button(self):
        self.click_on_button_wait_of_visible(OrderPageSecondLocators.BUTTON_YES)

    @allure.step('Находим элемент с текстом \'Заказ оформлен\' на тиките успешной регистрации заказа')
    def get_order_is_done_element(self):
        return self.wait_and_find_element(OrderPageSecondLocators.ORDER_IS_DONE)
