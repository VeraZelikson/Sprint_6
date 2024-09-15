from pages.main_page import MainPage
from conftest import driver
from data import TestData
import pytest
import allure


class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления ожидаемого текста по клику на каждый вопрос')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.EXPECTED_ANSWER_FAQ)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer