import sys
import logging
from pathlib import Path
from datetime import datetime

# Hacer que el script funcione aunque se ejecute desde otra ubicación
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from scraper.redbus_scraper.extractor import scrape_redbus

# ========== CONFIGURACIÓN GLOBAL ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Parámetros de ciudad
from_city_id = 195105
from_name = "Lima (Todos)"
to_city_id = 195256
to_name = "Trujillo (Todos)"

# Fechas objetivo (fase 2)
fechas = [
    "13-Jun-2025",
    "14-Jun-2025",
    "15-Jun-2025",
    "16-Jun-2025",
    "17-Jun-2025"
]

# Validar fechas antes de empezar
for fecha in fechas:
    try:
        datetime.strptime(fecha, "%d-%b-%Y")
    except ValueError:
        logging.error(f"❌ Fecha mal formateada: {fecha}. Usa formato 'DD-MMM-YYYY'")
        exit()

# Carpeta de destino
output_dir = Path("data/redbus/Trujillo/junio")
output_dir.mkdir(parents=True, exist_ok=True)

# ======= EJECUCIÓN CONTROLADA POR LOTE =======
logging.info("🚀 Iniciando scraping en lote...")
total = len(fechas)

for i, fecha in enumerate(fechas, start=1):
    logging.info(f"📆 Procesando fecha {i}/{total}: {fecha}")
    try:
        scrape_redbus(
            from_city_id=from_city_id,
            to_city_id=to_city_id,
            from_name=from_name,
            to_name=to_name,
            date_str=fecha,
            output_dir=output_dir
        )
    except Exception as e:
        logging.error(f"❌ Fallo al procesar {fecha}: {e}")
        continue

logging.info("✅ Fase 2 completada con todos los intentos ejecutados.")
