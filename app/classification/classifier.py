from app.classification.keyword_matcher import KeywordMatcher
from app.domain.question import Question


class QuestionClassifier:

    def __init__(self):
        self.matcher = KeywordMatcher()

    def classify(self, questions: list[Question], syllabus: dict):

        for question in questions:

            result = self.matcher.match(
                question.question_text,
                syllabus
            )

            question.chapter = result.chapter
            question.topic = result.topic
            question.classification_confidence = result.confidence

        return questions