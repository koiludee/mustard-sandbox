from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

place_order_button = (By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_cart(self):
        BasePage.home_open(self)
        HomePage.cart_click()

    def order_place_button_is_displayed(self):
        return BasePage.is_element_visible(self, *place_order_button)