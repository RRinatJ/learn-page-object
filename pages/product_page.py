from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage): 
    def test_add_to_cart(self):                
        self.should_be_add_to_cart_button()
        self.click_add_to_cart_button() 
        self.solve_quiz_and_get_code()                 
        self.check_name_of_product() 
        self.check_price_of_product() 
        
    def should_be_add_to_cart_button(self):
        # реализуйте проверку, что есть кнопка добавления заказа
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add to cart button is not presented"   
        
    def click_add_to_cart_button(self):
        # клик по кнопке добавления товара
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_button.click()
    
    def check_name_of_product(self):
        # Проверка названия товара добавленного в корзину        
        self.webdriver_wait_element(5, *ProductPageLocators.MESSAGE_WITH_NAME_PRODUCT)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        message_with_name_product = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_NAME_PRODUCT)        
        assert name_product.text == message_with_name_product.text, "Name in message is wrong!"
        
    def check_price_of_product(self):
        # Проверка цены товара добавленного в корзину        
        self.webdriver_wait_element(5, *ProductPageLocators.MESSAGE_WITH_PRICE_PRODUCT)
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        message_with_price_product = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE_PRODUCT)
        assert price_product.text == message_with_price_product.text, "Price in message is wrong!"