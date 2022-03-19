import pytest
from pages.searchresults_page import SearchResults
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.mark.sorting_by_new
def test_sorting_by_new(selenium):
    page = SearchResults(selenium)
    page.sortingbtn_click()
    page.sortingnewbtn_click()
    if "sorting=new" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_nearest_delivery_date
def test_sorting_by_nearest_delivery_date(selenium):
    page = SearchResults(selenium)
    page.ozondeliverybtn_click()
    if "delivery=2" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_type
def test_sorting_by_type(selenium):
    page = SearchResults(selenium)
    page.typefilterbtn_click()
    if "type=60209" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_brand
def test_sorting_by_brand(selenium):
    page = SearchResults(selenium)
    page.brandfilterbtn_click()
    if "morelux" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_installment
def test_sorting_by_installment(selenium):
    page = SearchResults(selenium)
    page.installmentfilterbtn_click()
    if "is_installment" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_premiumfilter
def test_sorting_by_premiumfilter(selenium):
    page = SearchResults(selenium)
    page.premiumfilterbtn_click()
    if "is_premium" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_discountfilter
def test_sorting_by_discountfilter(selenium):
    page = SearchResults(selenium)
    page.discountfilterbtn.click()
    if "isdiscount" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_markeddownfilter
def test_sorting_by_markeddownfilter(selenium):
    page = SearchResults(selenium)
    page.markeddownfilterbtn.click()
    if "ismarkeddown" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_price
@pytest.mark.parametrize(
    "floorprice, ceilingprice, is_ok", [
        (100, 1000, True),
        (10, 200, True),
        (0, 2000, True),
        (0, 50, True),
        (-1, 100, False),
        (-0, -1, False),
        (None, False),
        ("", False),
    ]
)
def test_sorting_by_price(selenium, floorprice, ceilingprice, is_ok):
    page = SearchResults(selenium)
    page.floorpriceinput.send_keys(floorprice)
    page.ceilingpriceinput.send_keys(ceilingprice)
    page.searchbtn.click()
    if is_ok:
        if "price=" not in selenium.current_url:
            raise Exception("error")
    else:
        if "price=-" in selenium.current_url:
            raise Exception("error")


@pytest.mark.sorting_by_raiting
def test_sorting_by_raiting(selenium):
    page = SearchResults(selenium)
    page.raitingbtn.click()
    if "rating=" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_sellerfilter
def test_sorting_by_sellerfilter(selenium):
    page = SearchResults(selenium)
    page.sellerfilterbtn.click()
    if "seller=" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_agefilter
def test_sorting_by_agefilter(selenium):
    page = SearchResults(selenium)
    page.agefilterbtn.click()
    if "ages=" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_specialneeds
def test_sorting_by_specialneeds(selenium):
    page = SearchResults(selenium)
    page.specialneedsfilterbtn.click()
    if "recommendations=" not in selenium.current_url:
        raise Exception("error")


@pytest.mark.sorting_by_weight
@pytest.mark.parametrize(
    "floorweight, ceilingweigh, is_ok", [
        (100, 1000, True),
        (10, 200, True),
        (0, 2000, True),
        (0, 50, True),
        (-1, 100, False),
        (-0, -1, False),
        (None, False),
        ("", False),
    ]
)
def test_sorting_by_weight(selenium, floorweight, ceilingweigh, is_ok):
    page = SearchResults(selenium)
    page.floorweightinput.send_keys(floorweight)
    page.ceilingweightinput.send_keys(ceilingweigh)
    page.searchbtn.click()
    if is_ok:
        if "weight=" not in selenium.current_url:
            raise Exception("error")
    else:
        if "weight=-" in selenium.current_url:
            raise Exception("error")


@pytest.mark.add_to_favorites
def test_add_to_favorites(selenium):
    page = SearchResults(selenium)
    page.specialneedsfilterbtn.click()
    if "recommendations=" not in selenium.current_url:
        raise Exception("error")
