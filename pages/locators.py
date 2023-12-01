from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASS = (By.ID, "id_registration-password1")
    REGISTER_REP_PASS = (By.ID, "id_registration-password2")
    REG_BTN = (By.CSS_SELECTOR, "#id_registration-redirect_url + button")


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
    BASKET = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner a")
    EMPTY_BASKET = (By.CLASS_NAME, "basket_summary")
