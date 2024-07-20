from selenium.webdriver.common.by import By


class BasketLocators:
    BASKET_STEPS = (By.XPATH, '//div[@data-testid="basketSteps"]')
    BASKET_TAB = (By.XPATH, '//div[@class="basketTab"]')
    BACK_TO_MAIN_BUTTON = (By.XPATH, '//a[@class="btnx normal grey arrowedLeft"]')