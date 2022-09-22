from pages.base_page import BasePage
from selenium.webdriver.common.by import By

about_us_button = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]/div[2]/div/nav/div[2]/a')
logo_button = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]/div[1]/div/a/img')
company_image = (By.XPATH, '//*[@id="sections"]/section[1]')


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://www.thesalondecorum.com/')

    @property
    def logo_button(self):
        return self.find_element(logo_button)

    @property
    def company_image(self):
        return self.find_element(company_image)

    @property
    def about_us_button(self):
        return self.find_element(about_us_button)
