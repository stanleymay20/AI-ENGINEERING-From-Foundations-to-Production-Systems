# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering the path from foundations and data work through machine learning, deep learning, NLP, computer vision, reinforcement learning, production deployment, MLOps, retrieval-augmented generation, tool-using agents, evaluation, security, observability, and production governance.

## Repository status

This repository is the canonical **reader companion, reproducibility, QA, and release-metadata repository** for the publication-controlled v2.4 edition.

Current controlled interior status:

- 6×9 technical-publisher layout
- 30 chapters
- 26 instructional figures
- real-world dataset labs
- code/output verification pass
- semantic table reconstruction pass
- figure integration and cross-reference pass
- accessibility QA pass
- print-interior PDF/DOCX maintained as controlled publication assets rather than casually duplicated into Git history

## Quick start

The exact deterministic reference environment uses Python 3.13.5. If your version manager understands `.python-version`, it can select the intended interpreter automatically.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the deterministic checks with:

```bash
python companion/reference_assertions.py
python companion/reference_output_smoke.py
```

## Dataset quick start

The repository does not redistribute raw third-party datasets. Instead, it provides a controlled registry plus reproducible acquisition tooling.

```bash
python companion/download_datasets.py --standard
```

To prepare every downloadable dataset used by the book, including the large UCI archives and MovieLens:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

See [`companion/DATASETS.md`](companion/DATASETS.md) and [`companion/dataset_registry.csv`](companion/dataset_registry.csv) for provenance, licensing/terms, chapter coverage, and redistribution policy.

## Repository layout

```text
companion/      principal runnable labs, dataset helpers, and reference tests
publishing/     imprint, ISBN, retailer metadata, pricing, and production planning
qa/             publication, code, dataset, table, figure, and layout QA evidence
release/        release metadata and checksums for frozen editions
requirements.txt
pyproject.toml
.python-version
```

The book promises standalone scripts for the **major assessed labs**. It does not claim that every instructional code cell in all 30 chapters is duplicated as a separate `.py` file. Notebook-style or sequential examples remain in the book; principal applied labs are maintained under `companion/`.

## Reproducibility

The companion examples separate deterministic reference checks from network/data-dependent labs. Where a dataset must be downloaded, its provenance and licensing are recorded in the dataset registry, and results are not represented as locally verified unless the relevant execution path was actually run.

The exact reference-test dependency pins are in `companion/requirements-reference.txt`. Broader supported ranges for ordinary reader work are retained in the companion-specific requirement files.

## Publication note

The technical interior is controlled, but commercial release remains gated on final ISBN/imprint assignment, retailer-specific cover wraps, final EPUBCheck, retailer preview/preflight, and a physical proof. See `qa/COMMERCIAL_RELEASE_GATE.md` and `qa/V2_4_EXTERNAL_DIAGNOSTIC_RECHECK.md`.
