from app.classification.classifier import QuestionClassifier
from app.classification.syllabus_loader import SyllabusLoader
from app.core.config import BASE_DIR, RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter

# Load syllabus
loader = SyllabusLoader()
syllabus = loader.load(
    BASE_DIR / "app" / "resources" / "syllabus" / "math_grade10.json"
)

# Extract questions
reader = PDFReader()
pages = reader.read(RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

segmenter = QuestionSegmenter()
questions = segmenter.segment(pages)

# Classify
classifier = QuestionClassifier()
questions = classifier.classify(questions, syllabus)

# Show first 10 results
for question in questions[:10]:
    print("-" * 70)
    print(f"Q.{question.question_number}({question.sub_question_number})")
    print(question.question_text)
    print(f"Chapter: {question.chapter}")
    print(f"Topic: {question.topic}")
    print(f"Confidence: {question.classification_confidence}")