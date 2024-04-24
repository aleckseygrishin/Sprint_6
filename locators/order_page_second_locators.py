from selenium.webdriver.common.by import By


class OrderPageSecondLocators:
    DATE_SCOOTER_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_CLICKABLE_ELEMENT = (By.XPATH, "//div[text()='* Срок аренды']/parent::div//span")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_FINISH_ORDER = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_IS_DONE = (By.XPATH, "//div[text()='Заказ оформлен']")
    FIRST_PERIOD_DAY = (By.XPATH, "//div[text()='сутки']")
    SECOND_PERIOD_DAY = (By.XPATH, "//div[text()='семеро суток']")
    COLOR_SCOOTER_BLACK = (By.ID, "black")
    COLOR_SCOOTER_GREY = (By.ID, "grey")
