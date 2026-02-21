from selenium.webdriver.common.by import By
from pages.base_page import BasePage


        
class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

       
    def verify_payment_page(self):
        """Verify that user is on the payment page."""
        # Example locator for the payment page heading or element
        wait = WebDriverWait(self.driver, 500)
        payment_header = self.browser.find_element("xpath", "//h1[contains(text(), 'Payment')]")
        
        # Assert or check presence of the element to verify correct page
        assert payment_header.is_displayed(), "User is not on the payment page"


    def proceed_to_checkout(self):
        self.driver.find_element("xpath", "//button[@id='button-cart']").click()
