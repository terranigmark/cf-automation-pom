from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    URL = "http://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button.radius")
        self.flash_message = (By.ID, "flash")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def get_flash_text(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.flash_message))
        return self.driver.find_element(*self.flash_message).text