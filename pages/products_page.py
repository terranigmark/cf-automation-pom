from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductsPage(BasePage):

    TITLE = (By.CSS_SELECTOR, "title")
    CART_BADGE = (By.CSS_SELECTOR, "shopping_cart_badge")
    CART_LINK = (By.ID, "shopping_cart_container")

    def add_product_by_name(self, product_name: str):
        add_button = (By.XPATH, f"//button[@id='add-to-cart-{product_name}']")
        self.click(add_button)

    def go_to_shopping_cart(self):
        self.click(self.CART_LINK)