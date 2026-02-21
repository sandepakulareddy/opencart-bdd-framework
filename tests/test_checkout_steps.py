from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage

# Link feature file
scenarios("../features/checkout.feature")


@given("User is on home page")
def open_home_page(browser):
    browser.get("https://tutorialsninja.com/demo/")
    browser.maximize_window()


@when("User selects a product")
def select_product(browser):
    HomePage(browser).select_product()


@when("User adds product to cart")
def add_to_cart(browser):
    HomePage(browser).add_to_cart()


@when("User proceeds to checkout")
def proceed_checkout(browser):
    CheckoutPage(browser).proceed_to_checkout()


@then("User should navigate till payment page")
def verify_payment_page(browser):
    CheckoutPage(browser).verify_payment_page()
