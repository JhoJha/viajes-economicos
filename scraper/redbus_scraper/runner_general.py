import sys
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta

# Asegurar imports desde raíz del proyecto
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from scraper.redbus_scraper.extractor import scrape_redbus

# ========== CONFIGURACIÓN ==========
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Ruta al diccionario de ciudades
city_ids_path = Path("scraper/redbus_scraper/config/city_ids.json")

if not city_ids_path.exists():
    logging.error("❌ No se encontró el archivo city_ids.json")
    sys.exit()

with open(city_ids_path, "r", encoding="utf-8") as f:
    city_ids = json.load(f)

# ========== INPUT INTERACTIVO ==========
print("\n🗺️  Ciudades disponibles:")
for ciudad in city_ids:
    print("   -", ciudad)

from_name = input("\n🔹 Ingresa ciudad de origen EXACTA (copiar/pegar de arriba): ").strip()
to_name = input("🔹 Ingresa ciudad de destino EXACTA: ").strip()

if from_name not in city_ids or to_name not in city_ids:
    logging.error("⛔ Error: nombre de ciudad inválido. Debe coincidir exactamente.")
    sys.exit()

from_city_id = city_ids[from_name]
to_city_id = city_ids[to_name]

fecha_inicio_str = input("📅 Fecha inicio (YYYY-MM-DD): ").strip()
fecha_fin_str = input("📅 Fecha fin (YYYY-MM-DD): ").strip()

# ========== VALIDACIÓN DE FECHAS ==========
try:
    fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin_str, "%Y-%m-%d")
except ValueError:
    logging.error("❌ Las fechas deben tener formato YYYY-MM-DD")
    sys.exit()

if fecha_inicio > fecha_fin:
    logging.error("❌ Fecha de inicio no puede ser mayor que la final.")
    sys.exit()

hoy = datetime.now()
if fecha_inicio < hoy:
    logging.warning("⚠️ Atención: estás incluyendo fechas pasadas. Puede que no haya resultados.")

MAX_DIAS = 45
if (fecha_fin - fecha_inicio).days + 1 > MAX_DIAS:
    logging.error(f"⚠️ Rango muy amplio. Máximo permitido: {MAX_DIAS} días.")
    sys.exit()

# ========== DICCIONARIO DE MESES EN ESPAÑOL ==========
meses_es = {
    1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
    5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
    9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
}

# ========== LOOP DE SCRAPING ==========
fechas = [(fecha_inicio + timedelta(days=i)).strftime("%d-%b-%Y")
          for i in range((fecha_fin - fecha_inicio).days + 1)]

total = len(fechas)
exitos = 0
fallos = 0

logging.info(f"🚀 Iniciando scraping: {from_name} → {to_name} | Total: {total} fechas")

for i, fecha_str in enumerate(fechas, start=1):
    try:
        fecha_obj = datetime.strptime(fecha_str, "%d-%b-%Y")
        nombre_mes = meses_es[fecha_obj.month]
        fecha_archivo = fecha_obj.strftime("%Y%m%d")

        output_dir = Path(f"data/redbus/{to_name.split()[0]}/{nombre_mes}")
        output_dir.mkdir(parents=True, exist_ok=True)

        archivo_json = output_dir / f"api_response_{fecha_archivo}.json"
        if archivo_json.exists():
            logging.info(f"📁 Ya existe: {archivo_json}, saltando...")
            continue

        logging.info(f"📆 Procesando fecha {i}/{total}: {fecha_str}")
        scrape_redbus(
            from_city_id=from_city_id,
            to_city_id=to_city_id,
            from_name=from_name,
            to_name=to_name,
            date_str=fecha_str,
            output_dir=output_dir
        )
        exitos += 1

    except Exception as e:
        logging.error(f"❌ Fallo al procesar {fecha_str}: {e}")
        fallos += 1

# ========== RESUMEN FINAL ==========
logging.info(f"✅ Scraping terminado | Éxitos: {exitos} | Fallos: {fallos}")
