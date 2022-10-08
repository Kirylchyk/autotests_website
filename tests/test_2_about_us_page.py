"""Module providingFunction printing python version."""
import sys
import allure
from pages.about_us_page import AboutPage


@allure.feature("About Us")
@allure.story("Logo Button")
def test_check_logo_button(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        about_page = AboutPage(driver)
        about_page.open()
    about_page.about_us_button.click()
    about_page.logo_button.click()
    get_url = driver.current_url
    if sys.exc_info()[0]:
        driver.get_screenshot_as_file('screenshot.png')
    assert get_url in "https://www.thesalondecorum.com/"


@allure.feature("About Us")
@allure.story("Image")
def test_check_company_image(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        about_page = AboutPage(driver)
        about_page.open()
    about_page.about_us_button.click()
    about_page.logo_button.click()
    assert about_page.company_image.is_displayed()


@allure.feature("About Us")
@allure.story("Email")
def test_check_company_email(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        about_page = AboutPage(driver)
        about_page.open()
    about_page.about_us_button.click()
    assert about_page.company_email.text in 'thesalondecorum@gmail.com'
