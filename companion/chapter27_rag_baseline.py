"""Chapter 27: fully offline lexical retrieval baseline + retrieval evaluation."""
from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    source: str
    text: str


DOCS = [
    Chunk("returns-1", "returns.md", "Customers may return unopened items within 30 days of delivery."),
    Chunk("ship-1", "shipping.md", "Standard shipping normally takes three to five business days."),
    Chunk("warranty-1", "warranty.md", "Hardware products include a two-year limited warranty."),
    Chunk("privacy-1", "privacy.md", "Account deletion requests are normally processed within seven days."),
]
QUERIES = [
    ("How long do I have to return an unopened item?", "returns-1"),
    ("When should standard delivery arrive?", "ship-1"),
    ("How long is the hardware warranty?", "warranty-1"),
    ("How quickly is an account deletion processed?", "privacy-1"),
]


class TfidfRetriever:
    def __init__(self, chunks: list[Chunk]):
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
        self.matrix = self.vectorizer.fit_transform([c.text for c in chunks])

    def retrieve(self, query: str, k: int = 3) -> list[tuple[Chunk, float]]:
        q = self.vectorizer.transform([query])
        scores = cosine_similarity(q, self.matrix)[0]
        order = scores.argsort()[::-1][:k]
        return [(self.chunks[i], float(scores[i])) for i in order]


def evaluate(retriever: TfidfRetriever, k: int = 3) -> None:
    hits, reciprocal_ranks = 0, []
    for query, expected in QUERIES:
        ranked = [c.chunk_id for c, _ in retriever.retrieve(query, k=k)]
        if expected in ranked:
            hits += 1
            reciprocal_ranks.append(1 / (ranked.index(expected) + 1))
        else:
            reciprocal_ranks.append(0.0)
    print(f"Recall@{k}: {hits / len(QUERIES):.3f}")
    print(f"MRR: {sum(reciprocal_ranks) / len(reciprocal_ranks):.3f}")


def main() -> None:
    retriever = TfidfRetriever(DOCS)
    evaluate(retriever)
    for chunk, score in retriever.retrieve("Can I return an unopened purchase?"):
        print(f"{score:.3f} | {chunk.source} | {chunk.text}")


if __name__ == "__main__":
    main()
