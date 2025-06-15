import os
import json
import time
import random
import logging
from datetime import datetime
import requests
from scraper.redbus_scraper.config.config import HEADERS, COOKIES, BODY  # Asegúrate de que config.py esté en el mismo paquete

def scrape_redbus(from_city_id, to_city_id, from_name, to_name, date_str, output_dir):
    """
    Realiza scraping a la API de RedBus y guarda el JSON crudo.
    Incluye validaciones de fecha, manejo de errores y adaptabilidad a bloqueos.
    """

    # Validar formato de fecha
    try:
        date_obj = datetime.strptime(date_str, "%d-%b-%Y")
    except ValueError:
        logging.error(f"❌ Fecha inválida: '{date_str}'. Usa formato 'DD-MMM-YYYY' (ej. 15-Jun-2025)")
        return

    # Crear carpeta si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Construir URL con parámetros
    url = (
        f"https://www.redbus.pe/search/SearchV4Results"
        f"?fromCity={from_city_id}&toCity={to_city_id}"
        f"&src={from_name.replace(' ', '%20')}&dst={to_name.replace(' ', '%20')}"
        f"&DOJ={date_str}&sectionId=0&groupId=0"
        f"&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0"
    )

    logging.info(f"🔍 Buscando: {from_name} → {to_name} | Fecha: {date_str}")

    try:
        response = requests.post(url, headers=HEADERS, cookies=COOKIES, json=BODY, timeout=15)

        # Manejo de bloqueos
        if response.status_code == 429:
            logging.warning("⚠️ Código 429 (Too Many Requests): Aumentando delay para evitar bloqueo.")
            time.sleep(random.uniform(10, 20))
            return

        if response.status_code == 403:
            logging.error("⛔ Código 403 (Forbidden): IP posiblemente bloqueada.")
            return

        response.raise_for_status()
        data = response.json()

        # Validar contenido de resultados
        results = data.get("onwardflights", [])
        if not results:
            logging.warning("⚠️ Respuesta sin viajes. Puede ser error silencioso o no hay buses.")
        else:
            logging.info(f"✅ {len(results)} resultados encontrados.")

        # Guardar archivo
        fecha_formato = date_obj.strftime("%Y%m%d")
        nombre_archivo = f"api_response_{fecha_formato}.json"
        ruta_salida = os.path.join(output_dir, nombre_archivo)

        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logging.info(f"📁 Archivo guardado en: {ruta_salida}")

    except requests.exceptions.Timeout:
        logging.error("⏱️ Timeout: El servidor no respondió a tiempo.")
    except requests.RequestException as e:
        logging.error(f"❌ Error de red: {e}")
    except Exception as e:
        logging.error(f"❌ Error inesperado: {e}")

    # Delay adaptativo entre llamadas
    delay = random.uniform(5, 10)
    logging.info(f"🕒 Esperando {delay:.2f} segundos antes de continuar...")
    time.sleep(delay)
