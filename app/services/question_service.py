from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter


class QuestionService:

    def get_questions(self, pdf_path=None):

        pdf = pdf_path or (RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

        reader = PDFReader()
        pages = reader.read(pdf)

        segmenter = QuestionSegmenter()

        return segmenter.segment(pages)