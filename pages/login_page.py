from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "Incorrect url, missing login path!"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.FORM_LOG_ON)
        assert login_form.is_displayed(), "Login form is not displayed"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.FORM_SIGN_IN)
        assert register_form.is_displayed(), "Register form is not displayed"
