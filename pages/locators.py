from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "h1 + .price_color")
    TEXT_AFTER_ADD_PRODUCT = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
    TEXT_AFTER_ADD_BASKET = (By.CSS_SELECTOR, ".alert-info div p:nth-child(1)")
    SUCCESS_MESSAGE = TEXT_AFTER_ADD_PRODUCT


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
