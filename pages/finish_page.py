from .base_page import BasePage
from selenium.webdriver.common.by import By


class FinishPage(BasePage):

    BUTTON_FINISH = (By.NAME, "finish")

    def click_finish_button(self):
        self.click(self.BUTTON_FINISH)