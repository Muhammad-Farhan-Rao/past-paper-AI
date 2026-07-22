# Past Paper AI Backend

## Overview

Past Paper AI Backend is an AI-powered system for extracting, classifying, and analyzing examination questions from PDF past papers.

## Features

- PDF Upload
- OCR using Tesseract
- Question Extraction
- Question Segmentation
- AI Keyword Classification
- Question Similarity Search
- FastAPI REST API
- Swagger Documentation

## Tech Stack

- Python
- FastAPI
- PyMuPDF
- pytesseract
- OpenCV
- scikit-learn
- Git
- GitHub

## Project Structure

app/
tests/
data/

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API

- GET /
- GET /health
- GET /questions
- GET /question/{question_number}
- GET /similar/{question_number}
- POST /upload

## Future Improvements

- Sentence Transformers
- Database Integration
- Authentication
- Docker Deployment