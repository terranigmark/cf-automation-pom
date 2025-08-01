from .base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    # Datos de prueba
    URL = "https://www.saucedemo.com/"

    # Selectores
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")

    # Acciones
    def load(self):
        self.visit(self.URL)

    def login_as_user(self, username: str, password: str):
        self.type(self.INPUT_USERNAME, username)
        self.type(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)

    def assert_login_title(self):
        assert "Swag Labs" in self.driver.title

    # def assert_inventory_url(self):
    #     assert "inventory" in self.driver.current_url, "No te encuentras en /inventory"

    # def assert_error_message():
