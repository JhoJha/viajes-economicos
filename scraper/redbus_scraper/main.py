from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

# 📁 Crear carpeta si no existe
os.makedirs("screenshots", exist_ok=True)

# ⚙️ Configurar opciones de Chrome
options = Options()
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36")

# 🚀 Iniciar navegador con WebDriver Manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("[INFO] Abriendo redbus.pe...")
    driver.get("https://www.redbus.pe/")
    time.sleep(5)

    print("[INFO] Tomando captura de pantalla...")
    driver.save_screenshot("screenshots/01_homepage.png")

    print("[ÉXITO] Captura guardada como screenshots/01_homepage.png")

except Exception as e:
    print(f"[ERROR] {e}")

finally:
    driver.quit()
