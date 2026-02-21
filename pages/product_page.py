from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (By.ID, "button-cart")

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART).click()
