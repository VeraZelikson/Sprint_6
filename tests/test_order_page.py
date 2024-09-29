import allure
from conftest import driver
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data import *
import pytest


class TestOrderPageOrder:
    @allure.title('Проверка оформления заказа')
    @allure.description('Проверка оформления заказа из двух точек входа')
    @pytest.mark.parametrize('button, test_data', [(MainPageLocators.ORDER_BUTTON_IN_HEADER, TestData.TEST_USER1),
                                                   (MainPageLocators.ORDER_BUTTON_IN_MAIN, TestData.TEST_USER2)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_element(button)
        order_page.click_on_element(button)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_displaying_of_button_check_status_of_order()