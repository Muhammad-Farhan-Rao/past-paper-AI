import json
from pathlib import Path


class SyllabusLoader:

    def load(self, file_path: Path) -> dict:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)