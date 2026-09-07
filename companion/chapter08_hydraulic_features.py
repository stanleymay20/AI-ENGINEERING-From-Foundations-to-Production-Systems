"""Chapter 8 reference: predictive-maintenance features from hydraulic sensor streams.

Run first:
    python companion/download_datasets.py --dataset hydraulic_systems --include-large

This deliberately uses a small sensor subset to keep memory bounded. It aggregates
cycle-level statistics and predicts cooler condition from the official profile labels.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def locate(root: Path, name: str) -> Path:
    matches = list(root.rglob(name))
    if not matches:
        raise FileNotFoundError(
            f"{name} not found under {root}. Run the hydraulic dataset downloader first."
        )
    return matches[0]


def aggregate_sensor(path: Path) -> np.ndarray:
    x = np.loadtxt(path)
    return np.column_stack(
        [
            x.mean(axis=1),
            x.std(axis=1),
            x.min(axis=1),
            x.max(axis=1),
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", default="data")
    args = parser.parse_args()

    raw = Path(args.data_root) / "uci" / "hydraulic_systems" / "raw"
    profile = np.loadtxt(locate(raw, "profile.txt"))

    selected = ["TS1.txt", "FS1.txt", "VS1.txt"]
    feature_blocks = [aggregate_sensor(locate(raw, name)) for name in selected]
    X = np.hstack(feature_blocks)
    y = profile[:, 0].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, stratify=y, random_state=42
    )
    model = HistGradientBoostingClassifier(random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print(f"feature matrix={X.shape}; target classes={sorted(np.unique(y).tolist())}")
    print(classification_report(y_test, pred, digits=3))


if __name__ == "__main__":
    main()
