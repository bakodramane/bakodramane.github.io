---
layout: post
title: "AI Readiness Assessment Toolkit to help NSOs benchmark their progress"
date: 2025-12-22
author: Dramane Bako
description: "Key words: AI, survey research, official statistics, machine learning, data quality, automation, household surveys, data analysis"
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, statistics, official-statistics, bilingual]
lang: en
translation_key: 2025-12-22-weekly-update-on-ai-tools-for-surveys-and-administrative-data-ai-readiness-asses
---

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Coverage Period: 22–28 December 2025

Key words: AI, survey research, official statistics, machine learning, data quality, automation, household surveys, data analysis

## **Executive Summary**

This week's update on artificial intelligence in survey research highlights significant advancements across the entire survey lifecycle, from data cleaning and collection to analysis and dissemination. Key developments include the use of large language models (LLMs) for data restoration and as a replacement for traditional survey methods, new frameworks for detecting AI-generated survey responses, and the release of comprehensive AI-readiness guides for national statistical offices. These trends indicate a rapid maturation of AI applications in the field, moving from experimental use cases to integrated, production-level systems.

A groundbreaking study in Nature Scientific Data demonstrates the power of masked language models (MLMs) like BERT and RoBERTa for restoring historical household survey data [1]. The research, focused on the Daegu-bu household registers from 1681–1876, employed a two-step methodology involving comprehensive data cleaning followed by AI-driven analysis to automate the reconstruction of missing and misinterpreted values. This approach has significant implications for modern survey research, offering a robust framework for handling incomplete or damaged survey records and automating data quality checks.

Research published in Computational Economics showcases the potential of AI to replace or augment traditional survey methods entirely [2]. The study uses LLMs to extract inflation expectations directly from the public discourse of economic experts on social media platforms like Twitter. This AI-driven approach enables real-time measurement of economic indicators without the need for costly and time-consuming surveys, offering enhanced timeliness and frequency. The methodology is sophisticated enough to distinguish between perceptions of past inflation and genuine forward-looking expectations, a limitation of simpler sentiment analysis techniques. This development signals a paradigm shift where AI can generate survey-equivalent data from existing online discourse, reducing respondent burden and providing a cost-effective alternative for high-frequency data collection.

Ensuring Data Quality in the Age of AI

As AI becomes more capable, ensuring the quality and authenticity of survey data is a growing concern. A study in Survey Practice evaluated the ability of OpenAI's agentic AI tool, Operator, to complete online surveys and investigated methods for detecting such AI-assisted responses [3]. The research found that while traditional methods like attention checks and honeypot questions are largely ineffective against modern AI agents, other indicators can reliably identify them.

These findings underscore the urgent need for survey researchers and statistical offices to develop and adapt new quality control mechanisms for the age of AI.

Institutional AI Readiness and Adoption

Recognizing the growing importance of AI, several organizations have released guidance and initiated programs to promote AI readiness.

PARIS21 has launched a comprehensive framework to help national statistical offices (NSOs), particularly in low- and middle-income countries, become "AI-ready" [4]. The SPEED framework (State, Policy, Expertise, Engine, and Delivery) provides a roadmap for responsible AI adoption, addressing challenges like weak infrastructure, limited budgets, and the need for technical expertise. It includes an upcoming AI Readiness Assessment Toolkit to help NSOs benchmark their progress.

In the United States, the Census Bureau has updated its Business Trends and Outlook Survey (BTOS) to include new core questions on AI adoption [8]. This represents the first systematic, large-scale government effort to track AI's economic impact through official statistics. Early data already shows a significant increase in AI use among U.S. businesses, from 3.7% in late 2024 to 10% by September 2025.

Meanwhile, the UK's Office for National Statistics (ONS) is considering making some household surveys mandatory to combat declining response rates [9]. This data crisis highlights the urgency for AI-enhanced methods that can improve engagement and reduce respondent burden, offering a more sustainable solution than legal mandates.

Emerging AI Tools and Platforms

The market for AI-powered survey tools is rapidly expanding. Artemis, a new AI Survey Assistant from ngSurvey, exemplifies the trend toward end-to-end automation [6]. It offers capabilities spanning the entire survey lifecycle:

Data Analysis: Delivers comprehensive insights, trend analysis, and effortless data filtering.

Open-Text Insights: Uses deep categorization and sentiment analysis to extract actionable insights from thousands of open-ended comments in any language.

Reporting: Generates executive summaries and presentation-ready reports in minutes.

Established platforms are also integrating AI. The SurveyCTO 2025 year-in-review highlights a major shift towards greater automation and interoperability, driven by AI [10]. The platform now features API-enabled data transfers, dynamic cloud-based datasets, and advanced capabilities for geospatial data collection and offline case management.

Privacy-Preserving AI

As data accessibility becomes a priority under new regulations like the U.S. Evidence Act, protecting respondent privacy is paramount. A paper on arXiv details the development of CenSyn, a machine learning framework for creating synthetic public-use microdata samples (PUMS) for the U.S. Census Bureau's business surveys [5]. This approach generates artificial data that preserves the statistical properties of the original restricted-use data without containing any real individual or business records. This allows for wider public access to valuable data for research and policymaking while adhering to strict confidentiality requirements.

## **Conclusion**

The developments of the past week demonstrate a clear and accelerating trend: AI is no longer a peripheral technology in survey research but is becoming a core component of modern data collection, processing, and analysis. From restoring historical data to creating new real-time indicators and ensuring data quality, AI is reshaping the field. For researchers and statistical offices, the key challenge is no longer whether to adopt AI, but how to do so responsibly, ethically, and effectively.

## **References**

[1] Mun, S., Lee, D., Yoo, J., & Lee, S. (2025). Reweaving the Threads of Korean History: AI-Driven Restoration of the Daegu-bu Household Registers (1681–1876). Scientific Data. https://www.nature.com/articles/s41597-025-06299-5

[2] Jaworski, K. (2025). Measuring Inflation Expectations Using Artificial Intelligence. Computational Economics. https://link.springer.com/article/10.1007/s10614-025-11231-5

[3] Martherus, J., Podkul, A., Cook, E., & Liebowitz, R. (2025). How to Detect AI-assisted Interviews in Online Surveys. Survey Practice. https://www.surveypractice.org/article/146046-how-to-detect-ai-assisted-interviews-in-online-surveys

[4] PARIS21. (2025). Towards AI-Ready National Statistical Offices: A Framework for Strengthening NSO Capacity in Low- and Middle-Income Countries. https://www.paris21.org/knowledge-base/towards-ai-ready-national-statistical-offices-framework-strengthening-nso-capacity

[5] Cisneros, J., et al. (2025). Developing synthetic microdata through machine learning for firm-level business surveys. arXiv. https://arxiv.org/html/2512.05948v2

[6] ngSurvey. (2025). Artemis — AI Survey Assistant for Design, Insights & Reporting. https://www.ngsurvey.com/agentic-survey-artemis

[7] Naddaf, M. (2025). More than half of researchers now use AI for peer review — often against guidance. Nature. https://www.nature.com/articles/d41586-025-04066-5

[8] U.S. Census Bureau. (2025). Business Trends and Outlook Survey - Methodology. https://www.census.gov/hfp/btos/methodology

[9] Bloomberg News. (2025). UK Stats Agency Studies Mandatory Surveys as Possible Fix for Data Crisis. https://www.bloomberg.com/news/articles/2025-12-19/ons-studies-mandatory-surveys-as-uk-mulls-how-to-fix-data-crisis

[10] Kuenzi, M. (2025). A year in review: 2025 from SurveyCTO. SurveyCTO. https://www.surveycto.com/events-trends/year-in-review-2025/

Contact: bakodramane@gmail.com
