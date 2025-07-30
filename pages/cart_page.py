from .base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    BUTTON_CHECKOUT = (By.ID, "checkout")

    def go_to_checkout(self):
        self.click(self.BUTTON_CHECKOUT)