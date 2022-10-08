"""Module providingFunction printing python version."""
import allure
from pages.cart_page import CartPage


@allure.feature("Cart Page")
@allure.story("Links are not broken")
def test_product_detailed_page(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        cart_page = CartPage(driver)
        cart_page.open()
    # cart_page.banner.click()
    cart_page.first_product.click()
    driver.implicitly_wait(10)
    assert cart_page.cart_button.is_enabled()


@allure.feature("Cart Page")
@allure.story("Cart actions")
def test_remove_product(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        cart_page = CartPage(driver)
        cart_page.open()
    with allure.step('Add product'):
        cart_page.first_product.click()
        cart_page.cart_button.click()
    cart_page.remove_button.click()
    assert cart_page.empty_cart.is_displayed()


@allure.feature("Cart Page")
@allure.story("Cart actions")
def test_add_product(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        cart_page = CartPage(driver)
        cart_page.open()
    cart_page.first_product.click()
    cart_page.cart_button.click()
    assert cart_page.shopping_cart_modal.is_enabled()


@allure.feature("Cart Page")
@allure.story("Cart actions")
def test_product_is_added(driver):
    """A dummy docstring."""
    with allure.step('Open page'):
        cart_page = CartPage(driver)
        cart_page.open()
    cart_page.first_product.click()
    description_raw = cart_page.product_description.text
    description_low = description_raw.lower()
    cart_page.cart_button.click()
    cart_page.close_button.click()
    cart_page.shopping_cart.click()
    description_cart_raw = cart_page.product_description_in_cart.text
    description_cart_low = description_cart_raw.lower()
    assert description_low == description_cart_low
