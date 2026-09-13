"""Optional legacy/reference recommender using MovieLens latest-small.

This script is retained for readers who independently choose to explore MovieLens.
It is NOT the Chapter 17 assessed lab for the v3.23.8 publication-repair candidate;
that lab now uses Online Retail II under CC BY 4.0. Review current GroupLens terms
before downloading or using MovieLens:

    python companion/download_datasets.py --dataset movielens_latest_small --include-movielens
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def find_ratings(data_root: Path) -> Path:
    root = data_root / "grouplens" / "movielens_latest_small"
    matches = list(root.rglob("ratings.csv"))
    if not matches:
        raise FileNotFoundError(
            "ratings.csv not found. Run the MovieLens downloader with --include-movielens."
        )
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="data")
    parser.add_argument("--movie-id", type=int, default=1)
    args = parser.parse_args()

    ratings = pd.read_csv(find_ratings(Path(args.data_root)))
    counts = ratings.groupby("movieId").size()
    popular = counts[counts >= 20].index
    subset = ratings[ratings["movieId"].isin(popular)]
    matrix = subset.pivot_table(
        index="movieId", columns="userId", values="rating", fill_value=0.0
    )

    if args.movie_id not in matrix.index:
        fallback = int(matrix.index[0])
        print(f"movieId={args.movie_id} lacks enough ratings; using {fallback}")
        movie_id = fallback
    else:
        movie_id = args.movie_id

    target = matrix.loc[[movie_id]]
    scores = cosine_similarity(target, matrix)[0]
    ranked = (
        pd.Series(scores, index=matrix.index)
        .drop(movie_id)
        .sort_values(ascending=False)
    )

    print(f"item-user matrix={matrix.shape}")
    print(f"nearest items to movieId={movie_id}:")
    print(ranked.head(10).round(3).to_string())


if __name__ == "__main__":
    main()
