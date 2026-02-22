from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = (By.ID, "button-cart")

    def add_to_cart(self):
        # Use a robust click with a short wait
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        wait = WebDriverWait(self.driver, 10)
        btn = wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        try:
            btn.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            self.driver.execute_script("arguments[0].click();", btn)
