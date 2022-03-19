from base_page import BasePage
from locators import SearchLocators
from selenium.webdriver.common.keys import Keys
import time
import os


class SearchPage(BasePage):
    url = "https://www.ozon.ru/"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(self.url)
        self.input = driver.find_element(*SearchLocators.SEARCH_INPUT)
        self.searchbtn = driver.find_element(*SearchLocators.SEARCH_BTN)
        self.categoriesbtn = driver.find_element(*SearchLocators.CATEGORIES_BTN)
        self.petsgoodsbtn = driver.find_element(*SearchLocators.PETS_GOODS_BTN)
        self.foodbtn = driver.find_element(*SearchLocators.FOOD_BTN)
        self.clearsearch = driver.find_element(*SearchLocators.CLEAR_SEARCH_BTN)
        self.clearhistory = driver.find_element(*SearchLocators.CLEAR_HISTORY_BTN)
        time.sleep(3)

    def enter_request(self, value):
        self.input.send_keys(value)

    def searchbtn_click(self):
        self.searchbtn.click()
        time.sleep(3)

    def categoriesbtn(self):
        self.categoriesbtn.click()
        time.sleep(3)

    def petsgoodsbtn(self):
        self.petsgoodsbtn.click()
        time.sleep(3)

    def foodbtn(self):
        self.foodbtn.click()
        time.sleep(3)

    def clearsearch(self):
        self.clearsearch.click()
        time.sleep(3)

    def clearhistory(self):
        self.clearhistory.click()
        time.sleep(3)
