from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_button_main_page(self, xpath):
        button_header = self.wait_clickable_and_find_element((By.XPATH, xpath))
        button_header.click()

