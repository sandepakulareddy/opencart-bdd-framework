from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException, StaleElementReferenceException
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CART_BUTTON = (By.ID, "cart-total")
    CHECKOUT_LINK = (By.LINK_TEXT, "Checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self, timeout: int = 20):
        """Open the cart and click the Checkout link with robust waits and fallbacks."""
        wait = WebDriverWait(self.driver, timeout)
        # Robustly click cart button (handle stale/interception with retries)
        for _ in range(3):
            try:
                wait.until(EC.presence_of_element_located(self.CART_BUTTON))
                cart_btn = self.driver.find_element(*self.CART_BUTTON)
                try:
                    cart_btn.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_btn)
                    self.driver.execute_script("arguments[0].click();", cart_btn)
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                continue

        # Robustly click checkout link
        for _ in range(3):
            try:
                wait.until(EC.presence_of_element_located(self.CHECKOUT_LINK))
                checkout = self.driver.find_element(*self.CHECKOUT_LINK)
                try:
                    checkout.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", checkout)
                    self.driver.execute_script("arguments[0].click();", checkout)
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                continue

    def verify_payment_page(self, timeout: int = 20):
        """Verify user reached the payment/checkout page by checking heading presence."""
        wait = WebDriverWait(self.driver, timeout)
        try:
            # Accept either 'Checkout' or 'Payment' headings depending on flow
            heading = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h1[contains(text(),'Checkout') or contains(text(),'Payment')]")
                )
            )
        except TimeoutException:
            raise AssertionError("User is not on the payment/checkout page")

        assert heading.is_displayed(), "User is not on the payment/checkout page"
