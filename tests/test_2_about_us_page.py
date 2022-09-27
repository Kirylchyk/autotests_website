from pages.about_us_page import AboutPage


def test_check_logo_button(driver):
    about_page = AboutPage(driver)
    about_page.open()
    about_page.about_us_button.click()
    about_page.logo_button.click()
    driver.implicitly_wait(10)
    get_url = driver.current_url
    assert get_url in "https://www.thesalondecorum.com/"


def test_check_company_image(driver):
    about_page = AboutPage(driver)
    about_page.open()
    about_page.about_us_button.click()
    about_page.logo_button.click()
    driver.implicitly_wait(10)
    assert about_page.company_image.is_displayed()


def test_check_company_email(driver):
    about_page = AboutPage(driver)
    about_page.open()
    about_page.about_us_button.click()
    driver.implicitly_wait(10)
    assert about_page.company_email.text in 'thesalondecorum@gmail.com'

