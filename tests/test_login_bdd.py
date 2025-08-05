import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.the_internet.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Enlaza los escenarios
scenarios('../features/login.feature')

@pytest.fixture
def login_page():
    return {}

@pytest.fixture
def driver():
    from selenium import webdriver
    d = webdriver.Chrome()
    yield d
    d.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@given('el usuario ingresa a la página de login')
def step_impl(login_page):
    login_page.load()

@when('el usuario introduce credenciales válidas')
def step_impl(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")

@when('el usuario introduce credenciales inválidas')
def step_impl(login_page):
    login_page.login("invalid", "invalid")

@then('debería ver la página segura')
def step_impl(driver, login_page):
    WebDriverWait(driver, 10).until(EC.url_contains("/secure"))
    assert "Secure Area" in driver.title, "Validar titulo pagina segura"
    driver.quit()

@then('debería ver un mensaje de error')
def step_impl(login_page):
    flash_text = login_page.get_flash_text()
    assert "Your username is invalid!" in flash_text
