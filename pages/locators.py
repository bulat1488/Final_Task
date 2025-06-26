from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    FORM_LOG_ON = (By.ID, "login_form")
    FORM_SIGN_IN = (By.ID, "register_form")

class ProductPageLocators:
    BTN_ADD_BUCKET = (By.CLASS_NAME, "btn-add-to-basket") # кнопка Добавление в корзину
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.product_main h1") # название товара
    ALERT_NAME_PRODUCT = (By.CSS_SELECTOR, "div.alertinner ") # название товара в алерте
    PRICE_PRODUCT = (By.CSS_SELECTOR, "div.product_main") # цена товара
    ALERT_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alert-info strong") # цена товара в алерте
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
