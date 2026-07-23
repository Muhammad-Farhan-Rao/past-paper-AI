import re
from typing import List
from app.utils.id_generator import IdGenerator
from app.domain.question import Question
from app.metadata.filename_parser import FilenameParser
from app.domain.page import Page
from app.utils.logger import logger

class QuestionSegmenter:

    def _build_question(
            self,
            page,
            metadata,
            section,
            question_number,
            sub_question,
            text
    ):

        return Question(

            id=IdGenerator.generate(),

            board="BISE Lahore",

            student_class="10",

            subject=metadata["subject"],

            year=metadata["year"],

            exam_type=metadata["exam_type"],

            section=section,

            question_number=question_number,

            sub_question_number=sub_question,

            question_text=text,

            marks=2 if section == "PART-I" else None,

            question_type="Short Question" if section == "PART-I" else "Long Question",

            chapter=None,

            topic=None,

            subtopic=None,

            page_number=page.page_number,

            source_file=page.source_file,

            extraction_confidence=page.extraction_confidence,

            classification_confidence=0.0,

            review_status="pending"
        )

    def segment(self, pages: List[Page]):
        parser = FilenameParser()

        all_questions = []

        for page in pages:

            metadata = parser.parse(page.source_file)

            section = self._find_section(page.text)

            blocks = self._split_main_questions(page.text)

            for block in blocks:

                main_question = self._extract_main_question_number(block)

                sub_questions = self._split_sub_questions(block)

                for number, text in sub_questions:
                    question = self._build_question(
                        page,
                        metadata,
                        section,
                        main_question,
                        number,
                        text
                    )

                    all_questions.append(question)
        logger.info(f"Extracted {len(all_questions)} questions")

        return all_questions

    def _find_section(self, text: str):

        match = re.search(r"PART\s*[–-]\s*([IVX]+)", text)

        return f"PART-{match.group(1)}" if match else "Unknown"

    def _split_main_questions(self, text: str):

        return re.findall(
            r"(Q\.\d+.*?)(?=PART\s*[–-]|Q\.\d+|\Z)",
            text,
            flags=re.DOTALL,
        )

    def _extract_main_question_number(self, block: str):

        match = re.search(r"Q\.(\d+)", block)

        return int(match.group(1)) if match else None

    def _split_sub_questions(self, block: str):

        pattern = r"\(([ivx]+|[a-z])\)"

        parts = re.split(pattern, block)

        sub_questions = []

        for i in range(1, len(parts), 2):

            number = parts[i]

            text = parts[i + 1].strip()

            sub_questions.append((number, text))

        return sub_questions