from base_page import BasePage
from locators import ChartLocators
from locators import SearchLocators
from selenium.webdriver.common.keys import Keys
import time
import os


class ChartPage(BasePage):
    url = "https://www.ozon.ru/cart/#cartItem=302473254"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(self.url)
        self.delitegoodsbtn = driver.find_element(*ChartLocators.DELITEGOODS_BTN)
        self.confirmdelitebtn = driver.find_element(*ChartLocators.CONFIRMDELITE_BTN)
        self.chooseallbtn = driver.find_element(*ChartLocators.CHOOSEALL_BTN)
        self.deliteallbtn = driver.find_element(*ChartLocators.DELITEALL_BTN)
        self.gotocheckoutbtn = driver.find_element(*ChartLocators.GOTOCHECKOUT_BTN)

    def delitegoodsbtn_click(self):
        self.delitegoodsbtn.click()
        time.sleep(3)

    def confirmdelitebtn_click(self):
        self.confirmdelitebtn.click()
        time.sleep(3)

    def chooseallbtn_click(self):
        self.chooseallbtn.click()
        time.sleep(3)

    def deliteallbtn_click(self):
        self.deliteallbtn.click()
        time.sleep(3)

    def gotocheckoutbtn_click(self):
        self.gotocheckoutbtn.click()
        time.sleep(3)
