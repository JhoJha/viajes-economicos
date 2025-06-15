# RedBus Scraper 

Este módulo forma parte del proyecto **Guía de Viajes Económicos desde Lima**. Su objetivo es automatizar el proceso de extracción de datos de pasajes de la web [RedBus.pe](https://www.redbus.pe) para realizar análisis comparativos de precios, horarios y servicios en rutas interprovinciales de Perú.

---

##  Características principales

* Extracción directa desde la **API interna** de RedBus (sin scraping de HTML).
* Manejo de headers, cookies y payload en archivo `config.py`.
* Generación de carpetas automática por ciudad y mes.
* Validación de formato de fechas, rango límite y bloqueos por exceso de peticiones (HTTP 429).
* Evita duplicados: no vuelve a scrapear fechas que ya tienen un archivo guardado.
* Guardado de resultados en formato JSON crudo.
* Modularización completa: separación clara entre extracción, procesamiento y ejecución.

---

##  Estructura de carpetas

```
scraper/
├── redbus_scraper/
│   ├── config/
│   │   ├── config.py          # Headers, cookies y body para requests POST
│   │   └── city_ids.json      # Diccionario ciudad → ID de RedBus
│   ├── data/                  # Carpeta base (no contiene los viajes)
│   ├── driver/                # Recursos como chromedriver si se usara Selenium
│   ├── logs/                  # Logs generados automáticamente (futuro)
│   ├── screenshots/           # Capturas de Selenium en fase 1 (opcional)
│   ├── extractor.py           # Función scrape_redbus() con validaciones robustas
│   ├── procesador.py          # Procesamiento modular (JSON → CSV, consola, resumen, etc.)
│   ├── main.py                # Fase 1: Navegación automatizada con Selenium
│   ├── fase2_runner.py        # Fase 2: Ejecutar múltiples fechas de una ruta
│   └── runner_general.py      # Versión interactiva completa: ciudades + fechas desde consola
```

---

## ⚙️ Código modularizado y funciones clave

### 🔹 `scrape_redbus(...)` en `extractor.py`

```python
scrape_redbus(
    from_city_id=195105,
    to_city_id=195256,
    from_name="Lima (Todos)",
    to_name="Trujillo (Todos)",
    date_str="15-Jun-2025",
    output_dir=Path("data/redbus/Trujillo/junio")
)
```

Esta función incluye:

* Manejo de errores HTTP (429, 403)
* Validación del formato de fecha
* Salto automático si el archivo ya existe
* Delay aleatorio entre peticiones

### 🔹 `runner_general.py` (interactivo)

* Solicita ciudad origen y destino
* Solicita fechas en formato YYYY-MM-DD
* Valida errores comunes
* Ejecuta scraping en lote solo si es válido

---

## ⚡ Uso rápido

```bash
python scraper/redbus_scraper/runner_general.py
```

### Ingresar por consola:

* Ciudad origen (copiar desde city\_ids.json, ej: `Lima (Todos)`)
* Ciudad destino (ej: `Trujillo (Todos)`)
* Fecha inicio: `2025-07-01`
* Fecha fin: `2025-07-31`

El sistema creará automáticamente carpetas como:

```
data/redbus/Trujillo/julio/api_response_20250726.json
```

---

##  Flujo de trabajo por fases

| Fase   | Descripción                                                              |
| ------ | ------------------------------------------------------------------------ |
| Fase 1 | `main.py`: Prueba con Selenium para observar el comportamiento de RedBus |
| Fase 2 | `fase2_runner.py`: Ejecutar múltiples fechas de una sola ruta            |
| Fase 3 | `runner_general.py`: Ejecutar scraping para fechas y rutas completas     |
| Fase 4 | `procesador.py`: Exportar resultados a consola, CSV o JSON simplificado  |

---

##  Requisitos

Instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

##  Pendientes / Siguientes pasos

* Automatizar scraping para múltiples rutas en bucle
* Validación de precios inusuales o caídas de precio
* Persistencia en base de datos SQLite
* Panel de visualización de precios históricos
* Integración con otras fuentes: clima, hospedaje, etc.

---

##  Licencia

Este proyecto es de uso académico y educativo. Todos los datos se extraen para fines de análisis no lucrativo.

---
