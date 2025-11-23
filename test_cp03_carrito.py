import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURACION ---
if not os.path.exists("../evidencias"):
    os.makedirs("../evidencias")

print("Iniciando Script 3 (CP-03): Agregar al Carrito (Version Robusta)...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1. INICIAR SESION
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Login enviado. Esperando inventario...")
    time.sleep(3)

    # 2. VALIDAR QUE ESTEMOS DENTRO
    if "inventory.html" not in driver.current_url:
        print("[ERROR CRITICO] No se logro entrar al inventario.")
        driver.save_screenshot("../evidencias/ERROR_Login_CP03.png")
        raise Exception("Fallo el login inicial")

    # 3. AGREGAR EL PRIMER PRODUCTO DE LA LISTA
    # En lugar de buscar por ID, buscamos todos los botones de inventario
    # y le damos clic al primero [0]
    print("Buscando botones de producto...")
    botones = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    
    if len(botones) > 0:
        botones[0].click() # Clic al primer producto (Mochila usualmente)
        print("Clic realizado en el primer producto.")
        time.sleep(2) # Esperar a que reaccione el carrito
    else:
        raise Exception("No se encontraron productos en la pantalla.")

    # 4. VALIDAR EL CARRITO
    try:
        carrito_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        
        if carrito_badge == "1":
            print("[EXITO] Se detecto el numero 1 en el carrito.")
            nombre_foto = "../evidencias/CP03_Carrito.png"
            driver.save_screenshot(nombre_foto)
            print("Evidencia guardada en: " + nombre_foto)
        else:
            print("[FALLO] El carrito tiene otro numero: " + carrito_badge)
            
    except Exception as e_badge:
        print("[FALLO] El carrito sigue vacio (No aparece el numero rojo).")
        driver.save_screenshot("../evidencias/ERROR_Carrito_Vacio.png")

except Exception as e:
    print("Error durante la prueba: " + str(e))

finally:
    driver.quit()
    print("Fin de la prueba.")