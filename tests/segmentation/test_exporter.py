from pathlib import Path
print("Current Working Directory:", Path.cwd())
from app.core.config import RAW_DATA_DIR, BASE_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_exporter import QuestionExporter
from app.segmentation.question_segmenter import QuestionSegmenter

reader = PDFReader()
pages = reader.read(RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

segmenter = QuestionSegmenter()
questions = segmenter.segment(pages)

exporter = QuestionExporter()
print(type(questions))
print(len(questions))
print(questions[0])
output_file = BASE_DIR / "data" / "processed" / "questions.json"

exporter.export_json(
    questions,
    output_file
)