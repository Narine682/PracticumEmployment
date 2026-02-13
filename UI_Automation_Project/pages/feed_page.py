import allure
from locators.locators import FeedPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.locators import MainPageLocators

class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Оформить заказ безопасно")
    def click_place_an_order_safe(self):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(FeedPageLocators.ORDER_LOADING_MODAL)
        )
        self.wait_for_clickable(MainPageLocators.PLACE_ORDER_BUTTON).click()
        order_number = self.wait_for_visible(MainPageLocators.ORDER_NUMBER).text
        self.wait_for_clickable(MainPageLocators.ORDER_MODAL_CLOSE).click()


    @allure.step("Получить общее количество выполненных заказов за все время")
    def get_total_count(self):
        try:
            el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedPageLocators.TOTAL_COUNTER)
            )
            return int(el.text) if el.text.strip() else 0
        except Exception as e:
            print(f"Не удалось получить общий счётчик:{e}")
            return 0

    @allure.step("Ожидать увеличения общего количества заказов")
    def wait_for_total_count_increase(self, previous_count):
        WebDriverWait(self.driver, 60).until(
            lambda d: int(self.driver.find_element(*FeedPageLocators.TOTAL_COUNTER).text) > previous_count
        )

    @allure.step("Получить количество заказов за сегодня")
    def get_today_count(self):
        try:
            el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(FeedPageLocators.TODAY_COUNTER)
            )
            return int(el.text) if el.text.strip() else 0
        except Exception as e:
            print(f"Не удалось получить счетчик за сегодня: {e}")
            return 0

    @allure.step("Ожидать увеличения количества заказов за сегодня ")
    def wait_for_today_count_increase(self, previous_count):
        WebDriverWait(self.driver, 60).until(
            lambda d: int(self.driver.find_element(*FeedPageLocators.TODAY_COUNTER).text) > previous_count
        )

    @allure.step("Получить список заказов в процессе выполнения")
    def get_orders_in_progress_numbers(self):
        numbers = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDERS_IN_PROGRESS)
        )
        return [n.text.strip() for n in numbers if n.text.strip()]

    @allure.step("Ожидать появления заказа {order_number} в списке 'В работе'")
    def wait_for_order_in_progress(self, order_number):
        WebDriverWait(self.driver, 60).until(
            lambda d: order_number in self.get_orders_in_progress_numbers()
        )


        