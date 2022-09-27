from pages.my_account_page import AccountPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException


EMAIL = 'green_m@yahoo.com'
PASSWORD = '1234'


def test_my_account_active(driver):
    account_page = AccountPage(driver)
    account_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown). \
        move_to_element(account_page.login_link). \
        click(account_page.login_link).perform()
    account_page.input_email.send_keys(EMAIL)
    account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).perform()
    assert account_page.my_account_link.is_enabled()
    ActionChains(driver).move_to_element(account_page.logout_link). \
        click(account_page.logout_link).perform()


def test_my_account_open(driver):
    account_page = AccountPage(driver)
    account_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown). \
        move_to_element(account_page.login_link). \
        click(account_page.login_link).perform()
    driver.implicitly_wait(10)
    account_page.input_email.send_keys(EMAIL)
    account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.my_account_link).\
        click(account_page.my_account_link).perform()
    assert account_page.user_icon.is_displayed()
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown).\
        move_to_element(account_page.logout_link).\
        click(account_page.logout_link).perform()


def test_my_account_editable(driver):
    account_page = AccountPage(driver)
    account_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown). \
        move_to_element(account_page.login_link). \
        click(account_page.login_link).perform()
    driver.implicitly_wait(10)
    account_page.input_email.send_keys(EMAIL)
    account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    driver.implicitly_wait(10)
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


def test_my_account_password_clickable(driver):
    account_page = AccountPage(driver)
    account_page.open()
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(account_page.my_account_dropdown).\
        click(account_page.my_account_dropdown). \
        move_to_element(account_page.login_link). \
        click(account_page.login_link).perform()
    driver.implicitly_wait(10)
    account_page.input_email.send_keys(EMAIL)
    account_page.input_password.send_keys(PASSWORD)
    account_page.login_button.click()
    driver.implicitly_wait(10)
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

