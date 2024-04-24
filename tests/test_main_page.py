import allure

import urls
from pages.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка current_url главной страницы')
    @allure.description('Проверяем, что при переходе на главную страницу фактический url == ожидаемому')
    def test_switching_on_main_page_from_order_page_current_url_correct(self, driver):
        switching = MainPage(driver)
        switching.open_page(urls.ORDER_URL)
        switching.click_on_main_logo_scooter()

        assert switching.get_current_url() == urls.MAIN_URL

    @allure.title('Проверка current_url страницы Dzen')
    @allure.description('Проверяем, что при переходе на страницу yandex.dzen фактический url == ожидаемому')
    def test_switching_on_yandex_dzen_page_current_url_correct(self, driver):
        switching = MainPage(driver)
        switching.open_page(urls.ORDER_URL)
        switching.click_on_yandex_logo_on_main_page()
        switching.switch_to_any_tab_and_wait_url_to_be_correct(urls.YANDEX_DZEN_URL)

        assert switching.get_current_url() == urls.YANDEX_DZEN_URL
