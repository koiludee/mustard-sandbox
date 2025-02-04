from conftest import driver
from pages.base_page import BasePage
from pages.cart_page import CartPage, place_order_button


def test_order_place_button_visible(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()
    assert cart_page.order_place_button_is_displayed()