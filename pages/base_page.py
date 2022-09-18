class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)
