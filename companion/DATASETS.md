# Dataset reproducibility

The repository does **not** commit raw third-party datasets into Git. Instead, it makes every dataset used by the book reproducibly obtainable from its official or library-managed source.

## One-command setup

Install the lightweight data dependencies:

```bash
python -m pip install -r companion/requirements-data.txt
```

Prepare the standard real-world labs and scikit-learn benchmarks:

```bash
python companion/download_datasets.py --standard
```

Prepare every downloadable dataset used by the book, including the two large UCI datasets and MovieLens:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

MovieLens is deliberately opt-in because its current GroupLens usage terms must be reviewed at the time of download. Raw MovieLens data is not redistributed by this repository.

List the controlled registry:

```bash
python companion/download_datasets.py --list
```

Fetch just one dataset:

```bash
python companion/download_datasets.py --dataset bike_sharing
```

The command writes `data/DATASET_MANIFEST.json` containing the files actually prepared plus SHA-256 hashes. The `data/` directory is gitignored.

## Coverage model

The registry covers four acquisition types:

1. **Real-world UCI labs** — downloaded using official UCI identifiers via `ucimlrepo`.
2. **scikit-learn benchmarks** — materialized from `load_*` functions or fetched using `fetch_20newsgroups` / `fetch_california_housing`.
3. **Framework benchmark archives** — MNIST, CIFAR-10, CIFAR-100 and IMDB are fetched from the upstream URLs used by the ecosystem rather than duplicated in Git.
4. **Synthetic examples** — `make_classification`, `make_blobs`, and `make_moons` are generated deterministically from the code; there is no dataset file to download.

## Controlled book datasets

The registry includes all named datasets materially used by the current study edition: Online Retail II, Bike Sharing, Bank Marketing, Condition Monitoring of Hydraulic Systems, Wholesale Customers, SMS Spam Collection, MovieLens latest-small, Individual Household Electric Power Consumption, Adult/Census Income, Iris, Breast Cancer Wisconsin Diagnostic, Digits, California Housing, 20 Newsgroups, MNIST, CIFAR-10, CIFAR-100 and IMDB Movie Reviews, plus the scikit-learn synthetic generators used in examples.

## ImageNet note

The book discusses ImageNet and uses ImageNet-pretrained model weights in transfer-learning examples. It does **not** require the reader to download or redistribute the raw ImageNet dataset. Keras/TensorFlow retrieves the selected pretrained weights as a model asset when those examples are run.

## Redistribution rule

A downloader is not a license grant. The registry records the intended book policy, but upstream terms govern. Large datasets and datasets with restrictive/unclear redistribution terms are fetched locally and never committed as repository blobs.
