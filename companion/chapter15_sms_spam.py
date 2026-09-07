"""Chapter 15 reference: SMS Spam text classification."""
from __future__ import annotations

import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


def main() -> None:
    ds = fetch_ucirepo(id=228)
    X = ds.data.features.copy()
    y = ds.data.targets.copy()

    text_col = X.columns[0]
    target = y.iloc[:, 0] if isinstance(y, pd.DataFrame) else y
    target = target.astype(str).str.lower().map({"spam": 1, "ham": 0})

    X_tr, X_te, y_tr, y_te = train_test_split(
        X[text_col].astype(str),
        target,
        test_size=0.25,
        stratify=target,
        random_state=42,
    )

    clf = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), min_df=2)),
            (
                "model",
                LogisticRegression(max_iter=1000, class_weight="balanced"),
            ),
        ]
    )
    clf.fit(X_tr, y_tr)
    print(classification_report(y_te, clf.predict(X_te), digits=3))


if __name__ == "__main__":
    main()
