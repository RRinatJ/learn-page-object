from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")    
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div")
    MESSAGE_WITH_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner > strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_WITH_PRICE_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner > p:nth-child(1) > strong")

class BasePageLocators():	
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
	BASKET_LINK = (By.CSS_SELECTOR, "a[href*='basket']")
	BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
	BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")