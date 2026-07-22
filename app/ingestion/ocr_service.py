from io import BytesIO
from pathlib import Path

import fitz
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


class OCRService:

    def extract_text(self, pdf_path: Path) -> list[str]:

        document = fitz.open(pdf_path)

        pages = []

        for page in document:

            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

            image = Image.open(BytesIO(pix.tobytes("png")))

            text = pytesseract.image_to_string(
                image,
                lang="eng",
                config="--psm 6"
            )

            print("OCR Length:", len(text))

            pages.append(text)

        document.close()

        return pages