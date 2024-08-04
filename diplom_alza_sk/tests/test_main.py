from diplom_alza_sk.elements import HeaderElement
from diplom_alza_sk.pages.basket_page import BasketPage
from diplom_alza_sk.pages.login_page import LoginPage
from diplom_alza_sk.pages.main_page import MainPage
from diplom_alza_sk.pages.order_page import OrdersPage


def test_open_website(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()


def test_open_orders(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_orders()

    orders_page = OrdersPage(driver)
    orders_page.assert_that_orderspage_is_opened()


def test_open_basket(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    header_element = HeaderElement(driver)
    header_element.open_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_that_basket_is_opened()


def test_context_menu(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()


def test_login(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_that_mainpage_is_opened()

    main_page.assert_context()
    header_element = HeaderElement(driver)
    header_element.open_login()

    login_page = LoginPage(driver)
    login_page.assert_that_login_is_opened()
