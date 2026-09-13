# Dataset & Companion Reproducibility Status

**Book:** AI Engineering: From Foundations to Production Systems  
**Frozen authority:** v3.22  
**Candidate:** v3.23.8 publication-repair branch  
**Status:** CANDIDATE EVIDENCE — fresh PR CI required before promotion

## Dataset coverage

`companion/dataset_registry.csv` contains **18 controlled entries** covering every named dataset materially used by the v3.23.8 candidate, plus the synthetic scikit-learn generators used by multiple examples.

The registry covers:

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

The Chapter 17 rights repair removes MovieLens from the controlled candidate publication set. Recommendation-system work now reuses **Online Retail II**, the UCI source already governed for Chapters 3-4, as transactional implicit feedback. The registry records DOI `10.24432/C5CG6D`, CC BY 4.0, official UCI acquisition, and attribution requirements.

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

Full setup, including large UCI archives:

```bash
python companion/download_datasets.py --all --include-large
```

Chapter 17 specifically:

```bash
python companion/download_datasets.py --dataset online_retail_ii --include-large
python companion/chapter17_online_retail_recommender.py
```

## Candidate QA gates

The v3.23.8 branch must pass fresh CI evidence after the candidate changes. The required gates are:

1. compile all companion Python source;
2. verify the controlled registry contains every required dataset and that Online Retail II covers Chapter 17;
3. enumerate the dataset CLI successfully;
4. install data/reference dependencies;
5. materialize Iris, Breast Cancer and Digits locally and verify their SHA-256 manifest records;
6. run the offline Chapter 27 retrieval baseline;
7. run the Chapter 28 bounded-agent authorization reference;
8. run all deterministic book-output regression groups;
9. run the offline reference-output smoke suite.

Until a fresh candidate-head run is green, this document is not a successor release certificate.

## External-source caveat

A green repository CI run does not imply that every large/network-dependent third-party dataset was freshly downloaded during that run. External-source availability can change independently of the repository. The acquisition code and registry are source-controlled, while upstream providers and their current license/usage terms remain authoritative.

Large UCI datasets are downloaded from official UCI archives so their native file structure is preserved. Network/service-sensitive examples must not be described as locally verified unless that exact external execution path was actually run.

## Verdict

The v3.23.8 dataset architecture is internally synchronized for candidate review. **Promotion remains blocked until fresh candidate-head CI passes and the publication-level PDF/EPUB/accessibility/checksum gates close.** Frozen v3.22 remains authoritative in the meantime.
