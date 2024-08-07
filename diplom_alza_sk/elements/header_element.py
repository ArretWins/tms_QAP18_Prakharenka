from diplom_alza_sk.pages.base_page import BasePage
from diplom_alza_sk.locators.header_locators import HeaderLocators
from diplom_alza_sk.locators.context_menu_locators import ContextMenuLocators


class HeaderElement(BasePage, HeaderLocators, ContextMenuLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_orders(self):
        self.click(self.ORDERS)

    def open_basket(self):
        self.click(self.BASKET)

    def open_login(self):
        self.click(self.CONTEXT_LOGIN)