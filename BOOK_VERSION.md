# Book Version and Reader Support Policy

## Current controlled manuscript/interior

- Book: *AI Engineering: From Foundations to Production Systems*
- Author: Stanley Osei-Wusu
- Edition: Code-Verified Illustrated Study Edition · 2026
- Edition number: **First Edition**
- Controlled version: **v3.19**
- Print interior: **413 physical pages**, exact 6 × 9 in
- Main matter: folio **1** begins after ten front-matter pages
- Archival PDF navigation: **53 curated entries**
- Retailer print-upload derivative: **0 bookmarks / 0 annotations or links / no document metadata stream / no Info metadata**
- Official EPUB validation: EPUBCheck 5.3.0 under EPUB 3.3 rules — **0 fatals / 0 errors / 0 warnings / 0 infos**

## v3.19 Production Case Studies pass

v3.19 supersedes v3.18 as the controlled manuscript/interior.

This pass adds six evidence-based engineering case files across Chapters 23-28:

- Knight Capital — deployment/change-control safety;
- Zillow Offers — forecasting uncertainty interacting with operational feedback/capacity;
- ChatGPT March 2023 — caching, concurrency, pooled connections, and tenant isolation;
- NIST face-recognition evaluations — aggregate accuracy versus subgroup risk;
- Air Canada chatbot — organizational accountability and grounding discipline, without misrepresenting the matter as an LLM/RAG-specific incident;
- Uber ATG Tempe crash — human oversight and automation complacency as a safety analogue, without misrepresenting it as an LLM-agent incident.

The source-code sequence is unchanged from v3.18. The Table 1-1 clean new-page repair is retained.

## Validation state

- 413/413 pages visually reviewed.
- 26/26 instructional figures preserved with alternative text.
- DOCX accessibility: 0 high / 0 medium / 0 low.
- 121/121 Source Code paragraphs match the v3.18 sequence exactly.
- 101 Python-parsable blocks pass AST parsing; 20 shell/config/prompt/diagram blocks are excluded from Python AST classification.
- All 30 chapter and five appendix starts reconcile with the v3.19 TOC.
- Table 1-1 begins on physical page 15 / main-matter folio 5.
- Exact archival PDF geometry: 413/413 pages at 432 × 648 pt.
- Source crop to archival rendering: 413/413 identical.
- Retailer print derivative renders identically to archival on 413/413 pages.
- EPUB structural/accessibility QA: 0 errors / 0 warnings.
- EPUBCheck 5.3.0: 0 fatals / 0 errors / 0 warnings / 0 infos.

## Canonical reader resources

- Repository: https://github.com/stanleymay20/AI-ENGINEERING-From-Foundations-to-Production-Systems
- Errata: `ERRATA.md`
- Dataset provenance and acquisition: `companion/DATASETS.md` and `companion/dataset_registry.csv`
- Reproducibility checks: `companion/`

## Support boundary

The repository accepts reproducible reports about book defects, companion-code defects, broken controlled acquisition instructions, accessibility defects, metadata defects, cross-reference/layout defects, case-study sourcing defects, and compatibility regressions affecting book examples. It is not a general-purpose help desk for unrelated Python, cloud-account, GPU, operating-system, or third-party service problems.

## Currency policy

AI libraries, model APIs, cloud services, security guidance, and platform interfaces change after publication. A later upstream change does not retroactively make an originally correct statement an erratum. Such changes are recorded as compatibility or currency notes when they materially affect reproducibility.

## Freeze policy

A frozen publication version is immutable. Substantive corrections create a new controlled version and trigger the relevant code, layout, PDF, EPUB, accessibility, metadata, sourcing, and checksum gates.

## A+++ programme boundary

The evidence-based production case-study target is closed in v3.19. The remaining competitive A+++ programme is additional explanatory engineering diagrams, a deeper professional index/code map, independent technical review, and professional copyedit/proofread.

## Commercial metadata boundary

The following must be supplied from real publishing decisions and must not be fabricated:

- final publisher/imprint name;
- ISBN for each applicable format;
- exact publication/on-sale date;
- paperback/hardcover ink, paper, binding and cover configuration;
- retail/list prices and currencies;
- territorial rights statement;
- retailer DRM choice where applicable;
- named reviewers, endorsements or review quotations unless actually obtained;
- platform-required disclosure answers such as AI-generated-content declarations.

## Commercial-release boundary

Manuscript/interior validation and metadata architecture do not by themselves complete commercial publication. Final identifier/imprint decisions, format-specific covers, retailer upload/preflight, pricing, and physical-proof acceptance remain separate distribution steps.