import urls
from locators.main_page_locators_question import MainPageLocatorsQuestion
from pages.main_page import MainPage


class TestMainPageQuestion:
    def test_first_question_element_and_text_is_visible(self, driver):
        checking_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[0]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[0]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_second_question_element_and_text_is_visible(self, driver):
        checking_text = 'Пока что у нас так: один заказ — один самокат. ' \
                        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[1]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[1]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_third_question_element_and_text_is_visible(self, driver):
        checking_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[2]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[2]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_fourth_question_element_and_text_is_visible(self, driver):
        checking_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[3]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[3]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_fifth_question_element_and_text_is_visible(self, driver):
        checking_text = 'Пока что нет! ' \
                        'Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[4]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[4]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_sixth_question_element_and_text_is_visible(self, driver):
        checking_text = 'Самокат приезжает к вам с полной зарядкой. ' \
                        'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. ' \
                        'Зарядка не понадобится.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[5]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[5]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_seventh_question_element_and_text_is_visible(self, driver):
        checking_text = 'Да, пока самокат не привезли. ' \
                        'Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[6]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[6]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)

    def test_eighth_question_element_and_text_is_visible(self, driver):
        checking_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        response = MainPageLocatorsQuestion.RESPONSES_QUESTIONS[7]
        button = MainPageLocatorsQuestion.QUESTIONS_BUTTONS[7]

        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)
