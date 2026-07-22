from app.core.config import RAW_DATA_DIR
from app.ingestion.pdf_reader import PDFReader
import fitz

doc = fitz.open(RAW_DATA_DIR / "Math_2024_Annual.pdf")
print("Total PDF Pages:", len(doc))
doc.close()
reader = PDFReader()

pages = reader.read(
    RAW_DATA_DIR / "Math_2024_Annual.pdf"
)

print(f"Pages: {len(pages)}")

print("=" * 80)

print(pages[0].text[:1500])