from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        #Переход в корзину
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()    

    def test_guest_cant_see_basket_items(self):
        #Проверяем, что нет товаров в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket items is presented, but should not be"

    def test_guest_see_basket_empty_text(self):
        #Проверяем, что есть сообщение о пустой корзине
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Basket empty text is not presented"
            
    