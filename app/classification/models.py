from dataclasses import dataclass


@dataclass
class ClassificationResult:
    chapter: str
    topic: str
    confidence: float