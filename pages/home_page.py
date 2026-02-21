from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    FIRST_PRODUCT = (By.XPATH, "//a[contains(text(),'MacBook')]")
    ADD_TO_CART_BTN = (By.XPATH, "//button[@id='button-cart']")

    def select_product(self):
        wait = WebDriverWait(self.driver, 20)

        # Wait until any product is visible
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'MacBook')]")
            )
        )

        product = wait.until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        )

        product.click()

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 20)

        add_btn = wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BTN)
        )

        add_btn.click()
