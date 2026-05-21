---
layout: post
title: "Stanford AI Index 2026, LLM-assisted survey analysis, and AI adoption in the US economy"
date: 2026-04-20
author: Dramane Bako
description: "Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis, AI adoption"
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, official-statistics, administrative-data]
lang: en
translation_key: 2026-04-20-weekly-update-on-ai-tools-for-surveys-and-administrative-data-stanford-ai-index-llm-survey-analysis
---

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms...) and administrative data for official statistics.

Coverage Period: 14 – 20 April 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis, AI adoption

## **Key Takeaways**

- **Stanford's 2026 AI Index Report** highlights that generative AI has reached a 53% population-level adoption rate within three years, with 58% of employees globally reporting AI use at work. However, public anxiety is rising, and the U.S. public reports the lowest trust in its government to regulate AI effectively.
- **The Federal Reserve** published a note on monitoring AI adoption in the U.S. economy, revealing that 18% of firms have adopted AI as of year-end 2025, and 78% of the labor force works at firms that have adopted AI.
- **LAPS (LLM-Assisted Public Survey)**, a new automated framework, was introduced to support end-to-end, hypothesis-driven statistical analysis of survey data, reducing cognitive burden while ensuring researcher agency.
- **Language Model Fine-Tuning on Scaled Survey Data** (SubPOP dataset) demonstrates that fine-tuning LLMs on structured survey data significantly improves the prediction of public opinion distributions, reducing the LLM-human gap by up to 46%.

### 1. AI Adoption and Public Opinion: Insights from the 2026 Stanford AI Index

The Stanford Institute for Human-Centered AI released its highly anticipated **2026 AI Index Report** in April 2026, providing a comprehensive, data-driven portrait of AI's rapid development and societal impact [1]. The report reveals that generative AI has achieved a 53% population-level adoption rate within just three years, spreading faster than the personal computer or the internet.

In the workplace, 58% of employees globally reported using AI on a semiregular or regular basis in 2025. Interestingly, workplace AI usage is higher in several emerging economies than in many advanced ones; in countries like India, China, Nigeria, the UAE, Egypt, and Saudi Arabia, the share exceeded 80% [2].

Despite the rapid adoption, public sentiment is complex. While 59% of global respondents feel optimistic about AI's benefits, 52% report that AI products make them nervous. In the United States, 64% of Americans expect AI to lead to fewer jobs over the next 20 years, and the U.S. public reported the lowest trust (31%) in its government to regulate AI responsibly among all surveyed countries [2].

### 2. Monitoring AI Adoption in the U.S. Economy

A recent note from the Federal Reserve examined trends in AI adoption in the U.S. economy using three publicly available surveys: the Census Bureau's Business Trends and Outlook Survey (BTOS), the Real-Time Population Survey (RPS), and the Survey of Business Uncertainty (SBU) [3].

The analysis found that about 18% of U.S. firms had adopted AI as of year-end 2025. However, when weighted by employment, the SBU estimates that 78% of the labor force works at firms that have adopted AI, and about 54% works at firms that use Large Language Models (LLMs) [3]. This indicates that while the absolute number of firms adopting AI is still growing, the largest employers have already integrated AI into their operations. The report also noted robust AI adoption in high-value services sectors, such as professional services and finance, suggesting that current AI usage is most prevalent in cognitive and analytical work.

### 3. LAPS: Automating Hypothesis-Driven Statistical Analysis of Public Surveys

A new paper presented at the CHI 2026 conference introduced **LAPS**, an LLM-assisted automated framework designed to support end-to-end, hypothesis-driven statistical analysis of public survey data [4]. Public surveys are vital for understanding social dynamics, but their analysis often imposes a high cognitive load due to structural complexity.

LAPS consists of four modules: Operationalization, Planning, Execution, and Reporting. It incorporates human-in-the-loop mechanisms to balance automation with user agency. A user study with 12 social science researchers demonstrated that LAPS ensures analytical stability, reduces the cognitive burden in the analysis workflow, and produces trustworthy, coherent outputs [4]. This tool represents a significant step forward in making complex survey data analysis more accessible and efficient for researchers.

### 4. Fine-Tuning LLMs on Scaled Survey Data for Opinion Prediction

Researchers from UC Berkeley and Microsoft Research proposed a novel approach to predicting public opinion distributions by directly fine-tuning LLMs on scaled survey data [5]. They curated **SubPOP**, a dataset of 3,362 questions and 70,000 subpopulation-response pairs from well-established public opinion surveys.

Prior methods attempted to steer LLMs using prompt engineering (describing subpopulations in the input prompt), but these approaches struggled to faithfully predict human response distributions. The study showed that fine-tuning on the SubPOP dataset greatly improved the match between LLM predictions and human responses across various subpopulations, reducing the LLM-human gap by up to 46% compared to baselines [5]. This advancement highlights the potential of survey-based fine-tuning to enable more efficient survey designs and accurate opinion prediction for diverse, real-world subpopulations.

## **References**

[1] Inside the AI Index: 12 Takeaways from the 2026 Report. Stanford HAI. https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report
[2] Public Opinion | The 2026 AI Index Report. Stanford HAI. https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion
[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
[4] LAPS: Automating Hypothesis-Driven Statistical Analysis of Public Survey Using Large Language Models. ACM Digital Library. https://dl.acm.org/doi/full/10.1145/3772318.3791665
[5] Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions. arXiv. https://arxiv.org/html/2502.16761v2
