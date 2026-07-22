from dataclasses import dataclass


@dataclass
class Question:
    id: str
    board: str
    class_name: str
    subject: str
    year: int
    exam_type: str

    section: str

    question_number: str
    sub_question_number: str | None

    question_text: str

    marks: int | None

    question_type: str

    chapter: str | None
    topic: str | None
    subtopic: str | None

    source_file: str
    page_number: int

    extraction_confidence: float
    classification_confidence: float

    review_status: str