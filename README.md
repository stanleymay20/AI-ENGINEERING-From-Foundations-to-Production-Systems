# AI Engineering: From Foundations to Production Systems

**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026

A project-based AI engineering textbook covering foundations, machine learning, deep learning, NLP, computer vision, reinforcement learning, deployment, MLOps, RAG, tool-using agents, evaluation, security, observability, governance, and production engineering judgment.

## Reader links

- **Errata and corrections:** [ERRATA.md](ERRATA.md)
- **Book version / support / update policy:** [BOOK_VERSION.md](BOOK_VERSION.md)
- **Dataset provenance and acquisition:** [companion/DATASETS.md](companion/DATASETS.md)
- **Dataset registry:** [companion/dataset_registry.csv](companion/dataset_registry.csv)
- **Principal runnable labs and reference checks:** [`companion/`](companion/)
- **Report a suspected defect:** use GitHub Issues and include the book version, location, evidence, and environment where relevant.

## Controlled publication status

The current controlled manuscript/interior is **v3.19**.

v3.19 is the **Production Case Studies** pass. It supersedes v3.18 by adding six evidence-based engineering case files across Chapters 23-28 while preserving the validated source-code sequence and the Table 1-1 layout repair.

The six case files cover:

1. Knight Capital — deployment/change-control failure.
2. Zillow Offers — forecasting uncertainty interacting with operational capacity and feedback.
3. ChatGPT March 2023 — caching, concurrency, pooled connections, and tenant isolation.
4. NIST face-recognition evaluations — aggregate accuracy versus subgroup risk.
5. Air Canada chatbot — grounding/accountability; not represented as proof of an LLM/RAG-specific incident.
6. Uber ATG Tempe crash — human oversight and automation complacency as a safety analogue; not represented as an LLM-agent incident.

The controlled interior is **413 pages, exact 6 × 9 in**.

Validated publication evidence includes:

- 413/413 pages visually reviewed;
- 30 chapters and five appendices reconciled with the v3.19 TOC;
- Table 1-1 retained on its clean new-page start at physical page 15 / folio 5;
- 26 instructional figures with alternative text;
- DOCX accessibility: **0 high / 0 medium / 0 low**;
- 121 Source Code paragraphs, byte-for-byte identical in sequence to v3.18;
- 101 Python-parsable blocks passing AST parsing, with 20 shell/config/prompt/diagram blocks correctly excluded;
- exact 6 × 9 archival PDF with **53 curated bookmarks** and **47 links**;
- retailer print PDF with **0 bookmarks, 0 links/annotations, no metadata stream, and no Info metadata**;
- source-crop-to-archival render identity on **413/413 pages**;
- archival-to-retailer render identity on **413/413 pages**;
- EPUB 3 with 26 figures, alternative text, **736 MathML elements**, **181 preformatted code blocks**, semantic navigation, and accessibility metadata;
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

Please report reproducible defects in the book, companion code, controlled dataset instructions, accessibility, metadata, cross-references, case-study sourcing, or compatibility regressions through GitHub Issues. General debugging of unrelated environments, cloud billing/accounts, third-party APIs, hardware, or custom projects is outside the book errata process.

## A+++ programme boundary

The evidence-based production case-study target is now closed in v3.19. The remaining competitive A+++ programme is:

- additional explanatory engineering diagrams;
- deeper professional subject index / stable code map;
- independent ML/deep-learning review;
- independent MLOps/production review;
- independent LLM/RAG/agent review;
- final professional copyedit/proofread.

## Commercial-release boundary

Commercial publication still requires final publisher/imprint and ISBN decisions, format-specific covers, exact publication date, pricing, retailer upload/preflight, and physical-proof acceptance.