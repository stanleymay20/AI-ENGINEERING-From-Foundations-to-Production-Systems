"""Chapter 9 reference: Wholesale Customers clustering."""
from __future__ import annotations

from ucimlrepo import fetch_ucirepo
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    ds = fetch_ucirepo(id=292)
    X = ds.data.features.copy().select_dtypes(include="number")
    X = X.drop(
        columns=[c for c in ["Channel", "Region"] if c in X.columns],
        errors="ignore",
    )

    for k in range(2, 7):
        pipe = Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "cluster",
                    KMeans(n_clusters=k, n_init="auto", random_state=42),
                ),
            ]
        )
        labels = pipe.fit_predict(X)
        scaled = pipe.named_steps["scale"].transform(X)
        print(f"k={k}: silhouette={silhouette_score(scaled, labels):.3f}")


if __name__ == "__main__":
    main()
