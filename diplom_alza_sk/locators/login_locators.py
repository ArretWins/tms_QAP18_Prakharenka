from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btnLogin"]')
