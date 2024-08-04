# Написать 5 автотестов по примеры ниже, на выбранного вами сайта либо на https://candymapper.com/
# (https://candymapperr2.com/ исправленный сайт)
#
# 1. Открыйть сайт http://thedemosite.co.uk/login.php
# 2. Ввести имя в поле username
# 3. Ввести пароль в поле password
# 4. Нажать на кнопку Test Login
# 5. Проверить, что Successful Login отображаются
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


URL = 'https://candymapper.com/'

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_sign_in_title(driver):
    driver.get(URL)
    x_button = driver.find_element(By.XPATH, '//div[@class="x-el x-el-div c1-1 c1-2 c1-r c1-47 c1-5f c1-5g '
                                             'c1-5d c1-12 c1-u c1-f3 c1-b3 c1-b c1-c c1-d c1-e c1-f c1-g"]').click()
    user_logo = driver.find_element(By.XPATH, '//span[@id="n-238369238407-membership-icon"]')
    user_logo.click()
    sing_in_title = driver.find_element(By.XPATH, '//a[@id="n-238369238407-membership-sign-in"]')
    sing_in_title.click()
    sing_in_button = driver.find_element(By.XPATH, '//button[@data-ux="ButtonPrimary"]')
    assert sing_in_button.is_displayed() is True


def test_create_account(driver):
    driver.get(URL)
    x_button = driver.find_element(By.XPATH, '//div[@class="x-el x-el-div c1-1 c1-2 c1-r c1-47 c1-5f c1-5g '
                                             'c1-5d c1-12 c1-u c1-f3 c1-b3 c1-b c1-c c1-d c1-e c1-f c1-g"]').click()
    user_logo = driver.find_element(By.XPATH, '//span[@id="n-238369238407-membership-icon"]')
    user_logo.click()
    create_account_title = driver.find_element(By.XPATH, '//a[@id="n-238369238407-membership-create-account"]')
    create_account_title.click()
    create_account_button = driver.find_element(By.XPATH, '//button[@data-ux="ButtonPrimary"]')
    assert create_account_button.is_displayed() is True


def test_halloween_party(driver):
    driver.get(URL)
    x_button = driver.find_element(By.XPATH, '//div[@class="x-el x-el-div c1-1 c1-2 c1-r c1-47 c1-5f c1-5g '
                                             'c1-5d c1-12 c1-u c1-f3 c1-b3 c1-b c1-c c1-d c1-e c1-f c1-g"]').click()
    halloween_party_button = driver.find_element(By.XPATH, '//a[@data-tccl="ux2.HEADER.header9.'
                                                           'Nav.Default.Link.Default.238385.click,click"]')
    halloween_party_button.click()
    subtitle = driver.find_element(By.XPATH, '//h6[@data-ux="Details"]')
    assert subtitle.is_displayed() is True


def test_footer_details(driver):
    driver.get(URL)
    x_button = driver.find_element(By.XPATH, '//div[@class="x-el x-el-div c1-1 c1-2 c1-r c1-47 c1-5f c1-5g '
                                             'c1-5d c1-12 c1-u c1-f3 c1-b3 c1-b c1-c c1-d c1-e c1-f c1-g"]').click()
    footer_details = driver.find_element(By.XPATH, '//div[@data-ux="FooterDetails"]')
    assert footer_details.is_displayed() is True


def test_sign_in(driver):
    driver.get(URL)

    x_button = driver.find_element(By.XPATH, '//div[@class="x-el x-el-div c1-1 c1-2 c1-r c1-47 c1-5f c1-5g '
                                             'c1-5d c1-12 c1-u c1-f3 c1-b3 c1-b c1-c c1-d c1-e c1-f c1-g"]').click()
    join_us_button = driver.find_element(By.XPATH, '//a[text()="JOIN US"]').click()
    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
    email_input.send_keys('mawy@mailinator.com')
    password_input = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_input.send_keys('123456aaa')
    sing_in_button = driver.find_element(By.XPATH, '//button[@data-ux="ButtonPrimary"]').click()
    time.sleep(1)
    alert_title = driver.find_element(By.XPATH, '//p[@role="alertdialog"]')
    assert alert_title.is_displayed() is True
