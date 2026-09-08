# Book Version and Reader Support Policy

## Current publication-infrastructure candidate

- Book: *AI Engineering: From Foundations to Production Systems*
- Author: Stanley Osei-Wusu
- Edition: Code-Verified Illustrated Study Edition · 2026
- Candidate: v3.13
- Basis: technically validated v3.12 interior plus publication-infrastructure additions

## Canonical reader resources

- Repository: https://github.com/stanleymay20/AI-ENGINEERING-From-Foundations-to-Production-Systems
- Errata: `ERRATA.md`
- Dataset provenance and acquisition: `companion/DATASETS.md` and `companion/dataset_registry.csv`
- Reproducibility checks: `companion/`

## Support boundary

The repository accepts reproducible reports about book defects, companion-code defects, broken controlled acquisition instructions, and compatibility regressions affecting book examples. It is not a general-purpose help desk for unrelated Python, cloud-account, GPU, operating-system, or third-party service problems.

## Currency policy

AI libraries, model APIs, cloud services, security guidance, and platform interfaces change after publication. A later upstream change does not retroactively make an originally correct statement an erratum. Such changes are recorded as compatibility or currency notes when they materially affect a reader's ability to reproduce the book.

## Freeze policy

A frozen publication version is immutable. Substantive corrections create a new controlled version and trigger the relevant code, layout, PDF, EPUB, accessibility, and checksum gates.