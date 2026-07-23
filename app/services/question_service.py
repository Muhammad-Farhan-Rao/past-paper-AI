from pathlib import Path

from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter
from app.utils.logger import logger

class QuestionService:

    def __init__(self):
        # Cache stores processed questions by PDF path
        self._cache = {}

    def get_questions(self, pdf_path=None):

        pdf = Path(pdf_path) if pdf_path else (RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

        cache_key = str(pdf.resolve())

        # Return cached questions if already processed
        if cache_key in self._cache:
            return self._cache[cache_key]

        logger.info(f"Cache miss: {pdf.name}")

        # Read and process PDF
        reader = PDFReader()
        pages = reader.read(pdf)

        segmenter = QuestionSegmenter()
        questions = segmenter.segment(pages)

        # Store in cache
        self._cache[cache_key] = questions

        return questions

    def clear_cache(self):
        self._cache.clear()