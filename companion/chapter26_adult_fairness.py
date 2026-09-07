"""Chapter 26 reference: simple group fairness audit on UCI Adult/Census Income.

This is an educational diagnostic, not a claim that any single fairness metric is
sufficient for a real decision system.
"""
from __future__ import annotations

import numpy as np
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def rate(mask: np.ndarray, values: np.ndarray) -> float:
    return float(values[mask].mean()) if mask.any() else float("nan")


def main() -> None:
    ds = fetch_ucirepo(id=2)
    X = ds.data.features.copy()
    y_raw = ds.data.targets.iloc[:, 0].astype(str)
    y = y_raw.str.contains(">50K", regex=False).astype(int)

    group_col = "sex" if "sex" in X.columns else "Sex"
    group = X[group_col].astype(str)
    X_model = X.drop(columns=["sex", "Sex"], errors="ignore")

    X_tr, X_te, y_tr, y_te, _g_tr, g_te = train_test_split(
        X_model, y, group, test_size=0.25, stratify=y, random_state=42
    )

    cat_cols = X_tr.select_dtypes(exclude=np.number).columns.tolist()
    num_cols = [c for c in X_tr.columns if c not in cat_cols]
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
    model = Pipeline(
        [("pre", pre), ("model", LogisticRegression(max_iter=1000))]
    )
    model.fit(X_tr, y_tr)
    pred = model.predict(X_te).astype(float)

    groups = sorted(g_te.astype(str).unique())
    y_arr = y_te.to_numpy()
    g_arr = g_te.astype(str).to_numpy()

    print("group audit on held-out predictions")
    for label in groups:
        mask = g_arr == label
        positive_rate = rate(mask, pred)
        actual_positive = mask & (y_arr == 1)
        tpr = rate(actual_positive, pred)
        print(
            f"{label:12s} n={mask.sum():5d} "
            f"predicted_positive_rate={positive_rate:.3f} TPR={tpr:.3f}"
        )


if __name__ == "__main__":
    main()
