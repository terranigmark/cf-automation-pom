import pytest
from pytest_bdd import scenarios, given, when, then
from pages.api.api_helper import APIHelper

# Enlaza los escenarios del .feature
scenarios('../features/api_login.feature')

# Fixture compartido que simula el 'context' de Behave
@pytest.fixture
def contexto():
    return {}

@given("el servicio de autenticación está disponible")
def verificar_servicio():
    api = APIHelper()
    assert api.is_service_up()

@when("envío credenciales válidas a /api/login")
def login_valido(contexto):
    api = APIHelper()
    contexto["response"] = api.login("eve.holt@reqres.in", "cityslicka")

@when("envío credenciales inválidas a /api/login")
def login_invalido(contexto):
    api = APIHelper()
    contexto["response"] = api.login("invalid", "wrong")

@then("debería recibir un token en la respuesta")
def verificar_token(contexto):
    r = contexto["response"]
    assert r.status_code == 200
    assert "token" in r.json()

@then("debería recibir un error 401")
def verificar_error(contexto):
    r = contexto["response"]
    assert r.status_code in (400, 401)
