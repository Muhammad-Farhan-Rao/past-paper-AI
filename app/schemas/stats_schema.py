from pydantic import BaseModel


class StatsSchema(BaseModel):

    total_questions: int

    short_questions: int

    long_questions: int

    subjects: list[str]

    years: list[int]

    exam_types: list[str]

    sections: dict[str, int]