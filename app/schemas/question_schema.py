from pydantic import BaseModel
from typing import Optional


class QuestionSchema(BaseModel):

    id: str

    board: str
    student_class: str
    subject: str
    year: int
    exam_type: str

    section: str

    question_number: int
    sub_question_number: Optional[str]

    question_text: str

    marks: Optional[int]

    question_type: str

    chapter: Optional[str]
    topic: Optional[str]
    subtopic: Optional[str]

    page_number: int
    source_file: str

    extraction_confidence: float
    classification_confidence: float

    review_status: str