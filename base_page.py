from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    url = None

    def __init__(self, driver, timeout=10):
        self.driver = webdriver.Chrome('/Users/olga/Desktop/chromedriver')
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

