"""Chapter 6 reference: real-data bike demand regression.

Fetches UCI Bike Sharing (id=275), derives a chronological ordering when date/hour
fields are available, compares a median baseline with a HistGradientBoostingRegressor,
and reports MAE/RMSE. This is a study reference, not a production forecast service.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder


def main() -> None:
    ds = fetch_ucirepo(id=275)
    X = ds.data.features.copy()
    y = ds.data.targets.copy()
    if isinstance(y, pd.DataFrame):
        target_col = "cnt" if "cnt" in y.columns else y.columns[-1]
        y = y[target_col]
    y = pd.to_numeric(y, errors="coerce")

    work = X.copy()
    if "dteday" in work.columns:
        dates = pd.to_datetime(work["dteday"], errors="coerce")
        hours = (
            pd.to_numeric(work["hr"], errors="coerce").fillna(0)
            if "hr" in work.columns
            else 0
        )
        order_key = dates + pd.to_timedelta(hours, unit="h")
        order = np.argsort(order_key.fillna(pd.Timestamp.max).to_numpy())
    else:
        order = np.arange(len(work))

    X = X.iloc[order].reset_index(drop=True)
    y = y.iloc[order].reset_index(drop=True)
    split = int(len(X) * 0.8)
    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    X_train = X_train.drop(columns=["dteday"], errors="ignore")
    X_test = X_test.drop(columns=["dteday"], errors="ignore")

    cat_cols = X_train.select_dtypes(exclude=np.number).columns.tolist()
    num_cols = [c for c in X_train.columns if c not in cat_cols]
    preprocess = ColumnTransformer(
        [
            ("num", SimpleImputer(strategy="median"), num_cols),
            (
                "cat",
                Pipeline(
                    [
                        ("impute", SimpleImputer(strategy="most_frequent")),
                        (
                            "encode",
                            OrdinalEncoder(
                                handle_unknown="use_encoded_value", unknown_value=-1
                            ),
                        ),
                    ]
                ),
                cat_cols,
            ),
        ]
    )
    model = Pipeline(
        [
            ("preprocess", preprocess),
            ("model", HistGradientBoostingRegressor(random_state=42)),
        ]
    )

    baseline = np.full(len(y_test), float(y_train.median()))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    for name, p in [("Median baseline", baseline), ("Gradient boosting", pred)]:
        mae = mean_absolute_error(y_test, p)
        rmse = mean_squared_error(y_test, p) ** 0.5
        print(f"{name:18s} MAE={mae:.3f} RMSE={rmse:.3f}")


if __name__ == "__main__":
    main()
