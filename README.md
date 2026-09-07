# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering the path from foundations and data work through machine learning, deep learning, NLP, computer vision, reinforcement learning, production deployment, MLOps, retrieval-augmented generation, tool-using agents, evaluation, security, observability, and production governance.

## Repository status

This repository is the canonical **reader companion, reproducibility, QA, and release-metadata repository** for the book.

Publication control is currently split deliberately:

- **v2.4** remains the last historically documented frozen interior/release baseline in the existing `V2_4_*` records;
- **v3.8** is the active forensic repair candidate as of 7 September 2026;
- v3.8 is **not yet a frozen commercial release** and must not be described as FINAL until the remaining all-page visual, EPUB, retailer-preflight, and physical-proof gates pass.

Current v3.8 repair-candidate status:

- exact 6×9 print geometry has been regenerated and preflighted;
- 30 chapters and five appendices remain synchronized with the static table of contents;
- code-wrap, syntax, output-label, paragraph-fragmentation, equation-rendering, stale-API, and technical-accuracy repairs have been applied across the manuscript;
- Chapter 21 now uses a genuine compact convolutional GAN example instead of an MLP mislabeled as DCGAN;
- generative-model evaluation guidance now treats FID as widely used but limited, and uses KID plus task-specific/human evaluation rather than a nonstandard scalar score;
- real-world dataset labs and the controlled dataset registry remain the source of truth for data provenance;
- companion CI tests Python 3.13.5 as the canonical environment and Python 3.12 as a compatibility gate;
- print-interior PDF/DOCX assets remain controlled publication artifacts rather than being casually duplicated into Git history.

See `qa/V3_8_FORENSIC_REPAIR_STATUS.md` for the active repair ledger once present. Historical v2.4 records remain preserved for traceability.

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

The v3.8 technical interior is an active **repair candidate**, not a frozen release. Commercial release remains gated on final all-page visual QA, EPUBCheck, ISBN/imprint assignment, retailer-specific cover wraps, KDP/Ingram preflight/preview, and a physical proof. Historical v2.4 release records remain useful evidence but must not be mistaken for v3.8 approval.
