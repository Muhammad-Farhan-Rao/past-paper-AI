from pydantic import BaseModel, Field


class UploadResponseSchema(BaseModel):

    message: str = Field(
        example="PDF uploaded successfully"
    )

    filename: str = Field(
        example="Math_2024_Annual.pdf"
    )

    pages: int = Field(
        example=2
    )

    questions_found: int = Field(
        example=34
    )

    ocr_used: bool = Field(
        example=False
    )