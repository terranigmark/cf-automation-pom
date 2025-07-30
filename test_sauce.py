import os.path
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized") #Abrimos el navegador maximizado
    options.add_argument("--incognito") #Modo incognito
    # options.add_argument("--window-size=1280,720") #Tener la ventana en un tamaño exacto
    # driver.set_window_size(1280, 720)

    driver = webdriver.Chrome(options=options)
    # ESPERAS EXPLICITAS
    # Es dinámico. Dependo de condiciones.
    # ESPERAS IMPLICITAS
    # Es estático. Tiempo exacto

    driver.implicitly_wait(5)
    # time.sleep(2)
    yield driver # Yo use el navegador en cada test

    driver.quit() #  cerrar el navegador independientemente de que la prueba falle o no

# PRIMERA PRUEBA: LOGIN EXITOSO
def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/") # Abre la pagina
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    # Enviar usuario y contraseña. Luego darle clic en el botón login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


    WebDriverWait(driver,10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME,"title").text == "Products"
    time.sleep(2)

# SEGUNDA PRUEBA: LOGIN INCORRECTO
def test_login_incorrecto(driver):
    driver.get("https://www.saucedemo.com/")  # Abre la pagina
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    # Enviar usuario y contraseña. Luego darle clic en el botón login
    driver.find_element(By.ID, "user-name").send_keys("ssss")
    driver.find_element(By.ID, "password").send_keys("sssss")
    driver.find_element(By.ID, "login-button").click()

    # Esperamos el mensaje de error
    error = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))

    assert "Epic sadface" in error.text
    time.sleep(2)

# TERCERA PRUEBA: CAPTURA DE PANTALLA SI FALLA
def test_captura_fallo(driver):
    driver.get("https://www.saucedemo.com/")  # Abre la pagina
    try:
        driver.find_element(By.ID, "elemento-falso") # El código va a intentar ejecutar esta línea, no lo va a encontrar y va a ejecutar la excepción
    except Exception as e:

        carpeta = "screeshots"
        nombre = f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        ruta_archivo = os.path.join(carpeta, nombre)
        #ruta_archivo = os.path.join(carpeta, "error_login.png")

        driver.save_screenshot(ruta_archivo)

        #driver.save_screenshot("error_test.png") # Captura de pantalla y guardado
        raise e

# CUARTA PRUEBA: MANEJO DE ESTADO
def test_login_logout(driver):
    driver.get("https://www.saucedemo.com/")  # Abre la pagina

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))

    # Enviar usuario y contraseña. Luego darle clic en el botón login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    login_button = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "login-button")))

    assert login_button.is_displayed()
    time.sleep(2)


# QUINTA PRUEBA: ALERTA VISIBLE
def test_alerta_con_demoqa(driver):
    driver.get("https://demoqa.com/alerts")

    boton_alerta = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"alertButton")))
    time.sleep(2)
    # SCROLL PARA VER EL BOTON
    driver.execute_script("arguments[0].scrollIntoView(true);", boton_alerta)
    time.sleep(2)

    boton_alerta.click()
    time.sleep(2)

    alert = WebDriverWait(driver,10).until(EC.alert_is_present())
    assert "You clicked a button" in alert.text
    alert.accept()
    time.sleep(2)