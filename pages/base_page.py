import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент по локатору')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Проматываем страницу до искомого элемента')
    def wait_clickable_and_find_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

        return element

    @allure.step('Переходим на другую вкладку браузера')
    def switch_to_any_tab_and_wait_url_to_be_correct(self, url):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Проматываем страницу до конца и нажимаем на элемент')
    def scroll_to_end_page_and_find_element(self, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click_on_button_clickable(locator)


    @allure.step('Открываем страницу по url')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Возвращаем текст элемента найденного по локатору')
    def get_text_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Возвращаем текущую ссылку на страницу')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверяем что элемент отображается пользователю')
    def check_is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()

    @allure.step('Нажимаем на найденную кнопку, ожидание по кликабельности')
    def click_on_button_clickable(self, locator):
        button_header = self.wait_clickable_and_find_element(locator)
        button_header.click()

    @allure.step('Нажимаем на найденную кнопку, ожидание по появлению')
    def click_on_button_wait_of_visible(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Заполняем поле переданным значением')
    def set_field_argument(self, locator, argument):
        input_element = self.wait_and_find_element(locator)
        input_element.send_keys(argument)
