from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    preset = Options()
    preset.add_argument('--headless')
    driver = webdriver.Chrome(options=preset)
    driver.maximize_window()
    yield driver
    driver.quit()