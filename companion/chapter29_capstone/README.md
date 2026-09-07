# Chapter 29 Capstone - Production Knowledge and Operations Assistant

Build a tenant-aware assistant that can answer from a controlled document corpus and invoke exactly one bounded tool.

## Required repository structure

```text
src/
  ingestion/
  retrieval/
  generation/
  tools/
  api/
evals/
tests/
infra/
docs/
README.md
```

## Minimum acceptance criteria

1. Ingestion preserves source, document version, tenant/workspace, and access-control metadata.
2. Retrieval has a frozen evaluation set with Recall@K and at least one ranking metric.
3. Answers include source attribution and abstain when evidence is insufficient.
4. Tool calls use a validated schema and application-side authorization.
5. Prompt-injection tests include malicious instructions inside retrieved documents.
6. Unit/integration tests run in CI.
7. The service is containerized and starts from a clean checkout.
8. Traces capture retrieval, model/tool calls, latency, errors, and token/cost metadata where available.
9. A runbook explains rollback, index rebuild, incident response, and known limitations.
10. A short model/system card describes intended use, non-goals, risks, and human-approval boundaries.

A successful demo is not sufficient. Preserve evidence that another engineer can reproduce and evaluate the system.
