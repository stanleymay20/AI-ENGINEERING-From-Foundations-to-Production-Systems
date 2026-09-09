# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering the path from foundations and data work through machine learning, deep learning, NLP, computer vision, reinforcement learning, production deployment, MLOps, retrieval-augmented generation, tool-using agents, evaluation, security, observability, and production governance.

## Reader links

- **Errata and corrections:** [ERRATA.md](ERRATA.md)
- **Book version / support / update policy:** [BOOK_VERSION.md](BOOK_VERSION.md)
- **Dataset provenance and acquisition:** [companion/DATASETS.md](companion/DATASETS.md)
- **Dataset registry:** [companion/dataset_registry.csv](companion/dataset_registry.csv)
- **Principal runnable labs and reference checks:** [`companion/`](companion/)
- **Report a suspected book or companion-code defect:** use this repository's GitHub Issues and include the book version, location, evidence, and environment where relevant.

## Controlled publication status

The current controlled manuscript/interior is **v3.16**.

v3.16 adds the professional publication metadata layer that was still thinner than major technical-publisher books. It adds a strengthened copyright/rights page, First Edition and controlled-build identification, explicit reader/audience positioning, prerequisites and hardware expectations, a "What This Book Is Not" boundary, conventions used in the book, edition/revision history, and a suggested citation. The technical 30-chapter core is unchanged from v3.15. Two front-matter pages were added, bringing the physical interior to **390 pages** while preserving the main-matter folio numbering and chapter starts.

Validated publication evidence includes:

- exact **6 × 9 in** print interior;
- **390 physical pages** with main matter still starting at folio 1;
- 30 chapters and five appendices;
- 26 instructional figures with alternative text;
- controlled code/output verification inherited from the unchanged technical core;
- changed-front-matter visual QA plus main-matter text/layout regression against v3.15;
- curated **53-entry** archival PDF navigation plus a separate retailer print-upload derivative;
- retailer print PDF with **0 bookmarks, 0 annotations/links, and no document metadata stream**;
- reflowable EPUB 3 with MathML, figures, code blocks, semantic navigation, accessibility metadata, descriptive metadata, and subject metadata;
- official **EPUBCheck 5.3.0** under EPUB 3.3 rules: **0 fatals / 0 errors / 0 warnings / 0 infos**.

The controlled DOCX/PDF/EPUB publication masters remain release artifacts outside ordinary Git history. This repository is the canonical reader companion, reproducibility, errata, QA, and release-metadata surface for those masters.

## Quick start

The deterministic reference environment uses Python 3.13.5.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run deterministic checks with:

```bash
python companion/reference_assertions.py
python companion/reference_output_smoke.py
```

## Dataset quick start

Raw third-party datasets are not casually redistributed. Use the controlled acquisition tooling:

```bash
python companion/download_datasets.py --standard
```

For all downloadable datasets, including large UCI archives and MovieLens where permitted:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

Always review the dataset registry and current upstream terms before redistribution.

## Repository layout

```text
companion/      principal runnable labs, dataset helpers, and reference tests
publishing/     imprint, ISBN, retailer metadata, pricing, and production planning
qa/             publication, code, dataset, table, figure, and layout QA evidence
release/        release metadata and checksums for frozen editions
ERRATA.md       controlled post-publication correction register
BOOK_VERSION.md edition, currency, support, and freeze policy
```

## Reproducibility policy

The companion separates deterministic reference checks from network-, data-, hardware-, and service-dependent labs. Results are not represented as locally verified unless the relevant execution path was actually run. Version-sensitive examples may legitimately vary across supported environments.

The book promises standalone scripts for the major assessed labs, not a one-to-one `.py` duplicate of every instructional cell in all 30 chapters.

## Reader support boundary

Please report reproducible defects in the book, companion code, controlled dataset instructions, accessibility, or compatibility regressions through GitHub Issues. General debugging of unrelated local environments, cloud billing/accounts, third-party APIs, hardware, or custom projects is outside the book errata process.

## Commercial-release boundary

The manuscript/interior and commercial metadata architecture are now substantially prepared, but commercial publication still requires final publisher/imprint and ISBN decisions, format-specific covers, exact publication date, pricing, retailer upload/preflight, and physical-proof acceptance. Those are distribution gates rather than evidence that the validated technical content is defective.