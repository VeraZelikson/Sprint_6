import allure
from conftest import driver
from pages.main_page import MainPage


class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу самоката по клику на лого "Самокат" в хэдере')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.waiting_for_download_parts_of_scooter_logo()
        main_page.click_on_parts_of_the_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзен" по клику на лого "Яндекс"')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.waiting_for_download_part_of_the_Yandex_logo()
        main_page.click_on_part_of_the_Yandex_logo()
        main_page.switch_to_next_tab()
        assert main_page.get_page_title() == 'Дзен'