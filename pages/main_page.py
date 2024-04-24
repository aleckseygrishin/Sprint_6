from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage(BasePage):
    SCOOTER_LOGO_ON_MAIN_PAGE = (By.XPATH, "//a[@href='/']")
    YANDEX_LOGO_ON_DZEN = (By.XPATH, "//a[@href='//yandex.ru']")

    def click_on_button_main_page(self, xpath):
        button_header = self.wait_clickable_and_find_element((By.XPATH, xpath))
        button_header.click()

    def switch_to_any_tab_and_return_current_url(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

        return self.driver.current_url

    def click_on_main_logo_scooter(self):
        button = self.wait_and_find_element(self.SCOOTER_LOGO_ON_MAIN_PAGE)
        button.click()

    def click_on_yandex_logo_on_main_page(self):
        button = self.wait_and_find_element(self.YANDEX_LOGO_ON_DZEN)
        button.click()
