from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
    
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_BUCKET)
        add_button.click()
        self.solve_quiz_and_get_code()
    
    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        alert_name = self.browser.find_element(By.CSS_SELECTOR, "div.alert-success strong").text
        assert product_name == alert_name, f"Product name mismatch: {product_name} != {alert_name}"
    
    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(By.CSS_SELECTOR, "div.alert-info strong").text
        assert product_price == basket_total, f"Price mismatch: {product_price} != {basket_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear"
