import allure
import urls
import pytest

from pages.order_page_first import OrderPageFirst
from pages.order_page_second import OrderPageSecond
from user_data import UserData


class TestOrderPage:
    @allure.title('Проверка полного пути заказа')
    @allure.description('Проверка полного пути заказа до окна с номер заказа. '
                        'Поиск и сравнение элемента с текстом \'Заказ оформлен\'')
    @pytest.mark.parametrize('first_name, second_name, place, metro_name, metro_locator, tel_number, '
                             'date, period, color, comment, button_locator',
                             [UserData.FIRST_DATA_SET, UserData.SECOND_DATA_SET])
    def test_full_order_path_order_number_assigned(self, driver, first_name, second_name,
                                                   place, metro_name, metro_locator, tel_number,
                                                   date, period, color, comment, button_locator):
        order_first_page = OrderPageFirst(driver)
        order_first_page.open_page(urls.MAIN_URL)
        # Проход по первой странице заказа
        order_first_page.click_on_button_clickable(button_locator)
        order_first_page.send_first_name(first_name)
        order_first_page.send_second_name(second_name)
        order_first_page.send_address(place)
        order_first_page.click_and_send_metro_list(metro_name)
        order_first_page.choose_metro_in_list(metro_locator)
        order_first_page.send_telephone(tel_number)
        order_first_page.click_button_next()
        # Проход по второй странице заказа
        order_second_page = OrderPageSecond(driver)
        order_second_page.send_date(date)
        order_second_page.click_and_select_rental_period(period)
        order_second_page.choose_color_scooter(color)
        order_second_page.write_comment_for_courier(comment)
        order_second_page.click_on_finish_order_button()
        order_second_page.click_on_yes_button()

        assert 'Заказ оформлен' in order_second_page.get_order_is_done_element().text
