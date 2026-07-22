from app.core.config import BASE_DIR
from app.classification.syllabus_loader import SyllabusLoader

loader = SyllabusLoader()

syllabus = loader.load(
    BASE_DIR / "app" / "resources" / "syllabus" / "math_grade10.json"
)

print(type(syllabus))
print()

for chapter, keywords in syllabus.items():
    print(chapter)
    print(keywords)
    print("-" * 40)