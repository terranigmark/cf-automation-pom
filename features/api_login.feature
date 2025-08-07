Feature: Autenticación vía API

  Como consumidor del servicio de autenticación
  Quiero validar el comportamiento del endpoint /api/login
  Para asegurarme de que responde correctamente a distintas credenciales

  Background:
    Given el servicio de autenticación está disponible

  Scenario: Login exitoso con credenciales válidas
    When envío credenciales válidas a /api/login
    Then debería recibir un token en la respuesta

  Scenario: Login fallido con credenciales inválidas
    When envío credenciales inválidas a /api/login
    Then debería recibir un error 401
