# Guía de Viajes Económicos desde Lima

Una aplicación web desarrollada con **Python y Streamlit** que te recomienda destinos de viaje desde Lima según tu presupuesto, el clima que prefieres y los precios actuales de pasajes y hospedaje.

---

## ¿Qué hace esta app?

- Te pregunta cuánto quieres gastar y qué clima prefieres.
- Consulta datos reales (scraping y APIs) sobre precios de viaje y clima.
- Te recomienda los destinos más baratos y adecuados para ti.
- Te muestra todo en una interfaz web bonita e interactiva.

---

## Tecnologías usadas

- Python
- Streamlit (frontend)
- Pandas
- Web Scraping (RedBus, Civa, etc.)
- APIs:
  - OpenWeatherMap (clima)
  - SUNAT / ExchangeRate (tipo de cambio)
  - Pixabay / Unsplash (imágenes)

---

## ¿Cómo ejecutar el proyecto?

```bash
# 1. Clona el repositorio
git clone git@github.com:JhoJha/viajes-economicos.git

# 2. Entra al proyecto
cd viajes-economicos

# 3. Activa tu entorno virtual y ejecuta
pip install -r requirements.txt
streamlit run main.py
```

## Estructura del proyecto
```bash
viajes-economicos/
│
├── main.py                # Interfaz con Streamlit
├── backend/               # Lógica y procesamiento
├── datos/                 # Archivos de datos
├── assets/                # Imágenes o íconos
├── README.md              # Este documento
└── requirements.txt       # Librerías necesarias
```
