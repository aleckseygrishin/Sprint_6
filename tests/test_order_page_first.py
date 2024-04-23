import time

import urls
from pages.order_page_second import OrderPageSecond


class TestOrderPage:

    def test(self, driver):
        order = OrderPageSecond(driver)
        order.open_page(urls.ORDER_URL)
        order.send_first_name("Алексей")
        order.send_second_name("Гришин")
        order.send_address("Тамбов")
        order.click_metro_list()
        order.choose_metro_in_list()
        order.send_telephone("89005553535")
        order.click_button_next()
        order.send_date('24.04.2024')
        time.sleep(5)





