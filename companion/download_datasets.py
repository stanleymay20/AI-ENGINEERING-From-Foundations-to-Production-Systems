"""Prepare every dataset used by the AI Engineering study edition.

Raw datasets are intentionally NOT committed to Git. This command downloads or
materializes them from their official/library-managed source into a local data/
directory and writes a SHA-256 manifest for reproducibility.

Examples
--------
# Standard non-large real-world labs + sklearn benchmarks
python companion/download_datasets.py --standard

# Everything, including large datasets, framework benchmark archives and MovieLens
python companion/download_datasets.py --all --include-large --include-movielens

# One or more named datasets
python companion/download_datasets.py --dataset bike_sharing --dataset iris
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

UCI = {
    "online_retail_ii": 502,
    "bike_sharing": 275,
    "bank_marketing": 222,
    "hydraulic_systems": 447,
    "wholesale_customers": 292,
    "sms_spam": 228,
    "household_power": 235,
    "adult": 2,
}
LARGE = {"online_retail_ii", "household_power", "hydraulic_systems"}
SKLEARN_BUILTIN = {"iris", "breast_cancer", "digits"}
SKLEARN_FETCH = {"20_newsgroups", "california_housing"}

# These datasets are better preserved in their native UCI archives rather than
# expanded into huge in-memory DataFrames by ucimlrepo.
UCI_RAW_ARCHIVES = {
    "online_retail_ii": "https://archive.ics.uci.edu/static/public/502/online%2Bretail%2Bii.zip",
    "hydraulic_systems": "https://archive.ics.uci.edu/static/public/447/condition%2Bmonitoring%2Bof%2Bhydraulic%2Bsystems.zip",
    "household_power": "https://archive.ics.uci.edu/static/public/235/individual%2Bhousehold%2Belectric%2Bpower%2Bconsumption.zip",
}

OFFICIAL_FILES = {
    "mnist": [
        ("https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz", "mnist.npz"),
    ],
    "cifar10": [
        ("https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz", "cifar-10-python.tar.gz"),
    ],
    "cifar100": [
        ("https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz", "cifar-100-python.tar.gz"),
    ],
    "imdb_reviews": [
        ("https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz", "imdb.npz"),
        ("https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb_word_index.json", "imdb_word_index.json"),
    ],
}

MOVIELENS_URL = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

STANDARD = {
    "bike_sharing",
    "bank_marketing",
    "hydraulic_systems",
    "wholesale_customers",
    "sms_spam",
    "adult",
    "iris",
    "breast_cancer",
    "digits",
    "california_housing",
    "20_newsgroups",
}

ALL_DOWNLOADABLE = (
    set(UCI)
    | SKLEARN_BUILTIN
    | SKLEARN_FETCH
    | set(OFFICIAL_FILES)
    | {"movielens_latest_small"}
)


def safe_extract_zip(archive: Path, destination: Path) -> None:
    """Extract a trusted dataset ZIP while preventing path traversal."""
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    with zipfile.ZipFile(archive) as zf:
        for member in zf.infolist():
            target = (destination / member.filename).resolve()
            if root not in target.parents and target != root:
                raise RuntimeError(f"unsafe ZIP member: {member.filename}")
        zf.extractall(destination)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def save_manifest_entry(
    entries: list[dict[str, str]], key: str, source: str, path: Path
) -> None:
    entries.append(
        {
            "dataset_key": key,
            "source": source,
            "path": str(path.as_posix()),
            "bytes": str(path.stat().st_size),
            "sha256": sha256(path),
        }
    )


def download(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".part")
    print(f"[download] {url}")
    req = urllib.request.Request(
        url, headers={"User-Agent": "AI-Engineering-Companion/2.4"}
    )
    with urllib.request.urlopen(req, timeout=120) as r, tmp.open("wb") as f:
        shutil.copyfileobj(r, f)
    tmp.replace(path)


def fetch_uci_raw_archive(
    key: str, out: Path, entries: list[dict[str, str]]
) -> None:
    url = UCI_RAW_ARCHIVES[key]
    target = out / "uci" / key
    target.mkdir(parents=True, exist_ok=True)
    archive = target / f"{key}.zip"

    if not archive.exists():
        download(url, archive)
    else:
        print(f"[cached] {archive}")

    save_manifest_entry(entries, key, url, archive)

    extracted = target / "raw"
    if not extracted.exists():
        safe_extract_zip(archive, extracted)
    print(f"[UCI raw] {key}: extracted to {extracted}")


def fetch_uci(
    key: str, uci_id: int, out: Path, entries: list[dict[str, str]]
) -> None:
    from ucimlrepo import fetch_ucirepo

    target = out / "uci" / key
    target.mkdir(parents=True, exist_ok=True)
    print(f"[UCI] {key} (id={uci_id})")

    ds = fetch_ucirepo(id=uci_id)

    features = target / "features.csv"
    ds.data.features.to_csv(features, index=False)
    save_manifest_entry(entries, key, f"UCI id={uci_id}", features)

    if ds.data.targets is not None:
        targets = target / "targets.csv"
        ds.data.targets.to_csv(targets, index=False)
        save_manifest_entry(entries, key, f"UCI id={uci_id}", targets)

    meta = {
        "uci_id": uci_id,
        "name": (
            ds.metadata.get("name")
            if isinstance(ds.metadata, dict)
            else getattr(ds.metadata, "name", None)
        ),
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    meta_path = target / "metadata.json"
    meta_path.write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    save_manifest_entry(entries, key, f"UCI id={uci_id}", meta_path)


def fetch_sklearn_builtin(
    key: str, out: Path, entries: list[dict[str, str]]
) -> None:
    import pandas as pd
    from sklearn.datasets import load_breast_cancer, load_digits, load_iris

    loaders = {
        "iris": load_iris,
        "breast_cancer": load_breast_cancer,
        "digits": load_digits,
    }

    print(f"[sklearn built-in] {key}")
    bunch = loaders[key](as_frame=True)

    target = out / "sklearn" / key
    target.mkdir(parents=True, exist_ok=True)

    frame = (
        bunch.frame
        if getattr(bunch, "frame", None) is not None
        else pd.DataFrame(bunch.data)
    )
    path = target / "data.csv"
    frame.to_csv(path, index=False)
    save_manifest_entry(
        entries, key, f"sklearn.datasets.{loaders[key].__name__}", path
    )


def fetch_20_newsgroups(
    out: Path, entries: list[dict[str, str]]
) -> None:
    from sklearn.datasets import fetch_20newsgroups

    print("[sklearn fetch] 20_newsgroups")
    target = out / "sklearn" / "20_newsgroups"
    target.mkdir(parents=True, exist_ok=True)

    for subset in ("train", "test"):
        bunch = fetch_20newsgroups(subset=subset, remove=())
        path = target / f"{subset}.jsonl"
        with path.open("w", encoding="utf-8") as f:
            for text, label in zip(bunch.data, bunch.target):
                f.write(
                    json.dumps(
                        {"target": int(label), "text": text},
                        ensure_ascii=False,
                    )
                    + "\n"
                )
        save_manifest_entry(
            entries,
            "20_newsgroups",
            "sklearn.datasets.fetch_20newsgroups",
            path,
        )


def fetch_california_housing_dataset(
    out: Path, entries: list[dict[str, str]]
) -> None:
    from sklearn.datasets import fetch_california_housing

    print("[sklearn fetch] california_housing")
    target = out / "sklearn" / "california_housing"
    target.mkdir(parents=True, exist_ok=True)

    bunch = fetch_california_housing(
        as_frame=True, data_home=str(target / "cache")
    )
    path = target / "data.csv"
    bunch.frame.to_csv(path, index=False)
    save_manifest_entry(
        entries,
        "california_housing",
        "sklearn.datasets.fetch_california_housing",
        path,
    )


def fetch_official_file_dataset(
    key: str, out: Path, entries: list[dict[str, str]]
) -> None:
    target = out / "benchmarks" / key
    target.mkdir(parents=True, exist_ok=True)

    for url, filename in OFFICIAL_FILES[key]:
        path = target / filename
        if not path.exists():
            download(url, path)
        else:
            print(f"[cached] {path}")
        save_manifest_entry(entries, key, url, path)


def fetch_movielens(
    out: Path, entries: list[dict[str, str]]
) -> None:
    print("[GroupLens] MovieLens latest-small")
    target = out / "grouplens" / "movielens_latest_small"
    target.mkdir(parents=True, exist_ok=True)

    archive = target / "ml-latest-small.zip"
    if not archive.exists():
        download(MOVIELENS_URL, archive)
    save_manifest_entry(entries, "movielens_latest_small", MOVIELENS_URL, archive)

    extracted = target / "ml-latest-small"
    if not extracted.exists():
        safe_extract_zip(archive, target)

    for path in sorted(extracted.glob("*")):
        if path.is_file():
            save_manifest_entry(
                entries, "movielens_latest_small", MOVIELENS_URL, path
            )


def load_registry(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return {row["dataset_key"]: row for row in csv.DictReader(f)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="data",
        help="Local data directory (gitignored by default)",
    )
    parser.add_argument(
        "--registry", default="companion/dataset_registry.csv"
    )
    parser.add_argument(
        "--list", action="store_true", help="List registered datasets and exit"
    )
    parser.add_argument(
        "--dataset", action="append", default=[], help="Dataset key; repeat as needed"
    )
    parser.add_argument(
        "--standard",
        action="store_true",
        help="Fetch standard non-large labs and sklearn benchmarks",
    )
    parser.add_argument(
        "--all", action="store_true", help="Select every downloadable dataset"
    )
    parser.add_argument(
        "--include-large", action="store_true", help="Allow large UCI datasets"
    )
    parser.add_argument(
        "--include-movielens",
        action="store_true",
        help="Accept current GroupLens terms and fetch MovieLens",
    )
    args = parser.parse_args()

    registry = load_registry(Path(args.registry))

    if args.list:
        for key, row in registry.items():
            print(
                f"{key:24} {row['category']:12} "
                f"ch={row['chapters']:8} {row['dataset']}"
            )
        return

    selected = set(args.dataset)
    if args.standard:
        selected |= STANDARD
    if args.all:
        selected |= ALL_DOWNLOADABLE

    if not selected:
        parser.error("Choose --standard, --all, or at least one --dataset KEY")

    unknown = selected - set(registry)
    if unknown:
        parser.error(f"Unknown dataset key(s): {', '.join(sorted(unknown))}")

    blocked_large = selected & LARGE if not args.include_large else set()
    if blocked_large:
        print(
            "Skipping large datasets without --include-large:",
            ", ".join(sorted(blocked_large)),
        )
        selected -= blocked_large

    if "movielens_latest_small" in selected and not args.include_movielens:
        print(
            "Skipping MovieLens without --include-movielens "
            "(review current GroupLens terms first)."
        )
        selected.remove("movielens_latest_small")

    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    entries: list[dict[str, str]] = []

    for key in sorted(selected):
        if key in UCI_RAW_ARCHIVES:
            fetch_uci_raw_archive(key, out, entries)
        elif key in UCI:
            fetch_uci(key, UCI[key], out, entries)
        elif key in SKLEARN_BUILTIN:
            fetch_sklearn_builtin(key, out, entries)
        elif key == "20_newsgroups":
            fetch_20_newsgroups(out, entries)
        elif key == "california_housing":
            fetch_california_housing_dataset(out, entries)
        elif key in OFFICIAL_FILES:
            fetch_official_file_dataset(key, out, entries)
        elif key == "movielens_latest_small":
            fetch_movielens(out, entries)
        elif key == "synthetic_sklearn":
            print("synthetic_sklearn is generated by examples; no download required")

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "registry": str(Path(args.registry).as_posix()),
        "files": entries,
    }
    manifest_path = out / "DATASET_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {manifest_path} with {len(entries)} file records")


if __name__ == "__main__":
    main()
