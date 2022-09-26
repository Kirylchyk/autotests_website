from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from time import sleep


FIRST_NAME = 'Mary'
LAST_NAME = 'Green'
EMAIL = 'green_m@yahoo.com'
MOBILE = '1234'
VALIDATION_MOBILE = '1'
ADDRESS = 'Street'
VALIDATE_ADDRESS = '1'
CITY = 'City'
POSTCODE = '12345'
PASSWORD = '1234'
CONFIRM_PASSWORD = '1234'


def test_register_form_open(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    assert register_page.register_form.is_displayed()


def test_register_empty(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    # register_page.banner.click()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    ActionChains(driver).move_to_element(register_page.submit_button).\
        click(register_page.submit_button).perform()
    assert register_page.error_message.is_enabled()


# def test_register_form_positive(driver):
#     register_page = RegisterPage(driver)
#     register_page.open()
#     driver.implicitly_wait(10)
#     ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
#         click(register_page.my_account_dropdown).\
#         move_to_element(register_page.register_link).\
#         click(register_page.register_link).perform()
#     register_page.first_name.send_keys(FIRST_NAME)
#     register_page.last_name.send_keys(LAST_NAME)
#     register_page.email.send_keys(EMAIL)
#     register_page.mobile.send_keys(MOBILE)
#     register_page.address.send_keys(ADDRESS)
#     register_page.city.send_keys(CITY)
#     register_page.postcode.send_keys(POSTCODE)
#     element = Select(register_page.zone)
#     element.select_by_visible_text('Arizona')
#     register_page.password.send_keys(PASSWORD)
#     register_page.confirm_password.send_keys(CONFIRM_PASSWORD)
#     register_page.submit_button.click()
#     assert register_page.success_message.is_displayed()


def test_register_form_validate_mobile(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    register_page.first_name.send_keys(FIRST_NAME)
    register_page.last_name.send_keys(LAST_NAME)
    register_page.email.send_keys(EMAIL)
    register_page.mobile.send_keys(VALIDATION_MOBILE)
    register_page.address.send_keys(ADDRESS)
    register_page.city.send_keys(CITY)
    register_page.postcode.send_keys(POSTCODE)
    element = Select(register_page.zone)
    element.select_by_visible_text('Arizona')
    register_page.password.send_keys(PASSWORD)
    register_page.confirm_password.send_keys(CONFIRM_PASSWORD)
    register_page.submit_button.click()
    sleep(5)
    assert register_page.mobile_error_message.is_enabled()


def test_register_form_validate_address(driver):
    register_page = RegisterPage(driver)
    register_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    register_page.first_name.send_keys(FIRST_NAME)
    register_page.last_name.send_keys(LAST_NAME)
    register_page.email.send_keys(EMAIL)
    register_page.mobile.send_keys(MOBILE)
    register_page.address.send_keys(VALIDATE_ADDRESS)
    register_page.city.send_keys(CITY)
    register_page.postcode.send_keys(POSTCODE)
    element = Select(register_page.zone)
    element.select_by_visible_text('Arizona')
    register_page.password.send_keys(PASSWORD)
    register_page.confirm_password.send_keys(CONFIRM_PASSWORD)
    register_page.submit_button.click()
    assert register_page.address_error_message.is_enabled()





