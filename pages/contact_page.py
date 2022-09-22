from pages.base_page import BasePage
from selenium.webdriver.common.by import By


logo_button = (By.XPATH, '//*[@id="header"]/div[2]/div[3]/div[2]/div[1]/div[1]/div/a/img')
email_link = (By.XPATH, '//*[@id="block-yui_3_17_2_1_1607618853653_6163"]/div/p[3]/a')
map_image = (By.XPATH, '//*[@id="block-4459ea897ddb7ca63d9e"]')
first_name_fill = (By.XPATH, '//*[@id="name-yui_3_17_2_1_1607619351343_6024"]/div[1]/label/input')
last_name_fill = (By.XPATH, '//*[@id="name-yui_3_17_2_1_1607619351343_6024"]/div[2]/label/input')
phone_1_fill = (By.XPATH, '//*[@id="phone-yui_3_17_2_1_1609255257783_17282"]/div[1]/label/input')
phone_2_fill = (By.XPATH, '//*[@id="phone-yui_3_17_2_1_1609255257783_17282"]/div[2]/label/input')
phone_3_fill = (By.XPATH, '//*[@id="phone-yui_3_17_2_1_1609255257783_17282"]/div[3]/label/input')
email_fill = (By.ID, 'email-yui_3_17_2_1_1607619351343_6025-field')
subject_fill = (By.ID, 'text-yui_3_17_2_1_1607619351343_6026-field')
message_fill = (By.ID, 'textarea-yui_3_17_2_1_1607619351343_6027-field')
submit_button = (By.XPATH, '//*[@id="block-yui_3_17_2_1_1607619351343_6019"]/div/div/div/form/div[2]/input')
success_message = (By.ID, 'block-yui_3_17_2_1_1607619351343_6019')
error_message = (By.XPATH, '//*[@id="block-yui_3_17_2_1_1607619351343_6019"]')


class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get('https://www.thesalondecorum.com/contact')

    @property
    def logo_button(self):
        return self.find_element(logo_button)

    @property
    def email_link(self):
        return self.find_element(email_link)

    @property
    def map_image(self):
        return self.find_element(map_image)

    @property
    def first_name_fill(self):
        return self.find_element(first_name_fill)

    @property
    def last_name_fill(self):
        return self.find_element(last_name_fill)

    @property
    def phone_1_fill(self):
        return self.find_element(phone_1_fill)

    @property
    def phone_2_fill(self):
        return self.find_element(phone_2_fill)

    @property
    def phone_3_fill(self):
        return self.find_element(phone_3_fill)

    @property
    def email_fill(self):
        return self.find_element(email_fill)

    @property
    def subject_fill(self):
        return self.find_element(subject_fill)

    @property
    def message_fill(self):
        return self.find_element(message_fill)

    @property
    def submit_button(self):
        return self.find_element(submit_button)

    @property
    def success_message(self):
        return self.find_element(success_message)

    @property
    def error_message(self):
        return self.find_element(error_message)
