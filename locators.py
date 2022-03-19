from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_INPUT = (By.TAG_NAME, "INPUT")
    SEARCH_BTN = (By.TAG_NAME, "svg")
    CATEGORIES_BTN = (By.TAG_NAME, "DIV")
    PETS_GOODS_BTN = (
        By.CSS_SELECTOR,
        "html > body > div:nth-of-type(10) > div > div:nth-of-type(2)"
        " > div > div > div:nth-of-type(2) > div > div > div > div:nth-of-type(2)"
        " > div:nth-of-type(12) > div:nth-of-type(2)"
                    )
    FOOD_BTN = (
        By.CSS_SELECTOR,
        "html > body > div:nth-of-type(10) > div > div:nth-of-type(2) "
        "> div > div > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > div:nth-of-type(10)"
              )
    CLEAR_SEARCH_BTN = (
        By.CSS_SELECTOR,
        "div#stickyHeader > div:nth-of-type(3) > div > form > div:nth-of-type(2) > div > svg > path"
                      )
    CLEAR_HISTORY_BTN = (
        By.CSS_SELECTOR,
        "div#stickyHeader > div:nth-of-type(3) > div > div > div > div:nth-of-type(2)"
        " > div > section > header > span"
                        )


class SearchResultsLocators:
    SORTING_BTN = (
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
        " > div:nth-of-type(2) > div:nth-of-type(4) > div > div > div > div > div > div"
                  )
    SORTINGNEW_BTN = (
        By.CSS_SELECTOR,
        "html > body > div:nth-of-type(10) > div > div > div > div:nth-of-type(2) > span"
                         )
    OZONDELIVERYSWITCH_BTN = (
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
        " > div > aside > div > div > label > div"
                            )
    TYPEFILTER_BTN = ( #сухой корм
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2) > div > aside > div:nth-of-type(3)"
        " > div:nth-of-type(2) > div > span > label > div"
                     )
    BRANDFILTER_BTN = ( #MoreLux
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2) > div > aside > div:nth-of-type(4)"
        " > div:nth-of-type(2) > div > a > label > div"
                      )
    INSTALLMENTFILTER_BTN = (
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
        " > div > aside > div:nth-of-type(4) > div > label > div"
                       )
    PREMIUMFILTER_BTN = (
        By.CSS_SELECTOR,
        "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
        " > div > aside > div:nth-of-type(5) > div > label > div"
                        )
    DISCOUNTFILTER_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3)"
                         " > div:nth-of-type(2) > div > aside > div:nth-of-type(6) > div > label > div"
                     )
    MARKEDDOWNFILTER_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(7) > div > label > div"
                         )
    FLOORPRICE_INPUT = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(8) > div:nth-of-type(2)"
                         " > div:nth-of-type(2) > div > div > input"
                       )
    CEILINGPRICE_INPUT = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(8) > div:nth-of-type(2)"
                         " > div:nth-of-type(2) > div:nth-of-type(2) > div > input"
                         )
    RATINGSWITCH_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(9) > div > label > div"
                        )
    SELLERFILTER_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
        " > div > aside > div:nth-of-type(10) > div:nth-of-type(2) > div > span > label > div"
                        )
    AGEFILTER_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(11) > div:nth-of-type(2) > div > span > label > div"
                    )
    SPECIALNEEDSFILTER_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(12) > div:nth-of-type(2) > div > span > label > div"
                            )
    FLOORWEIGHT_INPUT = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(13) > div:nth-of-type(2)"
                         " > div:nth-of-type(2) > div > div > input"
                        )
    CEILINGWEIGHT_INPUT = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(2)"
                         " > div > aside > div:nth-of-type(13) > div:nth-of-type(2)"
                         " > div:nth-of-type(2) > div:nth-of-type(2) > div > input"
                        )


class FavoritesLocators:
    PRODUCTINSTOCK_FILTER = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(3) > div > div >"
                         " div:nth-of-type(2) > div:nth-of-type(2) > label:nth-of-type(2) > span"
                            )
    PRODUCTOUTOFSTOCK_FILTER = (
        By.CSS_SELECTOR, "div#layoutPage > div > div:nth-of-type(3) > div:nth-of-type(3) > div > div >"
                         " div:nth-of-type(2) > div:nth-of-type(2) > label:nth-of-type(3) > span"
                                )
    CLEARFILTERS_BTN = (
        By.XPATH, "//*[@id='layoutPage']/div[1]/div[3]/div[3]/div[2]/div[2]/div/div[2]/button/svg"
                        )


class GoodsLocators:
    ADDTOCHART_BTN = (
        By.XPATH, "//*[@id='layoutPage']/div[1]/div[4]/div[3]/div[2]/div[2]/div/div/div/div[4]"
                  "/div/div/div/div/div/div[1]/button/span/span"
                    )
    GOTOCHART_BTN = (
        By.XPATH, "//*[@id='layoutPage']/div[1]/div[4]/div[3]/div[2]/div[2]/div/div/div/div[4]/div/div/"
                  "div/div/div/div/div[1]/button/span/div/div/div[1]"
                    )


class ChartLocators:
    DELITEGOODS_BTN = (
        By.CSS_SELECTOR, "div#split-Main-0 > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2)"
                         " > span:nth-of-type(2)"
                        )
    CONFIRMDELITE_BTN = (
        By.XPATH, "/html/body/div[10]/div/div[2]/div/div/section/div[3]/div/button/span/span"
                        )
    CHOOSEALL_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div > div > div:nth-of-type(3) > div:nth-of-type(4)"
                         " > div > div > div > div > label > label > div"
                    )
    DELITEALL_BTN = (
        By.CSS_SELECTOR, "div#layoutPage > div > div > div > div:nth-of-type(3) > div:nth-of-type(4)"
                         " > div > div > div > div > span"
                    )
    GOTOCHECKOUT_BTN = (
        By.XPATH, "//*[@id='layoutPage']/div[1]/div/div/div[3]/div[4]/div[2]/div/section/div[1]/div[1]/div/button"
                        )
