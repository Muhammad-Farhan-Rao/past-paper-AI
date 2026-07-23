from pydantic import BaseModel, Field
from typing import Optional


class QuestionSchema(BaseModel):

    id: str = Field(
        example="8719b619-5a01-4d05-a461-979360cf0988"
    )

    board: str = Field(
        example="BISE Lahore"
    )

    student_class: str = Field(
        example="10"
    )

    subject: str = Field(
        example="Mathematics"
    )

    year: int = Field(
        example=2024
    )

    exam_type: str = Field(
        example="Annual"
    )

    section: str = Field(
        example="PART-I"
    )

    question_number: int = Field(
        example=2
    )

    sub_question_number: Optional[str] = Field(
        example="iii"
    )

    question_text: str = Field(
        example="Solve by factorization: x² - x - 20 = 0"
    )

    marks: Optional[int] = Field(
        example=2
    )

    question_type: str = Field(
        example="Short Question"
    )

    chapter: Optional[str] = Field(
        example="Quadratic Equations"
    )

    topic: Optional[str] = Field(
        example="Factorization"
    )

    subtopic: Optional[str] = Field(
        example=None
    )

    page_number: int = Field(
        example=1
    )

    source_file: str = Field(
        example="Math_2024_Annual_Text.pdf"
    )

    extraction_confidence: float = Field(
        example=1.0
    )

    classification_confidence: float = Field(
        example=0.95
    )

    review_status: str = Field(
        example="pending"
    )