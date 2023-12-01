from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()

    def should_be_text_product_after_add(self):
        NAME = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        assert self.browser.find_element(*ProductPageLocators.TEXT_AFTER_ADD_PRODUCT).text == \
               f"{NAME} был добавлен в вашу корзину.", "No correct product text"

    def should_be_text_basket_after_add(self):
        PRICE = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        assert self.browser.find_element(*ProductPageLocators.TEXT_AFTER_ADD_BASKET).text == \
               f"Стоимость корзины теперь составляет {PRICE}", "No correct basket text"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "message not disappeared"
