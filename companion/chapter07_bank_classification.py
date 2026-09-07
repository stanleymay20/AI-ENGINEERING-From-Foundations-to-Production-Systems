"""Chapter 7 reference: Bank Marketing classification with a leakage-aware pipeline."""
from __future__ import annotations

import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    ds = fetch_ucirepo(id=222)
    X = ds.data.features.copy()
    y = ds.data.targets.copy()
    if isinstance(y, pd.DataFrame):
        y = y.iloc[:, 0]
    y = y.astype(str).str.lower().map({"yes": 1, "no": 0}).fillna(
        pd.to_numeric(y, errors="coerce")
    )

    # 'duration' is only known after a marketing call ends and is therefore
    # leakage for a realistic pre-call targeting model.
    X = X.drop(columns=["duration"], errors="ignore")

    cat_cols = X.select_dtypes(exclude=np.number).columns.tolist()
    num_cols = [c for c in X.columns if c not in cat_cols]
    pre = ColumnTransformer(
        [
            (
                "num",
                Pipeline(
                    [
                        ("imp", SimpleImputer(strategy="median")),
                        ("scale", StandardScaler()),
                    ]
                ),
                num_cols,
            ),
            (
                "cat",
                Pipeline(
                    [
                        ("imp", SimpleImputer(strategy="most_frequent")),
                        ("ohe", OneHotEncoder(handle_unknown="ignore")),
                    ]
                ),
                cat_cols,
            ),
        ]
    )
    clf = Pipeline(
        [
            ("pre", pre),
            (
                "model",
                LogisticRegression(max_iter=1000, class_weight="balanced"),
            ),
        ]
    )

    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )
    clf.fit(X_tr, y_tr)
    prob = clf.predict_proba(X_te)[:, 1]
    pred = (prob >= 0.5).astype(int)

    print(f"ROC-AUC: {roc_auc_score(y_te, prob):.3f}")
    print(classification_report(y_te, pred, digits=3))


if __name__ == "__main__":
    main()
