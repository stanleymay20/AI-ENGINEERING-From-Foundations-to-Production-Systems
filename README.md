# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering foundations, machine learning, deep learning, NLP, computer vision, reinforcement learning, deployment, MLOps, RAG, tool-using agents, evaluation, security, observability, governance, and production engineering judgment.

## Reader links

- **Errata and corrections:** [ERRATA.md](ERRATA.md)
- **Book version / support / update policy:** [BOOK_VERSION.md](BOOK_VERSION.md)
- **Chapter-to-code map:** [CHAPTER_TO_CODE_MAP.md](CHAPTER_TO_CODE_MAP.md)
- **Dataset provenance and acquisition:** [companion/DATASETS.md](companion/DATASETS.md)
- **Dataset registry:** [companion/dataset_registry.csv](companion/dataset_registry.csv)
- **Principal runnable labs and reference checks:** [`companion/`](companion/)
- **Report a suspected defect:** use GitHub Issues and include the book version, location, evidence, and environment where relevant.

## Controlled publication status

The current frozen and authoritative manuscript/interior is **v3.21**.

v3.21 supersedes v3.20 after a controlled forensic repair and repagination pass. It integrates the corrected Appendix C answer guide, targeted mathematical/ML/production repairs, a leakage-safe Chapter 22 LSTM example, a complete Chapter 25 DDP example, responsible-AI source/definition repairs, and a professional subject index.

The controlled interior is **440 physical pages, exact 6 × 9 in**.

Validated publication evidence includes:

- complete visual QA across the final 440-page lineage;
- 30 chapters and five appendices reconciled to the final v3.21 TOC;
- professional subject index integrated at folio 413;
- **38 instructional figures**, with **38/38 alternative text**;
- DOCX accessibility: **0 high / 0 medium / 0 low**;
- **121/121 Source Code** blocks retained;
- exactly two intended code replacements versus v3.20: Chapter 22 LSTM and Chapter 25 DDP;
- **101 Python-classified blocks AST PASS**, with 20 intentional non-Python/non-AST exclusions;
- archival PDF: **440 pages at exact 432 × 648 pt**, 53 curated bookmarks, 47 links, tagged structure and metadata retained;
- retailer print PDF: **440 pages at exact 432 × 648 pt**, 0 bookmarks, 0 links/annotations, no XMP and no `/Info` dictionary;
- archival-to-retailer render identity: **440/440 pages PASS**;
- EPUB 3: 57 XHTML files, 38 images, 38/38 image alt texts, **739 MathML elements**, **181 preformatted code blocks**, semantic navigation and accessibility metadata;
- official **EPUBCheck 5.3.0** under EPUB 3.3 rules: **0 fatals / 0 errors / 0 warnings / 0 infos**.

The controlled DOCX/PDF/EPUB masters remain release artifacts outside ordinary Git history. This repository is the canonical reader companion, reproducibility, errata, QA, and release-metadata surface.

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

```bash
python companion/download_datasets.py --standard
```

For all downloadable datasets, including larger sources where permitted:

```bash
python companion/download_datasets.py --all --include-large --include-movielens
```

Always review the dataset registry and current upstream terms before redistribution.

## Reproducibility policy

The companion separates deterministic reference checks from network-, data-, hardware-, and service-dependent labs. Results are not represented as locally verified unless the relevant execution path was actually run. Version-sensitive examples may legitimately vary across supported environments.

## Reader support boundary

Please report reproducible defects in the book, companion code, controlled dataset instructions, accessibility, metadata, cross-references, diagrams, case-study sourcing, or compatibility regressions through GitHub Issues. General debugging of unrelated environments, cloud billing/accounts, third-party APIs, hardware, or custom projects is outside the book errata process.

## A+++ programme boundary

The internal forensic-repair, explanatory-diagram, professional-index, chapter-to-code-map, accessibility, PDF and EPUB validation targets are closed for frozen v3.21. Remaining publication-programme work is external/commercial rather than a reason to reopen the frozen book without evidence of a defect:

- genuine independent ML/deep-learning technical review;
- genuine independent MLOps/production technical review;
- genuine independent LLM/RAG/agent technical review;
- professional copyedit/proofread where still required;
- physical proof and retailer preflight.

## Commercial-release boundary

Commercial publication still requires final publisher/imprint and ISBN decisions, format-specific covers, exact publication date, pricing, retailer upload/preflight, and physical-proof acceptance. No reviewer identity, endorsement, ISBN, proof approval, or retailer approval is implied by the frozen v3.21 technical state.
