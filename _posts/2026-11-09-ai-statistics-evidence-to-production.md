---
layout: post
title: "AI for official statistics: from document extraction to governed production"
date: 2026-11-09
lang: en
translation_key: weekly-ai-update-2026-11-09
permalink: /ai-statistics-evidence-to-production/
categories: [official-statistics, artificial-intelligence]
tags: [AI, surveys, data-processing, imputation, governance]
---

## Executive summary

This update covers seven developments reported between 19 October and 6 November 2026. New generally available document parsing and image inspection functions could help statistical offices process administrative records and scanned questionnaires. Beta workflow and metadata features could make extraction more repeatable and data definitions easier to review. Meanwhile, recent work from the Office for National Statistics (ONS) and the UN Economic Commission for Europe (UNECE) shows that measuring AI and using machine learning for imputation remain methodological questions, not simply software choices. Vendor availability is **not** statistical validation: each proposed use below requires a controlled benchmark against established methods.

## At a glance

| Development | Lifecycle stage | Maturity | Practical interpretation |
|---|---|---|---|
| BigQuery `AI.PARSE_DOCUMENT` (2 November) | Ingest; structure | Stable (generally available) | Extract layout to JSON; verify fields and tables |
| Databricks AI Function tasks (4 November) | Clean; code | Beta | Run incremental parsing, extraction and classification with review |
| Google sensitive-data TIFF inspection (2 November) | Protect; validate | Released feature | Screen multi-page scans before wider access |
| Databricks Unity Catalog wikis (6 November) | Integrate; document | Beta | Record intended use and source definitions |
| Google Agent Registry skills (6 November) | Govern; audit | Stable for registry; encryption preview | Version and scan reusable agent instructions |
| ONS AI measurement agenda (4–5 November) | Survey; analyse | Emerging methodology | Refine AI adoption questions and thematic accounts |
| UNECE editing and imputation meeting (19–21 October) | Edit; impute | Emerging evidence | Test inference when ML is used in imputation |

## Collection, integration and documentation

**Document parsing is easier to operationalise.** Google made BigQuery `AI.PARSE_DOCUMENT` generally available on 2 November. It converts document layout elements, including paragraphs, lists, tables and images, to structured JSON. A census office could use it to pre-process historical forms or administrative PDFs, but should compare extracted values with double-keyed samples, preserve original page references and route low-confidence or unusual cases to staff. Layout extraction does not establish that a variable has the correct statistical meaning. [1]

**Metadata collaboration is moving closer to the data.** Databricks introduced Unity Catalog wikis in beta on 6 November. Data stewards can describe a table's meaning, intended use and sources, with suggestions and comments from authorised users. For linked population and agricultural census frames, a wiki could record unit definitions, reference dates and permissible joins. Keep the approved statistical metadata and revision history authoritative; a wiki alone is not a formal quality assessment. [2]

## Editing, coding, imputation and analysis

**Incremental AI processing can be scheduled, but remains beta.** Databricks added AI Function tasks for jobs on 4 November. They can apply document parsing, extraction or classification to new or changed files or rows and write results to a governed table. A pilot could code free-text crop or occupation descriptions, retaining the source text, model version, confidence and human decision. Measure precision and recall by language, region and rare categories, and reconcile every re-run with the input register. [3]

**Inference after machine-learning imputation needs explicit scrutiny.** UNECE's 19–21 October expert meeting included David Haziza's keynote on statistical inference in the presence of ML imputation and a Spanish National Statistics Institute contribution on monitored selective editing for categorical data. These are conference contributions, not evidence of a universally production-ready method. For an agricultural survey, compare bias, variance and coverage with a design-aware baseline; retain sampling weights, document missingness assumptions and evaluate difficult subgroups before changing an estimator. [4]

**Measuring AI itself is becoming a statistical design task.** In a 4 November lecture published on 5 November, ONS described gaps in identifying AI producers, purchased and in-house applications, data investment, quality change and the intensity of AI use. It plans further thematic-account and survey work. Offices considering an AI module in business surveys should separate adoption, frequency, expenditure, own-account development and observed outcomes, then test respondent interpretation. The lecture is a research agenda, not a new official-statistics series. [5]

## Privacy, security and responsible dissemination

**Scanned records gain another screening route.** On 2 November, Google Sensitive Data Protection added inspection of TIFF images, including multi-page TIFFs up to 50 pages, in content inspection, Cloud Storage jobs and discovery. This could help identify personal information in digitised census schedules before researchers receive access. Detection is imperfect: test local names, handwritten content and languages, and apply access control and disclosure review even after a clean scan. [6]

**Reusable agent instructions now have stronger controls.** On 6 November, Google reported generally available standalone skills in Agent Registry, including registration, immutable revisions and publisher details. Security scanning and policy controls were also announced; customer-managed encryption of skill payloads remains in preview. An office could version an assistant's approved validation or publication instructions, review changes and restrict who may invoke tools. This does not validate statistical outputs or remove prompt-injection risk from source documents. [7]

## Implications for statistical offices

These releases favour small, measurable pilots over wholesale automation. Separate technical success (a file parsed or task completed) from statistical success (correct units, codes, estimates and uncertainty). Preserve source records, transformation versions and reviewer decisions. Where a service processes confidential microdata, confirm location, retention, contractual controls and lawful access before uploading it. Published figures and explanatory text still require a named statistical owner and reproducible checks.

## Next actions

1. Select one bounded document or free-text coding workload and create a human-reviewed reference sample.
2. Benchmark extraction or classification by language, subgroup and rare category; record correction time and total cost.
3. Document source definitions, joins and permitted uses for one administrative-data integration.
4. Assess privacy scanning on local TIFF examples and verify residual disclosure risks manually.
5. Draft an AI measurement module with cognitive testing and a clear distinction between adoption and intensive use.

## Sources

1. Google Cloud, [release notes, 2 November 2026](https://docs.cloud.google.com/release-notes) — BigQuery `AI.PARSE_DOCUMENT` availability.
2. Databricks, [November 2026 platform release notes, 6 November](https://docs.databricks.com/gcp/en/release-notes/product/2026/november) — Unity Catalog wikis beta.
3. Databricks, [November 2026 platform release notes, 4 November](https://docs.databricks.com/gcp/en/release-notes/product/2026/november) — AI Function tasks beta.
4. UNECE, [Expert Meeting on Statistical Data Editing, 19–21 October 2026](https://unece.org/statistics/events/SDE2026) — programme and conference contributions.
5. ONS, [James Benford's Deane-Stone lecture, 4 November 2026](https://www.ons.gov.uk/news/news/jamesbenford2026deanestonelecturenationalinstituteofeconomicandsocialresearch4november2026), published 5 November.
6. Google Cloud, [Sensitive Data Protection release notes, 2 November 2026](https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes) — TIFF inspection.
7. Google Cloud, [release notes, 6 November 2026](https://docs.cloud.google.com/release-notes) — Agent Registry skills and security controls.
