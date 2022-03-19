from base_page import BasePage
from locators import SearchResultsLocators
from locators import SearchLocators
from selenium.webdriver.common.keys import Keys
import time
import os


class SearchResults(BasePage):
    url = "https://www.ozon.ru/category/korm-dlya-koshek-12348/?category_was_predicted=true&from_global" \
          "=true&text=%D0%BA%D0%BE%D1%80%D0%BC+%D0%B4%D0%BB%D1%8F+%D0%BA%D0%BE%D1%88%D0%B5%D0%BA"

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        driver.get(self.url)
        self.sortingbtn = driver.find_element(*SearchResultsLocators.SORTING_BTN)
        self.sortingnewbtn = driver.find_element(*SearchResultsLocators.SORTINGNEW_BTN)
        self.ozondeliverybtn = driver.find_element(*SearchResultsLocators.OZONDELIVERYSWITCH_BTN)
        self.typefilterbtn = driver.find_element(*SearchResultsLocators.TYPEFILTER_BTN)
        self.brandfilterbtn = driver.find_element(*SearchResultsLocators.BRANDFILTER_BTN)
        self.installmentfilterbtn = driver.find_element(*SearchResultsLocators.INSTALLMENTFILTER_BTN)
        self.premiumfilterbtn = driver.find_element(*SearchResultsLocators.PREMIUMFILTER_BTN)
        self.discountfilterbtn = driver.find_element(*SearchResultsLocators.DISCOUNTFILTER_BTN)
        self.markeddownfilterbtn = driver.find_element(*SearchResultsLocators.MARKEDDOWNFILTER_BTN)
        self.floorpriceinput = driver.find_element(*SearchResultsLocators.FLOORPRICE_INPUT)
        self.ceilingpriceinput = driver.find_element(*SearchResultsLocators.CEILINGPRICE_INPUT)
        self.raitingbtn = driver.find_element(*SearchResultsLocators.RATINGSWITCH_BTN)
        self.sellerfilterbtn = driver.find_element(*SearchResultsLocators.SELLERFILTER_BTN)
        self.agefilterbtn = driver.find_element(*SearchResultsLocators.AGEFILTER_BTN)
        self.specialneedsfilterbtn = driver.find_element(*SearchResultsLocators.SPECIALNEEDSFILTER_BTN)
        self.floorweightinput = driver.find_element(*SearchResultsLocators.FLOORWEIGHT_INPUT)
        self.ceilingweightinput = driver.find_element(*SearchResultsLocators.CEILINGWEIGHT_INPUT)
        self.searchbtn = driver.find_element(*SearchLocators.SEARCH_BTN)

    def sortingbtn_click(self):
        self.sortingbtn.click()
        time.sleep(3)

    def sortingnewbtn_click(self):
        self.sortingnewbtn.click()
        time.sleep(3)

    def ozondeliverybtn_click(self):
        self.ozondeliverybtn.click()
        time.sleep(3)

    def typefilterbtn_click(self):
        self.typefilterbtn.click()
        time.sleep(3)

    def brandfilterbtn_click(self):
        self.brandfilterbtn.click()
        time.sleep(3)

    def installmentfilterbtn_click(self):
        self.installmentfilterbtn.click()
        time.sleep(3)

    def premiumfilterbtn_click(self):
        self.premiumfilterbtn.click()
        time.sleep(3)

    def discountfilterbtn_click(self):
        self.discountfilterbtn.click()
        time.sleep(3)

    def markeddownfilterbtn_click(self):
        self.markeddownfilterbtn.click()
        time.sleep(3)

    def enter_floorprice(self, value):
        self.floorpriceinput.send_keys(value)

    def enter_ceilingprice(self, value):
        self.ceilingpriceinput.send_keys(value)

    def raitingbtn_click(self):
        self.raitingbtn.click()
        time.sleep(3)

    def sellerfilterbtn_click(self):
        self.sellerfilterbtn.click()
        time.sleep(3)

    def agefilterbtn_click(self):
        self.agefilterbtn.click()
        time.sleep(3)

    def specialneedsfilterbtn_click(self):
        self.specialneedsfilterbtn.click()
        time.sleep(3)

    def enter_floorweight(self, value):
        self.floorweightinput.send_keys(value)

    def enter_ceilingweight(self, value):
        self.ceilingweightinput.send_keys(value)

    def searchbtn_click(self):
        self.searchbtn.click()
        time.sleep(3)
