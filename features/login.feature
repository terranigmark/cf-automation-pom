Feature: Autenticación de usuario

  Como usuario registrado
  Quiero poder iniciar sesión
  Para acceder a mis funcionalidades restringidas

  Scenario: Login exitoso
    Given el usuario ingresa a la página de login
    When el usuario introduce credenciales válidas
    Then debería ver la página segura

  Scenario: Login fallido
    Given el usuario ingresa a la página de login
    When el usuario introduce credenciales inválidas
    Then debería ver un mensaje de error
