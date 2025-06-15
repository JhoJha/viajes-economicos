from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import logging
import traceback
import sys

# ========== CONFIGURACIÓN RUTAS ABSOLUTAS ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR, "logs")
SCREEN_DIR = os.path.join(BASE_DIR, "screenshots")
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREEN_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

# ========== LOGGING CONFIGURADO ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, "execution_log.txt"), mode="w", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

def log(msg):
    print(msg)
    logging.info(msg)

def save_screenshot(driver, name):
    path = os.path.join(SCREEN_DIR, name)
    driver.save_screenshot(path)
    log(f"📸 Captura guardada: {path}")

# ========== CONFIGURACIÓN DEL DRIVER ==========
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113.0")
    options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    log("✅ Driver de Chrome iniciado correctamente.")
    return driver

# ========== FLUJO PRINCIPAL ==========
if __name__ == "__main__":
    driver = None

    try:
        log("🟢 Logging iniciado correctamente.")
        driver = setup_driver()
        wait = WebDriverWait(driver, 15)

        # 1. Ir a RedBus
        log("🌐 Abriendo redbus.pe...")
        driver.get("https://www.redbus.pe")
        wait.until(EC.presence_of_element_located((By.ID, "src")))
        save_screenshot(driver, "01_homepage.png")

        # 2. ORIGEN: Lima (Todos)
        log("⌨️ Esperando campo de entrada origen...")
        input_origen = wait.until(EC.presence_of_element_located((By.ID, "src")))
        input_origen.click()
        input_origen.send_keys("Lima")
        time.sleep(1.5)
        save_screenshot(driver, "02_input_origen_lima.png")

        log("🔍 Buscando sugerencias para 'Lima (Todos)'...")
        time.sleep(1)
        save_screenshot(driver, "debug_sugerencias_origen.png")

        sugerencias_origen = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*[contains(text(), "Lima (Todos)")]')))

        seleccionado = False
        for opcion in sugerencias_origen:
            log(f"🔸 Opción encontrada: {opcion.text}")
            if "lima (todos)" in opcion.text.lower():
                log(f"✅ Seleccionando opción: {opcion.text}")
                opcion.click()
                seleccionado = True
                break

        if not seleccionado:
            raise Exception("❌ No se encontró la opción 'Lima (Todos)' entre las sugerencias.")

        save_screenshot(driver, "02_origin_selected_lima_todos.png")

        # 3. DESTINO: Trujillo (Todos)
        log("🧭 Seleccionando destino: Trujillo...")
        input_destino = wait.until(EC.presence_of_element_located((By.ID, "dest")))
        input_destino.click()
        input_destino.send_keys("Trujillo")
        time.sleep(1)
        sugerencias_destino = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//*[contains(text(), "Trujillo (Todos)")]')))
        for opcion in sugerencias_destino:
            if "trujillo (todos)" in opcion.text.lower():
                log(f"✅ Seleccionando opción: {opcion.text}")
                opcion.click()
                break
        save_screenshot(driver, "03_destination_selected_trujillo_todos.png")

        # 4. FECHA: 15 de junio 2025
        log("📅 Seleccionando fecha de ida: 15/06/2025...")
        calendario = wait.until(EC.element_to_be_clickable((By.ID, "onwardCal")))
        calendario.click()
        time.sleep(1)
        dia_15 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="15"]')))
        dia_15.click()
        save_screenshot(driver, "04_date_selected.png")

        # 5. BUSCAR
        log("🔍 Haciendo clic en BUSCAR...")
        boton_buscar = wait.until(EC.element_to_be_clickable((By.ID, "search_button")))
        boton_buscar.click()
        time.sleep(6)
        save_screenshot(driver, "06_results_loaded.png")

        log("🎯 Fase 1 completada correctamente.")

    except Exception as e:
        log(f"❌ Error crítico: {str(e)}")
        log(traceback.format_exc())

    finally:
        if driver is not None:
            try:
                driver.quit()
                log("🔚 Driver cerrado. Fin del proceso.")
            except Exception as close_err:
                log(f"⚠️ Error al cerrar el driver: {close_err}")
        else:
            log("⚠️ Driver no se inició correctamente.")

