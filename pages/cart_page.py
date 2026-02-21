from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

    CART_BUTTON = (By.ID, "cart-total")
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")

    def go_to_checkout(self):
        self.driver.find_element(*self.CART_BUTTON).click()
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
