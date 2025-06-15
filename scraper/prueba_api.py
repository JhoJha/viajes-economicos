import os
import sys
import json
import time
import logging
import requests
from datetime import datetime

# 👉 Agregamos el path raíz para imports robustos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scraper.redbus_scraper.config.config import HEADERS, COOKIES, BODY

def prueba_api():
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    # Datos de prueba
    from_city_id = 195105
    to_city_id = 195256
    from_name = "Lima (Todos)"
    to_name = "Trujillo (Todos)"
    date_str = "15-Jun-2025"

    # Construcción de URL
    url = (
        f"https://www.redbus.pe/search/SearchV4Results"
        f"?fromCity={from_city_id}&toCity={to_city_id}"
        f"&src={from_name.replace(' ', '%20')}&dst={to_name.replace(' ', '%20')}"
        f"&DOJ={date_str}&sectionId=0&groupId=0"
        f"&limit=20&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0"
    )

    logging.info("🔍 Enviando prueba a API RedBus...")

    try:
        response = requests.post(url, headers=HEADERS, cookies=COOKIES, json=BODY, timeout=15)
        logging.info(f"📡 Código de estado: {response.status_code}")

        data = response.json()

        if "onwardflights" not in data or not data["onwardflights"]:
            logging.warning("⚠️ No se encontraron viajes o 'onwardflights' está vacío.")
        else:
            logging.info(f"✅ Se encontraron {len(data['onwardflights'])} viajes.")
        
        # Guardar archivo
        os.makedirs("pruebas_unitarias", exist_ok=True)
        output_path = os.path.join("pruebas_unitarias", f"test_api_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logging.info(f"📁 Respuesta guardada en: {output_path}")

    except Exception as e:
        logging.error(f"❌ Error inesperado: {e}")

    # Delay para evitar bloqueos
    time.sleep(2)

if __name__ == "__main__":
    prueba_api()
