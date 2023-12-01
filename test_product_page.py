import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage


@pytest.mark.parametrize('N', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, N):
    link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{N}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_text_product_after_add()
    page.should_be_text_basket_after_add()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.no_goods_in_basket()
    page.should_be_message_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", "qj3lg0bDL")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.parametrize('N', [i if i != 7 else pytest.param(7, marks=pytest.mark.xfail) for i in range(10)])
    def test_user_can_add_product_to_basket(self, browser, N):
        link = f"https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer{N}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_text_product_after_add()
        page.should_be_text_basket_after_add()
