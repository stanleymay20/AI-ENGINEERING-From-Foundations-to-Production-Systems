# Companion Code

This directory accompanies the frozen **v3.22 Code-Verified Illustrated Study Edition** of *AI Engineering: From Foundations to Production Systems* and is being synchronized on this branch for the **v3.23.8 publication-repair review candidate**. v3.22 remains the frozen authority until an explicit successor promotion.

The deterministic reference environment and principal companion-code architecture were established during the validated technical-core programme. Candidate-specific changes must pass fresh repository CI before they can be cited as successor evidence.

## What is implemented

The repository includes:

- real-data chapter scripts for principal applied labs;
- a controlled `dataset_registry.csv` for materially used named datasets;
- `download_datasets.py` for controlled acquisition without casually committing raw third-party data;
- `verify_dataset_registry.py` to fail CI if required dataset coverage is lost;
- deterministic reference assertions and output smoke tests;
- core/reference/data dependency files;
- a Chapter 29 production-capstone acceptance checklist.

See [DATASETS.md](DATASETS.md) for dataset setup and redistribution rules.

## Reproducibility standard

Examples fall into three categories:

1. **Deterministic reference checks** — expected outputs are regression-tested in a controlled reference environment.
2. **Real-data labs** — require official datasets and may need network access.
3. **Version/service-sensitive examples** — TensorFlow, Transformers, MLflow, DVC, LIME, AIF360, Docker, hosted model APIs, and multi-GPU workflows. These must not be represented as locally verified unless that exact execution path was run.

## Current layout

```text
chapter03_04_online_retail_eda.py
chapter06_bike_regression.py
chapter07_bank_classification.py
chapter08_california_regression.py
chapter08_hydraulic_features.py
chapter09_wholesale_clustering.py
chapter15_sms_spam.py
chapter17_online_retail_recommender.py
chapter22_power_timeseries_baseline.py
chapter26_adult_fairness.py
chapter27_rag_baseline.py
chapter28_tool_agent.py
chapter29_capstone/
dataset_registry.csv
download_datasets.py
verify_dataset_registry.py
DATASETS.md
reference_assertions.py
reference_output_smoke.py
requirements-core.txt
requirements-data.txt
requirements-reference.txt
```

## Chapter 17 dataset control

The v3.23.8 candidate uses **Online Retail II** for the recommendation lab. It treats valid customer-product purchases as implicit feedback, preserves timestamps for chronological evaluation, and does not invent explicit ratings from transaction quantities. The dataset is the same controlled UCI source used in Chapters 3-4, DOI `10.24432/C5CG6D`, recorded as CC BY 4.0 in the registry.

## Dataset rule

Raw third-party datasets are not part of Git history. The repository records provenance, acquisition method, usage terms, and reproducible materialization instructions. `data/` remains gitignored.

## Reader support and errata

- Book/version policy: [`../BOOK_VERSION.md`](../BOOK_VERSION.md)
- Confirmed errata: [`../ERRATA.md`](../ERRATA.md)
- Suspected defects: open a repository Issue and identify the book version, location, evidence, and environment where relevant.

## Code-map boundary

The book promises standalone scripts for the major assessed labs, not a one-to-one `.py` duplicate of every instructional cell in all 30 chapters. See [`../CHAPTER_TO_CODE_MAP.md`](../CHAPTER_TO_CODE_MAP.md) for the controlled map.

The publication rule is simple: **do not confuse illustrative output with verified output**. Any result printed in the book should either be reproducibly generated under the stated reference environment or clearly labelled representative/version-sensitive.
