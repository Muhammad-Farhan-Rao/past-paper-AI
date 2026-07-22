from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter

reader = PDFReader()

pages = reader.read(
    RAW_DATA_DIR /
    "Math_2024_Annual.pdf"
)

print("=" * 80)
print(pages[0].text[:3000])
print("=" * 80)

segmenter = QuestionSegmenter()

questions = segmenter.segment(
    pages,
    year=2024,
    exam_type="Annual"
)

print(len(questions))

for question in questions[:5]:
    print("-" * 80)
    print(question.question_number)
    print(question.question_text[:500])