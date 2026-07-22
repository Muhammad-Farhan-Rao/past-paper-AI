from pathlib import Path

from app.ingestion.pdf_reader import PDFReader

from app.core.config import RAW_DATA_DIR

from app.ingestion.json_exporter import JSONExporter
from app.core.config import PROCESSED_DATA_DIR

pdf_path = RAW_DATA_DIR / "Math_2024_Annual.pdf"

reader = PDFReader()

pages = reader.read(str(pdf_path))

exporter = JSONExporter()

output = PROCESSED_DATA_DIR / "Math_2024_Annual.json"

exporter.export(pages, output)

print("JSON Exported Successfully!")

print(f"Total Pages: {len(pages)}")

for page in pages:
    # print("-" * 50)
    # print(f"Page: {page.page_number}")
    # print(f"OCR Needed: {page.needs_ocr}")
    # print(page.text[:300])
    print(page.page_number)
    print(page.needs_ocr)