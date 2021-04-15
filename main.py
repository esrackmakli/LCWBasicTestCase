from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LCW:
    CATEGORY_PAGE = (By.ID, 'mega_menu_dd_1')
    PRODUCT_PAGE = (By.CLASS_NAME, "a_model_item")
    SIZE = (By.XPATH, '//a[@size="M"]')
    ADD_TO_CART = (By.ID, 'pd_add_to_cart')
    MAIN_PAGE = (By.CLASS_NAME, 'col-xs-4 col-lg-2')
    IS_ON_MAIN_PAGE = (By.CLASS_NAME, 'col-md-12')
    IS_ON_CATEGORY_PAGE = (By.XPATH, '//h1[contains(text(),"Kadın Giyim")]')
    IS_ON_PRODUCT_PAGE = (By.CLASS_NAME, 'product-code')

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.lcwaikiki.com/tr-TR/TR")
        self.wait = WebDriverWait(self.driver, 15)

    def test_case(self):
        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_MAIN_PAGE)).is_displayed()
        self.wait.until(ec.element_to_be_clickable(self.CATEGORY_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(
            self.IS_ON_CATEGORY_PAGE)).text == "Kadın Giyim", "here isn't category page"
        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()
        assert self.wait.until(ec.presence_of_all_elements_located(self.IS_ON_PRODUCT_PAGE))[
                   1].is_displayed() == "here isn't product page"
        self.wait.until(ec.presence_of_element_located(self.SIZE)).click()
        self.wait.until(ec.element_to_be_clickable(self.ADD_TO_CART)).click()
        self.wait.until(ec.element_to_be_clickable(self.MAIN_PAGE)).click()
        assert self.wait.until(ec.presence_of_element_located(self.IS_ON_MAIN_PAGE)).is_displayed()


LCW().test_case()
