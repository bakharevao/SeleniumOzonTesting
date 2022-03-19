from base_page import BasePage
from locators import GoodsLocators
from locators import SearchLocators
from selenium.webdriver.common.keys import Keys
import time
import os


class GoodsPage(BasePage):
    url = "https://www.ozon.ru/product/korm-suhoy-sam-s-field-dlya-vzroslyh-koshek-s-beloy-ryboy-ovoshchami" \
          "-i-yablokami-400-g-301576510/?sh=c3SzPu0YoA"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(self.url)
        self.addtochartbtn = driver.find_element(*GoodsLocators.ADDTOCHART_BTN)
        self.gotochartbtn = driver.find_element(*GoodsLocators.GOTOCHART_BTN)

    def addtochartbtn_click(self):
        self.addtochartbtn.click()
        time.sleep(3)

    def gotochartbtn_click(self):
        self.gotochartbtn.click()
        time.sleep(3)
