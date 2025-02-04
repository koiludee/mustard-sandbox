from conftest import driver
from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

def test_home_grid_product_quantity(driver):
        base_page = BasePage(driver)
        home_page = HomePage(driver)
        base_page.home_open()
        base_page.wait_for_element(By.CSS_SELECTOR, '.card-block')
        home_page.check_grid_product_qty(9)




