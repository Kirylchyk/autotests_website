from pages.base_page import BasePage
from selenium.webdriver.common.by import By


logo_button = (By.XPATH, '/html/body/header/div/div/div[2]/div/a/img')
search_field = (By.XPATH, '//*[@id="search"]/input')
search_button = (By.XPATH, '//*[@id="search"]/span/button')
banner = (By.XPATH, '/html/body/div[2]/a')
searched_element = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div/div[2]/div/h4/a')
detailed_search_field = (By.ID, 'input-search')
category_drop_down = (By.XPATH, '//*[@id="content"]/div[1]/div/div[2]/select')
checkbox_subcategory = (By.XPATH, '//*[@id="content"]/div[1]/div/div[3]/label/input')
checkbox_description = (By.XPATH, '//*[@id="description"]')
detailed_search_button = (By.ID, 'button-search')
detailed_searched_element = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div/div[2]/div/h4/a')
no_results_message = (By.XPATH, '//*[@id="content"]/p')
results_text = (By.XPATH, '/html/body/div[2]/div/div/div/h1')
search_result = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div/div[1]/a/div[1]/img')
popup_buttons = (By.CLASS_NAME, 'button-group')
alert_message = (By.CLASS_NAME, 'alert')
button_cart = (By.ID, 'button-cart')


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://salondecorum.mysalon2me.com/')

    @property
    def logo_button(self):
        return self.find_element(logo_button)

    @property
    def search_field(self):
        return self.find_element(search_field)

    @property
    def banner(self):
        return self.find_element(banner)

    @property
    def search_button(self):
        return self.find_element(search_button)

    @property
    def searched_element(self):
        return self.find_element(searched_element)

    @property
    def detailed_search_field(self):
        return self.find_element(detailed_search_field)

    @property
    def category_drop_down(self):
        return self.find_element(category_drop_down)

    @property
    def checkbox_subcategory(self):
        return self.find_element(checkbox_subcategory)

    @property
    def checkbox_description(self):
        return self.find_element(checkbox_description)

    @property
    def detailed_search_button(self):
        return self.find_element(detailed_search_button)

    @property
    def detailed_searched_element(self):
        return self.find_element(detailed_searched_element)

    @property
    def no_results_message(self):
        return self.find_element(no_results_message)

    @property
    def results_text(self):
        return self.find_element(results_text)

    @property
    def search_result(self):
        return self.find_element(search_result)

    @property
    def popup_buttons(self):
        return self.find_element(popup_buttons)

    @property
    def popup_button_view(self):
        return self.find_element(popup_button_view)

    @property
    def alert_message(self):
        return self.find_element(alert_message)

    @property
    def button_cart(self):
        return self.find_element(button_cart)

    @property
    def product_class(self):
        return self.find_element(product_class)
