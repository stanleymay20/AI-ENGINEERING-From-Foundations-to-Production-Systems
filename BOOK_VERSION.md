# Book Version and Reader Support Policy

## Current controlled manuscript/interior

- Book: *AI Engineering: From Foundations to Production Systems*
- Author: Stanley Osei-Wusu
- Edition: Code-Verified Illustrated Study Edition · 2026
- Edition number: **First Edition**
- Controlled version: **v3.17**
- Print interior: **406 physical pages**, exact 6 × 9 in
- Main matter: folio **1** begins after ten front-matter pages
- Archival PDF navigation: **53 curated entries**
- Retailer print-upload derivative: **0 bookmarks / 0 annotations or links / no document metadata stream**
- Official EPUB validation: EPUBCheck 5.3.0 under EPUB 3.3 rules — **0 fatals / 0 errors / 0 warnings / 0 infos**

## v3.17 Authority & Depth pass

v3.17 supersedes v3.16 as the controlled manuscript/interior.

The pass:

- repairs stale Chapter 29 references to the current Chapter 27 RAG architecture and Chapter 28 bounded-agent/guardrail architecture;
- expands Chapter 19 with model-adaptation decision logic, PEFT/LoRA, quantized adaptation, adaptation-data discipline, holdout evaluation, and release/versioning considerations;
- expands Chapter 25 with production inference engineering, including prefill/decode reasoning, KV caching, batching/admission control, optimized kernels/compilation, quantization, routing, caching, and cost per successful task;
- adds a curated **Primary Sources and Further Reading** section to all 30 chapters;
- reconciles TOC and selected-index pagination after the expansion.

The source-code sequence is byte-for-byte unchanged from v3.16. The new interior is 406 pages.

## Validation state

- 406/406 pages visually reviewed.
- 26/26 instructional figures preserved with alternative text.
- DOCX accessibility: 0 high / 0 medium / 0 low.
- 101 Python-parsable source blocks pass AST parsing; 20 non-Python/config/prompt/diagram source-style blocks are excluded from Python AST classification.
- All 30 chapter and five appendix start pages reconcile with the TOC.
- Exact archival PDF normalization removes only LibreOffice's blank bottom surplus; 406/406 normalized renders preserve page content.
- Retailer print derivative renders identically to the archival master on 406/406 pages.
- EPUB structural/accessibility QA: 0 errors / 0 warnings.
- EPUBCheck 5.3.0: 0 fatals / 0 errors / 0 warnings / 0 infos.

## Canonical reader resources

- Repository: https://github.com/stanleymay20/AI-ENGINEERING-From-Foundations-to-Production-Systems
- Errata: `ERRATA.md`
- Dataset provenance and acquisition: `companion/DATASETS.md` and `companion/dataset_registry.csv`
- Reproducibility checks: `companion/`

## Support boundary

The repository accepts reproducible reports about book defects, companion-code defects, broken controlled acquisition instructions, accessibility defects, metadata defects, cross-reference defects, and compatibility regressions affecting book examples. It is not a general-purpose help desk for unrelated Python, cloud-account, GPU, operating-system, or third-party service problems.

## Currency policy

AI libraries, model APIs, cloud services, security guidance, and platform interfaces change after publication. A later upstream change does not retroactively make an originally correct statement an erratum. Such changes are recorded as compatibility or currency notes when they materially affect a reader's ability to reproduce the book.

## Freeze policy

A frozen publication version is immutable. Substantive corrections create a new controlled version and trigger the relevant code, layout, PDF, EPUB, accessibility, metadata, and checksum gates.

## A+++ programme boundary

v3.17 closes the Authority & Depth pass. The broader competitive A+++ programme remains open for evidence-based production case studies, additional explanatory engineering diagrams, a deeper professional index/code map, and independent human technical/copy review.

## Commercial metadata boundary

The following must be supplied from real publishing decisions and must not be fabricated in the manuscript or repository:

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