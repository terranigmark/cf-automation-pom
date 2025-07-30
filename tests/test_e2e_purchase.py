import pytest
# Page Objects
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"

@pytest.mark.e2e
def test_user_purchase_product_positive(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)

    login.load()
    login.login_as_user(STANDARD_USER, PASSWORD)
    products.add_product_by_name("sauce-labs-backpack")
    products.go_to_shopping_cart()
    cart.go_to_checkout()

@pytest.mark.e2e
def test_user_purchase_locked_user(driver):
    login = LoginPage(driver)

    login.load()
    login.login_as_user(LOCKED_USER, PASSWORD)