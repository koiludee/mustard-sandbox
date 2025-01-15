from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.demoblaze.com/index.html')

    def click_nav_brand_button(self):
        nav_brand_btn = self.driver.find_element(By.CSS_SELECTOR, '''[id="nava"]''')
        nav_brand_btn.click()

    def click_nav_home_button(self):
        home_button = self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
        home_button.click()

    def click_nav_contact_button(self):
        contact_button = self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
        contact_button.click()

    def click_nav_about_button(self):
        about_button = self.driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[3]/a')
        about_button.click()

    def click_nav_cart_button(self):
        cart_button = self.driver.find_element(By.XPATH, '//*[@id="cartur"]')
        cart_button.click()

    def click_nav_login_button(self):
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login2"]')
        login_button.click()

    def click_nav_signup_button(self):
        signup_button = self.driver.find_element(By.XPATH, '//*[@id="signin2"]')
        signup_button.click()

    def click_nav_login_in_button(self):
        login_in_button = self.driver.find_element(By.XPATH, '//*[@id="cartur"]')
        login_in_button.click()

    def click_menu_monitors(self):
        monitors_menu = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        monitors_menu.click()

    def click_menu_phones(self):
        phones_menu = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('phone')"]''')
        phones_menu.click()

    def click_menu_laptops(self):
        laptop_menu = self.driver.find_element(By.CSS_SELECTOR, '''[onclick="byCat('notebook')"]''')
        laptop_menu.click()

    def click_galaxy_s6(self):
        galaxy_s6 = self.driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')
        galaxy_s6.click()

    def check_product_qty(self, qty):
        product_qty = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(product_qty) == qty
