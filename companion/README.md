# Companion Code

This directory accompanies the **v2.4 Code-Verified Illustrated Study Edition** of *AI Engineering: From Foundations to Production Systems*.

## Reproducibility standard

Examples fall into three categories:

1. **Deterministic reference checks** — expected outputs are regression-tested in a frozen reference environment.
2. **Real-data labs** — require official datasets and may need network access to obtain them.
3. **Version/service-sensitive examples** — such as TensorFlow, Transformers, MLflow, DVC, LIME, AIF360, Docker, hosted model APIs, and multi-GPU workflows. These must not be represented as locally verified unless that exact execution path was run.

## Planned companion layout

```text
chapter06_bike_regression.py
chapter07_bank_classification.py
chapter09_wholesale_clustering.py
chapter15_sms_spam.py
chapter22_power_timeseries_baseline.py
chapter27_rag_baseline.py
chapter28_tool_agent.py
chapter29_capstone/
dataset_registry.csv
download_uci_datasets.py
reference_assertions.py
reference_output_smoke.py
requirements-core.txt
requirements-reference.txt
```

The publication rule is simple: **do not confuse illustrative output with verified output**. Any result printed in the book should either be reproducibly generated under the stated reference environment or clearly labelled representative/version-sensitive.
