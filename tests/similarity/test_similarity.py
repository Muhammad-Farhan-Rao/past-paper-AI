from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
from app.segmentation.question_segmenter import QuestionSegmenter
from app.similarity.vectorizer import QuestionVectorizer
from app.similarity.similarity_engine import SimilarityEngine

reader = PDFReader()
pages = reader.read(RAW_DATA_DIR / "Math_2024_Annual_Text.pdf")

segmenter = QuestionSegmenter()
questions = segmenter.segment(pages)

texts = [q.question_text for q in questions]

vectorizer = QuestionVectorizer()
vectors = vectorizer.fit_transform(texts)

engine = SimilarityEngine()

results = engine.find_similar(vectors, 0)

print("Original Question:")
print(questions[0].question_text)
print()

print("Most Similar Questions:")
print("-" * 70)

for index, score in results:
    print(f"Similarity: {score:.2f}")
    print(questions[index].question_text)
    print("-" * 70)