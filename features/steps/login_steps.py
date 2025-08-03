from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('el usuario ingresa a la página de login')
def step_impl(context):
    # Crear el driver se ejecutara dese $proyecto/environment.py
    #context.driver = webdriver.Chrome()
    context.driver.get("http://the-internet.herokuapp.com/login")

@when('el usuario introduce credenciales válidas')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("tomsmith")
    context.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    context.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

@when('el usuario introduce credenciales inválidas')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys("invalid")
    context.driver.find_element(By.ID, "password").send_keys("invalid")
    context.driver.find_element(By.CSS_SELECTOR, "button.radius").click()

@then('debería ver la página segura')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("/secure"))
    assert "Secure Area" in context.driver.title, "Validar titulo pagina segura"
    context.driver.quit()

@then('debería ver un mensaje de error')
def step_impl(context):
    error = context.driver.find_element(By.ID, "flash")
    assert "Your username is invalid!" in error.text
    # El driver.quit se ejecutara dese $proyecto/environment.py
    #context.driver.quit()