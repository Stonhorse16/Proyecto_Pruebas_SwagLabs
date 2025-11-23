import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


if not os.path.exists("../evidencias"):
    os.makedirs("../evidencias")

print("🔹 Iniciando Script 1 (CP-01): Login Exitoso...")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) 

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2) 


    url_actual = driver.current_url
    
    if "inventory.html" in url_actual:
        print(" PRUEBA EXITOSA: Login correcto.")

        nombre_foto = "../evidencias/CP01_Exito_Login.png"
        driver.save_screenshot(nombre_foto)
        print(f" Evidencia guardada en: {nombre_foto}")
        
    else:
        print(f" PRUEBA FALLIDA: No entró al sistema. URL: {url_actual}")

except Exception as e:
    print(f" Error: {e}")

finally:

    driver.quit()
    print(" Fin de la prueba.")