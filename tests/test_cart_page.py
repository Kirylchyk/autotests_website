from pages.cart_page import CartPage


def test_product_detailed_page(driver):
    cart_page = CartPage(driver)
    cart_page.open()
    cart_page.banner.click()
    driver.implicitly_wait(10)
    cart_page.first_product.click()
    driver.implicitly_wait(10)
    assert cart_page.cart_button.is_displayed()


def test_remove_product(driver):
    cart_page = CartPage(driver)
    cart_page.open()
    driver.implicitly_wait(10)
    cart_page.first_product.click()
    driver.implicitly_wait(10)
    cart_page.cart_button.click()
    cart_page.remove_button.click()
    assert cart_page.empty_cart.is_displayed()


def test_add_product(driver):
    cart_page = CartPage(driver)
    cart_page.open()
    driver.implicitly_wait(10)
    cart_page.first_product.click()
    driver.implicitly_wait(10)
    cart_page.cart_button.click()
    assert cart_page.shopping_cart_modal.is_enabled()


def test_product_is_added(driver):
    cart_page = CartPage(driver)
    cart_page.open()
    driver.implicitly_wait(10)
    cart_page.first_product.click()
    description_raw = cart_page.product_description.text
    description_low = description_raw.lower()
    driver.implicitly_wait(10)
    cart_page.cart_button.click()
    cart_page.close_button.click()
    driver.implicitly_wait(10)
    cart_page.shopping_cart.click()
    description_cart_raw = cart_page.product_description_in_cart.text
    description_cart_low = description_cart_raw.lower()
    assert description_low == description_cart_low
