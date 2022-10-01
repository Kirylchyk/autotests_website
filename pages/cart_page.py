"""Module providingFunction printing python version."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


banner = (By.XPATH, '/html/body/div[2]/a')
first_product = (By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div[1]/'
                           'div/div[2]/div/div[1]/div/div/div[1]/a/div[1]/img')
cart_button = (By.ID, 'button-cart')
shopping_cart_modal = (By.CLASS_NAME, 'apc-modal-title')
product_description = (By.XPATH, '//*[@id="content"]/div/div[2]/h1')
shopping_cart = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a/span')
close_button = (By.XPATH, '//*[@id="apc-modal-content"]/button')
product_description_in_cart = (By.XPATH, '//*[@id="content"]/form/'
                                         'div/table/tbody/tr/td[2]/a')
logo_button = (By.XPATH, '//*[@id="logo"]/a/img')
remove_button = (By.XPATH, '//*[@id="apc-modal-content"]/div[2]/div[2]/div[1]/'
                           'table/tbody/tr[2]/td[6]/button/i')
empty_cart = (By.XPATH, '//*[@id="apc-modal-content"]/div[2]/div/div[1]')


class CartPage(BasePage):
    """A dummy docstring."""
    def __init__(self, driver):
        """A dummy docstring."""
        super().__init__(driver)
        self.driver = driver

    def open(self):
        """A dummy docstring."""
        self.driver.get('https://salondecorum.mysalon2me.com/')

    @property
    def banner(self):
        """A dummy docstring."""
        return self.find_element(banner)

    @property
    def first_product(self):
        """A dummy docstring."""
        return self.find_element(first_product)

    @property
    def cart_button(self):
        """A dummy docstring."""
        return self.find_element(cart_button)

    @property
    def shopping_cart_modal(self):
        """A dummy docstring."""
        return self.find_element(shopping_cart_modal)

    @property
    def product_description(self):
        """A dummy docstring."""
        return self.find_element(product_description)

    @property
    def shopping_cart(self):
        """A dummy docstring."""
        return self.find_element(shopping_cart)

    @property
    def product_description_in_cart(self):
        """A dummy docstring."""
        return self.find_element(product_description_in_cart)

    @property
    def close_button(self):
        """A dummy docstring."""
        return self.find_element(close_button)

    @property
    def logo_button(self):
        """A dummy docstring."""
        return self.find_element(logo_button)

    @property
    def remove_button(self):
        """A dummy docstring."""
        return self.find_element(remove_button)

    @property
    def empty_cart(self):
        """A dummy docstring."""
        return self.find_element(empty_cart)
