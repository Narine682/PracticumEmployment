import time

import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from utils.constants import TEST_EMAIL, TEST_PASSWORD, BASE_URL



@allure.feature("Лента заказов")
class TestOrdersFeed:
    @allure.title("Общий счётчик увеличивается после создания заказа")
    def test_total_counter_updates(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open_url(BASE_URL)
            main_page.check_overlay_start()

        with allure.step("Переходим в Личный кабинет"):
            main_page.click_login_account_button()

        with allure.step("Авторизация пользователя"):
            login_page = LoginPage(driver)
            login_page.login(TEST_EMAIL, TEST_PASSWORD)


        with allure.step("Сохраняем текущее значение общего счётчика"):
            main_page.go_to_orders_feed()
            total_before = feed_page.get_total_count()

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingredient()
            main_page.click_place_an_order()
            order_number = main_page.wait_for_order_number()
            main_page.close_order_modal()

        with allure.step("Проверяем увеличение общего счётчика"):
            main_page.go_to_orders_feed()
            total_after = feed_page.get_total_count()
            assert total_after > total_before, (f"Счётчик не увеличивается: {total_before} {total_after}")

    @allure.title("Счетчик 'Выполнено сегодня' увеличивается после создания заказа")
    def test_today_counter_updates(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)


        with allure.step("Открываем главную страницу"):
             main_page.open_url(BASE_URL)
             main_page.check_overlay_state()

        with allure.step("Переходим в Личный кабинет"):
            main_page.click_login_account_button()

        with allure.step("Авторизуемся"):
            login_page.login(TEST_EMAIL, TEST_PASSWORD)

        with allure.step("Сохраняем текущее значение счётчика 'Выполнено сегодня'"):
             main_page.go_to_orders_feed()
             today_before = feed_page.get_today_count()

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingredient()
            main_page.click_place_an_order()
            order_number = main_page.wait_for_order_number()
            main_page.close_order_modal()

        with allure.step("Проверяем увеличение счётчика 'Выполнено сегодня' "):
             main_page.go_to_orders_feed()
             today_after = feed_page.get_today_count()
             assert today_after > today_before, (
                     f"'Выполнено сегодня' не увеличился: {today_before} {today_after}")


    @allure.title("Новый заказ отображается в блоке 'В работе'")
    def test_order_appears_in_progress(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Открываем страницу и авторизуемся"):
            main_page.open_url(BASE_URL)
            main_page.check_overlay_start()

        with allure.step("Переходим в Личный кабинет"):
            main_page.click_login_account_button()

        with allure.step("Авторизуемся"):
            login_page.login(TEST_EMAIL, TEST_PASSWORD)

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingredient()
            main_page.click_place_an_order()
            old_order_number = "9999"
            order_number = main_page.wait_for_order_number(old_number=old_order_number)
            main_page.close_order_modal()

        with allure.step("Проверяем, что заказ отображается в разделе 'В работе'"):
            main_page.go_to_orders_feed()
            in_progress_numbers = feed_page.get_orders_in_progress_numbers()
            assert any(order_number in num for num in in_progress_numbers), (
                f"Заказ {order_number} не найден в разделе 'В работе'")




