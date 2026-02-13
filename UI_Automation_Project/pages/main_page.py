import allure
from locators.locators import MainPageLocators
from locators.locators import FeedPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть страницу")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Нажимаем кнопку 'Личный кабинет'")
    def click_login_account_button(self):
        self.driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()

    @allure.step("Проверить и закрыть оверлей, если он появился")
    def check_overlay_start(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.OVERLAY)
            )
            overlay = self.find(MainPageLocators.OVERLAY)
            self.js_click(overlay)
        except:
            pass


    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        tab = self.wait_for_clickable(MainPageLocators.CONSTRUCTOR_TAB, timeout=30)
        self.js_click(tab)


    @allure.step("Перейти в Ленту заказов")
    def go_to_orders_feed(self):
        tab = self.wait_for_clickable(MainPageLocators.ORDERS_FEED_TAB, timeout=30)
        self.js_click(tab)
        self.wait_for_overlay_disappear()

    @allure.step("Прокрутить к разделу Булки")
    def scroll_to_bun(self):
        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_BUN)


    @allure.step("Прокрутить к разделу Соусы")
    def scroll_to_sauce(self):
        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_SAUCE)

    @allure.step("Прокрутить к разделу Начинки")
    def scroll_to_filling(self):
        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_MAIN)



    @allure.step("Открыть детали ингредиента")
    def open_ingredient(self, locator):
            self.wait_for_visible_and_scroll(locator, timeout=30)
            self.wait_for_clickable(locator, timeout=30).click()
            self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=20)


    @allure.step("Безапасно нажать кнопку 'Оформить заказ'")
    def click_place_an_order_safe(self):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(MainPageLocators.OVERLAY)
        )
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Закрыть окно деталей ингредиента")
    def close_ingredient_modal(self):
        try:
            self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=15)
            close_btn = self.wait_for_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE, timeout=15)
            self.js_click(close_btn)
            self.wait_for_not_visible(MainPageLocators.MODAL_WINDOW, timeout=15)
        except TimeoutException:
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=30)
            except:
                raise AttributeError("Не удалось закрыть модальное окно ингредиента")


    @allure.step("Проверить, что окно ингредиента открыто")
    def is_ingredient_modal_opened(self):
        return self.is_visible(MainPageLocators.MODAL_WINDOW)


    @allure.step("Проверить, что окно ингредиента закрыто")
    def is_ingredient_modal_closed(self):
        return not self.is_visible(MainPageLocators.MODAL_WINDOW)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self, ingredient):
        try:
            counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0

    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        self.close_overlay_if_present()
        bun = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_BUN)
        )
        drop_area = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_DROP_AREA)
        )
        actions = ActionChains(self.driver)
        actions.drag_and_drop(bun, drop_area).perform()

    @allure.step("Создать заказ и получить номер")
    def create_order_and_get_number(self):
        self.add_bun_to_constructor()
        self.click(MainPageLocators.ORDER_BUTTON)
        self.wait_for_visible(MainPageLocators.ORDER_NUMBER)
        order_number = self.find(MainPageLocators.ORDER_NUMBER).text
        self.click(MainPageLocators.ORDER_MODAL_CLOSE)
        return order_number


    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.wait_for_visible(MainPageLocators.ORDER_MODAL, timeout=30)
        btn = self.wait_for_clickable(MainPageLocators.ORDER_MODAL_CLOSE, timeout=30)
        self.js_click(btn)
        self.wait_for_not_visible(MainPageLocators.ORDER_MODAL, timeout=30)


    @allure.step("Проверить, что вкладка Конструктор отображается")
    def is_constructor_tab_displayed(self):
        return  self.is_visible(MainPageLocators.CONSTRUCTOR_TAB)


    @allure.step("Проверить, что вкладка Лента Заказов отображается")
    def is_orders_feed_tab_displayed(self):
        return self.is_visible(MainPageLocators.ORDERS_FEED_TAB)


    def js_drag_and_drop(self, source_locator, target_locator):
            """
            Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
            :param source_locator: Локатор элемента, который нужно перетащить.
            :param target_locator: Локатор элемента, куда нужно перетащить.
            """
            self.find_element_with_wait(source_locator)
            self.find_element_with_wait(target_locator)

            element_from = self.driver.find_element(*source_locator)
            element_to = self.driver.find_element(*target_locator)

            self.driver.execute_script("""
                var source = arguments[0];
                var target = arguments[1];

                var evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);

                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);

                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);

                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                target.dispatchEvent(evt);

                evt = document.createEvent("DragEvent");
                evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                source.dispatchEvent(evt);
            """, element_from, element_to)

    def find_element_with_wait(self, locator, timeout=60):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Перетаскиваем все ингредиенты в конструктор")
    def drag_and_drop_ingredient(self):
        self.close_overlay_if_present()

        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_BUN)
        self.js_drag_and_drop(MainPageLocators.DRAGGABLE_BUN, MainPageLocators.CONSTRUCTOR_DROP_AREA)

        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_MAIN)
        self.js_drag_and_drop(MainPageLocators.DRAGGABLE_SAUCE, MainPageLocators.CONSTRUCTOR_DROP_AREA)

        self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_SECTION_MAIN)
        self.js_drag_and_drop(MainPageLocators.DRAGGABLE_MAIN, MainPageLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Ожидание обновления ингредиента")
    def wait_for_ingredient_update(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d:
                self.get_bun_counter() > 0
            )
        except TimeoutException:
            pass


    @allure.step("Нажимаем кнопку 'Оформить заказ'")
    def click_place_an_order(self):
        try:
            self.wait_for_clickable(MainPageLocators.PLACE_ORDER_BUTTON, timeout=30)
            self.click(MainPageLocators.PLACE_ORDER_BUTTON)
        except Exception as e:
            print(f"Ошибка при нажатии кнопки заказа:{e}")
            raise


    @allure.step('Ожидать номер заказа')
    def wait_for_order_number(self, old_number=None, timeout=30):
        """
        Ждем появления нового номера заказа, который отличается от old_number
        """
        try:
            def check_new_order(drv):
                element = drv.find_element(*MainPageLocators.ORDER_NUMBER)
                if element.text and element.text != old_number:
                    return element.text
                return False
            new_order_number = WebDriverWait(self.driver, timeout).until(check_new_order)
            return new_order_number
        except TimeoutException:
            raise TimeoutException("Не удалось дождаться нового номера заказа")

    @allure.step('Получаем счётчик булки')
    def get_bun_counter(self):
        try:
            bun = self.find(MainPageLocators.INGREDIENT_BUN)
            counter = bun.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0

    @allure.step("Проверить состояние затемняющего оверлея и закрыть его, если нужно")
    def check_overlay_state(self, expected_state="not_visible"):
        try:
            overlay = self.driver.find_element(*MainPageLocators.OVERLAY)
            is_visible = overlay.is_displayed()

            if expected_state == "visible" and not is_visible:
                raise AttributeError("Оверлей должен быть видимым, но его нет")

            if expected_state == "not_visible" and not is_visible:
               self.close_overlay_if_present()

        except Exception:
            if expected_state == "visible":
                raise
