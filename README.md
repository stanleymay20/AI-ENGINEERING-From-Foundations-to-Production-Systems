# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering the path from foundations and data work through machine learning, deep learning, NLP, computer vision, reinforcement learning, production deployment, MLOps, retrieval-augmented generation, tool-using agents, evaluation, security, observability, and production governance.

## Repository status

This repository is the canonical source and companion-code repository for the publication-controlled **v2.4** interior.

Current controlled interior status:

- 6×9 technical-publisher layout
- 30 chapters
- 26 instructional figures
- real-world dataset labs
- code/output verification pass
- semantic table reconstruction pass
- figure integration and cross-reference pass
- accessibility QA pass
- print-interior PDF/DOCX maintained as release artifacts

## Dataset quick start

The repository does not redistribute raw third-party datasets. Instead, it provides a controlled registry plus reproducible acquisition tooling.

```bash
python -m pip install -r companion/requirements-data.txt
python companion/download_datasets.py --standard
```

To prepare every downloadable dataset used by the book, including the large UCI archives and MovieLens:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

See [`companion/DATASETS.md`](companion/DATASETS.md) and [`companion/dataset_registry.csv`](companion/dataset_registry.csv) for provenance, licensing/terms, chapter coverage, and redistribution policy.

## Repository layout

```text
manuscript/     publication-controlled Markdown/source material
companion/      runnable examples, dataset helpers, and reference tests
figures/        instructional figures used by the book
qa/             publication, code, table, figure, and layout QA records
release/        release metadata and checksums for frozen editions
```

## Reproducibility

The companion examples separate deterministic reference checks from network/data-dependent labs. Where a dataset must be downloaded, its provenance and licensing are recorded in the dataset registry, and results are not represented as locally verified unless the relevant execution path was actually run.

## Publication note

The repository tracks the technical source and reproducibility assets. ISBN, final imprint metadata, retailer-specific cover wrap, EPUB distribution files, and other commercial publishing metadata are maintained as release-stage artifacts.
