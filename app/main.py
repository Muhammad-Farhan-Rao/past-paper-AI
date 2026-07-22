from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Past Paper AI Backend",
    description="""
AI-powered backend for extracting, classifying, and analyzing past paper questions.

Features:
- PDF Upload
- OCR
- Question Extraction
- AI Classification
- Similarity Search
""",
    version="1.0.0"
)

app.include_router(router)