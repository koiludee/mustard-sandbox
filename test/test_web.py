from conftest import driver
from time import sleep
from pages.homepage import HomePage
from pages.product_content_page import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")

def test_monitor_qty(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitors()
    sleep(2)
    homepage.check_product_qty(2)
