from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "No empty basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "No correct message"
