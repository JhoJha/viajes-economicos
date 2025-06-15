import json
import csv
import logging
from datetime import datetime
from pathlib import Path

# ========== CONFIGURACIÓN ==========
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
input_path = Path("data/api_response_20250615_005630.json")
output_base = Path("data/salida_redbus")

# ========== CARGAR JSON ==========
try:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        inventarios = data["inventories"]
except Exception as e:
    logging.error(f"❌ No se pudo cargar el JSON: {e}")
    exit()

# ========== PARSEO ==========
viajes = []
for bus in inventarios:
    try:
        viajes.append({
            "empresa": bus.get("travelsName", "Desconocida"),
            "hora_salida": bus.get("departureTime", "")[:16],
            "hora_llegada": bus.get("arrivalTime", "")[:16],
            "precio_min": min(bus["fareList"]) if "fareList" in bus else 0.0,
            "precio_max": max(bus["fareList"]) if "fareList" in bus else 0.0,
            "asientos_disponibles": bus.get("availableSeats", 0),
            "tipo_bus": bus.get("busType", "No especificado"),
            "duracion_min": bus.get("journeyDurationMin", None),
            "punto_partida": bus["bpData"][0]["Name"] if bus.get("bpData") else "N/D",
            "punto_llegada": bus["dpData"][0]["Name"] if bus.get("dpData") else "N/D",
        })
    except Exception as e:
        logging.warning(f"⚠️ Error procesando un viaje: {e}")

# ========== MOSTRAR EN CONSOLA ==========
logging.info(f"🚌 Total de viajes extraídos: {len(viajes)}")
for v in viajes[:5]:
    print(f"- {v['empresa']} | {v['hora_salida']} → {v['hora_llegada']} | S/.{v['precio_min']} - {v['precio_max']}")

# ========== GUARDAR EN CSV ==========
csv_path = output_base.with_suffix(".csv")
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=viajes[0].keys())
    writer.writeheader()
    writer.writerows(viajes)
logging.info(f"✅ CSV guardado en {csv_path}")

# ========== GUARDAR EN JSON SIMPLIFICADO ==========
json_path = output_base.with_suffix(".json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(viajes, f, indent=2, ensure_ascii=False)
logging.info(f"✅ JSON simplificado guardado en {json_path}")
