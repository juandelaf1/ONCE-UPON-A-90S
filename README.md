# 📼🕹️ Once Upon a -90s-: Historias con IA y Nostalgia 🚀

<img width="2000" height="1124" alt="once_upon_a_90s_banner" src="https://github.com/user-attachments/assets/f2edbff4-4629-4ae4-9ff2-f12d5cd84a2b" />
>  **La inteligencia artificial viaja al pasado para contar historias noventeras**

🎯 ¿Qué es este proyecto?
Este proyecto busca crear un espacio donde los jóvenes actuales puedan descubrir cómo era la vida en los años 90, a través de historias generadas con inteligencia artificial. Hoy en día, la tecnología ha transformado la forma en que interactuamos, trabajamos y nos divertimos. Sin embargo, los años 90 fueron una época única, marcada por la creatividad, la exploración sin pantallas y la conexión social sin redes digitales.

## ✨ Descripción General

`Once Upon a -90s-` es una aplicación de Data Engineering que despliega un modelo de Google Gemini (LLM) a través de una **API REST**. Su función principal es generar **historias cómicas ambientadas en los años 90**, protagonizadas por personajes actuales que se enfrentan a la tecnología retro.

Las historias se **almacenan en una base de datos SQLite** y son accesibles mediante endpoints de la API. La solución está completamente **dockerizada** para facilitar su despliegue y uso. Se incluye un frontend simple en Streamlit para una demostración interactiva.


## 🏗️ Arquitectura Simplificada

La aplicación consta de:

* **Frontend (Streamlit - Opcional):** Interfaz para interactuar con la API.
* **Backend (FastAPI):**
    * Gestiona los **endpoints** (`/generate_story/`, `/stories/`, etc.).
    * Integra el **modelo Google Gemini** para generar historias.
    * Almacena datos en **SQLite** (usando SQLAlchemy y Pydantic para buena práctica).
* **Docker:** Empaqueta y ejecuta el backend de forma consistente.


📂 Estructura del Proyecto

Once-Upon-A-90s/
├── .env                 
├── Dockerfile            
├── requirements.txt      
├── start.sh             
├── main.py               
└── streamlit_app.py      

## 🛠️ Requisitos Previos

* **Docker Desktop:** Instalado y ejecutándose.
* **Python 3.9+:** Para ejecutar scripts locales.
* **Clave API de Google Gemini:** Necesaria para el modelo de IA.


## 🚀 Configuración y Ejecución Rápida

1.  **Clona el repo:** `git clone https://github.com/tu-usuario/Once-Upon-A-90s.git && cd Once-Upon-A-90s`
2.  **Crea `.env`:** Añade `GEMINI_API_KEY=tu_clave_aqui` en un archivo `.env` en la raíz.
3.  **Inicia el Backend (API Docker):**
    ```bash
    chmod +x start.sh # Solo la primera vez
    ./start.sh
    ```
    La API estará en `http://localhost:8080` (docs en `/docs`).
4.  **Inicia el Frontend (Streamlit - Opcional):**
    * Abre **otra terminal** en la misma carpeta.
    * Instala: `pip install streamlit requests` (si no lo tienes).
    * Ejecuta: `streamlit run streamlit_app.py`
    * El frontend abrirá en `http://localhost:8501`.


## ⚙️ Endpoints de la API

* `GET /`: Página de bienvenida.
* `POST /generate_story/`: Genera y guarda una historia (JSON: `{"title": "...", "protagonists": ["...", "..."]}`).
* `GET /stories/`: Lista todas las historias.
* `GET /stories/{story_id}`: Obtiene una historia por su ID.


## 🗑️ Detener la Aplicación

Para detener todos los servicios de Docker:

```bash
docker-compose down

✨ Tecnologías Destacadas
FastAPI: API REST de alto rendimiento.
Google Gemini: Modelo de IA para generación de texto.
SQLite: Base de datos ligera y persistente.
SQLAlchemy & Pydantic: ORM y validación de datos para buenas prácticas.
Docker & Docker Compose: Contenerización y orquestación.
Streamlit: Frontend interactivo .

📝 Autor

 Juan Manuel de la Fuente Larrocca
