# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

This is the canonical reader companion, reproducibility, errata, QA, and release-metadata repository for the book.

## Reader links

- **Errata and corrections:** [ERRATA.md](ERRATA.md)
- **Book version / update policy:** [BOOK_VERSION.md](BOOK_VERSION.md)
- **Dataset provenance and acquisition:** [companion/DATASETS.md](companion/DATASETS.md)
- **Dataset registry:** [companion/dataset_registry.csv](companion/dataset_registry.csv)
- **Principal runnable labs and reference checks:** [`companion/`](companion/)
- **Report a suspected book or companion-code defect:** use this repository's GitHub Issues and include the book version, location, evidence, and environment where relevant.

## Publication control

The technically validated v3.12 interior passed the controlled DOCX/PDF/code/visual gates and official EPUBCheck 5.3.0 under EPUB 3.3 rules with 0 fatals, 0 errors, 0 warnings, and 0 infos. The v3.13 publication-infrastructure candidate adds reader-facing repository/errata/version/support metadata without reopening the 30 technical chapters unless a substantiated defect is found.

Print-interior DOCX/PDF/EPUB masters remain controlled publication artifacts outside ordinary Git history. Repository records describe and support those masters; they do not replace them.

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

Please report reproducible defects in the book, companion code, controlled dataset instructions, or compatibility regressions through GitHub Issues. General debugging of unrelated local environments, cloud billing/accounts, third-party APIs, or custom projects is outside the book errata process.

## Release boundary

Commercial publication still requires final imprint/ISBN decisions, format-specific covers, retailer upload/preflight, and physical-proof acceptance. Those are distribution gates rather than evidence that the validated technical content is defective.