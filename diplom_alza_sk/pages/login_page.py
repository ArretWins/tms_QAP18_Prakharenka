from diplom_alza_sk.pages.base_page import BasePage
from diplom_alza_sk.elements.locators import LoginLocators


class LoginPage(BasePage, LoginLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_that_login_is_opened(self):
        assert self.get_element(self.EMAIL_FIELD)
        assert self.get_element(self.PASSWORD_FIELD)
        assert self.get_element(self.LOGIN_BUTTON)
