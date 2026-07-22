"""
Page Model

Purpose:
Represents one page extracted from a PDF document.

Responsibility:
Store page-level extraction data only.
"""

from dataclasses import dataclass


@dataclass
class Page:
    page_number: int
    text: str
    source_file: str
    needs_ocr: bool
    extraction_confidence: float