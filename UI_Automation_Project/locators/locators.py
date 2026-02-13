from selenium.webdriver.common.by import By
class MainPageLocators:
    """Локаторы для главной страницы(Конструктор)"""
    # Кнопки навигации в шапке
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED = (By.LINK_TEXT, "Лента Заказов")
    ORDERS_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
    DRAGGABLE_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a")
    DRAGGABLE_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']/ancestor::a")
    DRAGGABLE_MAIN = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']/ancestor::a")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")




    #  разделы ингредиентов
    INGREDIENT_SECTION_BUN = (By.XPATH, "//h2[text()='Булки']")
    INGREDIENT_SECTION_SAUCE = (By.XPATH, "//h2[text()='Соусы']")
    INGREDIENT_SECTION_MAIN = (By.XPATH, "//h2[text()='Начинки']")

    INGREDIENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")
    INGREDIENT_MAIN = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")

    INGREDIENT_DETAILS_NAME = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    INGREDIENT_PARENT = (By.XPATH, "/..")
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    #  Модальное окна
    MODAL_OPENED_CLASS = "Modal_modal_opened"
    MODAL_WINDOW = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
    INGREDIENT_MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='close']")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//button[contains(text(),'Оформить заказ')]")

    #   Зона конструктора (куда перетаскивают)
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]//ul")
    ORDER_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='close']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_LOADING_MODAL = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")

class FeedPageLocators:
    """Локаторы для страницы Ленты заказов"""

    #   Счётчики в ленте заказов
    ORDER_LOADING_MODAL = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_CARDS = (By.XPATH, "//ul[contains(@class, 'orderList')]/li")
    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[preceding-sibling::p[contains(text(), 'В работе')]]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul/li")



class AuthLocators:
    """Локаторы для авторизации"""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON_AUTH = (By.XPATH, "//button[text()='Войти']")

