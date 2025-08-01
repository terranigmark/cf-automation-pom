from .base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.type(self.INPUT_FIRST_NAME, first_name)
        self.type(self.INPUT_LAST_NAME, last_name)
        self.type(self.INPUT_POSTAL_CODE, postal_code)
        self.click(self.BUTTON_CONTINUE)