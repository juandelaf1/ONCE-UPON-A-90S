# 📼🕹️ Once Upon a -90s-  
## 🤖 Historias con IA, FastAPI y Nostalgia Noventera

<img width="2000" height="1124" alt="once_upon_a_90s_banner" src="https://github.com/user-attachments/assets/f2edbff4-4629-4ae4-9ff2-f12d5cd84a2b" />

>  **La inteligencia artificial viaja al pasado para contar historias noventeras**


**Once Upon a -90s-** es una aplicación de **Data Engineering + IA Generativa** que crea historias cómicas ambientadas en los años 90 utilizando **Google Gemini (LLM)**, expuestas a través de una **API REST con FastAPI**, persistidas en base de datos y desplegadas con **Docker**.

> 💡 Proyecto orientado a demostrar cómo integrar modelos generativos en una arquitectura backend moderna y reproducible.

---

## 🎯 ¿Qué problema aborda este proyecto?

Las nuevas generaciones han crecido en un entorno dominado por pantallas, redes sociales y automatización.  
Los años 90 representan una época previa a esta hiperconectividad, marcada por:

- 📞 Comunicación sin smartphones  
- 🎮 Tecnología limitada pero creativa  
- 🤝 Interacciones sociales más presenciales  

Este proyecto utiliza **IA generativa** para crear historias que conectan ambos mundos:  
**personajes actuales enfrentándose a la vida noventera**, de forma humorística y narrativa.

---

## ✨ Descripción General

Once Upon a -90s- es una **API de generación de historias** que:

- Recibe un título y protagonistas
- Genera una historia ambientada en los años 90 usando **Google Gemini**
- Almacena las historias en una base de datos **SQLite**
- Permite consultarlas mediante endpoints REST
- Incluye un **frontend opcional en Streamlit** para demostración interactiva

Toda la solución está **dockerizada**, facilitando su ejecución y despliegue.

---

## 🏗️ Arquitectura del Sistema

La aplicación se compone de los siguientes elementos:

### 🖥️ Frontend (opcional)
- **Streamlit**
- Interfaz simple para consumir la API y visualizar historias

### ⚙️ Backend (FastAPI)
- Exposición de endpoints REST (`/generate_story`, `/stories`, etc.)
- Integración con **Google Gemini (LLM)**
- Persistencia en base de datos **SQLite**
- Validación de datos con **Pydantic**
- ORM con **SQLAlchemy**

### 📦 Infraestructura
- **Docker** para contenerización
- Script de arranque automatizado

---

## 📂 Estructura del Proyecto

```bash
Once-Upon-A-90s/
├── .env                  # Variables de entorno (API Key)
├── Dockerfile             # Imagen del backend
├── requirements.txt       # Dependencias
├── start.sh               # Script de arranque
├── main.py                # API FastAPI
└── streamlit_app.py       # Frontend Streamlit (opcional)



🛠️ Requisitos Previos

🐳 Docker Desktop (instalado y en ejecución)

🐍 Python 3.9+ (para ejecución local / frontend)

🔑 Google Gemini API Key

🚀 Configuración y Ejecución Rápida
1️⃣ Clonar el repositorio
git clone https://github.com/juandelaf1/ONCE-UPON-A-90S.git
cd ONCE-UPON-A-90S

2️⃣ Configurar variables de entorno

Crear un archivo .env en la raíz del proyecto:

GEMINI_API_KEY=tu_api_key_aqui

3️⃣ Ejecutar el backend (FastAPI + Docker)
chmod +x start.sh   # Solo la primera vez
./start.sh


La API estará disponible en:

🌐 http://localhost:8080

📚 Swagger Docs: http://localhost:8080/docs

4️⃣ Ejecutar el frontend (opcional)

En otra terminal:

pip install streamlit requests
streamlit run streamlit_app.py


Frontend disponible en:
👉 http://localhost:8501

⚙️ Endpoints de la API
🔹 GET /

Página de bienvenida.

🔹 POST /generate_story/

Genera y guarda una historia.

Request:

{
  "title": "Una tarde sin WiFi",
  "protagonists": ["Lucas", "Martina"]
}


Response:

{
  "id": 1,
  "title": "Una tarde sin WiFi",
  "story": "Historia generada por IA..."
}

🔹 GET /stories/

Devuelve todas las historias almacenadas.

🔹 GET /stories/{story_id}

Obtiene una historia específica por ID.

🗑️ Detener la Aplicación

Para detener los servicios Docker:

docker-compose down

🧰 Tecnologías Utilizadas

⚡ FastAPI – API REST moderna y de alto rendimiento

🤖 Google Gemini (LLM) – Generación de texto con IA

🗄️ SQLite – Persistencia ligera

🧩 SQLAlchemy & Pydantic – ORM y validación

🐳 Docker & Docker Compose – Contenerización

🖥️ Streamlit – Frontend interactivo

🔮 Posibles Mejoras Futuras

🔐 Autenticación por API Key

📊 Logging y métricas

🧪 Tests automatizados

☁️ Despliegue en la nube (Render / Railway)

🧠 Versionado de prompts

🌍 Internacionalización de historias

🧑‍💻 Autor

Juan Manuel de la Fuente Larrocca
Proyecto desarrollado como demostración de integración entre IA Generativa, APIs y despliegue moderno.
