from selenium.webdriver.common.by import By
from pages.order_page_first import OrderPageFirst


class OrderPageSecond(OrderPageFirst):
    DATE_SCOOTER_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

    def send_date(self, date):
        input_first_name = self.wait_and_find_element(self.DATE_SCOOTER_DELIVERY)
        input_first_name.send_keys(date)

