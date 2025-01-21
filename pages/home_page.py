from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    #Home
    home_button = (By.CSS_SELECTOR, '''[id="nava"]''')

    #Navigation bar
    navbar_home_button = (By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
    navbar_contact_button = (By.XPATH, '//*[@id="navbarExample"]/ul/li[2]/a')
    navbar_about_button = (By.XPATH, '//*[@id="navbarExample"]/ul/li[3]/a')
    navbar_cart_button = (By.XPATH, '//*[@id="cartur"]')
    navbar_login_button = (By.XPATH, '//*[@id="login2"]')
    navbar_signup_button = (By.XPATH, '//*[@id="signin2"]')

    #Side menu
    menu_monitors_button = (By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
    menu_phones_button = (By.CSS_SELECTOR, '''[onclick="byCat('phone')"]''')
    menu_laptops_button = (By.CSS_SELECTOR, '''[onclick="byCat('notebook')"]''')

    #Previous/Next button
    prev_button = (By.XPATH, '//*[@id="prev2"]')
    next_button = (By.XPATH, '//*[@id="next2"]')

    #Carousel
    PAGINATOR_BUTTON_XPATH = '//*[@id="carouselExampleIndicators"]/ol/li[{}]'

    carousel_prev_button = (By.XPATH, '//*[@id="carouselExampleIndicators"]/a[1]/span[1]')
    carousel_next_button = (By.XPATH, '//*[@id="carouselExampleIndicators"]/a[2]/span[1]')
    paginator_button_first = (By.XPATH, PAGINATOR_BUTTON_XPATH.format(1))
    paginator_button_second = (By.XPATH, PAGINATOR_BUTTON_XPATH.format(2))
    paginator_button_third = (By.XPATH, PAGINATOR_BUTTON_XPATH.format(3))


    def click_galaxy_s6(self):
        HomePage.open(self, 'https://www.demoblaze.com/index.html')
        HomePage.click(self, By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a')

    def check_product_qty(self, qty):
        product_qty = self.driver.find_elements(By.CSS_SELECTOR, '.card')
        assert len(product_qty) == qty
