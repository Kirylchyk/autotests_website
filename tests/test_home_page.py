from pages.home_page import HomePage


def test_check_logo_button(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.logo_button.click()
    driver.implicitly_wait(10)
    assert home_page.call_now_button.is_displayed()


def test_check_shop_page_is_open(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(10)
    home_page.shop_link.click()
    driver.switch_to.window(driver.window_handles[1])
    get_url = driver.current_url
    assert get_url in "https://salondecorum.mysalon2me.com/"


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


def test_background_image(driver):
    home_page = HomePage(driver)
    home_page.open()
    driver.implicitly_wait(10)
    assert home_page.image_background.is_displayed()


# def test_instagram_link(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     driver.implicitly_wait(10)
#     ActionChains(driver).move_to_element(home_page.instagram_icon).click(home_page.instagram_icon).perform()
#     driver.switch_to.window(driver.window_handles[1])
#     get_url = driver.current_url
#     assert get_url in "https://www.instagram.com/dec0rum/"


# def test_facebook_link(driver):
#     home_page = HomePage(driver)
#     home_page.open()
#     driver.implicitly_wait(10)
#     ActionChains(driver).move_to_element(home_page.facebook_icon).click(home_page.facebook_icon).perform()
#     driver.implicitly_wait(10)
#     driver.switch_to.window(driver.window_handles[1])
#     get_url = driver.current_url
#     assert get_url in "https://www.facebook.com/thesalondecorum"

