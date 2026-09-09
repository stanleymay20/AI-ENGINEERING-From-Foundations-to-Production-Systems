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

The current controlled manuscript/interior is **v3.18**.

v3.18 is a focused production-layout repair that supersedes v3.17. The technical Authority & Depth content from v3.17 is preserved, while **Table 1-1 — AI Engineering Lifecycle: Activities and Assistant Support** now begins on a clean new page at physical page 15 / main-matter folio 5.

The controlled interior remains **406 pages, exact 6 × 9 in**. All 30 chapter and five appendix start pages remain unchanged.

Validated publication evidence includes:

- exact **6 × 9 in** print interior;
- **406 physical pages**;
- Table 1-1 forced to a clean new-page start;
- 397/406 source-render pages pixel-identical to v3.17; only pages 2, 5, and 14-20 changed, and all nine changed pages were visually inspected;
- 30 chapters and five appendices with unchanged start pages;
- 26 instructional figures with alternative text;
- DOCX accessibility audit: **0 high / 0 medium / 0 low**;
- source-code/output paragraph sequence unchanged from v3.17;
- curated **53-entry** archival PDF navigation plus a separate retailer print-upload derivative;
- retailer print PDF with **0 bookmarks, 0 annotations/links, and no document metadata stream**;
- source-normalized-to-archival rendering identity on **406/406 pages**;
- archival-to-retailer rendering identity on **406/406 pages**;
- reflowable EPUB 3 with 26 figures, alternative text, MathML, 181 preformatted code blocks, semantic navigation, and accessibility metadata;
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

Please report reproducible defects in the book, companion code, controlled dataset instructions, accessibility, metadata, cross-references, or compatibility regressions through GitHub Issues. General debugging of unrelated local environments, cloud billing/accounts, third-party APIs, hardware, or custom projects is outside the book errata process.

## A+++ programme boundary

v3.18 closes the Table 1-1 layout repair. The competitive A+++ programme remains open for evidence-based production case studies, additional explanatory engineering diagrams, a deeper professional subject index/code map, and independent human technical/copy review.

## Commercial-release boundary

Commercial publication still requires final publisher/imprint and ISBN decisions, format-specific covers, exact publication date, pricing, retailer upload/preflight, and physical-proof acceptance. Those are distribution gates rather than evidence that the validated manuscript/interior is defective.