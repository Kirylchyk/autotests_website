"""Module providingFunction printing python version."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


banner = (By.XPATH, '/html/body/div[2]/a')
my_account_dropdown = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
login_link = (By.CLASS_NAME, 'login_link')
input_email = (By.ID, 'input-email')
input_password = (By.ID, 'input-password')
login_button = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
my_account_link = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[1]/a')
user_icon = (By.CLASS_NAME, 'user-icon')
edit_account = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/ul/li[1]/a/div/i')
edit_password = (By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/ul/li[2]')
logout_link = (By.CLASS_NAME, 'logout_link')


class AccountPage(BasePage):
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
    def my_account_dropdown(self):
        """A dummy docstring."""
        return self.find_element(my_account_dropdown)

    @property
    def login_link(self):
        """A dummy docstring."""
        return self.find_element(login_link)

    @property
    def input_email(self):
        """A dummy docstring."""
        return self.find_element(input_email)

    @property
    def input_password(self):
        """A dummy docstring."""
        return self.find_element(input_password)

    @property
    def login_button(self):
        """A dummy docstring."""
        return self.find_element(login_button)

    @property
    def my_account_link(self):
        """A dummy docstring."""
        return self.find_element(my_account_link)

    @property
    def user_icon(self):
        """A dummy docstring."""
        return self.find_element(user_icon)

    @property
    def edit_account(self):
        """A dummy docstring."""
        return self.find_element(edit_account)

    @property
    def edit_password(self):
        """A dummy docstring."""
        return self.find_element(edit_password)

    @property
    def logout_link(self):
        """A dummy docstring."""
        return self.find_element(logout_link)
