from pages.base_page import BasePage
from selenium.webdriver.common.by import By


logo_button = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]/div[1]/div/a/img')
footer = (By.XPATH, '//*[@id="page-section-5fd24102c2790c009a2253f0"]/div[2]')
call_now_button = (By.CLASS_NAME, 'sqs-block-button-element--medium')
image_background = (By.XPATH, '//*[@id="sections"]/section[1]/div[1]/img')
instagram_icon = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[2]/div[1]/a[1]')
facebook_icon = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[2]/div[1]/a[2]')
shop_link = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]/div[2]/div/nav/div[3]/a')


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://www.thesalondecorum.com/')

    @property
    def logo_button(self):
        return self.find_element(logo_button)

    @property
    def footer_section(self):
        return self.find_element(footer)

    @property
    def call_now_button(self):
        return self.find_element(call_now_button)

    @property
    def image_background(self):
        return self.find_element(image_background)

    @property
    def instagram_icon(self):
        return self.find_element(instagram_icon)

    @property
    def facebook_icon(self):
        return self.find_element(facebook_icon)

    @property
    def shop_link(self):
        return self.find_element(shop_link)
