from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='login-username'].form-control")
    LOGIN_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='login-password'].form-control")
    REGISTER_EMAIL_FORM = (By.CSS_SELECTOR, "input[name='registration-email'].form-control")
    REGISTER_PASSWORD_FORM = (By.CSS_SELECTOR, "input[name='registration-password1'].form-control")
    REGISTER_PASSWORD_CONFIRM_FORM = (By.CSS_SELECTOR, "input[name='registration-password2'].form-control")
    REGISTER_CLICK_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.alert > div > p:nth-child(1) > strong")
    BASKET_COST = (By.CSS_SELECTOR, "div.alertinner > p > strong")



