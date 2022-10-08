import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.set_window_position(0, 0)
    chrome_driver.set_window_size(1920, 1080)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(10)
    yield chrome_driver
    chrome_driver.quit()
