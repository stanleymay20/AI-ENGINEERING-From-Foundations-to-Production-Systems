# Dataset & Companion Reproducibility Status

**Book:** AI Engineering: From Foundations to Production Systems  
**Controlled interior:** v2.4  
**Status:** PASS — repository-level reproducibility architecture

## Dataset coverage

`companion/dataset_registry.csv` contains **19 controlled entries** covering every named dataset materially used by the current study edition, plus the synthetic scikit-learn generators used by multiple examples.

The registry covers:

- Online Retail II
- Bike Sharing
- Bank Marketing
- Condition Monitoring of Hydraulic Systems
- Wholesale Customers
- SMS Spam Collection
- MovieLens latest-small
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

Full setup, including large UCI archives and opt-in MovieLens:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

## Automated QA evidence

GitHub Actions run **34107524876** on commit **912a85a0ca07877f0151d9ab6a7965937197414d** completed successfully.

The run passed all of the following gates:

1. compile all companion Python source;
2. verify the controlled registry contains every required dataset;
3. enumerate the dataset CLI successfully;
4. install data/reference dependencies;
5. materialize Iris, Breast Cancer and Digits locally and verify their SHA-256 manifest records;
6. run the offline Chapter 27 retrieval baseline;
7. run the Chapter 28 bounded-agent authorization reference;
8. run all **12 deterministic book-output regression groups**;
9. run the offline reference-output smoke suite.

## External-source caveat

A green repository CI run does not imply that every large/network-dependent third-party dataset was freshly downloaded during that run. External-source availability can change independently of the repository. The acquisition code and registry are source-controlled, while upstream providers and their current license/usage terms remain authoritative.

MovieLens remains explicitly opt-in. Large UCI datasets are downloaded from official UCI archives so their native file structure is preserved. Network/service-sensitive examples must not be described as locally verified unless that exact external execution path was actually run.

## Verdict

**All datasets required by the book are now reproducibly available through the repository architecture.** Raw third-party data is intentionally not committed; it is obtained from controlled upstream sources according to the registry and redistribution policy.
