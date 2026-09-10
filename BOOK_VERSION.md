# Book Version and Reader Support Policy

## Current controlled manuscript/interior

- Book: *AI Engineering: From Foundations to Production Systems*
- Author: Stanley Osei-Wusu
- Edition: Code-Verified Illustrated Study Edition · 2026
- Edition number: **First Edition**
- Controlled version: **v3.22 — FROZEN / AUTHORITATIVE**
- Print interior: **445 physical pages**, exact 6 × 9 in
- Main matter: folio **1** begins after ten front-matter pages
- Instructional figures: **38 total**
- Chapter terminology previews: **30/30 chapters**
- Appendix F: **100-entry Abbreviations and Acronyms reference**, starts at folio **415**
- Professional Subject Index: starts on a fresh page at folio **419**
- Archival PDF navigation: **54 curated bookmarks / 47 links**
- Retailer print-upload derivative: **0 bookmarks / 0 annotations or links / no XMP / empty document information metadata**
- Official EPUB validation: EPUBCheck 5.3.0 under EPUB 3.3 rules — **0 fatals / 0 errors / 0 warnings / 0 infos**

## Frozen master SHA-256 values

- DOCX: `6e3860c21dd4d33d7be1c0df1b292db0b3368fbf973d2142dbb68d37cc826800`
- Archival PDF: `8bb260c9a24e775340758f62f9fa97805d13576cb38dd249218e98fa5ae530b6`
- Retailer print PDF: `7d22e34d217633c2e9eeda036e10ab3c76daee44c9ce6c1155c42b1101911a1b`
- EPUB 3: `3036e0e9ed9243d0b1ce632c7cd4497b88f5a20adee6f265e3fe566822b51912`

The controlled publication binaries remain outside ordinary Git history. These hashes identify the frozen v3.22 masters.

## v3.22 terminology-pedagogy pass

v3.22 supersedes v3.21 as the controlled manuscript/interior.

The release adds a reader-first terminology system without reopening the validated technical substance of v3.21. Every chapter now presents a compact **Key Terms & Acronyms** preview before its Learning Objectives. Important abbreviations are expanded where they are first taught in context. **Appendix F: Abbreviations and Acronyms** provides an alphabetical recall aid rather than acting as a prerequisite for comprehension. The Professional Subject Index remains the deeper contextual navigation layer.

The pass also corrects the final front-matter publication-state wording and improves copyright-page separation/spacing. The chapter-to-code map, technical examples, equations, figures and source-code sequence remain governed by their prior controlled evidence except where explicitly revalidated below.

## Validation state

- controlled visual QA completed across the final v3.22 lineage;
- 30/30 chapter terminology previews occur on the chapter-opening pages before Learning Objectives;
- Appendix F contains 100 abbreviation/acronym entries across folios 415–418;
- Professional Subject Index starts at folio 419 on a fresh page;
- 7/7 DOCX sections are 6 × 9 in;
- 38/38 instructional figures have non-empty alternative text;
- DOCX accessibility: 0 high / 0 medium / 0 low;
- 121/121 Source Code blocks are text-identical in sequence to frozen v3.21;
- 101 Python-classified blocks pass AST parsing; the same 20 intentional non-Python/non-AST exclusions remain;
- 738 Word mathematical objects retained, unchanged from v3.21 under the same counting method;
- six document tables retained, unchanged in count from v3.21;
- archival PDF: 445/445 pages at exact 432 × 648 pt, 54 curated bookmarks, 47 links, 0 non-link annotations, tagged structure and metadata retained;
- retailer PDF: 445/445 pages at exact 432 × 648 pt, 0 bookmarks, 0 links, 0 annotations, no XMP and empty document information metadata;
- archival-to-retailer render identity: 445/445 PASS;
- exact-trim archival PDF contains 0 out-of-bounds text blocks;
- EPUB custom structural validation: 0 broken resource references / 0 broken fragment references;
- EPUB contains 38 images, 38/38 image alt texts, 739 MathML elements, 181 preformatted code blocks, semantic navigation, Appendix F navigation, and accessibility metadata;
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

Frozen v3.22 is immutable. Any substantive correction to manuscript text, code, equations, figures, captions, terminology apparatus, index, TOC, pagination, front/back matter, PDF navigation/metadata, or EPUB content creates **v3.23+** and triggers the materially affected code, layout, figure, PDF, EPUB, accessibility, metadata, sourcing, and checksum gates.

## A+++ programme boundary

The internal forensic-repair, explanatory-diagram, professional-index, terminology-pedagogy, chapter-to-code-map, accessibility, PDF and EPUB validation targets are closed for v3.22. Remaining work is external/commercial:

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

The frozen v3.22 manuscript/interior and its QA evidence do not by themselves complete commercial publication. Final identifier/imprint decisions, format-specific covers, retailer upload/preflight, pricing, and physical-proof acceptance remain separate distribution steps.
