"""Chapter 22 reference: household power forecasting baseline.

Uses UCI Individual Household Electric Power Consumption (id=235). The task is
one-step-ahead prediction of Global_active_power using lagged values. This deliberately
starts with a simple baseline before deep-learning extensions.
"""
from __future__ import annotations

import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.metrics import mean_absolute_error


def main() -> None:
    ds = fetch_ucirepo(id=235)
    X = ds.data.features.copy()

    candidates = [c for c in X.columns if "Global_active_power" in str(c)]
    if not candidates and ds.data.targets is not None:
        targ = ds.data.targets.copy()
        candidates = [c for c in targ.columns if "Global_active_power" in str(c)]
        if candidates:
            X[candidates[0]] = targ[candidates[0]]

    if not candidates:
        raise RuntimeError(
            "Global_active_power column not found; inspect UCI metadata/schema."
        )

    s = pd.to_numeric(X[candidates[0]], errors="coerce").dropna().reset_index(drop=True)

    actual = s.iloc[1:].to_numpy()
    pred = s.iloc[:-1].to_numpy()
    split = int(len(actual) * 0.8)

    print(
        f"Held-out persistence MAE: "
        f"{mean_absolute_error(actual[split:], pred[split:]):.4f}"
    )
    print(
        "Next: compare a seasonal baseline and an ML/LSTM model on the same "
        "chronological holdout."
    )


if __name__ == "__main__":
    main()
