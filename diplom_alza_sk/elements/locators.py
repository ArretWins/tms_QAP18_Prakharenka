from selenium.webdriver.common.by import By

class HeaderLocators:
    MAIN_LOGO = (By.XPATH, '//a[@class="header-alz-42"]')
    SEARCH_FIELD = (By.XPATH, '//input[@class="header-alz-401 default-placeholder"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-testid="button-search"]')
    PROFILE_FIELD = (By.XPATH, '//div[@class="header-alz-21 header-alz-34"]')
    CONTEXT_MENU = (By.XPATH, '//div[@class="header-alz-141"]')
    ORDERS = (By.XPATH, '//a[@data-testid="headerOrdersIcon"]')
    BASKET = (By.XPATH, '//a[@data-testid="headerBasketIcon"]')


class OrderLocators:
    SEARCH_ORDER_TEXT = (By.XPATH, '//span[contains(@class,"reactPage-alz-61 reactPage-alz-49")]')
    SEARCH_ORDER_INPUT = (By.XPATH, '//input[contains(@class,"react-page-mnn31 placeholder")]')
    SEARCH_ORDER_BUTTON = (By.XPATH, '//button[@data-testid="searchButton"]')


class OrderLocators:
    SEARCH_ORDER_TEXT = (By.XPATH, '//span[contains(@class,"reactPage-alz-61 reactPage-alz-49")]')
    SEARCH_ORDER_INPUT = (By.XPATH, '//input[contains(@class,"react-page-mnn31 placeholder")]')
    SEARCH_ORDER_BUTTON = (By.XPATH, '//button[@data-testid="searchButton"]')


class BasketLocators:
    BASKET_STEPS = (By.XPATH, '//div[@data-testid="basketSteps"]')
    BASKET_TAB = (By.XPATH, '//div[@class="basketTab"]')
    BACK_TO_MAIN_BUTTON = (By.XPATH, '//a[@class="btnx normal grey arrowedLeft"]')


class ContextMenuLocators:
    CONTEXT_LOGIN = (By.XPATH, '//a[@data-testid="headerNavigationLogin"]')


class LoginLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@id="userName"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@id="btnLogin"]')
