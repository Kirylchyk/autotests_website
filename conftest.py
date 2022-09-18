import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(scope='session')
# def driver():
#     chrome_driver = webdriver.Chrome
#     chrome_driver.maximize_window()
#     yield chrome_driver
#     chrome_driver.quit()


@pytest.fixture(scope='session')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('window-size=1920,1080')
    chrome_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    chrome_driver.implicitly_wait(15)
    yield chrome_driver
    chrome_driver.quit()
