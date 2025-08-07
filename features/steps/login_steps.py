from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.the_internet.login_page import LoginPage

@given('el usuario ingresa a la página de login')
def step_impl(context):
    # Crear el driver se ejecutara dese $proyecto/environment.py
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('el usuario introduce credenciales válidas')
def step_impl(context):
    context.login_page.login("tomsmith", "SuperSecretPassword!")

@when('el usuario introduce credenciales inválidas')
def step_impl(context):
    context.login_page.login("invalid", "invalid")

@then('debería ver la página segura')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("/secure"))
    assert "Secure Area" in context.driver.title, "Validar titulo pagina segura"
    context.driver.quit()

@then('debería ver un mensaje de error')
def step_impl(context):
    flash_text = context.login_page.get_flash_text()
    assert "Your username is invalid!" in flash_text
    context.driver.quit()