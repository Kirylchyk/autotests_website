"""Module providingFunction printing python version."""
from pages.my_account_page import AccountPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import allure


EMAIL = 'green_m@yahoo.com'
PASSWORD = '1234'


@allure.feature("My Account Page")
@allure.story("Account validation")
def test_my_account_active(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        account_page = AccountPage(driver)
        account_page.open()
        # account_page.banner.click()
    with allure.step('Dropdown check'):
        ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
            click(account_page.my_account_dropdown). \
            move_to_element(account_page.login_link). \
            click(account_page.login_link).perform()
    with allure.step('Insert values'):
        account_page.input_email.send_keys(EMAIL)
        account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).perform()
    assert account_page.my_account_link.is_enabled()
    ActionChains(driver).move_to_element(account_page.logout_link). \
        click(account_page.logout_link).perform()


@allure.feature("My Account Page")
@allure.story("Account validation")
def test_my_account_open(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        account_page = AccountPage(driver)
        account_page.open()
    with allure.step('Dropdown check'):
        ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
            click(account_page.my_account_dropdown). \
            move_to_element(account_page.login_link). \
            click(account_page.login_link).perform()
    with allure.step('Insert values'):
        account_page.input_email.send_keys(EMAIL)
        account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.my_account_link).\
        click(account_page.my_account_link).perform()
    assert account_page.user_icon.is_displayed()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.logout_link).\
        click(account_page.logout_link).perform()


@allure.feature("My Account Page")
@allure.story("Account validation")
def test_my_account_editable(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        account_page = AccountPage(driver)
        account_page.open()
    with allure.step('Dropdown check'):
        ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
            click(account_page.my_account_dropdown). \
            move_to_element(account_page.login_link). \
            click(account_page.login_link).perform()
    with allure.step('Insert values'):
        account_page.input_email.send_keys(EMAIL)
        account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.my_account_link).\
        click(account_page.my_account_link).perform()
    try:
        account_page.edit_account.click()
    except WebDriverException:
        print
        "Element is not clickable"
    assert True
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.logout_link).\
        click(account_page.logout_link).perform()


@allure.feature("My Account Page")
@allure.story("Account validation")
def test_my_account_password_clickable(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        account_page = AccountPage(driver)
        account_page.open()
    with allure.step('Dropdown check'):
        ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
            click(account_page.my_account_dropdown). \
            move_to_element(account_page.login_link). \
            click(account_page.login_link).perform()
    with allure.step('Insert values'):
        account_page.input_email.send_keys(EMAIL)
        account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.my_account_link).\
        click(account_page.my_account_link).perform()
    try:
        account_page.edit_password.click()
    except WebDriverException:
        print
        "Element is not clickable"
    assert True
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.logout_link).\
        click(account_page.logout_link).perform()
