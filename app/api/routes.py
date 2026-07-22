from fastapi import APIRouter
from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter
from app.similarity.vectorizer import QuestionVectorizer
from app.similarity.similarity_engine import SimilarityEngine
from fastapi import UploadFile, File
from pathlib import Path
import shutil
router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Past Paper AI Backend Running"
    }


@router.get("/health")
def health():
    return {
        "status": "OK"
    }

@router.get("/questions")
def get_questions():

    reader = PDFReader()

    pages = reader.read(
        RAW_DATA_DIR / "Math_2024_Annual_Text.pdf"
    )

    segmenter = QuestionSegmenter()

    questions = segmenter.segment(pages)

    return questions

@router.get("/question/{question_number}")
def get_question(question_number: int):

    reader = PDFReader()
    pages = reader.read(RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

    segmenter = QuestionSegmenter()
    questions = segmenter.segment(pages)

    for question in questions:
        if question.question_number == question_number:
            return question

    return {"error": "Question not found"}

@router.get("/similar/{question_number}")
def get_similar_questions(question_number: int):

    reader = PDFReader()
    pages = reader.read(
        RAW_DATA_DIR / "Math_2024_Annual_Text.pdf"
    )

    segmenter = QuestionSegmenter()
    questions = segmenter.segment(pages)

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

    return results

@router.post("/upload")
def upload_pdf(file: UploadFile = File(...)):

    upload_dir = RAW_DATA_DIR
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }