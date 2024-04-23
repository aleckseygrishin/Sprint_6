from selenium.webdriver.common.by import By
from pages.order_page_first import OrderPageFirst


class OrderPageSecond(OrderPageFirst):
    DATE_SCOOTER_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_CLICKABLE_ELEMENT = (By.XPATH, "//div[text()='* Срок аренды']/parent::div//span")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_FINISH_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_IS_DONE = (By.XPATH, "//div[text()='Заказ оформлен']")

    def send_date(self, date):
        input_first_name = self.wait_and_find_element(self.DATE_SCOOTER_DELIVERY)
        input_first_name.send_keys(date)

    def click_and_select_rental_period(self, period_day):
        rental_period_click = self.wait_and_find_element(self.RENTAL_PERIOD_CLICKABLE_ELEMENT)
        rental_period_click.click()

        rental_period_choose_date = self.wait_and_find_element((By.XPATH, f"//div[text()='{period_day}']"))
        rental_period_choose_date.click()

    def choose_color_scooter(self, color):
        color_scooter = self.wait_and_find_element((By.ID, f"{color}"))
        color_scooter.click()

    def write_comment_for_courier(self, comment):
        input_comment = self.wait_and_find_element(self.COMMENT_FOR_COURIER)
        input_comment.send_keys(comment)

    def click_on_finish_order_button(self):
        button_order = self.wait_and_find_element(self.BUTTON_FINISH_ORDER)
        button_order.click()

    def click_on_yes_button(self):
        button_yes = self.wait_and_find_element(self.BUTTON_YES)
        button_yes.click()

    def get_order_is_done_element(self):
        return self.wait_and_find_element(self.ORDER_IS_DONE)
