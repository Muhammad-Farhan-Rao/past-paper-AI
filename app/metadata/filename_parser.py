import re
from pathlib import Path


class FilenameParser:

    SUBJECTS = {
        "Math": "Mathematics",
        "Physics": "Physics",
        "Chemistry": "Chemistry",
        "Biology": "Biology",
        "English": "English",
        "Computer": "Computer Science"
    }

    def parse(self, file_path):

        filename = Path(file_path).stem

        metadata = {
            "subject": None,
            "year": None,
            "exam_type": None
        }

        # Subject
        for short_name, full_name in self.SUBJECTS.items():

            if short_name.lower() in filename.lower():
                metadata["subject"] = full_name
                break

        # Year
        match = re.search(r"(20\d{2})", filename)

        if match:
            metadata["year"] = int(match.group())

        # Exam Type
        if "annual" in filename.lower():
            metadata["exam_type"] = "Annual"

        elif "supply" in filename.lower():
            metadata["exam_type"] = "Supply"

        return metadata