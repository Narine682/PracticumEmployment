
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthLocators, MainPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    @allure.step("Закрыть overlay если он есть")
    def close_overlay_if_present(self):
        try:
            overlay = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.OVERLAY)
            )
            self.driver.execute_script("arguments[0].click();", overlay)
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(MainPageLocators.OVERLAY)
            )
        except:
            pass
    @allure.step("Открыть форму входа")
    def open_login_form(self):
        try:
            self.click(AuthLocators.LOGIN_BUTTON_AUTH)
        except:
            element = self.find(AuthLocators.LOGIN_BUTTON_AUTH)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.close_overlay_if_present()
        self.open_login_form()

        email_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)

        login_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON_AUTH))
        login_button.click()







