from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEngine:

    def find_similar(
        self,
        vectors,
        question_index,
        top_k=5
    ):

        similarities = cosine_similarity(
            vectors[question_index],
            vectors
        ).flatten()

        ranked = sorted(
            enumerate(similarities),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[1:top_k + 1]