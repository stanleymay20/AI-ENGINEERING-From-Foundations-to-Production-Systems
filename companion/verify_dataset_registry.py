"""Static QA for the book's dataset registry and acquisition coverage."""
from __future__ import annotations

import csv
from pathlib import Path

REQUIRED = {
    "online_retail_ii", "bike_sharing", "bank_marketing", "hydraulic_systems",
    "wholesale_customers", "sms_spam", "movielens_latest_small", "household_power",
    "adult", "iris", "breast_cancer", "digits", "california_housing",
    "20_newsgroups", "mnist", "cifar10", "cifar100", "imdb_reviews",
    "synthetic_sklearn",
}
REQUIRED_COLUMNS = {
    "dataset_key", "dataset", "chapters", "category", "source", "identifier_or_url",
    "acquisition", "license_or_terms", "redistribution_policy", "large",
}


def main() -> None:
    path = Path(__file__).with_name("dataset_registry.csv")
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert rows, "dataset registry is empty"
    assert REQUIRED_COLUMNS <= set(rows[0]), "registry columns incomplete"

    keys = [r["dataset_key"] for r in rows]
    assert len(keys) == len(set(keys)), "duplicate dataset_key"

    missing = REQUIRED - set(keys)
    assert not missing, f"missing required datasets: {sorted(missing)}"

    for row in rows:
        for col in (
            "dataset_key", "dataset", "source", "acquisition",
            "license_or_terms", "redistribution_policy",
        ):
            assert row[col].strip(), f"{row['dataset_key']}: blank {col}"

    print(f"PASS dataset registry: {len(rows)} entries; all required book datasets covered")


if __name__ == "__main__":
    main()
