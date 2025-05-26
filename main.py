# Once-Upon-A-90s/main.py

import os
import google.generativeai as genai
import asyncio
from datetime import datetime
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# --- 0. Carga de Variables de Entorno y Configuración de Gemini ---

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY no encontrada")

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

# --- 1. Configuración de la Base de Datos (SQLAlchemy) ---

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/90s_stories.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class StoryDB(Base):
    __tablename__ = "stories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    protagonists = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- 2. Modelos Pydantic para la API (Entrada y Salida) ---

PERSONAJES_VALIDOS = ["Rafa", "Alex", "Hugo", "Cris", "Dani", "Pau", "Arturo", "Juan", "Karla", "Eric", "Alberto"]

class StoryRequest(BaseModel):
    title: str = Field(..., min_length=5, max_length=100, description="Título para la historia cómica de los 90.")
    protagonists: List[str] = Field(
        ...,
        min_items=1,
        max_items=len(PERSONAJES_VALIDOS),
        description=f"Nombres de 1 a {len(PERSONAJES_VALIDOS)} protagonistas (elegir de: {', '.join(PERSONAJES_VALIDOS)})."
    )

class StoryResponse(BaseModel):
    id: int
    title: str
    protagonists: List[str]
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class StoriesListResponse(BaseModel):
    stories: List[StoryResponse]

# --- 3. Inicialización de la Aplicación FastAPI ---

app = FastAPI(
    title="Once Upon a -90s- API",
    description="API REST para generar historias cómicas de los 90 con Google Gemini, y almacenarlas en SQLite.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# --- 4. Lógica del Generador de Historias (LLM Service integrado) ---

async def generar_historia_90s_logic(titulo: str, protagonistas: List[str]) -> str:
    protagonistas_str = ", ".join(protagonistas)
    prompt = f"""
    Eres un escritor de historias de comedia. Tu tarea es crear una aventura **muy corta y graciosa** (máximo 2-3 párrafos)
    ambientada en los años 90.

    Los protagonistas son jóvenes de la época actual, totalmente dependientes de la tecnología moderna,
    que han sido transportados a un día típico de los años 90. Sus nombres son: {protagonistas_str}.
    El título de su aventura es: "{titulo}".

    La historia debe narrar sus hilarantes y absurdos intentos de **sobrevivir a situaciones cotidianas de los 90**,
    chocando con la falta de WiFi, la obligación de usar un teléfono fijo de disco para quedar,
    la ausencia de redes sociales para documentar todo, los VHS, los CDs que se rayan,
    la necesidad de usar un mapa de papel, y la comunicación sin WhatsApp.

    Integra de 1 a 2 **"Consejos de Supervivencia de los 90"** de forma cómica y directa,
    como si fueran advertencias útiles para alguien de hoy en día.
    Por ejemplo:
    - "Consejo de Supervivencia #1: Si el teléfono tiene cable, ¡estás atrapado! No intentes buscar la 'nube'."
    - "Consejo de Supervivencia #2: Para quedar con alguien, tienes que llamar a un teléfono fijo y esperar a que CONTESTE. No hay ubicación en tiempo real."
    - "Consejo de Supervivencia #3: El 'buffering' de los 90 era un casete de VHS que no rebobinaste."

    Que el tono sea muy ligero, divertido, y resalte su confusión, frustración y momentos absurdos mientras intentan adaptarse a este "mundo analógico".
    Finaliza la historia de forma abrupta y cómica, o con una moraleja humorística.
    """
    try:
        response = await asyncio.to_thread(gemini_model.generate_content, prompt)
        return response.text
    except Exception as e:
        print(f"Error al generar historia con Gemini: {e}")
        raise ValueError(f"Error al generar historia con Gemini: {e}")

# --- 5. Endpoints de la API ---

@app.get("/", response_class=HTMLResponse, summary="Página de bienvenida de la API")
async def read_root():
    # El título en el HTML se actualiza aquí
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Once Upon a -90s- API</title>
        <style>
            body { font-family: 'Arial', sans-serif; background-color: #f4f4f4; color: #333; margin: 0; padding: 20px; }
            .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); max-width: 800px; margin: 20px auto; }
            h1 { color: #0056b3; text-align: center; }
            h2 { color: #0056b3; margin-top: 25px; }
            ul { list-style-type: disc; padding-left: 20px; }
            li { margin-bottom: 10px; }
            code { background-color: #e0e0e0; padding: 2px 4px; border-radius: 4px; font-family: 'Courier New', monospace; }
            pre { background-color: #e0e0e0; padding: 15px; border-radius: 5px; overflow-x: auto; }
            .docs-link { display: block; margin-top: 20px; font-size: 1.1em; text-align: center; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenido a la API "Once Upon a -90s-"</h1>
            <p>Esta API genera historias cómicas ambientadas en los años 90 con Google Gemini, y las almacena en una base de datos SQLite.</p>
            
            <h2>Endpoints disponibles:</h2>
            <ul>
                <li><code>GET /</code>: Esta página de bienvenida.</li>
                <li><code>POST /generate_story/</code>: Genera una nueva historia cómica de los 90 y la guarda.</li>
                <li><code>GET /stories/</code>: Lista todas las historias generadas y guardadas.</li>
                <li><code>GET /stories/{story_id}</code>: Obtiene una historia específica por su ID.</li>
            </ul>
            <p>Puedes interactuar con la API usando:</p>
            <ul>
                <li>La <a href="/docs">documentación interactiva (Swagger UI)</a></li>
                <li>Herramientas como Postman, Insomnia o <code>curl</code></li>
            </ul>
            <p>Ejemplo de cuerpo JSON para <code>POST /generate_story/</code>:</p>
            <pre><code>{
    "title": "El Misterio del Video Club Vacío",
    "protagonists": ["Alex", "Karla"]
}</code></pre>
            <p>El campo <code>protagonists</code> debe ser una lista con entre 1 y 11 nombres válidos de nuestra lista.</p>
            <p>¡Disfruta de tu viaje al pasado!</p>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=status.HTTP_200_OK)


@app.post("/generate_story/", response_model=StoryResponse, status_code=status.HTTP_201_CREATED,
          summary="Genera una nueva historia cómica de los 90 y la guarda")
async def create_story(
    story_req: StoryRequest,
    db: Session = Depends(get_db)
):
    for prota in story_req.protagonists:
        if prota not in PERSONAJES_VALIDOS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El personaje '{prota}' no es válido. Los personajes válidos son: {', '.join(PERSONAJES_VALIDOS)}"
            )

    try:
        generated_content = await generar_historia_90s_logic(
            titulo=story_req.title,
            protagonistas=story_req.protagonists
        )

        protagonists_str_for_db = ", ".join(story_req.protagonists)

        db_story = StoryDB(
            title=story_req.title,
            protagonists=protagonists_str_for_db,
            content=generated_content
        )
        
        db.add(db_story)
        db.commit()
        db.refresh(db_story)

        return StoryResponse(
            id=db_story.id,
            title=db_story.title,
            protagonists=story_req.protagonists,
            content=db_story.content,
            created_at=db_story.created_at
        )

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        print(f"Error al generar o guardar historia: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor al generar la historia.")


@app.get("/stories/", response_model=StoriesListResponse, summary="Lista todas las historias generadas")
async def get_all_stories(db: Session = Depends(get_db)):
    stories_db = db.query(StoryDB).all()

    stories_parsed = []
    for s in stories_db:
        prots_list = s.protagonists.split(", ") if s.protagonists else []
        stories_parsed.append(StoryResponse(
            id=s.id,
            title=s.title,
            protagonists=prots_list,
            content=s.content,
            created_at=s.created_at
        ))
    
    return {"stories": stories_parsed}


@app.get("/stories/{story_id}", response_model=StoryResponse, summary="Obtiene una historia por su ID")
async def get_story_by_id(story_id: int, db: Session = Depends(get_db)):
    db_story = db.query(StoryDB).filter(StoryDB.id == story_id).first()
    if db_story is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Historia no encontrada")
    
    prots_list = db_story.protagonists.split(", ") if db_story.protagonists else []
    return StoryResponse(
        id=db_story.id,
        title=db_story.title,
        protagonists=prots_list,
        content=db_story.content,
        created_at=db_story.created_at
    )
