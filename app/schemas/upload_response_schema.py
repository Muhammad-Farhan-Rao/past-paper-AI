from pydantic import BaseModel


class UploadResponseSchema(BaseModel):

    message: str

    filename: str

    pages: int

    questions_found: int

    ocr_used: bool