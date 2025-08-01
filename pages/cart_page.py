from .base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    BUTTON_CHECKOUT = (By.ID, "checkout")
    BUTTON_CONTINUE_SHOPPING = (By.ID, "continue-shopping")

    def go_to_checkout(self):
        self.click(self.BUTTON_CHECKOUT)

    def continue_shopping(self):
        self.click(self.BUTTON_CONTINUE_SHOPPING)