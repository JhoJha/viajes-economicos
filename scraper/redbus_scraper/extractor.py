import requests
import json
import logging
from datetime import datetime

# ========== CONFIGURAR LOGGING ==========
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ========== PARÁMETROS ==========
from_city_id = 195105  # Lima (Todos)
to_city_id = 195256    # Trujillo (Todos)
date = '15-Jun-2025'

# ========== URL DE LA API ==========
url = (
    f"https://www.redbus.pe/search/SearchV4Results"
    f"?fromCity={from_city_id}&toCity={to_city_id}"
    f"&src=Lima%20(Todos)&dst=Trujillo%20(Todos)"
    f"&DOJ={date}&sectionId=0&groupId=0"
    f"&limit=0&offset=0&sort=0&sortOrder=0&meta=true&returnSearch=0"
)

# ========== HEADERS Y COOKIES ==========
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "es-ES,es;q=0.9",
    "content-type": "application/json",
    "origin": "https://www.redbus.pe",
    "referer": "https://www.redbus.pe/pasajes-de-bus/lima-a-trujillo",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/137.0.0.0 Safari/537.36",
}

# Las cookies son largas, puedes copiar las que te pasé como string o extraerlas con Selenium si prefieres
cookies = {
    "country": "PER",
    "currency": "PEN",
    "language": "es",
    "defaultCountry": "PER",
    # Agrega aquí otras cookies clave como deviceSessionId, _ga, etc si fallara el request
}

# ========== BODY ==========
body = {
    "onlyShow": [],
    "dt": [],
    "SeaterType": [],
    "AcType": [],
    "travelsList": [],
    "amtList": [],
    "bpList": [],
    "dpList": [],
    "CampaignFilter": [],
    "rtcBusTypeList": [],
    "at": [],
    "persuasionList": [],
    "bpIdentifier": [],
    "bcf": [],
    "opBusTypeFilterList": []
}

# ========== EJECUCIÓN ==========
logging.info("🔍 Enviando solicitud a la API interna de RedBus...")

response = requests.post(url, headers=headers, cookies=cookies, json=body)

if response.status_code == 200:
    logging.info("✅ Respuesta recibida correctamente.")
    
    # Guardar respuesta
    data = response.json()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"data/api_response_{timestamp}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    logging.info(f"📁 Datos guardados en: {output_path}")

else:
    logging.error(f"❌ Error en la solicitud. Código: {response.status_code}")
