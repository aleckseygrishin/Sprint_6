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

    @allure.step('Проматываем страницу до конца')
    def scroll_to_end_page_and_find_element(self, locator):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.wait_and_find_element(locator)

    @allure.step('Открываем страницу по url')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Возвращаем текст элемента найденного по локатору')
    def get_text_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Проверяем что элемент отображается пользователю')
    def check_is_displayed(self, locator):
        element = self.driver.find_element(*locator)
        return element.is_displayed()
