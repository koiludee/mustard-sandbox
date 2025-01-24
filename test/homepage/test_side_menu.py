from webbrowser import Chrome

import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

def test_home_grid_product_quantity():
        driver = webdriver.Chrome()
        page = HomePage(driver)
        page.home_open()
        page.wait_for_element(By.CSS_SELECTOR, '.card-block')
        page.check_grid_product_qty(9)




