import json
from dataclasses import asdict
from pathlib import Path

from app.domain.question import Question


class QuestionExporter:

    def export(
            self,
            questions: list[Question],
            output_file: Path
    ):

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
                output_file,
                "w",
                encoding="utf-8"
        ) as file:

            json.dump(
                [asdict(question)
                 for question in questions],

                file,

                indent=4,

                ensure_ascii=False
            )