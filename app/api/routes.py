from fastapi import APIRouter
from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter
from app.similarity.vectorizer import QuestionVectorizer
from app.similarity.similarity_engine import SimilarityEngine
from fastapi import UploadFile, File
from pathlib import Path
from fastapi import Query
from typing import Optional
from app.services.service_container import question_service
from app.schemas.stats_schema import StatsSchema
from app.schemas.upload_response_schema import UploadResponseSchema
from app.schemas.question_schema import QuestionSchema
from app.utils.logger import logger
import shutil
router = APIRouter()


@router.get("/")
def home():

    logger.info("Home endpoint accessed")

    return {
        "message": "Past Paper AI Backend Running"
    }


@router.get("/health")
def health():

    logger.info("Health endpoint checked")

    return {
        "status": "OK"
    }

@router.get(
    "/questions",
    response_model=list[QuestionSchema],
    tags=["Questions"],
    summary="Get all extracted questions",
    description="Returns all extracted questions."
)

def get_questions(pdf: Optional[str] = None):

    questions = (
        question_service.get_questions(RAW_DATA_DIR / pdf)
        if pdf
        else question_service.get_questions()
    )

    logger.info(f"Returned {len(questions)} questions")

    return questions

@router.get(
    "/search",
    tags=["Questions"],
    summary="Search questions by keyword"
)
def search_questions(
    keyword: str = Query(..., description="Keyword to search"),
    pdf: Optional[str] = None
):

    questions = (
        question_service.get_questions(RAW_DATA_DIR / pdf)
        if pdf
        else question_service.get_questions()
    )
    logger.info(f"Searching for keyword: {keyword}")

    results = []

    keyword = keyword.lower()

    for question in questions:

        search_text = f"""
        {question.question_text}
        {question.subject}
        {question.chapter}
        {question.topic}
        {question.question_type}
        """

        if keyword.lower() in search_text.lower():

            results.append(question)
    logger.info(f"Found {len(results)} matching questions")

    return results

@router.get(
    "/question/{question_number}",
    response_model=QuestionSchema,
    tags=["Questions"],
    summary="Get a single question",
    description="Returns a question using its main question number."
)
def get_question(
    question_number: int,
    pdf: Optional[str] = None
):

    questions = (
        question_service.get_questions(RAW_DATA_DIR / pdf)
        if pdf
        else question_service.get_questions()
    )

    for question in questions:
        if question.question_number == question_number:
            return question

    return {"error": "Question not found"}

@router.get(
    "/similar/{question_number}",
    tags=["AI"],
    summary="Find similar questions",
    description="Returns questions that are similar using TF-IDF and cosine similarity."
)
def get_similar_questions(
    question_number: int,
    pdf: Optional[str] = None
):

    questions = (
        question_service.get_questions(RAW_DATA_DIR / pdf)
        if pdf
        else question_service.get_questions()
    )

    # Find the index of the requested question
    question_index = None

    for i, question in enumerate(questions):
        if question.question_number == question_number:
            question_index = i
            break

    if question_index is None:
        return {"error": "Question not found"}

    texts = [q.question_text for q in questions]

    vectorizer = QuestionVectorizer()
    vectors = vectorizer.fit_transform(texts)

    engine = SimilarityEngine()
    similar = engine.find_similar(vectors, question_index)

    results = []

    for index, score in similar:
        results.append({
            "question_number": questions[index].question_number,
            "sub_question": questions[index].sub_question_number,
            "similarity": round(float(score), 2),
            "question_text": questions[index].question_text
        })
    logger.info(
        f"Found {len(results)} similar questions for Question {question_number}"
    )
    return results

@router.post(
    "/upload",
    response_model=UploadResponseSchema,
    tags=["Upload"],
    summary="Upload a PDF",
    description="Uploads a PDF into the raw data directory."
)
def upload_pdf(file: UploadFile = File(...)):

    upload_dir = RAW_DATA_DIR
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    questions = question_service.get_questions(file_path)

    reader = PDFReader()

    pages = reader.read(file_path)
    logger.info(f"Uploaded PDF: {file.filename}")

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename,
        "pages": len(pages),
        "questions_found": len(questions),
        "ocr_used": any(page.needs_ocr for page in pages)
    }

@router.get(
    "/stats",
    response_model=StatsSchema,
    tags=["Analytics"],
    summary="Project Statistics",
    description="Returns statistics about the extracted questions."
)
def get_statistics(pdf: Optional[str] = None):

    questions = (
        question_service.get_questions(RAW_DATA_DIR / pdf)
        if pdf
        else question_service.get_questions()
    )

    stats = {

        "total_questions": len(questions),

        "short_questions":
            sum(
                1
                for q in questions
                if q.question_type == "Short Question"
            ),

        "long_questions":
            sum(
                1
                for q in questions
                if q.question_type == "Long Question"
            ),

        "subjects":
            sorted(
                list(
                    {
                        q.subject
                        for q in questions
                    }
                )
            ),

        "years":
            sorted(
                list(
                    {
                        q.year
                        for q in questions
                    }
                )
            ),

        "exam_types":
            sorted(
                list(
                    {
                        q.exam_type
                        for q in questions
                    }
                )
            ),

        "sections": {}
    }

    for question in questions:

        section = question.section

        stats["sections"][section] = (
            stats["sections"].get(section, 0) + 1
        )
    logger.info("Statistics generated successfully")
    return stats