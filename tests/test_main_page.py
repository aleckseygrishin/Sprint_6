import urls
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


class TestMainPage:
    def test_switching_on_main_page_from_order_page_current_url_correct(self, driver):
        switching = MainPage(driver)
        switching.open_page(urls.ORDER_URL)
        switching.click_on_main_logo_scooter()

        assert driver.current_url == urls.MAIN_URL

    def test_switching_on_yandex_dzen_page_current_url_correct(self, driver):
        switching = MainPage(driver)
        switching.open_page(urls.ORDER_URL)
        switching.click_on_yandex_logo_on_main_page()
        check_url = switching.switch_to_any_tab_and_return_current_url(urls.YANDEX_DZEN_URL)

        assert check_url == urls.YANDEX_DZEN_URL
