import allure
import pytest

import urls
from locators.main_page_locators_question import MainPageLocatorsQuestion
from pages.main_page import MainPage
from user_data import UserData


class TestMainPageQuestion:
    @allure.title('Проверка ответа на вопрос на главной странице')
    @allure.description('Проверяем, что ответ на вопрос виден пользователю и фактический текст совпадает с ожидаемым')
    @pytest.mark.parametrize('response, button, checking_text', [
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[0], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[0],
         UserData.QUESTION_CHECKING_TEXT[0]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[1], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[1],
         UserData.QUESTION_CHECKING_TEXT[1]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[2], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[2],
         UserData.QUESTION_CHECKING_TEXT[2]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[3], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[3],
         UserData.QUESTION_CHECKING_TEXT[3]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[4], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[4],
         UserData.QUESTION_CHECKING_TEXT[4]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[5], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[5],
         UserData.QUESTION_CHECKING_TEXT[5]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[6], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[6],
         UserData.QUESTION_CHECKING_TEXT[6]],
        [MainPageLocatorsQuestion.RESPONSES_QUESTIONS[7], MainPageLocatorsQuestion.QUESTIONS_BUTTONS[7],
         UserData.QUESTION_CHECKING_TEXT[7]]
    ])
    def test_first_question_element_and_text_is_visible(self, driver, response, button, checking_text):
        question = MainPage(driver)
        question.open_page(urls.MAIN_URL)
        question.click_on_question_main_page(button)

        assert question.get_text_element(response) == checking_text and question.check_is_displayed(response)
