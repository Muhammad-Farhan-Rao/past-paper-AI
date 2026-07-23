"""
PDF Reader Component

Responsibility:
Read a PDF file and return a list of Page objects.
"""

from app.utils.logger import logger
import fitz  # PyMuPDF
from pathlib import Path
from app.domain.page import Page

from app.ingestion.ocr_service import OCRService

class PDFReader:

    def __init__(self):
        self.ocr = OCRService()

    def read(self, pdf_path: str | Path) -> list[Page]:

        pdf_file = Path(pdf_path)
        logger.info(f"Reading PDF: {pdf_file.name}")

        if not pdf_file.exists():
            logger.error(f"PDF not found: {pdf_path}")
            raise FileNotFoundError(f"{pdf_path} not found.")

        document = fitz.open(pdf_file)

        pages = []

        ocr_pages = None

        for page_number, page in enumerate(document, start=1):

            text = page.get_text().strip()

            needs_ocr = len(text) == 0

            if needs_ocr:
                logger.info(f"OCR required for page {page_number}")

                if ocr_pages is None:
                    ocr_pages = self.ocr.extract_text(pdf_file)

                text = ocr_pages[page_number - 1]

            page_data = Page(
                page_number=page_number,
                text=text,
                source_file=pdf_file.name,
                needs_ocr=needs_ocr,
                extraction_confidence=0.90 if needs_ocr else 1.0,
            )

            pages.append(page_data)

        document.close()

        logger.info(f"Successfully read {len(pages)} pages from {pdf_file.name}")

        return pages