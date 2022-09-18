from pages.home_page import HomePage


def test_check_logo_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.lego_start_button.click()
    home_page.accept_cookies.click()
    home_page.logo_button.click()
    driver.implicitly_wait(10)
    assert home_page.home_search.is_displayed()

