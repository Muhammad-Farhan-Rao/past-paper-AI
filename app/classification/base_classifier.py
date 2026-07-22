from abc import ABC, abstractmethod

from app.classification.models import ClassificationResult


class BaseClassifier(ABC):

    @abstractmethod
    def classify(self, question_text: str) -> ClassificationResult:
        pass