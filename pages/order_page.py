from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData
import allure


class OrderPage(BasePage):
    @allure.step('Клик по дропдауну станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.METRO_STATION)

    @allure.step('Ввод даты заказа в поле "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.FIELDS_DATE).send_keys(TestData.TEST_USER1[5])

    @allure.step('Клик по выбранной дате в календаре в поле "Когда привезти самокат"')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.CALENDAR_ITEM)

    @allure.step('Проверка отображения кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_of_element(OrderPageLocators.BUTTON_VIEW_STATUS)

    @allure.step('Заполнить первую часть формы и нажать кнопку "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.FIELDS_NAME)
        self.click_on_element(OrderPageLocators.FIELDS_NAME)
        self.send_keys_to_input(OrderPageLocators.FIELDS_NAME, test_data[0])
        self.click_on_element(OrderPageLocators.FIELDS_SURNAME)
        self.send_keys_to_input(OrderPageLocators.FIELDS_SURNAME, test_data[1])
        self.click_on_element(OrderPageLocators.FIELDS_ADDRESS)
        self.send_keys_to_input(OrderPageLocators.FIELDS_ADDRESS, test_data[2])
        self.click_on_element(OrderPageLocators.METRO_STATION)
        self.send_keys_to_input(OrderPageLocators.METRO_STATION, test_data[3])
        self.click_on_element(OrderPageLocators.SELECT_ITEM_IN_DROPDOWN_METRO)
        self.click_on_element(OrderPageLocators.FIELD_PHONE)
        self.send_keys_to_input(OrderPageLocators.FIELD_PHONE, test_data[4])
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнить вторую часть формы и окно подтверждения')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.FIELDS_DATE)
        self.click_on_element(OrderPageLocators.FIELDS_DATE)
        self.send_keys_to_input(OrderPageLocators.FIELDS_DATE, test_data[5])
        self.click_on_element(OrderPageLocators.COLOR_SAMOKATO)
        self.click_on_element(OrderPageLocators.RENTAL_TERM)
        self.click_on_element(OrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.COMMENT)
        self.send_keys_to_input(OrderPageLocators.COMMENT, test_data[6])
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.wait_visibility_of_element(OrderPageLocators.YES_PLACE_ORDER)
        self.click_on_element(OrderPageLocators.YES_PLACE_ORDER)
