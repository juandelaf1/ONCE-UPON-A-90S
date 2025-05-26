# Once-Upon-A-90s/streamlit_app.py

import streamlit as st
import requests
import json

# URL de API de FastAPI
API_URL = "http://localhost:8080"

st.set_page_config(page_title="Once Upon a -90s- Story Generator", layout="centered")

# Título Streamlit 
st.title("📚 Once Upon a -90s- Story Generator") 
st.markdown("""
¡Bienvenido al generador de historias de los 90! 📼🕹️ ¿Qué tal una aventura hilarante 
donde los jóvenes de hoy se enfrentan a la tecnología retro?
""")

# --- Generar Nueva Historia ---
st.header("✨ Generar una Nueva Historia de los 90")

with st.form("generate_story_form"):
    title = st.text_input("Título de la Historia", placeholder="El Día que el WiFi Desapareció")
    
    # Personajes válidos
    PERSONAJES_VALIDOS = ["Rafa", "Alex", "Hugo", "Cris", "Dani", "Pau", "Arturo", "Juan", "Karla", "Eric", "Alberto"]
    protagonists = st.multiselect(
        "Selecciona los Protagonistas",
        options=PERSONAJES_VALIDOS,
        help="Elige entre 1 y 11 protagonistas de la lista. Estos son jóvenes de hoy transportados a los 90."
    )

    submitted = st.form_submit_button("Generar y Guardar Historia")

    if submitted:
        if not title:
            st.error("Por favor, introduce un título para la historia.")
        elif not protagonists:
            st.error("Por favor, selecciona al menos un protagonista.")
        else:
            try:
                payload = {
                    "title": title,
                    "protagonists": protagonists
                }
                
                with st.spinner("Generando tu aventura de los 90... esto puede tardar un momento..."):
                   
                    response = requests.post(f"{API_URL}/generate_story/", json=payload, timeout=120) 

                if response.status_code == 201:
                    story_data = response.json()
                    st.success("¡Historia generada y guardada con éxito!")
                    st.subheader(story_data["title"])
                    st.write(f"**Protagonistas:** {', '.join(story_data['protagonists'])}")
                    st.write(story_data["content"])
                    st.caption(f"ID: {story_data['id']} | Creada el: {story_data['created_at']}")
                else:
                    st.error(f"Error al generar la historia: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("No se pudo conectar con la API. Asegúrate de que la API de FastAPI esté corriendo en http://localhost:8080.")
            except requests.exceptions.Timeout:
                st.error("La solicitud a la API excedió el tiempo límite. Inténtalo de nuevo más tarde o revisa la conexión.")
            except Exception as e:
                st.error(f"Ocurrió un error inesperado: {e}")

st.markdown("---")

# --- Historias Guardadas ---
st.header("📖 Historias Guardadas")

if st.button("Recargar Historias"):
    try:
        with st.spinner("Cargando historias..."):
            response = requests.get(f"{API_URL}/stories/")
        
        if response.status_code == 200:
            stories = response.json().get("stories", [])
            if stories:
                stories.sort(key=lambda x: x['created_at'], reverse=True) 
                for story in stories:
                    st.subheader(story["title"])
                    st.write(f"**Protagonistas:** {', '.join(story['protagonists'])}")
                    st.write(story["content"])
                    st.caption(f"ID: {story['id']} | Creada el: {story['created_at']}")
                    st.markdown("---")
            else:
                st.info("Aún no hay historias guardadas. ¡Genera una!")
        else:
            st.error(f"Error al cargar historias: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("No se pudo conectar con la API. Asegúrate de que la API de FastAPI esté corriendo en http://localhost:8080.")
    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")

# Cargar historias 
if 'initial_load' not in st.session_state:
    st.session_state.initial_load = True
    try:
        response = requests.get(f"{API_URL}/stories/")
        if response.status_code == 200:
            stories = response.json().get("stories", [])
            if stories:
                stories.sort(key=lambda x: x['created_at'], reverse=True)
                for story in stories:
                    st.subheader(story["title"])
                    st.write(f"**Protagonistas:** {', '.join(story['protagonists'])}")
                    st.write(story["content"])
                    st.caption(f"ID: {story['id']} | Creada el: {story['created_at']}")
                    st.markdown("---")
            else:
                st.info("Aún no hay historias guardadas. ¡Genera una!")
        else:
            st.error(f"Error al cargar historias: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("No se pudo conectar con la API. Asegúrate de que la API de FastAPI esté corriendo en http://localhost:8080.")
    except Exception as e:
        st.error(f"Ocurrió un error inesperado: {e}")
