# Book Version and Reader Support Policy

## Current controlled manuscript/interior

- Book: *AI Engineering: From Foundations to Production Systems*
- Author: Stanley Osei-Wusu
- Edition: Code-Verified Illustrated Study Edition · 2026
- Edition number: **First Edition**
- Controlled version: **v3.21 — FROZEN / AUTHORITATIVE**
- Print interior: **440 physical pages**, exact 6 × 9 in
- Main matter: folio **1** begins after ten front-matter pages
- Instructional figures: **38 total**
- Professional Subject Index: starts at folio **413**
- Archival PDF navigation: **53 curated bookmarks / 47 links**
- Retailer print-upload derivative: **0 bookmarks / 0 annotations or links / no XMP / no `/Info` dictionary**
- Official EPUB validation: EPUBCheck 5.3.0 under EPUB 3.3 rules — **0 fatals / 0 errors / 0 warnings / 0 infos**

## Frozen master SHA-256 values

- DOCX: `dedee8e8659770f598d793736de7fbee5457de17a779dd80b73514d49deb6e38`
- Archival PDF: `ac1dbf6a5bf9ba97a40b46e222d281359917db4d9f14f4a22b46ec92dd73f0f7`
- Retailer print PDF: `33742bae3a83390f2bb86d343bf13f9030e4c173348ba65e369a8d106865c132`
- EPUB 3: `54ec846d9543b8cebfc48e0aaafd4d22f09c8f2c456d892aec18155008795518`

The controlled publication binaries remain outside ordinary Git history. These hashes identify the frozen v3.21 masters.

## v3.21 forensic repair and professional-index pass

v3.21 supersedes v3.20 as the controlled manuscript/interior.

The release integrates the accepted forensic repair set, including the corrected Appendix C answer guide, targeted mathematical/evaluation corrections, the Chapter 21 GAN-objective repair, leakage-safe Chapter 22 LSTM preprocessing and evaluation, current Chapter 23 FastAPI/container wording, a complete Chapter 25 DDP example, Chapter 26 responsible-AI/differential-privacy corrections, and a professional subject index.

## Validation state

- complete visual QA across the final 440-page lineage;
- 7/7 DOCX sections are 6 × 9 in;
- 38/38 instructional figures have non-empty alternative text;
- DOCX accessibility: 0 high / 0 medium / 0 low;
- 121/121 Source Code blocks retained;
- 119 code blocks unchanged from v3.20;
- exactly two intentional repaired code blocks: Chapter 22 LSTM and Chapter 25 DDP;
- 101 Python-classified blocks pass AST parsing; 20 intentional non-Python/non-AST exclusions;
- all 30 chapter and five appendix starts reconcile with the final v3.21 TOC;
- professional subject index integrated at folio 413;
- archival PDF: 440/440 pages at exact 432 × 648 pt, 53 curated bookmarks, 47 links, 0 non-link annotations, tagged structure and metadata retained;
- retailer PDF: 440/440 pages at exact 432 × 648 pt, 0 bookmarks, 0 links, 0 annotations, no XMP and no `/Info` dictionary;
- archival-to-retailer render identity: 440/440 PASS;
- EPUB custom structural suite: 0 errors / 0 warnings;
- EPUB contains 57 XHTML files, 38 images, 38/38 image alt texts, 739 MathML elements, 181 preformatted code blocks, semantic navigation and accessibility metadata;
- fresh official EPUBCheck 5.3.0: **0 fatals / 0 errors / 0 warnings / 0 infos**.

## Canonical reader resources

- Repository: https://github.com/stanleymay20/AI-ENGINEERING-From-Foundations-to-Production-Systems
- Chapter-to-code map: `CHAPTER_TO_CODE_MAP.md`
- Errata: `ERRATA.md`
- Dataset provenance and acquisition: `companion/DATASETS.md` and `companion/dataset_registry.csv`
- Reproducibility checks: `companion/`

## Support boundary

The repository accepts reproducible reports about book defects, companion-code defects, controlled acquisition instructions, accessibility defects, metadata defects, cross-reference/layout defects, diagram defects, case-study sourcing defects, and compatibility regressions affecting book examples. It is not a general-purpose help desk for unrelated Python, cloud-account, GPU, operating-system, or third-party service problems.

## Currency policy

AI libraries, model APIs, cloud services, security guidance, and platform interfaces change after publication. A later upstream change does not retroactively make an originally correct statement an erratum. Such changes are recorded as compatibility or currency notes when they materially affect reproducibility.

## Freeze policy

Frozen v3.21 is immutable. Any substantive correction to manuscript text, code, equations, figures, captions, index, TOC, pagination, front/back matter, PDF navigation/metadata, or EPUB content creates **v3.22+** and triggers the materially affected code, layout, figure, PDF, EPUB, accessibility, metadata, sourcing, and checksum gates.

## A+++ programme boundary

The internal forensic-repair, explanatory-diagram, professional-index, chapter-to-code-map, accessibility, PDF and EPUB validation targets are closed for v3.21. Remaining work is external/commercial:

- genuine independent ML/deep-learning technical review;
- genuine independent MLOps/production technical review;
- genuine independent LLM/RAG/agent technical review;
- professional copyedit/proofread where still required;
- final print-provider/retailer preflight and physical proof.

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

The frozen v3.21 manuscript/interior and its QA evidence do not by themselves complete commercial publication. Final identifier/imprint decisions, format-specific covers, retailer upload/preflight, pricing, and physical-proof acceptance remain separate distribution steps.
