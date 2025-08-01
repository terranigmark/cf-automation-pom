from .base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutCompletePage(BasePage):

    COMPLETE_HEADER_MESSAGE = "Thank you for your order!"
    COMPLETE_TEXT_MESSAGE = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def validate_purchase_completion_message(self):
        assert self.text_of_element(self.COMPLETE_HEADER) == self.COMPLETE_HEADER_MESSAGE
        assert self.text_of_element(self.COMPLETE_TEXT) == self.COMPLETE_TEXT_MESSAGE