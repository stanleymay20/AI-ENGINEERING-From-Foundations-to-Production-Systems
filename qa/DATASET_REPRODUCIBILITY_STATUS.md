# Dataset & Companion Reproducibility Status

**Book:** AI Engineering: From Foundations to Production Systems  
**Frozen authority:** v3.22  
**Candidate alignment:** v3.23.8 production-repair review candidate  
**Status:** REVALIDATION REQUIRED ON THIS BRANCH

## Dataset coverage

`companion/dataset_registry.csv` contains controlled entries for every dataset materially used by the v3.23.8 candidate plus the optional MovieLens reference.

The required book datasets include:

- Online Retail II — Chapters 3-4 and 17
- Bike Sharing
- Bank Marketing
- Condition Monitoring of Hydraulic Systems
- Wholesale Customers
- SMS Spam Collection
- Individual Household Electric Power Consumption
- Adult / Census Income
- Iris
- Breast Cancer Wisconsin (Diagnostic)
- Digits
- California Housing
- 20 Newsgroups
- MNIST
- CIFAR-10
- CIFAR-100
- IMDB Movie Reviews
- scikit-learn synthetic generators

MovieLens latest-small is retained only as an **optional reference** and is not a v3.23.8 book dependency. The Chapter 17 assessed recommendation lab now uses Online Retail II under UCI CC BY 4.0.

ImageNet is discussed and ImageNet-pretrained weights are used in transfer-learning examples, but raw ImageNet is not a reader dataset dependency and is therefore not redistributed or downloaded by the dataset preparation command.

## Repository policy

Raw third-party datasets are intentionally excluded from Git history. Instead, the repository contains:

- provenance and chapter mapping;
- official/library-managed acquisition methods;
- license/terms notes and redistribution policy;
- a one-command dataset preparation tool;
- SHA-256 manifests for locally materialized files;
- reader-facing setup instructions;
- real-data chapter scripts for the principal applied labs.

`data/` remains gitignored.

## Commands

Standard setup:

```bash
python -m pip install -r companion/requirements-data.txt
python companion/download_datasets.py --standard
```

Chapter 17 Online Retail II recommendation lab:

```bash
python companion/download_datasets.py --dataset online_retail_ii --include-large
python companion/chapter17_online_retail_recommender.py
```

Optional MovieLens exploration remains explicitly opt-in:

```bash
python companion/download_datasets.py --dataset movielens_latest_small --include-movielens
```

## Revalidation gate

The previous frozen-v3.22 CI evidence remains historical evidence only. Because this branch changes the Chapter 17 dataset mapping and adds a new companion script, promotion requires a fresh exact-head GitHub Actions run covering compilation, dataset-registry verification, dataset CLI enumeration, existing deterministic checks, RAG/agent smoke checks, and reference-output assertions.

A green repository CI run will not imply that every large/network-dependent third-party dataset was freshly downloaded. External-source availability can change independently of the repository. The acquisition code and registry are source-controlled, while upstream providers and their current license/usage terms remain authoritative.

## Verdict

**Architecture is aligned for v3.23.8, but this branch is not publication-green until fresh CI passes.**
