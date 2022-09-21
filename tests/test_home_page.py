from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_check_logo_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.logo_button.click()
    driver.implicitly_wait(10)
    assert home_page.call_now_button.is_displayed()


def test_check_footer(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(10)
    assert home_page.footer_section.is_displayed()


def test_check_call_now(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(10)
    assert home_page.call_now_button.is_enabled()


def test_instagram_link(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[2]/div[1]/a[1]')
    ActionChains(driver).move_to_element(element).click(element).perform()
    driver.switch_to.window(driver.window_handles[1])
    get_url = driver.current_url
    assert get_url in "https://www.instagram.com/dec0rum/"


# def test_facebook_link(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     driver.implicitly_wait(10)
#     element = driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[2]/div[1]/a[2]')
#     ActionChains(driver).move_to_element(element).click(element).perform()
#     driver.implicitly_wait(10)
#     driver.switch_to.window(driver.window_handles[1])
#     get_url = driver.current_url
#     assert get_url in "https://www.facebook.com/thesalondecorum"






