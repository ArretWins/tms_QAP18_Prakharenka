from selenium.webdriver.common.by import By


class OrderLocators:
    SEARCH_ORDER_TEXT = (By.XPATH, '//span[contains(@class,"reactPage-alz-61 reactPage-alz-49")]')
    SEARCH_ORDER_INPUT = (By.XPATH, '//input[contains(@class,"react-page-mnn31 placeholder")]')
    SEARCH_ORDER_BUTTON = (By.XPATH, '//button[@data-testid="searchButton"]')
