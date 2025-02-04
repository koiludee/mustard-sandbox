from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def home_open(self):
        BasePage.open(self, 'https://www.demoblaze.com/index.html')

    def find_element_args(self, *args):
        return self.driver.find_element(*args)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_element_by_title(self, title_text):
        return self.driver.find_element(By.XPATH, f'//*[text()="{title_text}"]')

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_clickable(self, by, locator):
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click(self, by, locator):
        element = self.wait_for_clickable(by, locator)
        element.click()

    def enter_text(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, by, locator):
        element = self.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def is_element_visible(self, by, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, locator))).is_displayed()
        except:
            return False

    def is_element_present(self, by, locator):
        try:
            self.driver.find_element(by, locator)
            return True
        except:
            return False



