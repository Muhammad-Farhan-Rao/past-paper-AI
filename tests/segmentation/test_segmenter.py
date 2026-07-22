from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter

reader = PDFReader()

pages = reader.read(
    RAW_DATA_DIR / "Math_2024_Annual_Text.pdf"
)

segmenter = QuestionSegmenter()

questions = segmenter.segment(pages)

print(f"Questions Extracted: {len(questions)}")
print("=" * 80)

for q in questions[:5]:
    print(q)
    print()