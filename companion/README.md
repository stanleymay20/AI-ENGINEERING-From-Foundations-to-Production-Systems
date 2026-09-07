# Companion Code

This directory accompanies *AI Engineering: From Foundations to Production Systems*.

The repository preserves the historical **v2.4 frozen-edition evidence**, while the manuscript is currently undergoing a controlled **v3.8 forensic repair pass**. The companion code is therefore treated as the reproducibility source for the active study edition without implying that v3.8 has already passed its commercial-release gate.

## What is implemented

The repository includes:

- real-data chapter scripts for the principal applied labs;
- a controlled `dataset_registry.csv` covering every named dataset materially used by the current book, including the California Housing exercise;
- `download_datasets.py`, which prepares datasets from official or library-managed sources without committing raw third-party data to Git;
- `verify_dataset_registry.py`, which fails CI if required dataset coverage is lost;
- deterministic reference assertions and output smoke tests;
- core/reference/data dependency files;
- a Chapter 29 production-capstone acceptance checklist.

See [DATASETS.md](DATASETS.md) for one-command dataset setup and redistribution rules.

## Reproducibility standard

Examples fall into three categories:

1. **Deterministic reference checks** — expected outputs are regression-tested in a frozen reference environment.
2. **Real-data labs** — require official datasets and may need network access to obtain them.
3. **Version/service-sensitive examples** — TensorFlow, Transformers, MLflow, DVC, LIME, AIF360, Docker, hosted model APIs, and multi-GPU workflows. These must not be represented as locally verified unless that exact execution path was run.

The current canonical Python interpreter is **3.13.5**. CI also exercises Python 3.12 as a compatibility gate; compatibility success does not redefine the canonical reference version.

## Current layout

```text
chapter03_04_online_retail_eda.py
chapter06_bike_regression.py
chapter07_bank_classification.py
chapter08_california_regression.py
chapter08_hydraulic_features.py
chapter09_wholesale_clustering.py
chapter15_sms_spam.py
chapter17_movielens_recommender.py
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

## Dataset rule

Raw third-party datasets are not part of the Git history. The repository instead records provenance, acquisition method, usage terms, and reproducible download/materialization instructions. `data/` remains gitignored.

The publication rule is simple: **do not confuse illustrative output with verified output**. Any result printed in the book should either be reproducibly generated under the stated reference environment or clearly labelled representative/version-sensitive.

The Chapter 21 DCGAN example in the active repair candidate deliberately uses MNIST-shaped offline smoke tensors for architecture/training-plumbing verification; real digit-generation work should switch to the controlled MNIST acquisition path rather than treating smoke tensors as observations.
