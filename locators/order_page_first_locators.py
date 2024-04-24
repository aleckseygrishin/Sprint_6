from selenium.webdriver.common.by import By


class OrderPageFirstLocators:
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SECOND_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    TELEPHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    METRO_LIST = (By.XPATH, "//input[@placeholder='* Станция метро']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")
    FIRST_METRO = (By.XPATH, "//div[text()='Сокольники']")
    SECOND_METRO = (By.XPATH, "//div[text()='Митино']")
    HEADER_BUTTON_ORDER = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    BUTTON_ON_MIDDLE_PAGE_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM')]")

