from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_match_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, f"Product name does not match, should {product_name}, given {added_product_name}"

    def should_match_product_cost(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert product_cost == basket_cost, f"Product cost does not match, should {product_cost}, given {basket_cost}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "Success message is presented, but should not be"
