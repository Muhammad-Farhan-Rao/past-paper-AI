import re
import uuid

from app.domain.page import Page
from app.domain.question import Question


class QuestionSegmenter:

    def segment(
            self,
            pages: list[Page],
            year: int,
            exam_type: str
    ) -> list[Question]:

        questions = []

        pattern = r"(Q\.\s*\d+.*?)(?=Q\.\s*\d+|$)"

        for page in pages:

            matches = re.findall(
                pattern,
                page.text,
                flags=re.DOTALL
            )

            for match in matches:

                question_number_match = re.search(
                    r"Q\.\s*(\d+)",
                    match
                )

                question_number = (
                    question_number_match.group(1)
                    if question_number_match
                    else "UNKNOWN"
                )

                question_type = "Short question"

                if "prove" in match.lower():
                    question_type = "Proof"

                questions.append(

                    Question(
                        id=str(uuid.uuid4()),

                        board="BISE Lahore",
                        class_name="10",
                        subject="Mathematics",

                        year=year,
                        exam_type=exam_type,

                        section="UNKNOWN",

                        question_number=question_number,
                        sub_question_number=None,

                        question_text=match.strip(),

                        marks=None,

                        question_type=question_type,

                        chapter=None,
                        topic=None,
                        subtopic=None,

                        source_file=page.source_file,
                        page_number=page.page_number,

                        extraction_confidence=page.extraction_confidence,
                        classification_confidence=0.0,

                        review_status="pending"
                    )
                )

        return questions