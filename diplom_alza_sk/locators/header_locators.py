from selenium.webdriver.common.by import By


class HeaderLocators:
    MAIN_LOGO = (By.XPATH, '//a[@class="header-alz-42"]')
    SEARCH_FIELD = (By.XPATH, '//input[@class="header-alz-401 default-placeholder"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-testid="button-search"]')
    PROFILE_FIELD = (By.XPATH, '//div[@class="header-alz-21 header-alz-34"]')
    CONTEXT_MENU = (By.XPATH, '//div[@class="header-alz-141"]')
    ORDERS = (By.XPATH, '//a[@data-testid="headerOrdersIcon"]')
    BASKET = (By.XPATH, '//a[@data-testid="headerBasketIcon"]')