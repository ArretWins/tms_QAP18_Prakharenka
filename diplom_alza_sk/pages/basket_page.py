from diplom_alza_sk.pages.base_page import BasePage
from diplom_alza_sk.locators.basket_locators import BasketLocators


class BasketPage(BasePage, BasketLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_basket_is_opened(self):
        assert self.get_element(self.BASKET_STEPS)
        assert self.get_element(self.BASKET_TAB)
        assert self.get_element(self.BACK_TO_MAIN_BUTTON)
