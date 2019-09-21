from pages.product_page import PageObject

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = PageObject(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу    
    page.test_add_to_cart()