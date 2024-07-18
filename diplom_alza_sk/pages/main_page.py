import time

from diplom_alza_sk.helpers import BASE_URL
from diplom_alza_sk.pages.base_page import BasePage
from diplom_alza_sk.elements.locators import HeaderLocators


class MainPage(BasePage, HeaderLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def assert_that_mainpage_is_opened(self):
        assert self.get_element(self.MAIN_LOGO)
        assert self.get_element(self.PROFILE_FIELD)
        assert self.get_element(self.BASKET)

    def assert_context(self):
        self.get_element(self.PROFILE_FIELD).click()
        time.sleep(1)
        assert self.get_element(self.CONTEXT_MENU)