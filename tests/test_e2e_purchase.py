import pytest
# Page Objects
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage
from pages.checkout_complete import CheckoutCompletePage

STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Hector"
LAST_NAME = "Vega"
POSTAL_CODE = "23085"

@pytest.mark.e2e
def test_user_purchase_product_positive(driver):
    login = LoginPage(driver)
    login.load()
    login.login_as_user(STANDARD_USER, PASSWORD)

    products = ProductsPage(driver)
    products.add_product_by_name("sauce-labs-backpack")
    products.go_to_shopping_cart()

    cart = CartPage(driver)
    cart.go_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    finish = FinishPage(driver)
    finish.click_finish_button()

    complete = CheckoutCompletePage(driver)
    complete.validate_purchase_completion_message()