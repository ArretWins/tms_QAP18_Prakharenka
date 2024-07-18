from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def checkbox(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def input_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.send_keys(text)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def add_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def delete_cookies(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.remove_cookie(cookie)

    def get_cookies(self, name):
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            if cookie['name'] == name:
                return cookie['value']

