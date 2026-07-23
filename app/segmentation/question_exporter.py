import json
from dataclasses import asdict
from pathlib import Path
from app.utils.logger import logger

from app.domain.question import Question


class QuestionExporter:

    def export_json(self, questions: list[Question], output_path: Path):

        data = [asdict(question) for question in questions]

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(f"Saved {len(questions)} questions to {output_path}")