# Guía de Viajes Económicos desde Lima

Una aplicación web desarrollada con Python y Streamlit que recomienda destinos de viaje desde Lima según tu presupuesto, el clima que prefieres y los precios reales de pasajes y hospedaje.

---

## ¿Qué hace esta app?

- Te pregunta cuánto quieres gastar, qué clima prefieres y en qué fecha deseas viajar.
- Consulta datos reales (scraping + APIs) sobre precios y clima.
- Calcula los destinos más económicos y adecuados para ti.
- Muestra los resultados en una interfaz web simple y amigable.

---

## ⚙️ Tecnologías utilizadas

| Herramienta       | Propósito                                |
|-------------------|-------------------------------------------|
| Python            | Lógica principal del sistema              |
| Streamlit         | Interfaz web (frontend)                   |
| Pandas            | Procesamiento de datos tabulares          |
| BeautifulSoup     | Scraping web de páginas como RedBus       |
| Requests          | Consumo de APIs                           |
| Git + GitHub      | Control de versiones y colaboración       |
| GitHub Actions    | Automatización del flujo DevOps           |

### APIs usadas:
- **OpenWeatherMap**: clima actual por ciudad
- **SUNAT o ExchangeRate API**: tipo de cambio actual
- **Pixabay / Unsplash**: imágenes de destinos

---

## 💻 ¿Cómo ejecutar el proyecto?

```bash
# 1. Clona el repositorio
git clone git@github.com:JhoJha/viajes-economicos.git

# 2. Entra al proyecto
cd viajes-economicos

# 3. Crea y activa el entorno virtual (Linux/Mac)
python3 -m venv venv
source venv/bin/activate

# 4. Instala las dependencias
pip install -r requirements.txt

# 5. Ejecuta la app
streamlit run frontend/main.py
```

---

## 📂 Estructura del proyecto

```
viajes-economicos/
├── backend/                 # Lógica principal del sistema
│   ├── evaluador.py         # Evaluación de destinos y filtros
│   ├── clima_api.py         # Obtención del clima por API
│   ├── tipo_cambio_api.py   # Conversión de moneda
│   ├── imagenes_api.py      # Imágenes de los destinos
│
├── scraper/                # Módulos de scraping de datos reales
│   ├── scraping_pasajes.py
│   ├── scraping_hospedajes.py
│
├── frontend/               # Interfaz de usuario con Streamlit
│   └── main.py
│
├── datos/                  # Archivos .csv o .json generados
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔄 DevOps aplicado en este proyecto

> Este proyecto simula un entorno profesional de desarrollo de software aplicando buenas prácticas DevOps:

- Uso de **Git y GitHub** para trabajo colaborativo con ramas por rol.
- Uso de **entorno virtual y requirements.txt** para mantener consistencia entre equipos.
- Configuración inicial de **GitHub Actions** para automatizar pruebas o despliegues (CI/CD).
- Organización del proyecto en carpetas modulares: `backend/`, `scraper/`, `frontend/`.

---

## Estado actual

- ✅ Repositorio estructurado y funcional
- ✅ Archivos creados y separados por responsabilidad
- 🛠️ En desarrollo: scraping real, conexión completa a APIs y pruebas
EOF
