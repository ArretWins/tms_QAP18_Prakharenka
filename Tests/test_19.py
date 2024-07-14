import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.bbc.com/'


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()


def tests_by_xpath(driver):
    driver.get(URL)
    bbc_main_logo = driver.find_element(By.XPATH, '//div[@class="sc-49542412-10 jTsKD"]')
    search_button = driver.find_element(By.XPATH, '//button[@class="sc-49542412-3 sc-49542412-4 ipGSFC eojOvQ"]')
    sing_in_button = driver.find_element(By.XPATH, '//button[@class="sc-238aa436-2 sc-238aa436-5 cUUVqo iPqQVG"]')
    home_button = driver.find_element(By.XPATH, '//a[@class="sc-f116bf72-4 yKcKi"]')
    sport_button = driver.find_element(By.XPATH, '//li[@data-testid="mainNavigationItemStyled"]'
                                                 '/div/a[@href="/sport"]')
    travel_button = driver.find_element(By.XPATH,
                                        '//li[@data-testid="mainNavigationItemStyled"]/div/a[@href="/travel"]')
    first_news = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div[2]/'
                                               'div[1]/div[1]/div[1]/div/a/div/div[2]/div[1]/div/h2')
    second_photo = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div[2]')
    clocks = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/section[1]/div/div[2]/'
                                           'div[1]/div[1]/div[2]/div/a/div/div[2]/div[2]/span[1]')
    only_text = driver.find_element(By.XPATH, '//h2[text()="Only from the BBC"]')

    assert URL in driver.current_url


def tests_by_css(driver):
    driver.get(URL)
    time.sleep(2)

    bbc_main_logo = driver.find_element(By.CSS_SELECTOR, 'div.sc-49542412-10.jTsKD')
    search_button = driver.find_element(By.CSS_SELECTOR, 'button.sc-49542412-3.sc-49542412-4.ipGSFC.eojOvQ')
    sing_in_button = driver.find_element(By.CSS_SELECTOR, 'button.sc-238aa436-2.sc-238aa436-5.cUUVqo.iPqQVG')
    home_button = driver.find_element(By.CSS_SELECTOR, 'a.sc-f116bf72-4.yKcKi')
    sport_button = driver.find_element(By.CSS_SELECTOR, 'li[data-testid="mainNavigationItemStyled"] > div > '
                                                        'a[href="/sport"]')
    travel_button = driver.find_element(By.CSS_SELECTOR, 'li[data-testid="mainNavigationItemStyled"] > div > '
                                                         'a[href="/travel"]')
    first_news = driver.find_element(By.CSS_SELECTOR, '#main-content > article > section:nth-of-type(1) > div '
                                                      '> div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) '
                                                      '> div:nth-of-type(1) > div > a > div > div:nth-of-type(2) '
                                                      '> div:nth-of-type(1) > div > h2')
    second_photo = driver.find_element(By.CSS_SELECTOR, '#main-content > article > section:nth-of-type(1) '
                                                        '> div > div:nth-of-type(2)')
    clocks = driver.find_element(By.CSS_SELECTOR, '#main-content > article > section:nth-of-type(1) > div '
                                                  '> div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) '
                                                  '> div:nth-of-type(2) > div > a > div > div:nth-of-type(2) '
                                                  '> div:nth-of-type(2) > span:nth-of-type(1)')
    only_text = driver.find_element(By.CSS_SELECTOR, '#main-content > article > section:nth-child(2) > div '
                                                     '> div:nth-child(1) > div > h2')

    assert URL in driver.current_url
