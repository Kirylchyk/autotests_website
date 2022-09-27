from pages.contact_page import ContactPage

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


def test_check_email_active(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    driver.implicitly_wait(10)
    assert contact_page.email_link.is_enabled()


def test_check_logo_button(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    contact_page.logo_button.click()
    driver.implicitly_wait(10)
    get_url = driver.current_url
    assert get_url in "https://www.thesalondecorum.com/"


def test_check_map_is_displayed(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    driver.implicitly_wait(10)
    assert contact_page.map_image.is_displayed()


# def test_positive_filling_contact_form(driver):
#     contact_page = ContactPage(driver)
#     contact_page.open()
#     driver.implicitly_wait(5)
#     contact_page.first_name_fill.send_keys(FIRST_NAME)
#     contact_page.last_name_fill.send_keys(LAST_NAME)
#     contact_page.phone_1_fill.send_keys(PHONE1)
#     contact_page.phone_2_fill.send_keys(PHONE2)
#     contact_page.phone_3_fill.send_keys(PHONE3)
#     contact_page.email_fill.send_keys(EMAIL)
#     contact_page.subject_fill.send_keys(SUBJECT)
#     contact_page.message_fill.send_keys(MESSAGE)
#     contact_page.submit_button.click()
#     driver.implicitly_wait(10)
#     assert contact_page.success_message.is_displayed()


def test_negative_filling_contact_form(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    driver.implicitly_wait(5)
    contact_page.submit_button.click()
    assert contact_page.error_message.is_displayed()


def test_error_email_filling_contact_form(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    driver.implicitly_wait(5)
    contact_page.first_name_fill.send_keys(FIRST_NAME)
    contact_page.last_name_fill.send_keys(LAST_NAME)
    contact_page.phone_1_fill.send_keys(PHONE1)
    contact_page.phone_2_fill.send_keys(PHONE2)
    contact_page.phone_3_fill.send_keys(PHONE3)
    contact_page.email_fill.send_keys(ERROR_EMAIL)
    contact_page.subject_fill.send_keys(SUBJECT)
    contact_page.message_fill.send_keys(MESSAGE)
    contact_page.submit_button.click()
    driver.implicitly_wait(10)
    assert contact_page.error_message.is_displayed()


def test_error_phone_filling_contact_form(driver):
    contact_page = ContactPage(driver)
    contact_page.open()
    driver.implicitly_wait(5)
    contact_page.first_name_fill.send_keys(FIRST_NAME)
    contact_page.last_name_fill.send_keys(LAST_NAME)
    contact_page.phone_1_fill.send_keys(PHONE1)
    contact_page.phone_2_fill.send_keys(PHONE2)
    contact_page.phone_3_fill.send_keys(ERROR_PHONE)
    contact_page.email_fill.send_keys(EMAIL)
    contact_page.subject_fill.send_keys(SUBJECT)
    contact_page.message_fill.send_keys(MESSAGE)
    contact_page.submit_button.click()
    driver.implicitly_wait(10)
    assert contact_page.error_message.is_displayed()
