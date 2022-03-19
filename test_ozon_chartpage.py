import pytest
from pages.cart_page import ChartPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.mark.delitegoodsbtn
def test_delitegoodsbtn(selenium):
    page = ChartPage(selenium)
    page.delitegoodsbtn.click()
    page.confirmdelitebtn.click()
    time.sleep(3)
    if "#cartItem=302473254" in selenium.current_url:
        raise Exception("error")


@pytest.mark.deliteallbtn
def test_deliteallbtn(selenium):
    page = ChartPage(selenium)
    page.chooseallbtn.click()
    page.deliteallbtn.click()
    page.confirmdelitebtn.click()
    time.sleep(3)
    if "#cartItem=302473254" in selenium.current_url:
        raise Exception("error")


@pytest.mark.gotocheckoutbtn
def test_gotocheckoutbtn(selenium):
    page = ChartPage(selenium)
    page.gotocheckoutbtn.click()
    time.sleep(3)
    if "gocheckout" not in selenium.current_url:
        raise Exception("error")
