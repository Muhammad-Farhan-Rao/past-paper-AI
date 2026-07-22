"""
PDF Reader Component

Responsibility:
Read a PDF file and return a list of Page objects.
"""

import fitz  # PyMuPDF
from pathlib import Path

from app.domain.page import Page


class PDFReader:

    def read(self, pdf_path: str) -> list[Page]:

        pdf_file = Path(pdf_path)

        if not pdf_file.exists():
            raise FileNotFoundError(f"{pdf_path} not found.")

        document = fitz.open(pdf_file)

        pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text()

            page_data = Page(
                page_number=page_number,
                text=text,
                source_file=pdf_file.name,
                needs_ocr=(len(text.strip()) == 0),
                extraction_confidence=1.0 if text.strip() else 0.0,
            )

            pages.append(page_data)

        document.close()

        return pages