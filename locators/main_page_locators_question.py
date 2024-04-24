from selenium.webdriver.common.by import By


class MainPageLocatorsQuestion:
    accordion_heading_id = "accordion__heading-"
    QUESTIONS_BUTTONS = [
        (By.ID, f"{accordion_heading_id}0"),
        (By.ID, f"{accordion_heading_id}1"),
        (By.ID, f"{accordion_heading_id}2"),
        (By.ID, f"{accordion_heading_id}3"),
        (By.ID, f"{accordion_heading_id}4"),
        (By.ID, f"{accordion_heading_id}5"),
        (By.ID, f"{accordion_heading_id}6"),
        (By.ID, f"{accordion_heading_id}7")
    ]

    RESPONSES_QUESTIONS = [
        (By.XPATH, "//div[@id='accordion__panel-0']"),
        (By.XPATH, "//div[@id='accordion__panel-1']"),
        (By.XPATH, "//div[@id='accordion__panel-2']"),
        (By.XPATH, "//div[@id='accordion__panel-3']"),
        (By.XPATH, "//div[@id='accordion__panel-4']"),
        (By.XPATH, "//div[@id='accordion__panel-5']"),
        (By.XPATH, "//div[@id='accordion__panel-6']"),
        (By.XPATH, "//div[@id='accordion__panel-7']")
    ]
