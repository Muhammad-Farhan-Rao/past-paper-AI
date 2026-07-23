from pydantic import BaseModel, Field


class StatsSchema(BaseModel):

    total_questions: int = Field(
        example=34
    )

    short_questions: int = Field(
        example=34
    )

    long_questions: int = Field(
        example=0
    )

    subjects: list[str] = Field(
        example=["Mathematics"]
    )

    years: list[int] = Field(
        example=[2024]
    )

    exam_types: list[str] = Field(
        example=["Annual"]
    )

    sections: dict[str, int] = Field(
        example={
            "PART-I": 34
        }
    )