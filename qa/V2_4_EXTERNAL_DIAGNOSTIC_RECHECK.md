# v2.4 External Diagnostic Recheck

Date: 2026-09-07

This note records a direct recheck of the reported pre-launch blockers against the controlled v2.4 DOCX/PDF and the live repository.

## Verdict

The external diagnostic was useful as a release challenge, but two manuscript blockers were not reproducible in the controlled v2.4 files.

### 1. Reported KMeans truncation — NOT REPRODUCED

The printed page 56 (physical PDF page 65) contains the complete statement:

```python
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)
```

The following silhouette-score and cluster-size statements are also present. The rendered page was visually inspected and the line is not clipped or truncated.

### 2. Reported Chapter 2 theta/odot corruption — NOT REPRODUCED

Printed page 14 renders the threshold example as ordinary Python:

```python
if accuracy >= 0.90:
```

Searches of the controlled DOCX found no literal `\\theta` or `\\odot` artifacts. The training-convergence reference output renders cleanly as `Iteration 01: loss=8.0000`, `Iteration 02: loss=6.4000`, etc.

### 3. Global Python syntax audit — PASS

The controlled DOCX contains 147 paragraphs using the Source Code style. Of these, 55 are explicitly captioned as PYTHON examples. Every explicitly labelled PYTHON block parses successfully with Python's `ast.parse`: **55/55 pass, 0 syntax failures**.

A blanket AST parse of every Source Code-style paragraph is not valid because that style is also used for Bash, YAML, Dockerfiles, diagrams, prompts, repository trees, and representative output.

### 4. Companion repository — IMPLEMENTED, with packaging improvements added

The book promises standalone scripts for the major assessed labs, not one standalone script for every chapter. The repository currently includes principal real-data/production labs for Chapters 3–4, 6, 7, 8, 9, 15, 17, 22, 26, 27, 28, plus Chapter 29 capstone acceptance material, dataset acquisition, registry verification, deterministic reference assertions, and output smoke tests.

To improve release ergonomics, the repository now also has:

- root `requirements.txt`;
- `.python-version` pinned to 3.13.5;
- `pyproject.toml` for the v2.4 companion environment;
- corrected `companion/requirements-reference.txt` wording for v2.4.

The public companion repository should not contain the full paid manuscript merely to satisfy a directory convention. Print/PDF/DOCX publication masters remain release-stage assets; the public repository's primary purpose is code, data provenance, reproducibility, QA evidence, and reader support.

### 5. ISBN/publication metadata — STILL A COMMERCIAL RELEASE GATE

ISBN assignment, final imprint metadata, retailer cover wraps, final EPUBCheck, retailer preflight, and physical proof approval remain required before commercial release. They are not evidence of manuscript corruption; they are normal publication-production gates.

## Controlled conclusion

**Manuscript technical blocker status: PASS on the two reported defects.**

**Repository reproducibility status: PASS, with root environment files now added.**

**Commercial launch status: HOLD pending ISBN/imprint/final cover/retailer preflight/physical proof.**
