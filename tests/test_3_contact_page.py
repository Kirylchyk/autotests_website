"""Module providingFunction printing python version."""
from pages.contact_page import ContactPage
import allure

FIRST_NAME = 'Mary'
LAST_NAME = 'Green'
EMAIL = 'green_m@yahoo.com'
SUBJECT = 'Question'
MESSAGE = 'How to buy Melu conditioner?'
PHONE1 = '123'
PHONE2 = '123'
PHONE3 = '1234'
ERROR_EMAIL = 'test'
ERROR_PHONE = 'AA'


@allure.feature("Contact Page")
def test_check_email_active(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    assert contact_page.email_link.is_enabled()


@allure.feature("Contact Page")
@allure.story("Links are not broken")
def test_check_logo_button(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    with allure.step('Click'):
        contact_page.logo_button.click()
    get_url = driver.current_url
    assert get_url in "https://www.thesalondecorum.com/"


@allure.feature("Contact Page")
@allure.story("Image")
def test_check_map_is_displayed(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    assert contact_page.map_image.is_displayed()


# def test_positive_filling_contact_form(driver):
#     contact_page = ContactPage(driver)
#     contact_page.open()
#     contact_page.first_name_fill.send_keys(FIRST_NAME)
#     contact_page.last_name_fill.send_keys(LAST_NAME)
#     contact_page.phone_1_fill.send_keys(PHONE1)
#     contact_page.phone_2_fill.send_keys(PHONE2)
#     contact_page.phone_3_fill.send_keys(PHONE3)
#     contact_page.email_fill.send_keys(EMAIL)
#     contact_page.subject_fill.send_keys(SUBJECT)
#     contact_page.message_fill.send_keys(MESSAGE)
#     contact_page.submit_button.click()
#     assert contact_page.success_message.is_displayed()


@allure.feature("Contact Page")
@allure.story("Contact Form")
def test_negative_filling_contact_form(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    contact_page.submit_button.click()
    assert contact_page.error_message.is_displayed()


@allure.feature("Contact Page")
@allure.story("Contact Form")
def test_error_email_filling_contact_form(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    with allure.step('Insert values'):
        contact_page.first_name_fill.send_keys(FIRST_NAME)
        contact_page.last_name_fill.send_keys(LAST_NAME)
        contact_page.phone_1_fill.send_keys(PHONE1)
        contact_page.phone_2_fill.send_keys(PHONE2)
        contact_page.phone_3_fill.send_keys(PHONE3)
        contact_page.email_fill.send_keys(ERROR_EMAIL)
        contact_page.subject_fill.send_keys(SUBJECT)
        contact_page.message_fill.send_keys(MESSAGE)
    contact_page.submit_button.click()
    assert contact_page.error_message.is_displayed()


@allure.feature("Contact Page")
@allure.story("Contact Form")
def test_error_phone_filling_contact_form(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        contact_page = ContactPage(driver)
        contact_page.open()
    with allure.step('Insert values'):
        contact_page.first_name_fill.send_keys(FIRST_NAME)
        contact_page.last_name_fill.send_keys(LAST_NAME)
        contact_page.phone_1_fill.send_keys(PHONE1)
        contact_page.phone_2_fill.send_keys(PHONE2)
        contact_page.phone_3_fill.send_keys(ERROR_PHONE)
        contact_page.email_fill.send_keys(EMAIL)
        contact_page.subject_fill.send_keys(SUBJECT)
        contact_page.message_fill.send_keys(MESSAGE)
    contact_page.submit_button.click()
    assert contact_page.error_message.is_displayed()
