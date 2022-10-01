"""Module providingFunction printing python version."""
from time import sleep
from pages.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains
import allure


@allure.feature("Home Page")
@allure.story("Logo Button")
def test_check_logo_button(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    home_page.logo_button.click()
    driver.implicitly_wait(10)
    assert home_page.call_now_button.is_displayed()


@allure.feature("Home_Page")
@allure.story("Check redirection")
def test_check_shop_page_is_open(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    home_page.shop_link.click()
    driver.switch_to.window(driver.window_handles[1])
    get_url = driver.current_url
    assert get_url in "https://salondecorum.mysalon2me.com/"


@allure.feature("Home_Page")
@allure.story("Footer")
def test_check_footer(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.footer_section.is_displayed()


@allure.feature("Home_Page")
@allure.story("Check Call-Now button")
def test_check_call_now(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.call_now_button.is_enabled()


@allure.feature("Home_Page")
@allure.story("Image")
def test_background_image(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    assert home_page.image_background.is_displayed()


@allure.feature("Home_Page")
@allure.story("Instagram redirection")
def test_instagram_link(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        home_page = HomePage(driver)
        home_page.open()
    ActionChains(driver).move_to_element(home_page.instagram_icon).\
        click(home_page.instagram_icon).perform()
    driver.switch_to.window(driver.window_handles[2])
    sleep(3)
    get_url = driver.current_url
    assert get_url in "https://www.instagram.com/dec0rum/"


# def test_facebook_link(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     driver.implicitly_wait(10)
#     ActionChains(driver).move_to_element(home_page.facebook_icon).
#     click(home_page.facebook_icon).perform()
#     driver.implicitly_wait(10)
#     driver.switch_to.window(driver.window_handles[1])
#     get_url = driver.current_url
#     assert get_url in "https://www.facebook.com/thesalondecorum"
