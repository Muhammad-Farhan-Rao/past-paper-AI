import json
from dataclasses import asdict
from pathlib import Path

from app.domain.page import Page


class JSONExporter:

    def export(self, pages: list[Page], output_file: Path):

        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(
                [asdict(page) for page in pages],
                file,
                indent=4,
                ensure_ascii=False
            )