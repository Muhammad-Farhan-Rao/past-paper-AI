from app.classification.base_classifier import BaseClassifier


class KeywordMatcher(BaseClassifier):

    def match(self, question_text: str, syllabus: dict) -> BaseClassifier:

        question = question_text.lower()

        best_chapter = "Unknown"
        best_topic = "Unknown"
        best_score = 0

        for chapter, keywords in syllabus.items():

            score = 0

            for keyword in keywords:

                if keyword.lower() in question:
                    score += 1

                    if score > best_score:
                        best_score = score
                        best_chapter = chapter
                        best_topic = keyword

        confidence = min(best_score / 3, 1.0)

        return BaseClassifier(
            chapter=best_chapter,
            topic=best_topic,
            confidence=confidence
        )