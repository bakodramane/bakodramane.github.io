---
layout: post
title: "Governed AI workflows for documents and private data"
date: 2026-06-15
author: Dramane Bako
description: "Recent AI developments for document extraction, synthetic data, private record linkage, tabular modelling and governed statistical workflows."
categories: [AI, Surveys, Administrative Data, Official Statistics]
tags: [AI tools, surveys, censuses, administrative data, official statistics]
lang: en
translation_key: weekly-ai-update-2026-06-15
---

## **Executive summary**

This week's developments strengthen several practical components around artificial intelligence (AI): extracting structured content from operational documents, enforcing constraints in synthetic data, screening potential record linkages privately, and governing model and agent activity. For statistical offices, the immediate opportunity is controlled piloting; recent research on tabular foundation models and differentially private synthesis remains experimental and requires independent validation before official use.

## **What is new this week**

### Editing and validation

**Unstructured 0.23.0 and 0.23.1 improve PDF extraction and provenance**

- **Release date:** 10-11 June 2026.
- **What it does:** Version 0.23.0 corrected text loss on dense PDF pages, improved alignment between extracted text and rotated page images, and added metadata describing enrichment origins. Version 0.23.1 added extraction of text entered in PDF AcroForm fields.
- **Why it matters for official statistics:** Survey forms, administrative returns and archived operational records frequently arrive as PDFs. Better extraction of form fields and more explicit provenance can support auditable conversion into reviewable records.
- **Practical use case:** Extract entries from completed electronic forms, then compare the resulting fields with questionnaire specifications before loading them into a staging database.
- **Implementation notes:** PDF extraction is not equivalent to validated data capture. Test representative layouts, languages, rotations, handwriting and scanned pages; retain the original file and page coordinates; and route uncertain or inconsistent records to human review.
- **Source:** [Unstructured releases](https://github.com/Unstructured-IO/unstructured/releases).

### Cleaning and quality assurance

**SDV 1.37 adds reusable constraint files for synthetic data workflows**

- **Release date:** Version 1.37.0 on 29 May 2026; version 1.37.1 on 11 June 2026.
- **What it does:** The Synthetic Data Vault (SDV) can now store and load constraints from files. Constraints encode relationships or validity rules that synthetic records should respect.
- **Why it matters for official statistics:** Synthetic survey or administrative data can appear plausible while violating questionnaire routing, accounting identities, date order or cross-table rules. Reusable constraint definitions make these controls easier to version and review.
- **Practical use case:** Apply documented rules such as age ranges, household relationships or start-date/end-date ordering when creating non-production test data.
- **Implementation notes:** Constraint compliance does not demonstrate confidentiality protection or analytical utility. Offices should separately measure disclosure risk, distributional fidelity, subgroup performance and fitness for each intended use.
- **Source:** [SDV releases](https://github.com/sdv-dev/SDV/releases).

### Processing and integration

**Docling 2.100-2.102 expands document conversion and service integration**

- **Release date:** 9-12 June 2026.
- **What it does:** Docling 2.100 added a DocLang backend, EPUB conversion and a table-orientation correction. Subsequent releases added explicit page-image controls and retrieval of conversion results through presigned artefacts.
- **Why it matters for official statistics:** Statistical agencies often need to convert methodological reports, classifications, forms and administrative documents into structured content while preserving tables and context.
- **Practical use case:** Build a controlled ingestion service for extracting tables and sections from incoming reports before indexing them for internal search or coding assistance.
- **Implementation notes:** Presigned artefacts require short expiry periods, least-privilege storage permissions and access logging. Evaluate table structure, reading order and character accuracy against a manually checked sample.
- **Source:** [Docling releases](https://github.com/docling-project/docling/releases).

**Appraisal proposes faster privacy-preserving screening before record linkage**

- **Publication date:** arXiv submission on 26 May 2026; the paper reports publication at the 2025 IEEE International Conference on Data Engineering.
- **What it does:** The paper proposes a screening stage that estimates whether two parties' data are sufficiently linkable before running a more expensive privacy-preserving record linkage process. The authors report substantial computational and communication improvements over selected baselines.
- **Why it matters for official statistics:** Agencies considering cross-government linkage may need to assess whether a proposed linkage has enough value without first disclosing identifiers or committing to a full linkage exercise.
- **Practical use case:** Screen candidate administrative sources before a population-register or census-linkage pilot, subject to the applicable legal authority and data-sharing agreement.
- **Implementation notes:** This is a specialised cryptographic research system, not a ready-made linkage service. Independent security review, threat modelling, linkage-quality evaluation and governance approval are necessary. The reported performance has not been confirmed for national statistical datasets.
- **Sources:** [arXiv record](https://arxiv.org/abs/2605.26882); [IEEE DOI record](https://doi.org/10.1109/ICDE65448.2025.00280).

### Analysis and modelling

**Schema-1 introduces a proposed data language model for raw tables**

- **Publication date:** 7 May 2026.
- **What it does:** The preprint presents Schema-1, a 140-million-parameter model designed to process raw cell values directly. The authors report results for row-level prediction, missing-value reconstruction and dataset-sector identification.
- **Why it matters for official statistics:** A model that learns table structure without extensive task-specific preprocessing could eventually support imputation, classification and exploratory quality checks across heterogeneous survey and administrative datasets.
- **Practical use case:** Compare the model with established imputation or classification baselines on public or fully de-identified benchmark data.
- **Implementation notes:** This is an emerging preprint with strong author-reported claims. Offices should check benchmark leakage, subgroup error, calibration, reproducibility and stability under realistic missingness mechanisms before considering sensitive or official data.
- **Source:** [Data Language Models preprint](https://arxiv.org/abs/2605.06290).

### Governance, privacy and responsible AI

**Tab-PE applies differential privacy to synthetic tabular data**

- **Publication date:** 6 June 2026.
- **What it does:** Tab-PE adapts a private-evolution approach to tabular data, using tabular operators to generate, privately score and select candidate records. The authors report better classification utility than selected baselines on datasets with higher-order correlations.
- **Why it matters for official statistics:** Differential privacy provides a formal framework for limiting the contribution of individual records, which is relevant when agencies assess synthetic microdata for research access or testing.
- **Practical use case:** Evaluate a differentially private synthetic-data method on a public census-like benchmark, with a pre-specified privacy budget and utility measures for key estimates.
- **Implementation notes:** The privacy guarantee depends on the complete mechanism, accounting assumptions and parameter choices. A formal guarantee does not establish that outputs are suitable for publication; disclosure review, utility testing and documentation remain necessary.
- **Source:** [Tab-PE preprint](https://arxiv.org/abs/2606.08259).

**MLflow 3.13 adds role-based access control and trace retention**

- **Release date:** 1 June 2026.
- **What it does:** MLflow 3.13 introduces role-based access control (RBAC) with workspace-scoped grants, automatic archival of older trace data, and additional tracing and governance options for coding agents and AI gateways.
- **Why it matters for official statistics:** AI-assisted coding, classification and analytical workflows need controlled access, retained evidence and auditable records of model or agent activity.
- **Practical use case:** Restrict who can run or review an experimental coding assistant, while retaining traces needed for quality assessment and incident investigation.
- **Implementation notes:** The release changes the permission model and removes legacy permission interfaces, so upgrades require a migration review. Traces may contain record fragments or outputs with confidential information; define minimisation, retention, encryption and access policies before enabling them.
- **Sources:** [MLflow 3.13 release notes](https://github.com/mlflow/mlflow/releases/tag/v3.13.0); [MLflow RBAC documentation](https://mlflow.org/docs/latest/self-hosting/security/role-based-access-control).

## **Implications for statistical offices**

The common direction is towards more governable AI-enabled pipelines rather than stand-alone models. Provenance metadata, explicit constraints, role-based permissions, trace retention and privacy-preserving protocols can make experimentation more accountable, but they do not replace statistical quality assurance. Agencies should connect each tool to an approved purpose, representative test data, measurable quality thresholds, security controls and a named human decision point.

The research items also reinforce the need to separate promising benchmark results from operational readiness. Differential privacy, private linkage and tabular foundation models should be assessed jointly by methodologists, subject-matter specialists, data-protection staff and security teams before use with confidential records.

## **Next actions**

- Build a small benchmark set of representative PDFs and score field, table and reading-order extraction.
- Version synthetic-data constraints alongside questionnaire and administrative-data specifications.
- Define a threat model and legal basis before testing privacy-preserving record linkage.
- Compare experimental tabular models with transparent statistical and machine-learning baselines.
- Review access roles, trace contents and retention periods for every AI-assisted workflow.
- Require documented disclosure-risk and utility assessments for synthetic microdata.

## **Sources**

- Unstructured. [Release notes for versions 0.23.0 and 0.23.1](https://github.com/Unstructured-IO/unstructured/releases), 10-11 June 2026.
- SDV project. [Release notes for versions 1.37.0 and 1.37.1](https://github.com/sdv-dev/SDV/releases), 29 May and 11 June 2026.
- Docling project. [Release notes for versions 2.100.0 to 2.102.1](https://github.com/docling-project/docling/releases), 9-12 June 2026.
- Huang et al. [Privacy-Preserving Screening for Record Linkage](https://arxiv.org/abs/2605.26882), arXiv submission, 26 May 2026.
- IEEE. [Conference DOI record](https://doi.org/10.1109/ICDE65448.2025.00280).
- Erol, Pezzoli and Kelahmet. [Data Language Models: A New Foundation Model Class for Tabular Data](https://arxiv.org/abs/2605.06290), 7 May 2026.
- Tran et al. [Differentially Private Synthetic Data via APIs 4: Tabular Data](https://arxiv.org/abs/2606.08259), 6 June 2026.
- MLflow. [MLflow 3.13.0 release notes](https://github.com/mlflow/mlflow/releases/tag/v3.13.0), 1 June 2026; [RBAC documentation](https://mlflow.org/docs/latest/self-hosting/security/role-based-access-control).