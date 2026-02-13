import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Кликнуть по элементу")
    def click(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("JS-клик по элементу")
    def js_click(self, element):
         self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Найти элемент")
    def find(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы")
    def find_all(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Ожидание видимости элемента")
    def wait_for_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_not_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))


    @allure.step("Ожидание увеличения текста")
    def wait_for_text_greater_then(self, locator, value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: int(self.find(locator).text.strip()) > value
        )

    @allure.step("Ожидание появления заказа в списке")
    def wait_for_order_in_list(self, locator, order_number, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: order_number in [e.text.strip() for e in self.find_all(locator, timeout=20)]
        )

    @allure.step("Проверка видимости элемента")
    def is_visible(self, locator, timeout=20):
        try:
            self.wait_for_visible(locator, timeout)
            return True
        except TimeoutException:
            return False


    @allure.step("Прокрутка к элементу")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)


    @allure.step("Ожидание элемента и прокрутка")
    def wait_for_visible_and_scroll(self, locator, timeout=30):
        element = self.wait_for_visible(locator, timeout)
        self.scroll_into_view(element)
        return element


    @allure.step("Очистить поле ввода")
    def clear_input(self, locator):
        element = self.find(locator)
        element.clear()

    @allure.step("Безопасный клик с ожиданием overlay")
    def safe_click(self, locator):
        self.wait_for_overlay_disappear()
        element = self.find(locator)
        self.scroll_into_view(element)
        self.js_click(element)


    @allure.step("Ожидание исчезновения элемента")
    def wait_for_element_disappear(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
    def wait_for_overlay_disappear(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(MainPageLocators.ORDER_LOADING_MODAL)
            )
        except TimeoutException:
            pass

    @allure.step("Проверка состояния overlay")
    def check_overlay_start(self, state="visible", timeout=10):
        if state == "visible":
            return self.wait_for_visible(MainPageLocators.ORDER_LOADING_MODAL, timeout)
        else:
            return self.wait_for_not_visible(MainPageLocators.ORDER_LOADING_MODAL, timeout)


    @allure.step("Получить локатор overlay")
    def get_overlay_locator(self):
        return MainPageLocators.ORDER_LOADING_MODAL


    @allure.step("Перемещение элемента (drag and drop)")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find(source_locator)
        target = self.find(target_locator)
        ActionChains(self.driver).drag_and_drop(source, target).perform()



    @allure.step("Закрытие overlay (если присутствует)")
    def close_overlay_if_present(self):
        overlay_locator = MainPageLocators.ORDER_LOADING_MODAL
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(overlay_locator))
            return
        except TimeoutException:
            pass
        try:
            overlay = self.driver.find_element(*overlay_locator)
            self.js_click(overlay)
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(overlay_locator)
            )
        except Exception:
            pass



















