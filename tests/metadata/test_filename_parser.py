from app.metadata.filename_parser import FilenameParser

parser = FilenameParser()

metadata = parser.parse(
    "Math_2024_Annual_Text.pdf"
)

print(metadata)