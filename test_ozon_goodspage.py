import pytest
from pages.goods_page import GoodsPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


@pytest.mark.addtochartbtn
def test_addtochartbtn(selenium):
    page = GoodsPage(selenium)
    page.addtochartbtn_click()
    time.sleep(2)
    try:
        selenium.find_element(By.XPATH, "//*[@id='layoutPage']/div[1]/div[4]/div[3]/div[2]/div[2]"
                                        "/div/div/div/div[4]/div/div/div/div/div/div[1]/button/span/span")
    except NoSuchElementException:
        return True
    return False


@pytest.mark.gotochartbtn
def test_gotochartbtn(selenium):
    page = GoodsPage(selenium)
    page.addtochartbtn_click()
    time.sleep(2)
    page.gotochartbtn.click()
    if "cart" not in selenium.current_url:
        raise Exception("error")

