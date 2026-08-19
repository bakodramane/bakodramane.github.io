---
layout: post
title: "AI measurement, structured outputs and statistical quality"
date: 2026-08-19
author: Dramane Bako
description: "Recent AI measurement, validation and governance updates for surveys, administrative data and official statistics."
categories: [AI, Surveys, Administrative Data, Official Statistics]
tags: [AI tools, surveys, censuses, administrative data, official statistics]
lang: en
translation_key: weekly-ai-update-2026-08-19
---

## **Executive summary**

This week's developments point to a practical shift: statistical organisations are moving from broad discussion of artificial intelligence (AI) to measurable adoption, structured outputs, traceable dissemination and stronger validation controls. The most relevant updates are useful for survey design, administrative-data pipelines and public dissemination, but they still require careful testing before any use in official statistical production.

## **What is new this week**

### Survey design and measurement

**U.S. Census Bureau BTOS AI supplement data products, released 18 June 2026**

The U.S. Census Bureau released Business Trends and Outlook Survey (BTOS) data products and visualisations from supplemental questions on business use of AI. The supplement covered AI adoption by industry, geography, firm size, business function and worker task, with BTOS continuing as a biweekly survey of employer businesses.

This matters because AI adoption is becoming a measurement topic, not only an internal technology question. A practical use case is adapting enterprise, labour-force or establishment surveys to capture AI use by business process, geography and size class. Implementation should document question wording, reference periods, mode effects, comparability over time and disclosure controls before using results for policy monitoring.

- **Sources:** [U.S. Census Bureau, BTOS data release](https://www.census.gov/newsroom/press-releases/2026/btos-june-18.html); [BTOS data page](https://www.census.gov/hfp/btos/data).

**ONS analysis of AI in UK businesses, released 20 July 2026**

The UK Office for National Statistics (ONS) published official statistics on AI use in UK businesses from the Business Insights and Conditions Survey. The release describes how businesses apply AI, the factors shaping uptake and where effects are emerging.

For statistical offices, the release is a useful example of integrating AI adoption into a recurring business survey rather than relying only on ad hoc technology surveys. A practical use case is comparing AI-use modules across business surveys and administrative business registers. Implementation should align classifications, preserve metadata on survey waves and avoid interpreting adoption indicators as productivity or welfare impacts unless those links are separately measured.

- **Sources:** [ONS, Artificial intelligence in UK businesses: 2023 to 2026](https://www.ons.gov.uk/releases/aiinukbusinesses); [GOV.UK official statistics page](https://www.gov.uk/government/statistics/ai-in-uk-businesses).

### Editing and validation

**Great Expectations 1.20.0, released 7 August 2026**

Great Expectations released version 1.20.0 of its open-source data validation library. The release is mainly a maintenance and reliability update, including fixes for read-only filesystem contexts, SQL metric aliases, unmet expectations when a column has no quantiles, SQLite quantile metrics and support promotion for `ExpectColumnValuesToMatchStrftimeFormat`.

This matters for statistical production because validation rules are often the first line of defence when administrative data, survey paradata or model outputs enter a pipeline. A practical use case is adding versioned expectations for identifier formats, date fields, range checks and missingness thresholds before AI-assisted coding or imputation. Implementation should pin versions, rerun existing validation suites and keep failed-row review procedures separate from automated correction.

- **Sources:** [Great Expectations on PyPI](https://pypi.org/project/great-expectations/); [Great Expectations 1.20.0 release notes](https://github.com/fivetran/great_expectations/releases).

### Processing and integration

**Transformers 5.15.0 and response parsing documentation, released 10 August 2026**

Hugging Face Transformers 5.15.0 was published on PyPI, and the project documentation now describes response templates and `parse_response()` for converting raw chat-model generations into structured message dictionaries. The documentation also covers streaming response parsing and typed tool-call arguments from JSON Schema.

This matters where agencies test large language models (LLMs) for coding free-text responses, extracting metadata or routing records for review. A practical use case is a controlled research workflow that parses LLM outputs into predefined fields for manual assessment rather than free-form text. Implementation should treat parser output as machine-generated evidence requiring validation, retain prompts and model versions where policy permits, and test for silent mis-parsing on edge cases and multilingual responses.

- **Sources:** [Transformers on PyPI](https://pypi.org/project/transformers/); [Hugging Face Transformers response parsing documentation](https://huggingface.co/docs/transformers/main/chat_response_parsing).

**Gemini API structured outputs documentation, updated 17 August 2026**

Google updated the Gemini API structured outputs documentation, which describes configuring models to return responses that follow a JSON Schema. The documentation identifies data extraction, structured classification and agentic workflows as use cases, while also noting limits such as partial JSON Schema support and possible rejection of complex schemas.

For official statistics, schema-constrained outputs are relevant to experimental classification, metadata extraction and controlled dissemination services. A practical use case is extracting standardised variables from public methodological documents or classifying incoming user questions by topic before routing. Implementation should validate semantic correctness after schema validation, avoid confidential microdata, keep human review for statistical decisions and monitor API changes through release notes.

- **Sources:** [Gemini API structured outputs](https://ai.google.dev/gemini-api/docs/structured-output?lang=rest); [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog).

### Reporting and dissemination

**UNECE AI-Ready Dissemination project and standards workshop materials, active in 2026**

UNECE's High-Level Group for the Modernisation of Official Statistics is running an AI-Ready Dissemination project in 2026, focused on making official statistical products discoverable, traceable and transparently cited by third-party AI systems. Related 2026 workshop materials cover standards, metadata management, AI-ready dissemination, SDMX, data bots and standards-based architectures for official statistics.

This matters because dissemination is becoming a machine-to-machine problem as well as a human website problem. A practical use case is reviewing whether key indicators expose persistent identifiers, reference periods, caveats, revision histories and machine-readable metadata for retrieval-augmented generation systems. Implementation should prioritise authoritative APIs, clear licences, citation guidance and benchmark tests for how external AI systems retrieve official figures.

- **Sources:** [UNECE HLG-MOS AI-Ready Dissemination project](https://unece.org/ru/node/395050); [UNECE Workshop on Supporting Standards 2026](https://unece.org/statistics/events/Standards2026).

### Governance, privacy and responsible AI

**Google DeepMind model cards updated for Gemini models, 13 August 2026**

Google DeepMind updated its model-card index, including a 13 August 2026 update for Gemini 3.7 Flash and July 2026 updates for Gemini 3.6 Flash and Gemini 3.5 Flash-Lite. Model cards provide structured summaries of how advanced AI models were designed and evaluated.

For statistical offices, the main lesson is governance practice rather than any single model choice. A practical use case is requiring model cards or equivalent documentation for any externally hosted model used in research, editing, coding or public communication. Implementation should record model identity, intended use, evaluation evidence, limitations, data handling terms, residual risks and deprecation dates; model cards do not replace local validation on statistical data.

- **Source:** [Google DeepMind model cards](https://deepmind.google/models/model-cards/).

**National Academies summary of 2026 AI Day for Federal Statistics, updated 22 July 2026**

The U.S. National Academies published a summary of the 2026 AI Day for Federal Statistics, covering active AI experimentation in federal statistical agencies and emphasising guardrails, evaluation, ethics, transparency, replicability and public trust. The article includes examples around survey implementation, coding of text responses and statistical leadership in AI deployment.

This matters because it frames AI as an operational and governance issue for statistical systems, not just a technical upgrade. A practical use case is setting up an AI review board or methods panel for pilots in coding, editing and dissemination. Implementation should define decision rights, evidence thresholds, audit trails, confidentiality controls and rollback procedures before scaling pilots into production workflows.

- **Source:** [National Academies, Federal Statistics Enters the Age of AI - Carefully](https://www.nationalacademies.org/news/federal-statistics-enters-the-age-of-ai-carefully).

## **Implications for statistical offices**

The common thread is that AI readiness depends on measurement, metadata and controls. Statistical offices need to measure AI adoption in the economy, but they also need to make their own data products easier for AI systems to cite accurately and harder for automated tools to detach from definitions, caveats and revision histories.

The tooling updates are useful, but they are not a substitute for statistical quality management. Structured outputs can make LLM results easier to validate, data-quality libraries can detect pipeline failures earlier, and model cards can improve procurement and governance. None of these remove the need for representative data, transparent methods, human review and local validation.

## **Next actions**

- Review whether business and establishment surveys include clear, comparable questions on AI adoption and use cases.
- Add validation suites for administrative-data intake, especially dates, identifiers, classifications, ranges and missingness.
- Test schema-constrained LLM outputs only on non-confidential or approved research data, with manual review.
- Inventory public indicators most likely to be retrieved by AI systems and strengthen metadata, citations and revision notes.
- Require model cards or equivalent documentation before piloting externally hosted AI models.
- Define evidence thresholds and rollback procedures before moving AI-assisted coding or dissemination pilots toward production.

## **Sources**

- [U.S. Census Bureau, Business Trends and Outlook Survey Data Release - June 18, 2026](https://www.census.gov/newsroom/press-releases/2026/btos-june-18.html)
- [U.S. Census Bureau, BTOS data page](https://www.census.gov/hfp/btos/data)
- [ONS, Artificial intelligence in UK businesses: 2023 to 2026](https://www.ons.gov.uk/releases/aiinukbusinesses)
- [GOV.UK, AI in UK businesses](https://www.gov.uk/government/statistics/ai-in-uk-businesses)
- [Great Expectations on PyPI](https://pypi.org/project/great-expectations/)
- [Great Expectations 1.20.0 release notes](https://github.com/fivetran/great_expectations/releases)
- [Transformers on PyPI](https://pypi.org/project/transformers/)
- [Hugging Face Transformers response parsing documentation](https://huggingface.co/docs/transformers/main/chat_response_parsing)
- [Gemini API structured outputs](https://ai.google.dev/gemini-api/docs/structured-output?lang=rest)
- [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog)
- [UNECE HLG-MOS AI-Ready Dissemination project](https://unece.org/ru/node/395050)
- [UNECE Workshop on Supporting Standards 2026](https://unece.org/statistics/events/Standards2026)
- [Google DeepMind model cards](https://deepmind.google/models/model-cards/)
- [National Academies, Federal Statistics Enters the Age of AI - Carefully](https://www.nationalacademies.org/news/federal-statistics-enters-the-age-of-ai-carefully)
