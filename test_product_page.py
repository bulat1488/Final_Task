from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
urls = [f"{product_base_link}/?promo=offer{no}"
        if no != 7 else pytest.param(f"{product_base_link}/?promo=offer{no}", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = login_link
        email = str(time.time()) + "@fakemail.org"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, 'bestpasswordever')
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = product_base_link
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = product_base_link
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_match_product_name()
        page.should_match_product_cost()


@pytest.mark.need_review
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_match_product_name()
    page.should_match_product_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket()
