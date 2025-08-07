from behave import given, when, then
from pages.api.api_helper import APIHelper

@given('el servicio de autenticación está disponible')
def step_impl(context):
    api = APIHelper()
    assert api.is_service_up()

@when('envío credenciales válidas a /api/login')
def step_impl(context):
    api = APIHelper()
    context.response = api.login("eve.holt@reqres.in", "cityslicka")

@when('envío credenciales inválidas a /api/login')
def step_impl(context):
    api = APIHelper()
    context.response = api.login("invalid", "wrong")

@then('debería recibir un token en la respuesta')
def step_impl(context):
    assert context.response.status_code == 200
    data = context.response.json()
    assert "token" in data

@then('debería recibir un error 401')
def step_impl(context):
    assert context.response.status_code in (400, 401)