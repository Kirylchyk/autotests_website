"""Module providingFunction printing python version."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


banner = (By.XPATH, '/html/body/div[2]/a')
my_account_dropdown = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a/span[1]')
register_link = (By.CLASS_NAME, 'regi_link')
register_form = (By.ID, 'account')
submit_button = (By.XPATH, '//*[@id="content"]/form/div/div')
error_message = (By.XPATH, '//*[@id="account"]/div[3]/div/div')
first_name = (By.ID, 'input-firstname')
last_name = (By.ID, 'input-lastname')
email = (By.ID, 'input-email')
mobile = (By.ID, 'input-telephone')
address = (By.ID, 'input-address-1')
city = (By.ID, 'input-city')
postcode = (By.ID, 'input-postcode')
zone = (By.ID, 'input-zone')
success_message = (By.XPATH, '/html/body/div[2]/div/div/div/h1')
password = (By.ID, 'input-password')
confirm_password = (By.ID, 'input-confirm')
mobile_error_message = (By.XPATH, '//*[@id="account"]/div[5]/div/div')
address_error_message = (By.XPATH, '//*[@id="address"]/div[2]/div/div')
postcode_error_message = (By.XPATH, '//*[@id="address"]/div[5]/div/div')
duplicate_email_warning = (By.XPATH, '/html/body/div[3]/div[1]/i')
login_link = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
login_button = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
input_email = (By.ID, "input-email")
input_password = (By.ID, 'input-password')
logout_button = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[3]/a')
login_alert = (By.CLASS_NAME, 'alert')


class RegisterPage(BasePage):
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
    def register_link(self):
        """A dummy docstring."""
        return self.find_element(register_link)

    @property
    def register_form(self):
        """A dummy docstring."""
        return self.find_elements(register_form)

    @property
    def submit_button(self):
        """A dummy docstring."""
        return self.find_element(submit_button)

    @property
    def error_message(self):
        """A dummy docstring."""
        return self.find_element(error_message)

    @property
    def first_name(self):
        """A dummy docstring."""
        return self.find_element(first_name)

    @property
    def last_name(self):
        """A dummy docstring."""
        return self.find_element(last_name)

    @property
    def email(self):
        """A dummy docstring."""
        return self.find_element(email)

    @property
    def mobile(self):
        """A dummy docstring."""
        return self.find_element(mobile)

    @property
    def address(self):
        """A dummy docstring."""
        return self.find_element(address)

    @property
    def city(self):
        """A dummy docstring."""
        return self.find_element(city)

    @property
    def postcode(self):
        """A dummy docstring."""
        return self.find_element(postcode)

    @property
    def zone(self):
        """A dummy docstring."""
        return self.find_element(zone)

    @property
    def success_message(self):
        """A dummy docstring."""
        return self.find_element(success_message)

    @property
    def password(self):
        """A dummy docstring."""
        return self.find_element(password)

    @property
    def confirm_password(self):
        """A dummy docstring."""
        return self.find_element(confirm_password)

    @property
    def mobile_error_message(self):
        """A dummy docstring."""
        return self.find_element(mobile_error_message)

    @property
    def address_error_message(self):
        """A dummy docstring."""
        return self.find_element(address_error_message)

    @property
    def postcode_error_message(self):
        """A dummy docstring."""
        return self.find_element(postcode_error_message)

    @property
    def duplicate_email_warning(self):
        """A dummy docstring."""
        return self.find_element(duplicate_email_warning)

    @property
    def login_link(self):
        """A dummy docstring."""
        return self.find_element(login_link)

    @property
    def login_button(self):
        """A dummy docstring."""
        return self.find_element(login_button)

    @property
    def input_email(self):
        """A dummy docstring."""
        return self.find_element(input_email)

    @property
    def input_password(self):
        """A dummy docstring."""
        return self.find_element(input_password)

    @property
    def logout_button(self):
        """A dummy docstring."""
        return self.find_element(logout_button)

    @property
    def login_alert(self):
        """A dummy docstring."""
        return self.find_element(login_alert)
