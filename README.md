<p align="center">
  <img src="https://github.com/user-attachments/assets/f2edbff4-4629-4ae4-9ff2-f12d5cd84a2b" alt="Once Upon a 90s Banner" width="800">
</p>

# ONCE UPON A '90S — AI-Powered 90s Nostalgia Story Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?logo=google&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **AI travels to the past to tell 90s stories. FastAPI + Google Gemini + Docker.**

---

## Elevator Pitch

**Problem**: New generations grew up in a hyperconnected world of smartphones and social media. The 90s — a time of limited technology but creative communication — is fading from cultural memory. There's no engaging way to experience or share 90s nostalgia through AI-generated storytelling.

**Hypothesis**: Combining Google Gemini (LLM) with a modern FastAPI backend and Docker deployment can generate engaging, humorous 90s-themed stories, preserved in a database and accessible via REST API.

**Solution**: Once Upon a '90s — an AI-powered story generation API that creates comic narratives set in the 90s. Features **FastAPI backend**, **Google Gemini LLM integration**, **SQLite persistence**, **Docker deployment**, and optional **Streamlit frontend**.

---

## Problem

- 90s culture is fading from collective memory
- No AI tools specifically for nostalgic storytelling
- New generations disconnected from pre-digital era experiences
- Need for creative, engaging content generation

## Key Features

| Feature | Description |
|---------|-------------|
| AI Story Generation | Google Gemini LLM creates 90s-themed stories |
| REST API | FastAPI endpoints for generation and retrieval |
| Database Persistence | SQLite via SQLAlchemy ORM |
| Docker Containerized | Reproducible deployment |
| Interactive Frontend | Optional Streamlit dashboard |
| API Documentation | Swagger UI at /docs |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome page |
| POST | `/generate_story/` | Generate and save a story |
| GET | `/stories/` | List all stories |
| GET | `/stories/{id}` | Get specific story |

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI |
| LLM | Google Gemini |
| Database | SQLite + SQLAlchemy |
| Validation | Pydantic |
| Frontend (optional) | Streamlit |
| Infrastructure | Docker + Docker Compose |

## Quick Start

```bash
git clone https://github.com/juandelaf1/ONCE-UPON-A-90S.git
cd ONCE-UPON-A-90S
# Add GEMINI_API_KEY to .env
./start.sh
# API: http://localhost:8080
# Swagger: http://localhost:8080/docs
```

---

## Author

**Juan de la Fuente** — [@juandelaf1](https://github.com/juandelaf1)

juandelafuentelarrocca@gmail.com
