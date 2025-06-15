# 🚌 RedBus Scraper – Fase 1

Proyecto parte de **"Guía de Viajes Económicos desde Lima"**, donde se automatiza la búsqueda de pasajes en [redbus.pe](https://www.redbus.pe) utilizando **Selenium + Python**.

---

## 📌 Objetivo de la Fase 1
Automatizar el llenado del formulario en RedBus.pe para buscar pasajes desde **Lima (Todos)** hasta **Trujillo (Todos)** en una fecha determinada (15 de junio de 2025), simulando la interacción humana real:

### Pasos automatizados:
1. Iniciar WebDriver con configuración personalizada
2. Abrir la web [https://www.redbus.pe](https://www.redbus.pe)
3. Escribir y seleccionar:
   - **Origen:** Lima (Todos)
   - **Destino:** Trujillo (Todos)
4. Elegir fecha: 15/06/2025
5. Hacer clic en **Buscar**
6. Capturar evidencias de cada paso (screenshots)
7. Registrar logs detallados del proceso

---

## 📸 Evidencias
Las siguientes capturas fueron tomadas durante la ejecución:

| Paso | Captura |
|------|---------|
| HomePage cargada | `01_homepage.png` |
| Entrada de "Lima" | `02_input_origen_lima.png` |
| Selección de "Lima (Todos)" | `02_origin_selected_lima_todos.png` |
| Selección de "Trujillo (Todos)" | `03_destination_selected_trujillo_todos.png` |
| Fecha seleccionada | `04_date_selected.png` |
| Resultados cargados | `06_results_loaded.png` |

---

## 🧠 Lógica técnica destacada
- Uso de `WebDriverWait` con `expected_conditions` para evitar errores por carga lenta
- XPath flexible y tolerante para capturar opciones tipo "Lima (Todos)"
- Capturas automáticas para depuración y documentación
- Logs automáticos con `logging` configurado a nivel profesional
- Separación de rutas: `logs/`, `screenshots/`, `data/`

---

## ⚙️ Tecnologías
- Python 3.13
- Selenium 4.x
- WebDriver Manager
- VSCode
- Git + GitHub

---

## 🚀 Próximos pasos (Fase 2)
- Extraer los datos de los resultados mostrados (precios, empresas, horarios)
- Guardarlos en archivos CSV o en una base de datos SQLite
- Manejar paginación y diferentes fechas

---

## 📂 Estructura del scraper
```
viajes-economicos/
└── scraper/
    └── redbus_scraper/
        ├── main.py
        ├── logs/
        │   └── execution_log.txt
        ├── screenshots/
        │   ├── 01_homepage.png
        │   ├── 02_input_origen_lima.png
        │   ├── ...
        └── data/   
```

---

## 👨‍💻 Autor
**Jhon**, estudiante de Ingeniería Estadística e Informática.

---

## 🌐 Licencia
MIT – Libre para estudiar, modificar y mejorar 
