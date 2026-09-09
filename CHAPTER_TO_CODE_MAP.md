# Chapter-to-Code Map

**Book:** *AI Engineering: From Foundations to Production Systems*  
**Edition:** Code-Verified Illustrated Study Edition · 2026  
**Controlled manuscript/interior:** v3.20  

This map helps readers locate the substantial runnable labs, dataset controls, reproducibility checks, and production scaffolds that accompany the book.

## What the repository does—and does not—promise

The repository is the canonical reader-companion, reproducibility, dataset, errata, QA, and release-metadata surface. It contains standalone implementations for the book's **major assessed labs** and shared engineering utilities. It is **not** a one-to-one `.py` mirror of every instructional code cell in all 30 chapters.

Use these execution labels when interpreting the map:

- **Deterministic** — selected behavior is regression-tested in the declared reference environment.
- **Data-dependent** — the lab requires controlled acquisition of real-world or benchmark data and may require network access.
- **Version-sensitive** — framework, hosted service, GPU/runtime, API, or infrastructure behavior may vary with the current environment; do not infer a frozen execution result unless explicitly documented.
- **Specification** — an acceptance scaffold or build contract, not a prebuilt production system.

For the current freeze/support policy, see [BOOK_VERSION.md](BOOK_VERSION.md). For confirmed corrections, see [ERRATA.md](ERRATA.md).

## Chapter map

| Ch. | Book focus | Companion artifact(s) | Execution / reader boundary |
|---:|---|---|---|
| 1 | AI engineering lifecycle and assistants | [README.md](README.md); [companion/README.md](companion/README.md) | **Orientation.** Repository-use and support policy; no separate Chapter 1 script is promised. |
| 2 | Python fundamentals | [reference_assertions.py](companion/reference_assertions.py); [reference_output_smoke.py](companion/reference_output_smoke.py) | **Deterministic, selected coverage.** Instructional cells remain in the book. |
| 3 | Data acquisition, quality, preprocessing | [chapter03_04_online_retail_eda.py](companion/chapter03_04_online_retail_eda.py); [download_datasets.py](companion/download_datasets.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major Online Retail II lab. |
| 4 | Exploratory data analysis | [chapter03_04_online_retail_eda.py](companion/chapter03_04_online_retail_eda.py) | **Data-dependent.** Shares the Online Retail II lab with Chapter 3. |
| 5 | ML concepts and experimental design | [dataset_registry.csv](companion/dataset_registry.csv); shared reference checks | **Mixed.** Iris and synthetic scikit-learn sources are registered; no dedicated Chapter 5 script is promised. |
| 6 | First scikit-learn regression model | [chapter06_bike_regression.py](companion/chapter06_bike_regression.py) | **Data-dependent.** Major Bike Sharing regression lab. |
| 7 | Classification and evaluation | [chapter07_bank_classification.py](companion/chapter07_bank_classification.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major Bank Marketing classification lab. |
| 8 | Trees and ensembles | [chapter08_hydraulic_features.py](companion/chapter08_hydraulic_features.py); [chapter08_california_regression.py](companion/chapter08_california_regression.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Hydraulic Systems is the principal real-world Chapter 8 project; California Housing is a benchmark helper. |
| 9 | Clustering | [chapter09_wholesale_clustering.py](companion/chapter09_wholesale_clustering.py) | **Data-dependent.** Major Wholesale Customers clustering lab. |
| 10 | Dimensionality reduction | [dataset_registry.csv](companion/dataset_registry.csv); shared reference checks | **Mixed.** Digits and 20 Newsgroups benchmark sources are registered; no dedicated Chapter 10 script is promised. |
| 11 | Neural-network foundations | shared reference checks | **Deterministic, selected coverage.** Core instructional code remains in the book. |
| 12 | TensorFlow/Keras neural networks | [dataset_registry.csv](companion/dataset_registry.csv) | **Version-sensitive / data-dependent.** MNIST and CIFAR-100 acquisition are registered. |
| 13 | CNNs | [dataset_registry.csv](companion/dataset_registry.csv) | **Version-sensitive / data-dependent.** CIFAR-10 acquisition is registered; no separate Chapter 13 script is promised. |
| 14 | RNNs and LSTMs | shared reference checks | **Version-sensitive.** Sequence-model walkthroughs remain in the book. |
| 15 | NLP fundamentals | [chapter15_sms_spam.py](companion/chapter15_sms_spam.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major SMS Spam lab; IMDB benchmark acquisition is also registered. |
| 16 | Conversational AI | shared reference checks | **Version-sensitive.** Dialogue/tool examples remain in the book; no unrestricted-agent implementation is implied. |
| 17 | Recommendation systems | [chapter17_movielens_recommender.py](companion/chapter17_movielens_recommender.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major MovieLens lab; raw MovieLens data is not redistributed. |
| 18 | Reinforcement learning and learning agents | shared reference checks | **Version-sensitive / in-book.** No dedicated standalone Chapter 18 script is currently promised. |
| 19 | Transformers and modern NLP | shared reference checks | **Version-sensitive.** Transformer/fine-tuning examples should not be read as a frozen hosted-service execution path. |
| 20 | Computer vision fundamentals | shared reference checks | **Version-sensitive / in-book.** No dedicated standalone Chapter 20 script is currently promised. |
| 21 | Generative and multimodal AI | [dataset_registry.csv](companion/dataset_registry.csv); shared reference checks | **Version-sensitive / data-dependent.** MNIST is registered. The DCGAN smoke tensors verify architecture/training plumbing; they are not represented as real MNIST observations. |
| 22 | Time-series analysis | [chapter22_power_timeseries_baseline.py](companion/chapter22_power_timeseries_baseline.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major Household Electric Power Consumption baseline. |
| 23 | Model deployment | shared reference checks; repository requirements | **Version-sensitive.** Deployment walkthroughs remain environment-sensitive; synthetic scikit-learn sources are registered where used. |
| 24 | MLOps | [companion-ci.yml](.github/workflows/companion-ci.yml); [requirements-reference.txt](companion/requirements-reference.txt); shared reference checks | **Deterministic + version-sensitive.** The repository itself is the CI/reproducibility surface; DVC/MLflow behavior remains version-sensitive. |
| 25 | Scaling AI systems | shared reference checks | **Version-sensitive.** Hardware/runtime-sensitive inference and scaling examples are not represented as universally locally verified. |
| 26 | Responsible AI | [chapter26_adult_fairness.py](companion/chapter26_adult_fairness.py); [dataset_registry.csv](companion/dataset_registry.csv) | **Data-dependent.** Major Adult / Census Income fairness-audit lab. |
| 27 | Embeddings, vector search, RAG | [chapter27_rag_baseline.py](companion/chapter27_rag_baseline.py) | **Runnable bounded baseline.** Retrieval and answer evaluation are explicit; production authorization remains an application responsibility. |
| 28 | Tool-using agents, structured outputs, guardrails | [chapter28_tool_agent.py](companion/chapter28_tool_agent.py) | **Runnable bounded baseline.** Tool schemas and guardrails are demonstrated; application-side authorization remains mandatory. |
| 29 | Fully integrated AI application | [Chapter 29 capstone specification](companion/chapter29_capstone/README.md); shared utilities | **Specification.** Acceptance scaffold for a production knowledge/operations assistant, not a prebuilt production system. |
| 30 | LLMOps, evaluation, security, observability, governance | [Chapter 29 capstone specification](companion/chapter29_capstone/README.md); [companion-ci.yml](.github/workflows/companion-ci.yml); [ERRATA.md](ERRATA.md); [BOOK_VERSION.md](BOOK_VERSION.md) | **Specification + operating discipline.** Chapter 30 closes the lifecycle by evaluating and operating the capstone. |

## Major assessed-lab quick map

| Chapter(s) | Principal lab | Script / scaffold | Data |
|---|---|---|---|
| 3–4 | Online retail preprocessing + EDA | [chapter03_04_online_retail_eda.py](companion/chapter03_04_online_retail_eda.py) | Online Retail II |
| 6 | Regression | [chapter06_bike_regression.py](companion/chapter06_bike_regression.py) | Bike Sharing |
| 7 | Classification | [chapter07_bank_classification.py](companion/chapter07_bank_classification.py) | Bank Marketing |
| 8 | Predictive-maintenance features | [chapter08_hydraulic_features.py](companion/chapter08_hydraulic_features.py) | Hydraulic Systems |
| 8 | Benchmark regression helper | [chapter08_california_regression.py](companion/chapter08_california_regression.py) | California Housing |
| 9 | Customer clustering | [chapter09_wholesale_clustering.py](companion/chapter09_wholesale_clustering.py) | Wholesale Customers |
| 15 | SMS text classification | [chapter15_sms_spam.py](companion/chapter15_sms_spam.py) | SMS Spam Collection |
| 17 | Recommendation | [chapter17_movielens_recommender.py](companion/chapter17_movielens_recommender.py) | MovieLens latest-small |
| 22 | Time-series baseline | [chapter22_power_timeseries_baseline.py](companion/chapter22_power_timeseries_baseline.py) | Household Electric Power Consumption |
| 26 | Fairness audit | [chapter26_adult_fairness.py](companion/chapter26_adult_fairness.py) | Adult / Census Income |
| 27 | RAG baseline | [chapter27_rag_baseline.py](companion/chapter27_rag_baseline.py) | Controlled/local corpus inputs |
| 28 | Bounded tool agent | [chapter28_tool_agent.py](companion/chapter28_tool_agent.py) | Controlled tool inputs |
| 29–30 | Production knowledge/operations assistant | [Chapter 29 capstone specification](companion/chapter29_capstone/README.md) | Controlled document corpus |

## Cross-chapter utilities

### Dataset acquisition and provenance

- [dataset_registry.csv](companion/dataset_registry.csv) — canonical registry of materially used named datasets, chapter coverage, source/identifier, acquisition route, terms, redistribution rule, and size flag.
- [DATASETS.md](companion/DATASETS.md) — setup and redistribution guidance.
- [download_datasets.py](companion/download_datasets.py) — controlled materialization of permitted datasets.
- [verify_dataset_registry.py](companion/verify_dataset_registry.py) — CI protection against loss of required dataset coverage.

### Deterministic reference checks

- [reference_assertions.py](companion/reference_assertions.py) — deterministic assertions for selected reference-tested behavior.
- [reference_output_smoke.py](companion/reference_output_smoke.py) — smoke checks for selected reference outputs.
- [requirements-reference.txt](companion/requirements-reference.txt) — deterministic reference dependency pins.
- [.python-version](.python-version) — canonical Python interpreter declaration.

### Reproducibility and CI

- [companion-ci.yml](.github/workflows/companion-ci.yml) — automated companion QA.
- [requirements.txt](requirements.txt) and the `companion/requirements-*.txt` files — reader setup and controlled testing dependency surfaces.

## Reproducibility rule

Do not confuse **illustrative output** with **verified output**. A result presented as verified should be reproducibly generated under the stated reference environment or explicitly labelled as representative, data-dependent, hardware-dependent, or version/service-sensitive.
