import pytest
from pages.favorites_page import Favorites
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.mark.productinstockbtn
def test_favorites_page_productinstock_filter(selenium):
    page = Favorites(selenium)
    page.productinstockbtn.click()
    if "avail=inStock" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.productoutofstockbtn
def test_favorites_page_productoutofstock_filter(selenium):
    page = Favorites(selenium)
    page.productoutofstockbtn.click()
    if "avail=notInStock" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.clearfiltersbtn
def test_favorites_page_clearfiltersbtn(selenium):
    page = Favorites(selenium)
    page.clearfiltersbtn.click()
    if "avail=notInStock" or "avail=inStock" in selenium.current_url:
        raise Exception("error")
