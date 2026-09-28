---
layout: post
title: "AI evaluation and compatible data pipelines"
date: 2026-09-28
author: Dramane Bako
description: "Recent AI and data-engineering developments for evaluation, optimisation, validation and governed statistical production."
categories: [AI, Surveys, Administrative Data, Official Statistics]
tags: [AI tools, surveys, censuses, administrative data, official statistics]
lang: en
translation_key: weekly-ai-update-2026-09-28
---

## **Executive summary**

This week’s most useful signal for statistical organisations is a shift from impressive demonstrations towards measurable and maintainable AI workflows. New evaluation and optimisation functions make it easier to compare candidate implementations against labelled data; data-quality and validation libraries are responding quickly to dependency changes; typed agent frameworks are improving constrained outputs; and a new frontier model arrives with a published system card. These developments can support coding, editing, document extraction and dissemination, but none removes the need for representative test data, deterministic controls, human review and formal release authority.

| Lifecycle stage | Development | Maturity | Recommended use now |
| --- | --- | --- | --- |
| Collection and processing | SQLAlchemy 2.1.1 | Stable dependency release | Compatibility testing for database-backed pipelines |
| Editing and validation | Great Expectations GX Core 1.23.2 | Stable corrective release | Controlled upgrade after backend regression tests |
| Coding and structured extraction | Pydantic AI 2.49.0 | Stable framework release | Constrained pilot outputs with external validation |
| Evaluation | Snowflake AI Function Evaluation | Public preview | Benchmark candidate functions on labelled, versioned records |
| Optimisation | Snowflake AI Function Optimization | Public preview | Explore quality–cost trade-offs in a sandbox |
| Analysis and reporting | Claude Opus 5.5 | Generally available model; capabilities still require local validation | Comparative, non-production evaluation only |
| Access and governance | Model Context Protocol for official statistics | Emerging implementation pattern | Read-only pilots over approved statistical interfaces |

## **What is new**

### Collection, integration and reproducibility

**SQLAlchemy 2.1.1, released 25 September 2026**

SQLAlchemy 2.1 became the current stable line for the widely used Python database toolkit. The release matters beyond application development because many validation, extraction and integration tools inherit database behaviour through SQLAlchemy. A dependency change can therefore alter connection handling, reflected types or generated SQL without any change to an agency’s own statistical code.

For surveys and administrative data, the practical use case is a pre-production compatibility matrix covering every supported database and driver. Offices should pin dependencies in production, run row-count, type, nullability and query-result comparisons on representative extracts, and record the driver and dialect versions in processing metadata. The release is stable, but institutional readiness depends on downstream compatibility.

- **Sources:** [SQLAlchemy 2.1 documentation](https://docs.sqlalchemy.org/en/21/intro.html); [SQLAlchemy change log](https://www.sqlalchemy.org/changelog/).

### Editing, validation and cleaning

**Great Expectations GX Core 1.23.2, released 25 September 2026**

GX Core 1.23.2 restores compatibility after SQLAlchemy 2.1 disrupted GX 1.23.1 on several SQL backends. The change log records fixes or guards affecting Snowflake, Databricks, PostgreSQL, BigQuery and SQL Server, including type matching, reflected mixed-case table names and database-URL masking. This is a corrective release rather than a new statistical method.

The operational lesson is important: automated validation can fail, or validate a different representation of a field, when a transitive dependency changes. A useful official-statistics pattern is to maintain a small “golden” dataset for every source system and compare validation outcomes before and after upgrades. Connection strings in logs should remain masked, yet the retained audit record must still identify the database, schema, code version and validation suite. Upgrade GX and SQLAlchemy together only after backend-specific regression tests.

- **Sources:** [GX Core change log](https://docs.greatexpectations.io/docs/core/changelog/); [GX SQL data-source guidance](https://docs.greatexpectations.io/docs/core/connect_to_data/sql_data/).

### Coding and structured extraction

**Pydantic AI 2.49.0, released 23 September 2026**

Pydantic AI 2.49.0 adds richer typed criteria, including explicit meanings for Boolean responses, and improves the handling of optional and union outputs. It also fixes propagation of graph-stream errors and makes instrumentation behaviour more explicit. These are framework-level changes for applications that ask models to return structured results.

For a statistical office, a practical pilot is assisted coding of short text into an approved classification, with the model restricted to valid codes plus an explicit “none of these” or review outcome. Structured output improves machine readability; it does not demonstrate correctness. Codes should be checked against the authoritative classification, confidence or abstention rules should be calibrated on labelled cases, and every auto-accepted record should remain traceable to the model, prompt, source text and classification version.

- **Sources:** [Pydantic AI 2.49.0 release](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0); [Pydantic AI output documentation](https://pydantic.dev/docs/ai/core-concepts/output/).

### Evaluation and optimisation

**Snowflake Cortex AI Function Evaluation, public preview from 21 September 2026**

`AI_FUNCTION_EVALUATION` measures the output quality of an AI function or Cortex AI call against a labelled dataset. Snowflake’s documentation places evaluation inside an experiment object and notes the permissions required to execute it. This converts informal spot-checking into a repeatable comparison, although the facility remains in public preview.

A relevant use case is comparing alternative extraction or classification functions on a frozen set of manually adjudicated survey responses, scanned forms or administrative descriptions. The evaluation set should reflect languages, rare classes and difficult cases; it must be separated from prompt development data. Offices should supplement aggregate scores with error matrices, subgroup results, abstention rates, cost and latency, then require subject-matter approval before production.

- **Sources:** [Snowflake evaluation release note](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-21-ai-function-evaluation-preview); [`AI_FUNCTION_EVALUATION` documentation](https://docs.snowflake.com/en/sql-reference/functions/ai_function_evaluation).

**Snowflake Cortex AI Function Optimization, public preview from 21 September 2026**

The companion optimisation capability searches across prompts and models for candidate implementations with different quality and cost characteristics. Snowflake’s guidance presents quality–cost comparisons between experiment runs and allows a selected run to be promoted into a new AI function.

For official statistics, this can help explore whether a less costly implementation meets a pre-specified acceptance threshold for document triage, code suggestions or metadata extraction. The search objective must not be reduced to a single average score: minimum performance for small domains, language groups and sensitive categories should be treated as constraints. Optimisation data must exclude confidential content unless the environment and contractual controls are approved. Because the feature is preview, promotion to production should remain outside the automated experiment.

- **Sources:** [Snowflake optimisation release note](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-21-ai-function-optimization-preview); [Cortex AI Function Evaluation and Optimization](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-function-studio).

### Analysis, reporting and dissemination

**Claude Opus 5.5, released 22 September 2026**

Anthropic released Claude Opus 5.5 as a generally available model and published a system card describing its evaluation and safety work. Vendor benchmarks and price claims are useful for screening, but they are not evidence of performance on a statistical office’s data, languages or disclosure rules.

A defensible use case is a head-to-head evaluation for drafting non-official summaries, code review or retrieval-assisted answers grounded in published statistics. The test should use a fixed corpus and score factual accuracy, citation fidelity, arithmetic, unsupported inference, multilingual consistency, privacy behaviour and cost. No model-generated narrative should be released as an official interpretation without accountable human approval and access to the underlying tables and metadata.

- **Sources:** [Claude Opus 5.5 documentation](https://platform.claude.com/docs/en/models/opus-5-5/overview); [Anthropic model system cards](https://www.anthropic.com/system-cards).

### Access, privacy and responsible AI

**Model Context Protocol (MCP) demonstrations for official statistics**

UNECE has listed material on responsible AI in official statistics using MCP, while the UNECE Responsible AI for Official Statistics Framework remains the stronger governance reference. MCP is an interoperability pattern that can expose tools or data resources to AI applications; it is not, by itself, an assurance mechanism.

For NSOs, the promising use case is a read-only assistant that queries approved dissemination APIs or semantic services instead of copying confidential microdata into a model prompt. An implementation should use allow-listed tools, least-privilege credentials, query and response logs, rate limits, disclosure controls and deterministic source citations. Treat this pattern as emerging until independent security testing and statistical-quality evaluation are complete.

- **Sources:** [UNECE documents listing](https://unece.org/media/documents); [UNECE Responsible AI for Official Statistics Framework](https://unece.org/statistics/documents/2025/10/reports/responsible-ai-official-statistics-framework); [UNECE Generative AI for Official Statistics report](https://unece.org/statistics/documents/2025/09/reports/generative-ai-official-statistics-hlg-mos-report).

## **Implementation and governance cautions**

- **Measure the statistical task, not only the model.** Evaluation sets should reflect the production population, languages, rare categories and known sources of error.
- **Separate development, evaluation and acceptance.** Reusing the same examples for prompt tuning and final scoring gives an optimistic result.
- **Keep deterministic controls.** Schema checks, edit rules, valid-code lists and disclosure checks should run outside the generative model.
- **Control dependency changes.** Lockfiles, software bills of materials and regression tests are necessary even when the visible change is only a patch.
- **Preserve provenance.** Record source versions, prompts, models, parameters, classifications, human decisions and release authority.
- **Restrict previews.** Public-preview and emerging capabilities belong in isolated pilots, not unattended production chains.

## **Implications for statistical offices**

The common direction is encouraging: evaluation is becoming a first-class component rather than an afterthought. That makes it easier to require evidence before adopting AI for coding, editing or reporting. At the same time, the GX–SQLAlchemy compatibility episode shows that conventional software dependencies remain a statistical-quality risk. AI governance therefore has to cover the complete processing chain, not just the model endpoint.

The most robust near-term architecture is hybrid: deterministic validation and disclosure controls surround a narrowly scoped AI component; labelled evaluation data measure its performance; logs preserve provenance; and a named statistical authority decides whether outputs can progress. Preview optimisation can help find candidates, but institutional acceptance criteria must remain fixed and independent of the vendor’s optimisation loop.

## **Next actions**

1. Create one versioned, multilingual evaluation set for a high-value task such as text coding or metadata extraction.
2. Add backend-specific regression tests before upgrading SQLAlchemy or GX in any production validation chain.
3. Define acceptance thresholds by important subgroup, not only as an overall average.
4. Pilot typed model outputs against an authoritative classification and route invalid or uncertain cases to human review.
5. Draft a read-only, least-privilege access pattern for AI tools connected to published statistical data.
6. Require a model card, local test report, provenance record and accountable sign-off before any production release.

## **Sources**

- [SQLAlchemy 2.1 documentation](https://docs.sqlalchemy.org/en/21/intro.html)
- [SQLAlchemy change log](https://www.sqlalchemy.org/changelog/)
- [GX Core change log](https://docs.greatexpectations.io/docs/core/changelog/)
- [GX SQL data-source guidance](https://docs.greatexpectations.io/docs/core/connect_to_data/sql_data/)
- [Pydantic AI 2.49.0 release](https://github.com/pydantic/pydantic-ai/releases/tag/v2.49.0)
- [Pydantic AI output documentation](https://pydantic.dev/docs/ai/core-concepts/output/)
- [Snowflake evaluation release note](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-21-ai-function-evaluation-preview)
- [`AI_FUNCTION_EVALUATION` documentation](https://docs.snowflake.com/en/sql-reference/functions/ai_function_evaluation)
- [Snowflake optimisation release note](https://docs.snowflake.com/en/release-notes/2026/other/2026-09-21-ai-function-optimization-preview)
- [Cortex AI Function Evaluation and Optimization](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-function-studio)
- [Claude Opus 5.5 documentation](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- [Anthropic model system cards](https://www.anthropic.com/system-cards)
- [UNECE documents listing](https://unece.org/media/documents)
- [UNECE Responsible AI for Official Statistics Framework](https://unece.org/statistics/documents/2025/10/reports/responsible-ai-official-statistics-framework)
- [UNECE Generative AI for Official Statistics report](https://unece.org/statistics/documents/2025/09/reports/generative-ai-official-statistics-hlg-mos-report)
