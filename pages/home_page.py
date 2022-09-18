from pages.base_page import BasePage
from selenium.webdriver.common.by import By


lego_start_button = (By.XPATH, '//*[@id="__next"]/div[5]/div/div/div[1]/div[1]/div/button')
logo_button = (By.XPATH, '//*[@id="__next"]/div[2]/header/div[2]/div[2]/div/div[3]/nav/a/img')
home_search = (By.XPATH, '//*[@id="__next"]/div[2]/header/div[2]/div[2]/div/div[5]/div/button')
accept_cookies = (By.XPATH, '/html/body/div[5]/div/aside/div/div/div[3]/div[1]/button[2]')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def lego_start_button(self):
        return self.find_element(lego_start_button)

    @property
    def accept_cookies(self):
        return self.find_element(accept_cookies)

    @property
    def logo_button(self):
        return self.find_element(logo_button)

    @property
    def home_search(self):
        return self.find_element(home_search)

    def open(self):
        self.driver.get('https://www.lego.com/')

