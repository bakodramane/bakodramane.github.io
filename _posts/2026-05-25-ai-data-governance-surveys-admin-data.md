---
layout: post
title: "AI Data Governance and Validation Moves for Statistical Systems"
date: 2026-05-25
author: Dramane Bako
description: "Recent AI-related updates for data validation, integration, survey measurement and governance in official statistics."
categories: [AI, Surveys, Administrative Data, Official Statistics]
tags: [AI tools, surveys, censuses, administrative data, official statistics]
lang: en
translation_key: weekly-ai-update-2026-05-25
---

## **Executive summary**

This week's developments point less to a single breakthrough than to a maturing operational agenda: data-quality tooling, governed integration, evaluation methods and AI-risk management are moving closer to routine statistical production. For national statistical offices, the practical message is to treat AI adoption as a data lifecycle issue, not only as a modelling issue.

## **What is new this week**

### Editing and validation

**Great Expectations open-source stewardship update, 6 May 2026.** Great Expectations announced that Fivetran will become the new steward of the GX Core open-source project, while GX Core is expected to remain an open-source, community-driven data-quality framework. For official statistics, expectation-based validation is a practical way to encode editing rules, range checks, referential checks and release-readiness tests.

- **Practical use case:** turn survey and administrative data edit rules into executable validation suites before imputation, integration or dissemination.
- **Implementation notes:** organisations using GX should track project governance, release cadence and migration guidance. A stewardship change should trigger dependency review, reproducibility checks and archiving of validation rules used in official releases.
- **Sources:** [Great Expectations community update](https://greatexpectations.io/blog/an-update-from-great-expectations/).

### Cleaning and quality assurance

**Subject matter expert evaluation flywheel for generative AI, 5 May 2026.** AWS Public Sector described a four-phase approach for integrating subject matter experts into generative AI evaluation: define quality criteria, build human-scored ground truth, compare automated metrics against expert judgement, and periodically recalibrate. Although it is a vendor implementation note, the evaluation pattern is relevant to statistical uses of large language models (LLMs).

- **Practical use case:** evaluate AI-assisted coding of occupations, products, causes of death, open survey responses or metadata descriptions against expert-coded benchmark cases.
- **Implementation notes:** start with rubrics that distinguish factual accuracy, classification consistency, uncertainty handling and policy sensitivity. Automated scoring should not replace expert review until correlation with human judgement has been measured and monitored.
- **Sources:** [AWS Public Sector Blog on subject matter experts in generative AI evaluation](https://aws.amazon.com/blogs/publicsector/integrating-subject-matter-experts-into-generative-ai-evaluation-with-the-aws-generative-ai-innovation-center/).

### Processing and integration

**DuckDB 1.5.3, released 20 May 2026.** DuckDB 1.5.3 adds Quack as a core extension, improves DuckLake support, and adds Iceberg, AWS and HTTPS extension features. Quack is still in beta, but the release is relevant for statistical teams using DuckDB for reproducible local analytics, register-level exploration or lightweight extract-transform-load work.

- **Practical use case:** prototype secure analytical processing of administrative extracts on laptops or controlled servers before moving workflows to production platforms.
- **Implementation notes:** treat Quack as experimental until production readiness is confirmed. For official production, document extension versions, compile-time options, network controls and access paths to object stores or lakehouse tables.
- **Sources:** [DuckDB 1.5.3 announcement](https://duckdb.org/2026/05/20/announcing-duckdb-153).

**Azure Databricks May 2026 Lakeflow updates.** Microsoft Learn lists May 2026 updates including Lakeflow Designer enabled by default for several workspace tiers, AI-assisted operator search, configurable sample sizes, Git import/export for visual data prep files, user-defined operators in public preview, managed ingestion connectors for Outlook, GitHub and Smartsheet in beta, and native data profiling for notebook results.

- **Practical use case:** build governed data-preparation workflows for administrative data pipelines, with visual transformations, profiling and source ingestion documented in version-controlled files.
- **Implementation notes:** beta connectors and public-preview operators should be evaluated outside production first. Email and collaboration-system ingestion can expose personal or confidential information, so retention rules, legal bases, data minimisation and access controls must be defined before use.
- **Sources:** [Azure Databricks May 2026 release notes](https://learn.microsoft.com/en-us/azure/databricks/release-notes/product/2026/may).

**Amazon SageMaker catalog integration pattern, 22 May 2026.** AWS described how Amazon is extending an enterprise data catalog into Amazon SageMaker to cover datasets, dashboards, metrics and other assets under common governance and identity controls. The system described is internal to Amazon, but the design pattern is relevant for statistical organisations that need AI-ready metadata across multiple data domains.

- **Practical use case:** connect administrative registers, survey frames, derived indicators and dashboards to a common catalogue so analysts can discover assets and request access consistently.
- **Implementation notes:** catalogues should include ownership, legal basis, sensitivity, lineage, retention and quality metadata. AI-readiness depends on metadata completeness and governed access, not only storage technology.
- **Sources:** [AWS Big Data Blog on integrating catalogues with SageMaker](https://aws.amazon.com/blogs/big-data/how-amazon-is-moving-to-integrate-catalogs-to-improve-data-discovery-with-amazon-sagemaker/).
### Analysis and modelling

**U.S. Census Bureau Business Trends and Outlook Survey AI module, 7 May 2026.** The U.S. Census Bureau released new Business Trends and Outlook Survey data products covering business use of artificial intelligence. The supplemental AI questions were collected from 17 November 2025 to 8 February 2026 and are available as data downloads and visualisations, with breakdowns by industry, geography and firm size.

- **Practical use case:** use the module design as a reference when developing survey questions on AI adoption, tasks supported by AI and workforce effects.
- **Implementation notes:** AI-adoption questions need cognitive testing because respondents may interpret "AI" differently across firm sizes and sectors. Where possible, pair self-reported adoption with task-specific examples and metadata about firm operations.
- **Sources:** [U.S. Census Bureau BTOS AI data release](https://www.census.gov/newsroom/press-releases/2026/btos-may-7.html).

### Reporting and dissemination

**Eurostat report on AI use in the European Union, 26 March 2026.** Eurostat published the 2026 edition of its statistical report on the use of AI technologies among enterprises and citizens in the European Union. The report provides an official statistical reference for measuring AI diffusion, complementing country-level survey work and digital economy indicators.

- **Practical use case:** benchmark national AI-adoption indicators against harmonised European definitions and reporting formats.
- **Implementation notes:** when using Eurostat indicators as comparators, check target population, enterprise-size thresholds, sector coverage and reference periods. Differences in questionnaire wording can affect comparability.
- **Sources:** [Eurostat 2026 report on AI technologies in the EU](https://ec.europa.eu/eurostat/web/products-statistical-reports/w/ks-01-26-009).

### Governance, privacy and responsible AI

**World Bank guidance on AI-derived inference in public financial institutions, 5 May 2026.** A World Bank blog argued that central banks and supervisory authorities need governance for AI-enabled inference, not only governance for the raw personal data they hold. The point applies beyond finance: administrative data systems can infer sensitive attributes when datasets are linked or modelled.

- **Practical use case:** review whether statistical or administrative AI systems can infer protected, sensitive or high-risk attributes that are not explicitly collected.
- **Implementation notes:** data protection impact assessments should cover inferred data, profiling, redress, transparency and limits on secondary use. "Not confirmed in sources" should be used internally for any claimed inference benefit that lacks validation evidence.
- **Sources:** [World Bank blog on AI governance and inference](https://blogs.worldbank.org/en/allaboutfinance/from-data-to-inference--why-ai-governance-matters-for-central-ba).

**IMF warning on AI-enabled cyber risk, 7 May 2026.** The International Monetary Fund warned that AI can accelerate vulnerability discovery, exploitation and correlated cyber failures across shared digital infrastructure. For statistical systems, the relevance is operational: AI pipelines, cloud platforms, survey systems and dissemination portals depend on the same security foundations as other public digital services.

- **Practical use case:** include AI-assisted threat scenarios in business continuity plans for census operations, survey collection systems and administrative-data exchange platforms.
- **Implementation notes:** integrate AI projects into cybersecurity governance from design stage. Priorities include identity management, patching, model and data access logs, incident response, disaster recovery and supplier concentration review.
- **Sources:** [IMF blog on AI-fuelled cyber risks](https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks).

## **Implications for statistical offices**

The common thread is that AI adoption depends on stronger data operations. Validation frameworks, catalogues, source connectors, evaluation rubrics and cyber controls are becoming as important as model selection. Statistical offices should therefore align AI pilots with existing quality frameworks, confidentiality rules, metadata standards and production-change controls.

There is also a clear distinction between production-ready and emerging components. Great Expectations, catalogues and validation rubrics can support current workflows, while beta connectors, public-preview operators and DuckDB's Quack protocol require controlled testing before any official production use.

## **Next actions**

- Inventory AI-related pilots across the statistical data lifecycle and link each one to a named business owner, data owner and quality owner.
- Convert high-priority editing and validation rules into executable tests for survey and administrative data pipelines.
- Build small expert-scored benchmark datasets for AI-assisted classification, coding, summarisation and metadata generation.
- Review whether linked administrative datasets or AI models can infer sensitive attributes not directly collected.
- Add AI-enabled cyber scenarios to continuity plans for surveys, censuses, data exchange and dissemination systems.
- Track beta and preview platform features separately from production-approved tools.

## **Sources**

- [Great Expectations, "An Update for the Great Expectations Community", 6 May 2026](https://greatexpectations.io/blog/an-update-from-great-expectations/)
- [AWS Public Sector Blog, "Integrating subject matter experts into generative AI evaluation", 5 May 2026](https://aws.amazon.com/blogs/publicsector/integrating-subject-matter-experts-into-generative-ai-evaluation-with-the-aws-generative-ai-innovation-center/)
- [DuckDB, "DuckDB 1.5.3: Not an Ordinary Patch Release", 20 May 2026](https://duckdb.org/2026/05/20/announcing-duckdb-153)
- [Microsoft Learn, "Azure Databricks release notes: May 2026"](https://learn.microsoft.com/en-us/azure/databricks/release-notes/product/2026/may)
- [AWS Big Data Blog, "How Amazon is moving to integrate catalogs to improve data discovery with Amazon SageMaker", 22 May 2026](https://aws.amazon.com/blogs/big-data/how-amazon-is-moving-to-integrate-catalogs-to-improve-data-discovery-with-amazon-sagemaker/)
- [U.S. Census Bureau, "Business Trends and Outlook Survey Data Release", 7 May 2026](https://www.census.gov/newsroom/press-releases/2026/btos-may-7.html)
- [Eurostat, "The use of artificial intelligence technologies in the European Union - Key results - 2026 edition", 26 March 2026](https://ec.europa.eu/eurostat/web/products-statistical-reports/w/ks-01-26-009)
- [World Bank Blogs, "From data to inference: Why AI governance matters for central banks in developing economies", 5 May 2026](https://blogs.worldbank.org/en/allaboutfinance/from-data-to-inference--why-ai-governance-matters-for-central-ba)
- [IMF Blog, "Financial Stability Risks Mount as Artificial Intelligence Fuels Cyberattacks", 7 May 2026](https://www.imf.org/en/blogs/articles/2026/05/07/financial-stability-risks-mount-as-artificial-intelligence-fuels-cyberattacks)
