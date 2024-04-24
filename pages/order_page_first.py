import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


class OrderPageFirst(MainPage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_LIST = (By.XPATH, "//input[@placeholder='* Станция метро']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    @allure.step('Заполняем поле Имя')
    def send_first_name(self, first_name):
        input_first_name = self.wait_and_find_element(self.FIRST_NAME)
        input_first_name.send_keys(first_name)

    @allure.step('Заполняем поле Фамилия')
    def send_second_name(self, second_name):
        input_second_name = self.wait_and_find_element(self.SECOND_NAME)
        input_second_name.send_keys(second_name)

    @allure.step('Заполняем поле Адресс')
    def send_address(self, address):
        input_address = self.wait_and_find_element(self.ADDRESS)
        input_address.send_keys(address)

    @allure.step('Заполняем поле Телефон')
    def send_telephone(self, telephone):
        input_telephone = self.wait_and_find_element(self.TELEPHONE)
        input_telephone.send_keys(telephone)

    @allure.step('Вводим название метро')
    def click_and_send_metro_list(self, metro_name):
        open_element = self.wait_and_find_element(self.METRO_LIST)
        open_element.click()
        open_element.send_keys(metro_name)

    @allure.step('Выбираем метро из списка')
    def choose_metro_in_list(self, metro_name):
        choose_metro = self.wait_and_find_element((By.XPATH, f"//div[text()='{metro_name}']"))
        choose_metro.click()

    @allure.step('Нажимаем кнопку \'Далее\'')
    def click_button_next(self):
        button_next = self.wait_and_find_element(self.BUTTON_NEXT)
        button_next.click()
