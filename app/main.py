from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Past Paper AI Backend",

    version="1.1.0",

    description="""
## AI Powered Past Paper Processing System

This backend extracts questions from PDF past papers using OCR,
segments questions, classifies them, finds similar questions,
and exposes everything through REST APIs.

### Features

- PDF Upload
- OCR
- Question Extraction
- Metadata Extraction
- AI Classification
- Similarity Search
- Statistics API

Developed using FastAPI.
"""
)

app.include_router(router)