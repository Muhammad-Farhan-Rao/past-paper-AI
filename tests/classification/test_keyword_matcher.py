from app.classification.keyword_matcher import KeywordMatcher
from app.classification.syllabus_loader import SyllabusLoader
from app.core.config import BASE_DIR

loader = SyllabusLoader()

syllabus = loader.load(
    BASE_DIR / "app" / "resources" / "syllabus" / "math_grade10.json"
)

matcher = KeywordMatcher()

question = "What is meant by radical equation?"

result = matcher.match(question, syllabus)

print(result)