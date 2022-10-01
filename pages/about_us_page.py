"""Module providingFunction printing python version."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


about_us_button = (By.LINK_TEXT, 'About Us')
logo_button = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]'
                         '/div[1]/div/a/img')
company_image = (By.CSS_SELECTOR, 'img[alt="Salon Decorum"]')
company_email = (By.XPATH, '//*[@id="block-c5578ab8171c75296c12"]/div/p[3]/a')


class AboutPage(BasePage):
    """A dummy docstring."""
    def __init__(self, driver):
        """A dummy docstring."""
        super().__init__(driver)
        self.driver = driver

    def open(self):
        """A dummy docstring."""
        self.driver.get('https://www.thesalondecorum.com/')

    @property
    def logo_button(self):
        """A dummy docstring."""
        return self.find_element(logo_button)

    @property
    def company_image(self):
        """A dummy docstring."""
        return self.find_element(company_image)

    @property
    def about_us_button(self):
        """A dummy docstring."""
        return self.find_element(about_us_button)


    @property
    def company_email(self):
        """A dummy docstring."""
        return self.find_element(company_email)
