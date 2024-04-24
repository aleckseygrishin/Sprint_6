import urls
import pytest
from pages.order_page_second import OrderPageSecond
from user_data import UserData


class TestOrderPage:
    @pytest.mark.parametrize('first_name, second_name, place, metro_name, tel_number, '
                             'date, period, color, comment, xpath',
                             [UserData.FIRST_DATA_SET, UserData.SECOND_DATA_SET])
    def test_full_order_path_order_number_assigned(self, driver, first_name, second_name, place, metro_name,
                                                   tel_number, date, period, color, comment, xpath):
        order = OrderPageSecond(driver)
        order.open_page(urls.MAIN_URL)
        order.click_on_button_main_page(xpath)
        order.send_first_name(first_name)
        order.send_second_name(second_name)
        order.send_address(place)
        order.click_and_send_metro_list(metro_name)
        order.choose_metro_in_list(metro_name)
        order.send_telephone(tel_number)
        order.click_button_next()
        order.send_date(date)
        order.click_and_select_rental_period(period)
        order.choose_color_scooter(color)
        order.write_comment_for_courier(comment)
        order.click_on_finish_order_button()
        order.click_on_yes_button()

        assert 'Заказ оформлен' in order.get_order_is_done_element().text
