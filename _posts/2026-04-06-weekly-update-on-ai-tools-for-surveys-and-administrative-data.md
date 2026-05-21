---
layout: post
title: "AI Adoption, LLM Evaluation and StatGPT"
date: 2026-04-06
author: Dramane Bako
description: "Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis"
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, official-statistics, administrative-data]
lang: en
translation_key: 2026-04-06-weekly-update-on-ai-tools-for-surveys-and-administrative-data
---

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Coverage Period: 30 March – 5 April 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis

## **Key Takeaways**

AI adoption in the US economy is growing rapidly: Business survey data from the Census Bureau show that about 18 percent of firms have adopted AI as of year-end 2025, with significant variation across firm size and industry cohorts.

Generative AI is transforming survey design but requires human oversight: While AI tools can accelerate survey writing and generate strong drafts, they often underestimate respondent burden and produce flawed response options, necessitating expert review.

Evaluating LLMs on complex statistical data is crucial: Organizations must implement structured evaluation frameworks to test LLM performance in tool-enabled, multistep analytic workflows, as stand-alone reasoning is insufficient for applied statistical work.

The IMF introduces StatGPT for official statistics: StatGPT leverages LLMs to generate structured queries against APIs of official statistical agencies, ensuring users receive exact published figures while benefiting from natural language interaction.

## **Natural Language Processing & LLMs for Survey Design**

Generative AI chatbots are increasingly used by UX researchers to quickly deploy surveys. When given a clear research objective and prompted to use survey-design best practices, tools like ChatGPT and Claude can generate a solid first draft in seconds [1]. However, these tools often underestimate respondent burden and can produce flawed response options, such as omitting an "Other" option or generating semantically unbalanced rating scales [1]. Therefore, human expertise remains essential for oversight and pilot testing with real people is crucial to reveal confusion or friction that AI cannot detect [1].

## **Machine Learning & AI for Survey Data Analysis, Weighting, and Estimation**

As organizations integrate large language models (LLMs) into analytic workflows, evaluating their performance on complex statistical data is critical. A recent evaluation framework tested LLM performance in tool-enabled, multistep analytic workflows using complex survey data [2]. The findings revealed that code execution is foundational; when limited to reasoning alone, error rates were substantial, but accuracy increased significantly when models could access data and execute code [2]. Furthermore, statistical competence varies meaningfully across models, especially for causal inference tasks, highlighting the need for structured evaluation frameworks grounded in real data and controlled tool use [2].

## **AI in Official Statistics and Household Surveys**

The adoption of AI in the US economy is being closely monitored through various surveys. Business survey data from the Census Bureau indicate that about 18 percent of firms have adopted AI as of year-end 2025 [3]. The Real-Time Population Survey reports that work-related Generative AI adoption stands at about 41 percent as of November 2025 [3]. These surveys also reveal considerable heterogeneity across firm size and industry cohorts, with robust adoption in high-value services sectors suggesting that current AI usage is most prevalent in cognitive and analytical work [3].

In the realm of official statistics, the IMF has introduced StatGPT, an initiative that leverages LLMs to generate structured queries against APIs of official statistical agencies [4]. This approach ensures that users receive the exact published figures while benefiting from natural language interaction, overcoming the limitations of off-the-shelf GenAI applications that frequently provide incorrect figures [4].

Additionally, the Committee on National Statistics, the Federal Committee on Statistical Methodology, and the National Institute of Statistical Sciences are organizing a second AI Day for Federal Statistics on April 30, 2026 [5]. This workshop will explore the implications of AI for federal statistics, providing opportunities for training, capacity building, and sharing best practices for using AI to drive government efficiency and modernize the federal workforce [5].

## **References**

[1] AI Can Help with Survey Writing, But It Still Requires Human Expertise. Nielsen Norman Group. https://www.nngroup.com/articles/ai-survey-writing/

[2] Trusting your LLM: AI’s handling of complex statistical data. Mathematica. https://www.mathematica.org/blogs/trusting-your-llm

[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

[4] StatGPT: AI for Official Statistics. International Monetary Fund. https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[5] AI Day for Federal Statistics 2026. Population Association of America. https://www.populationassociation.org/events/event-description?CalendarEventKey=f26dfb08-99f4-42fa-921a-019cb515a57b&Home=%2Fhome

Contact: bakodramane@gmail.com
