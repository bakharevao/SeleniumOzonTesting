import pytest
from pages.search_page import SearchPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


@pytest.mark.search_page
@pytest.mark.parametrize(
    "request, is_ok", [
        ("корм для кошек", True),
        ("кор для кошек сухой", True),
        ("rjhv lkz rjitr ce[jq", True),
        ("для кошек корм", True),
        ("ко для кош", False),
        ("rj lk rji", False),
        (None, False),
        ("", False),
    ]
)
def test_search_page(selenium, request, is_ok):
    page = SearchPage(selenium)
    page.clearsearch.click()
    page.enter_request(request)
    page.searchbtn_click()
    if is_ok:
        assert page.get_relative_link() != "category/korm-dlya-koshek-12348/?category_was" \
                                           "_predicted=true&from_global=true&text=корм+для+кошек", "search error"
    else:
        assert page.get_relative_link() == "category/korm-dlya-koshek-12348/?category_was" \
                                       "_predicted=true&from_global=true&text=корм+для+кошек", "search error"


@pytest.mark.search_correct_category
def test_search_page_correct_category(selenium):
    page = SearchPage(selenium)
    page.clearsearch.click()
    page.categoriesbtn.click()
    page.petsgoodsbtn.click()
    page.enter_request("корм для кошек")
    page.searchbtn_click()
    assert page.get_relative_link() != "category/korm-dlya-koshek-12348/?category_was" \
                                           "_predicted=true&from_global=true&text=корм+для+кошек", "search error"


@pytest.mark.search_incorrect_category
def test_search_page_incorrect_category(selenium):
    page = SearchPage(selenium)
    page.clearsearch.click()
    page.categoriesbtn.click()
    page.petsgoodsbtn.click()
    page.enter_request("корм для кошек")
    page.searchbtn_click()
    assert page.get_relative_link() != "category/korm-dlya-koshek-12348/?category_was" \
                                       "_predicted=true&from_global=true&text=корм+для+кошек", "search error"


@pytest.mark.clear_search
def test_clear_search(selenium):
    page = SearchPage(selenium)
    page.enter_request("корм для кошек")
    page.clearsearch.click()
    page.searchbtn_click()
    assert page.get_relative_link() == "category/korm-dlya-koshek-12348/?category_was" \
                                       "_predicted=true&from_global=true&text=корм+для+кошек", "search error"


@pytest.mark.clear_history
def test_clear_history(selenium):
    page = SearchPage(selenium)
    page.enter_request("корм для кошек")
    page.searchbtn_click()
    page.clearsearch.click()
    time.sleep(5)
    try:
        selenium.find_element(By.CSS_SELECTOR, "div#stickyHeader > div:nth-of-type(3) > div > div >"
                                               " div > div:nth-of-type(2) > div > section > header > span")
    except NoSuchElementException:
        return True
    return False

