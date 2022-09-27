from pages.shop_page import ShopPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

SEARCH = 'Shampoo'
SEARCH_EMPTY = '1!@#$%67'


def test_check_logo(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.banner.click()
    assert shop_page.logo_button.is_displayed()


def test_search_positive(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_field.send_keys(SEARCH)
    shop_page.search_button.click()
    assert shop_page.logo_button.is_displayed()


def test_search_correct_results(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_field.send_keys(SEARCH)
    shop_page.search_button.click()
    assert "Shampoo" in shop_page.searched_element.text


def test_search_with_conditions_applied(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_button.click()
    shop_page.detailed_search_field.send_keys(SEARCH)
    shop_page.category_drop_down.is_displayed()
    element = Select(shop_page.category_drop_down)
    element.select_by_visible_text('Shop All')
    shop_page.checkbox_subcategory.click()
    shop_page.checkbox_description.click()
    shop_page.detailed_search_button.click()
    assert "Shampoo" in shop_page.detailed_searched_element.text


def test_search_with_no_results(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_button.click()
    shop_page.detailed_search_field.send_keys(SEARCH_EMPTY)
    shop_page.detailed_search_button.click()
    assert shop_page.no_results_message.is_displayed()


def test_search_text_match(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_button.click()
    shop_page.detailed_search_field.send_keys(SEARCH_EMPTY)
    shop_page.detailed_search_button.click()
    assert SEARCH_EMPTY in shop_page.results_text.text


def test_search_hover_over(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    driver.implicitly_wait(10)
    shop_page.search_field.send_keys(SEARCH)
    shop_page.search_button.click()
    ActionChains(driver).move_to_element(shop_page.search_result).perform()
    assert shop_page.popup_buttons.is_enabled()





