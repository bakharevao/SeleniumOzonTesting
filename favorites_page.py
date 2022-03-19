from base_page import BasePage
from locators import FavoritesLocators
from locators import SearchLocators
from selenium.webdriver.common.keys import Keys
import time
import os


class Favorites(BasePage):
    url = "https://www.ozon.ru/my/favorites"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(self.url)
        self.productinstockbtn = driver.find_element(*FavoritesLocators.PRODUCTINSTOCK_FILTER)
        self.productoutofstockbtn = driver.find_element(*FavoritesLocators.PRODUCTOUTOFSTOCK_FILTER)
        self.clearfiltersbtn = driver.find_element(*FavoritesLocators.CLEARFILTERS_BTN)

    def productinstockbtn_click(self):
        self.productinstockbtn.click()
        time.sleep(3)

    def productoutofstockbtn_click(self):
        self.productoutofstockbtn.click()
        time.sleep(3)

    def clearfiltersbtn_click(self):
        self.clearfiltersbtn.click()
        time.sleep(3)

