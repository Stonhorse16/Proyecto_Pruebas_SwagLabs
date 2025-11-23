import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURACION ---
if not os.path.exists("../evidencias"):
    os.makedirs("../evidencias")

print("Iniciando Script 2 (CP-02): Usuario Bloqueado...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. Entrar al sitio
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)

    # 2. Ingresar usuario BLOQUEADO
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # 3. Clic en Login
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) # Esperamos a que salga el error

    # --- VALIDACION ---
    # Buscamos el texto del elemento h3 que tiene el error
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    print("Mensaje detectado: " + mensaje_error)
    
    # Verificamos si dice lo que esperamos
    if "Sorry, this user has been locked out" in mensaje_error:
        print("[EXITO] El sistema detecto el bloqueo correctamente.")
        
        # Foto de evidencia
        nombre_foto = "../evidencias/CP02_Bloqueo.png"
        driver.save_screenshot(nombre_foto)
        print("Evidencia guardada en: " + nombre_foto)
        
    else:
        print("[FALLO] El mensaje no es el correcto.")

except Exception as e:
    print("Error: " + str(e))

finally:
    driver.quit()
    print("Fin de la prueba.")