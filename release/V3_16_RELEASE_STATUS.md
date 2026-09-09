# AI Engineering v3.16 — Controlled Release Status

**Book:** *AI Engineering: From Foundations to Production Systems*  
**Author:** Stanley Osei-Wusu  
**Edition:** Code-Verified Illustrated Study Edition · 2026  
**Edition number:** First Edition  
**Controlled version:** v3.16  
**Physical interior:** 390 pages, exact 6 × 9 in

## Verdict

**PASS — controlled manuscript/interior and publication-metadata architecture.**

v3.16 supersedes v3.15 as the current controlled pre-commercial publication master. The v3.16 change set adds professional publication/front-matter metadata while preserving the validated 30-chapter technical core.

## Validation evidence

- DOCX accessibility audit: **0 high / 0 medium / 0 low**.
- Instructional figures: **26/26 preserved with alternative text**.
- PDF geometry: **390/390 pages at 432 × 648 pt**.
- Archival PDF navigation: **53 curated outline entries** and **47 links**.
- Retailer print PDF: **0 outline entries / 0 links / no document metadata stream**.
- Archival vs retailer rendering: **390/390 pixel-identical**.
- Main-matter text regression vs v3.15: **380/380 corresponding pages exact**.
- EPUB: 26 figures with non-empty alt text, **736 MathML expressions**, **181 preformatted code blocks**.
- Official EPUBCheck 5.3.0 under EPUB 3.3 rules: **0 fatals / 0 errors / 0 warnings / 0 infos**.

## Frozen artifact SHA-256 values

- DOCX: `9fe578f4c37f816f67a115374eec0a3225f19de8853078ea37ab18f00bb92cfd`
- Navigable archival PDF: `675264c999220b1e38d43cb23ee1b43974c6044649f394240cd6754867030ee2`
- Retailer print-upload PDF: `dfd03673b621aba78a0b8dd0dd986659ae73859a79223e97457e053b52b95f18`
- EPUB 3 publication master: `75386fb579cf0413a1ba2ee84b13cbf2a4e7f46b3165864905e3d7b149d6624d`
- Final controlled package ZIP: `95baf537fcdcc6c502d0aeb1adf7b56d386005f317c61255075fdab12d998135`

The binary publication masters remain controlled release artifacts outside ordinary Git history.

## Reader and commercial metadata surfaces

- `README.md` — current controlled-version overview
- `BOOK_VERSION.md` — version/support/freeze policy
- `ERRATA.md` — correction register
- `.github/ISSUE_TEMPLATE/book-errata.yml` — structured reader reports
- `publishing/AI_ENGINEERING_METADATA_MASTER.md` — canonical commercial metadata draft
- `publishing/KDP_METADATA_v3_16.md` — KDP field-ready metadata
- `publishing/INGRAM_METADATA_v3_16.md` — IngramSpark/ONIX-oriented metadata
- `publishing/PRICING_AND_FORMAT_STRATEGY.md` — 390-page pricing/format planning scenario

## Intentionally open commercial fields

The following must not be fabricated and remain outside the frozen manuscript until the real value is chosen or assigned:

- final publisher/imprint decision;
- format-specific ISBNs;
- exact publication/on-sale date;
- final print ink/paper/binding choices;
- final cover files/spine width;
- list prices, wholesale discount and returnability;
- territorial-rights declaration;
- ebook DRM choice where applicable;
- named reviewers/endorsements not yet actually obtained;
- platform-required AI-content disclosure answers.

## Release boundary

The manuscript/interior and metadata architecture are controlled and validated. Commercial publication is not complete until identifiers/imprint are finalized, format-specific covers are produced, retailer upload/preflight passes, and a physical proof is accepted.

## Repository boundary

Historical v2.4/v3.x QA and release records remain in Git for provenance and should not be rewritten to pretend they were current v3.16 evidence. PR #2 is a separate historical repair branch and is not authorized for merge by this release record.