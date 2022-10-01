"""Module providingFunction printing python version."""
from time import sleep
from pages.register_page import RegisterPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import allure


FIRST_NAME = 'Mary'
LAST_NAME = 'Green'
EMAIL = 'green_m@yahoo.com'
MOBILE = '1234'
VALIDATION_MOBILE = '1'
ADDRESS = 'Street'
VALIDATE_ADDRESS = '1'
CITY = 'City'
POSTCODE = '12345'
VALIDATION_POSTCODE = '1'
PASSWORD = '1234'
CONFIRM_PASSWORD = '1234'


@allure.feature("Register Page")
@allure.story("Form validation")
def test_register_form_open(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
        # register_page.banner.click()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    assert register_page.first_name.is_enabled()


@allure.feature("Register Page")
@allure.story("Form validation")
def test_register_empty(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
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


@allure.feature("Register Page")
@allure.story("Data validation")
def test_register_form_validate_mobile(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    with allure.step('Insert values'):
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


@allure.feature("Register Page")
@allure.story("Data validation")
def test_register_form_validate_address(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    with allure.step('Insert values'):
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


@allure.feature("Register Page")
@allure.story("Data validation")
def test_register_form_validate_postcode(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    with allure.step('Insert values'):
        register_page.first_name.send_keys(FIRST_NAME)
        register_page.last_name.send_keys(LAST_NAME)
        register_page.email.send_keys(EMAIL)
        register_page.mobile.send_keys(MOBILE)
        register_page.address.send_keys(ADDRESS)
        register_page.city.send_keys(CITY)
        register_page.postcode.send_keys(VALIDATION_POSTCODE)
        element = Select(register_page.zone)
        element.select_by_visible_text('Arizona')
        register_page.password.send_keys(PASSWORD)
        register_page.confirm_password.send_keys(CONFIRM_PASSWORD)
    register_page.submit_button.click()
    assert register_page.postcode_error_message.is_enabled()


@allure.feature("Register Page")
@allure.story("Data validation")
def test_register_form_duplicate(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.register_link).perform()
    with allure.step('Insert values:'):
        register_page.first_name.send_keys(FIRST_NAME)
        register_page.last_name.send_keys(LAST_NAME)
        register_page.email.send_keys(EMAIL)
        register_page.mobile.send_keys(MOBILE)
        register_page.address.send_keys(ADDRESS)
        register_page.city.send_keys(CITY)
        register_page.postcode.send_keys(POSTCODE)
        element = Select(register_page.zone)
        element.select_by_visible_text('Arizona')
        register_page.password.send_keys(PASSWORD)
        register_page.confirm_password.send_keys(CONFIRM_PASSWORD)
    register_page.submit_button.click()
    assert register_page.duplicate_email_warning.is_displayed()


@allure.feature("Register Page")
@allure.story("Form validation")
def test_login(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.login_link).perform()
    assert register_page.login_button.is_displayed()


@allure.feature("Register Page")
@allure.story("Login validation")
def test_login_positive(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.login_link).\
        click(register_page.login_link).perform()
    with allure.step('Insert values'):
        register_page.input_email.send_keys(EMAIL)
        register_page.input_password.send_keys(PASSWORD)
    register_page.login_button.click()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).perform()
    assert register_page.logout_button.is_displayed()
    register_page.logout_button.click()


@allure.feature("Register Page")
@allure.story("Login validation")
def test_login_negative(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    # register_page.banner.click()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).\
        move_to_element(register_page.register_link).\
        click(register_page.login_link).perform()
    register_page.login_button.click()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown).\
        click(register_page.my_account_dropdown).perform()
    assert register_page.login_alert.is_displayed()


@allure.feature("Register Page")
@allure.story("Login validation")
def test_login_empty_password(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        register_page = RegisterPage(driver)
        register_page.open()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown). \
        click(register_page.my_account_dropdown). \
        move_to_element(register_page.register_link). \
        click(register_page.login_link).perform()
    with allure.step('Insert values'):
        register_page.input_email.send_keys(EMAIL)
    register_page.login_button.click()
    ActionChains(driver).move_to_element(register_page.my_account_dropdown). \
        click(register_page.my_account_dropdown).perform()
    assert register_page.login_alert.is_displayed()
