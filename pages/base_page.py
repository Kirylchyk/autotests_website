"""Module providingFunction printing python version."""


class BasePage:
    """A dummy docstring."""

    def __init__(self, driver):
        """A dummy docstring."""
        self.driver = driver

    def find_element(self, *args):
        """A dummy docstring."""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        """A dummy docstring."""
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)
