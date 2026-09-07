# v3.8 Forensic Repair Status

**Date:** 2026-09-07  
**Book:** *AI Engineering: From Foundations to Production Systems*  
**Edition:** Code-Verified Illustrated Study Edition · 2026  
**Status:** REPAIR CANDIDATE — NOT FINAL / NOT COMMERCIAL-RELEASE APPROVED

## Why v3.8 exists

The v2.4 publication candidate was independently re-audited rather than inherited as ready. The audit found manuscript-level code-wrap failures, missing/broken mathematical notation, stale technical claims, output/prose mismatches, export-geometry problems, paragraph fragmentation, stale TOC pagination, absent curated PDF navigation, and several examples whose explanatory prose did not match the code actually printed.

The v3.x repair sequence is a controlled remediation of those findings. Historical `V2_4_*` QA and release files remain preserved as evidence of the older state; they must not be read as approval of v3.8.

## Material repairs completed through v3.8

- Restored and re-typeset damaged formulas for PCA, activations, dense layers, Batch Normalization, LSTM/GRU, matrix factorization/ALS, and VAE loss terms.
- Repaired renderer-sensitive conditional-probability symbols and other lost/corrupted glyphs.
- Reworked high-risk Python blocks to avoid arbitrary 6×9 line wrapping and validated edited Python-looking blocks with AST parsing.
- Corrected stale Python semantics around dictionary ordering and ndarray homogeneity/contiguity.
- Corrected stale MLflow Model Registry stage guidance and explicit-run wording.
- Updated Keras augmentation guidance away from deprecated `ImageDataGenerator`-centric teaching.
- Aligned BERT prose with `AutoTokenizer` / `AutoModelForSequenceClassification` examples and reframed BERT as a landmark baseline rather than assumed 2026 state-of-the-art.
- Removed categorical claims that CNNs or StyleGAN are universally state-of-the-art in 2026.
- Reframed diffusion-model claims to avoid universal-superiority language.
- Replaced a nonstandard `Generative Adversarial Score (GAS)` teaching point with Kernel Inception Distance (KID) plus task-specific/human evaluation guidance.
- Reframed FID as widely used but limited; added Heusel et al. (2017) and Jayasumana et al. (2024) references.
- Rebuilt the Chapter 21 example so it is a genuine compact convolutional GAN using `ConvTranspose2d` and `Conv2d`, raw logits, `BCEWithLogitsLoss`, and separated discriminator/generator updates.
- Made the Chapter 21 smoke dataset explicit: MNIST-shaped random tensors are used only for offline plumbing verification and are not represented as real MNIST observations.
- Repaired the truncated Chapter 18 multi-agent grid-world project and Chapter 19 support-ticket/BERT project.
- Reconciled Chapter 29 from obsolete Flask/image-classification prose to the FastAPI/numeric-classifier implementation actually printed.
- Removed internal editorial-review residue from reader-facing text.
- Repaired more than one hundred confirmed paragraph-continuity breaks introduced during earlier manuscript construction.
- Recomputed the static table of contents from rendered pagination. Current printed starts remain synchronized for all 30 chapters and five appendices.

## Current print artifact evidence

The current rendered v3.8 candidate is:

- **377 pages**;
- exact trim candidate normalized to **432 × 648 pt (6.000 × 9.000 in)**;
- unencrypted and text-based rather than scanned;
- fonts embedded/subset in the PDF;
- curated PDF outline reduced to **46 navigation entries** covering front matter, six Parts, all 30 Chapters, and Appendices A-E;
- existing link/annotation objects preserved during exact-trim normalization.

The print files remain controlled publication artifacts outside Git history.

## Companion/reproducibility state

- Canonical Python interpreter: **3.13.5** via `.python-version`.
- Pull-request CI exercises Python 3.13.5 and Python 3.12 compatibility.
- Deterministic reference dependencies remain pinned in `companion/requirements-reference.txt`.
- The controlled dataset registry remains authoritative for dataset provenance/acquisition and does not redistribute raw third-party datasets.
- Principal applied labs remain under `companion/`; the book does not promise a one-to-one `.py` mirror for every instructional code cell.

## Release gates still OPEN

v3.8 must **not** be renamed FINAL solely because the targeted repairs above pass. The remaining release gate includes:

1. full-resolution visual inspection of every page in the latest rendered master after the final content change;
2. final figure/table/caption and cross-reference reconciliation;
3. final reference-output consistency sweep across all executable examples;
4. accessibility/navigation verification on the final exact PDF, not an earlier candidate;
5. EPUB 3.3 build and EPUBCheck with repaired code/math semantics;
6. KDP and IngramSpark interior preflight/preview against the exact upload artifact;
7. final ISBN/imprint metadata and retailer-specific cover wraps;
8. physical proof review before commercial-release approval.

## Publication verdict

**Current verdict: HOLD — technically much stronger than v2.4, but still a repair candidate.**

No repository file, workflow success, or historical v2.4 release note should be interpreted as proof that the v3.8 book is commercially FINAL until the open gates above are closed with evidence.
