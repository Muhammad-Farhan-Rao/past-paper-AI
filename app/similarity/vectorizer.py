from sklearn.feature_extraction.text import TfidfVectorizer


class QuestionVectorizer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit_transform(self, questions: list[str]):
        return self.vectorizer.fit_transform(questions)

    def transform(self, questions: list[str]):
        return self.vectorizer.transform(questions)