---
title: "Weekly Update: AI in Survey Research and Household Surveys / Mise à jour hebdomadaire : l'IA dans la recherche par sondage et les enquêtes auprès des ménages"
date: 2026-01-05
categories: [AI, Survey Research, Weekly Update]
tags: [artificial intelligence, survey research, household surveys, statistics, bilingual]
lang: en-fr
---

## 🇬🇧 English

# Weekly Update: AI in Survey Research and Household Surveys

_Week of March 9, 2026_

**Author:** Manus AI

## Executive Summary

This weekly update surveys the most recent developments in the application of artificial intelligence (AI) to survey research and household surveys, covering the full lifecycle from questionnaire design and data collection through processing, analysis, and dissemination. The reporting period has been particularly active, coinciding with the 57th Session of the United Nations Statistical Commission (UNSC57, 3–6 March 2026) in New York, where AI-readiness for official data and statistics was a central theme. Key highlights include a new UNECE HLG-MOS work programme for 2026 that launches dedicated projects on AI-ready dissemination and trust; a high-level UN seminar on AI-readiness for official statistics; a new IMF working paper using GPT-4.1 to build a global fiscal policy database; a Nature Communications study combining machine learning and satellite imagery to estimate the Human Development Index at sub-national scale; and a new arXiv preprint proposing an unsupervised framework for detecting inattentive survey respondents. The overarching theme is a transition from experimentation to institutionalization: NSOs are moving from pilot projects to embedding AI into core statistical production workflows, while simultaneously grappling with governance, trust, and capacity challenges.

## 1\. AI in Data Collection and Fieldwork

### 1.1. Machine Learning for Survey Sampling and Adaptive Design

The use of machine learning to optimize survey sampling is gaining momentum. By automating quality control processes, machine learning bolsters the robustness of sample selection and data collection procedures, enabling real-time adjustments to sampling strategies based on incoming data [\[1\]](#footnote-1). This approach, often referred to as adaptive survey design, allows survey managers to reallocate fieldwork resources dynamically, targeting areas or subgroups where response rates are low or data quality is poor.

The UNECE HLG-MOS has recognized the strategic importance of this area and is launching a new activity in 2026 on **"Advancing Cost-Effective Data Collection Using Paradata and Adaptive Survey Design,"** proposed by the Australian Bureau of Statistics (ABS). The initiative seeks to consolidate methodological developments across NSOs and develop a blueprint for increasing the use of paradata—data about the data collection process itself—to optimize survey quality and resource allocation. This builds directly on the outcomes of the ASCENT (Advanced Survey Cost-Effectiveness with Nonresponse Treatment) project and reflects the increasing importance of leveraging operational data for evidence-based survey design [\[2\]](#footnote-2).

### 1.2. AI-Assisted Fieldwork and Interviewer Support

AI is being increasingly integrated into Computer-Assisted Personal Interviewing (CAPI) and Computer-Assisted Telephone Interviewing (CATI) systems. AI tools can monitor interviewer performance in real-time, flag potential errors or inconsistencies, and provide dynamic prompts to interviewers when a respondent's answer requires clarification. In qualitative research settings, AI is being used to pre-screen hundreds of respondent profiles and surface the most qualified candidates, while also automating transcription and translation tasks that previously caused significant delays [\[3\]](#footnote-3).

A recent study published in JMIR Human Factors examined mode effects between telephone and web interviews, finding that CATI interviews resulted in higher numbers of reported symptoms compared to web-based modes, a finding with important implications for the design of mixed-mode surveys and the interpretation of mode effects in the context of AI-assisted interviewing [\[4\]](#footnote-4).

### 1.3. Detecting Inattentive Respondents and Survey Fraud

A significant challenge in survey research is the detection of inattentive or fraudulent respondents who provide random or low-effort answers. Traditional safeguards, such as attention checks, are often costly, reactive, and inconsistent. A new preprint submitted to arXiv on 2 March 2026 proposes a unified, label-free framework for inattentiveness detection that scores response coherence using two complementary unsupervised approaches: geometric reconstruction via Autoencoders and probabilistic dependency modeling via Chow-Liu trees [\[5\]](#footnote-5).

"The framework provides survey platforms with a scalable, domain-agnostic diagnostic tool that links data quality directly to instrument design, enabling auditing without additional respondent burden." — Triantafyllopoulos & Ipeirotis (2026) [\[6\]](#footnote-5)

The study's key finding is that detection effectiveness is driven less by model complexity than by survey structure: instruments with coherent, overlapping item batteries exhibit strong covariance patterns that allow even linear models to reliably separate attentive from inattentive respondents. This reveals a critical "Psychometric-ML Alignment": the same design principles that maximize measurement reliability also maximize algorithmic detectability.

## 2\. AI in Data Processing and Analysis

### 2.1. Automated Coding of Open-Ended Responses

The automated coding of open-ended survey responses—including occupation titles, industry descriptions, and free-text answers—has long been a goal for statistical offices seeking to reduce manual processing costs. The advent of powerful LLMs has brought this goal within reach. Research presented at the First Workshop on Bridging NLP and Survey Science demonstrates the potential of LLMs to accurately code job titles and other textual data, with an LLM integrated directly into questionnaire scripting software to probe for further relevant detail on job tasks and industry before coding to a standard occupational classification [\[7\]](#footnote-6).

A complementary study published in 2026 examines how LLM-driven contextual probing can improve the quality of open-ended survey responses, providing systematic experimental validation that LLM-driven contextual prompts increase the number and depth of topics covered in respondent answers [\[8\]](#footnote-7). These developments are poised to have a major impact on the production of official statistics, enabling more detailed and timely analysis of labor market dynamics.

### 2.2. Data Editing, Imputation, and Quality Control

AI-powered tools are being developed to address the challenges of data editing, imputation of missing data, and overall data quality control. Deep learning models can be trained to identify and correct errors in survey data, while advanced imputation techniques based on machine learning are proving to be more effective than traditional methods for handling missing values. A systematic survey published in PMC in March 2026 evaluates how missing patient-reported outcome data are handled in randomized controlled trials, finding significant variation in the quality of reporting and the sophistication of imputation methods employed [\[9\]](#footnote-8).

A comparative study published in medRxiv in February 2026 evaluates three methodologies for imputing missing data—Denoising Autoencoders (DAE), Self-Attention-based Imputation for Time Series (SAITS), and MICE+LightGBM—finding that deep learning approaches offer advantages in handling complex missingness patterns [\[10\]](#footnote-9). These findings have direct relevance for household surveys, where item non-response and unit non-response are persistent challenges.

### 2.3. Machine Learning for Poverty and Welfare Analysis

AI is enabling researchers to combine traditional household survey data with novel data sources, such as high-resolution satellite imagery, to produce more granular and timely estimates of poverty and well-being. A landmark study co-authored by the UNDP Human Development Report Office (HDRO), published in Nature Communications on 17 February 2026, demonstrates how satellite imagery and machine learning can extend the Human Development Index (HDI) from national averages to highly localized estimates [\[11\]](#footnote-10). The research reports results for 61,530 municipalities and counties worldwide and also assesses differences using 10-by-10-kilometer grid tiles.

"Almost all the data that we have about the world is collected from household surveys that are then aggregated up to some convenient administrative area... \[this study\] reveals within-country disparities that national statistics can miss." — Phys.org summary of the Sherman et al. (2026) study [\[12\]](#footnote-11)

The study is co-authored with academic collaborators at the Stanford Doerr School of Sustainability, Caltech, and the University of British Columbia, and reflects HDRO's investment in innovating on human development metrics through partnerships with leading research institutions. The estimates are designed to complement—not replace—official national HDI reporting.

### 2.4. AI for Fiscal and Economic Analysis

A new IMF Working Paper (WP/26/43), published on 6 March 2026, demonstrates the use of AI for large-scale economic data processing. The paper builds the first global quarterly narrative database of discretionary government spending actions by applying a fixed GPT-4.1 prompt to Economist Intelligence Unit (EIU) Country Reports, covering an unbalanced panel of 64 countries from 1952:Q1 to 2023:Q4 [\[13\]](#footnote-12). The resulting series identifies exogenous spending shocks for fiscal multiplier analysis, and the authors validate the database by replicating expert narrative coding and showing that the identified shocks predict subsequent movements in measured government spending. This represents a significant advance in the use of LLMs for "text-as-data" approaches in economics and official statistics.

The following table summarizes key AI applications in survey data processing and analysis:

Application Area

AI Technology

Key Development (2026)

Source

Occupation coding

LLMs (GPT-class)

SOCbot integrates LLM into CAPI scripting for real-time coding

Sturgis et al. (2025) [\[14\]](#footnote-6)

Open-ended response analysis

LLMs

Contextual probing improves response depth and topic coverage

Wieland et al. (2026) [\[15\]](#footnote-7)

Missing data imputation

Autoencoders, SAITS

Deep learning outperforms MICE for complex missingness

medRxiv (2026) [\[16\]](#footnote-9)

Poverty mapping

Satellite imagery + ML

HDI estimated for 61,530 municipalities worldwide

Sherman et al., Nature Comms (2026) [\[17\]](#footnote-10)

Fiscal policy analysis

GPT-4.1

Global narrative database of spending shocks, 64 countries

IMF WP/26/43 [\[18\]](#footnote-12)

Inattentive respondent detection

Autoencoders, Chow-Liu trees

Unsupervised framework links data quality to instrument design

Triantafyllopoulos & Ipeirotis (2026) [\[19\]](#footnote-5)

## 3\. AI in Dissemination and Reporting

### 3.1. AI-Ready Dissemination: A New HLG-MOS Priority

The concept of "AI-ready" dissemination is emerging as a top priority for the international statistical community. The HLG-MOS 2026 Work Programme launches a dedicated project titled **"AI-Ready Dissemination — Optimizing Statistical Products for Third-Party AI Consumption."** The project recognizes that as AI services such as chatbots increasingly serve as primary access points for information, it is essential that statistical organizations optimize their dissemination practices to ensure their data remains discoverable, interpretable, and trustworthy when consumed by AI systems [\[20\]](#footnote-2).

The project is organized around four work packages: (1) knowledge sharing and case studies; (2) quality frameworks for AI-ready statistical data, including an AI-readiness maturity framework or scorecard; (3) technical approaches for AI-ready statistical data, including the use of SDMX, Data Commons, and emerging protocols such as Model Context Protocol (MCP) servers; and (4) communication with external actors, including AI model developers and service providers.

### 3.2. The UN Statistical Commission's AI-Readiness Seminar

The 57th Session of the UN Statistical Commission (UNSC57) featured a landmark Friday Seminar on Emerging Issues on 27 February 2026, titled **"AI-Readiness for Official Data and Statistics."** The seminar brought together senior statisticians, technology experts, and policymakers to discuss the challenges and opportunities of making official statistics AI-ready [\[21\]](#footnote-13).

The seminar defined the objective of AI-readiness as follows:

"The objective of AI-readiness of official data and statistics is to provide users who search for and access data and statistics through AI with correct, timely, coherent, human-understandable, and contextually relevant official data and metadata, with a clear indication of their provenance and vintage." — UNSD, 2026 [\[22\]](#footnote-13)

The seminar was organized around four sessions covering: (1) the challenge and opportunity for official statistics in the AI age; (2) making data and metadata machine-readable and machine-understandable; (3) data governance, licensing frameworks, and capacity; and (4) a concluding roundtable with heads of Eurostat, the World Bank, Statistics South Africa, and the Swiss Federal Statistical Office. A key message from the seminar was that NSOs must embrace both a technical role (ensuring data quality, machine-readability, and interoperability) and a stewardship role (governing the AI ecosystem and establishing guardrails for the use of official data).

### 3.3. Generative AI for Statistical Reporting

The UNECE HLG-MOS published its report on "Generative AI for Official Statistics" in September 2025, which continues to be widely referenced as the field evolves. The report explores how generative AI is reshaping the production, use, and communication of official statistics, and provides a framework for NSOs to evaluate and adopt generative AI tools responsibly [\[23\]](#footnote-14). Building on this work, the 2026 programme includes continued exploration of how LLMs can be used to automate the generation of statistical narratives and press releases, while ensuring accuracy and adherence to quality standards.

## 4\. AI in National and International Statistical Offices

### 4.1. UNECE HLG-MOS: Responsible AI and Uncertainty Quantification

The HLG-MOS "Applying Data Science and Modern Methods" (ADSaMM) Group is finalizing two major deliverables in early 2026. The first is a guidance document on **Uncertainty Quantification (UQ)**, providing practical recommendations for statistical organizations to integrate UQ as a routine component of measurement when using machine learning or AI models, strengthening the reliability and assurance of official statistics. The second is a training program on **Responsible AI (RAI)**, including modules on responsible AI foundations, MLOps and LLMOps, and Explainable AI (XAI), designed to reduce biases, improve transparency, and safeguard privacy [\[24\]](#footnote-2).

### 4.2. Eurostat: Measuring AI Adoption

Eurostat is actively monitoring the adoption of AI across the European Union. A report published on 10 February 2026 revealed that 63.8% of young people aged 16-24 in the EU used generative AI tools in 2025—nearly twice the share of the overall adult population [\[25\]](#footnote-15). A separate Eurostat study on types of AI technologies found that machine learning, predictive analytics, conversational assistants, and computer vision are the most widely used AI technologies among EU businesses. This data provides crucial context for NSOs as they consider how to engage with a public that is increasingly accustomed to interacting with AI.

### 4.3. U.S. Census Bureau: Measuring AI in Business Surveys

The U.S. Census Bureau has taken concrete steps to measure the impact of AI on the U.S. economy by adding AI-specific questions to its **Business Trends and Outlook Survey (BTOS)** and the **Annual Business Survey**. As of December 2025, 17 percent of businesses in the BTOS report using AI in their business functions, according to a speech by Federal Reserve Governor Barr [\[26\]](#footnote-16). A bipartisan group of senators has pushed for even more detailed data on AI's impact, reflecting the growing policy interest in understanding AI adoption across the economy.

### 4.4. Malaysia and Other NSOs at UNSC57

At the 57th UN Statistical Commission, Malaysia highlighted its adoption of AI-enabled solutions, including AgroBot on the TaniStats 2.0 platform, to enhance agricultural data collection and improve user responsiveness [\[27\]](#footnote-17). This is one of many examples from developing countries of NSOs beginning to leverage AI tools to modernize their statistical production processes, even in resource-constrained environments. The PARIS21 AI-readiness framework for NSOs is providing guidance to developing country statistical offices on how to build the capacity needed to adopt AI responsibly.

### 4.5. UNICEF and the Future of Household Surveys

At UNSC57, UNICEF convened a side event focused on the future of household surveys, with a particular focus on the Multiple Indicator Cluster Surveys (MICS) programme. The event highlighted the growing role of AI in shaping the future of household survey design, data collection, and analysis, and explored how AI can be used to reduce the cost and time required to produce high-quality household survey data in low- and middle-income countries [\[28\]](#footnote-18).

## 5\. Conclusion

The week of March 9, 2026 has been a landmark period for AI in survey research and official statistics. The convergence of the 57th UN Statistical Commission, the release of the UNECE HLG-MOS 2026 Work Programme, and a wave of new research publications signals that the field is entering a new phase of maturity. NSOs are moving from isolated experiments to systematic integration of AI into their core statistical production workflows. The key challenges ahead are not primarily technical but institutional: building the governance frameworks, quality standards, and human capacity needed to deploy AI responsibly and maintain public trust in official statistics.

The following table provides a summary of the key developments covered in this update:

Development

Organization

Date

Significance

AI-readiness seminar at UNSC57

UNSD

27 Feb 2026

Sets agenda for AI-ready official statistics globally

HLG-MOS 2026 Work Programme

UNECE

March 2026

Launches AI-Ready Dissemination and Trust Matters projects

GPT-4.1 for fiscal policy database

IMF

6 March 2026

Demonstrates LLM for large-scale text-as-data analysis

HDI estimation from satellite imagery

UNDP/Stanford/Caltech/UBC

17 Feb 2026

Sub-national poverty mapping using ML

Unsupervised inattentive respondent detection

NYU/Cornell

2 March 2026

Scalable AI tool for survey data quality

LLM for occupation coding (SOCbot)

University of Southampton

2025

Automates ISCO coding in CAPI systems

AI questions in BTOS and Annual Business Survey

US Census Bureau

2025–2026

Measures AI adoption in the US economy

63.8% of EU youth use generative AI

Eurostat

10 Feb 2026

Contextualizes AI literacy for NSO engagement

AgroBot for agricultural data collection

Statistics Malaysia

2026

AI adoption in developing country NSO

## References

1.  SAE International. (2026, February 22). _How Machine Learning is Changing Survey Sampling_. [https://sae2025.org/how-machine-learning-is-changing-survey-sampling/](https://sae2025.org/how-machine-learning-is-changing-survey-sampling/) [↑](#footnote-ref-1)
    
2.  UNECE. (2026, March). _HLG-MOS Work Programme for 2026_. [https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf](https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf) [↑](#footnote-ref-2)
    
3.  The Logit Group. (2026, March 5). _How AI Is Transforming Qualitative Fieldwork_. [https://logitgroup.com/ai-qualitative-fieldwork/](https://logitgroup.com/ai-qualitative-fieldwork/) [↑](#footnote-ref-3)
    
4.  JMIR Human Factors. (2026, March 6). _Mode Effects Between Telephone and Web Interviews in the Post-Pandemic Era_. [https://humanfactors.jmir.org/2026/1/e80631](https://humanfactors.jmir.org/2026/1/e80631) [↑](#footnote-ref-4)
    
5.  Triantafyllopoulos, I., & Ipeirotis, P. (2026, March 2). _Learning to Pay Attention: Unsupervised Modeling of Attentive and Inattentive Respondents in Survey Data_. arXiv:2603.02427. [https://arxiv.org/abs/2603.02427](https://arxiv.org/abs/2603.02427) [↑](#footnote-ref-5)
    
6.  Triantafyllopoulos, I., & Ipeirotis, P. (2026, March 2). _Learning to Pay Attention: Unsupervised Modeling of Attentive and Inattentive Respondents in Survey Data_. arXiv:2603.02427. [https://arxiv.org/abs/2603.02427](https://arxiv.org/abs/2603.02427) [↑](#footnote-ref-5)
    
7.  Sturgis, P., Fung, L., & Roberts, C. (2025). _Using Large Language Models to measure and classify occupations in surveys_. First Workshop on Bridging NLP and Survey Science. [https://openreview.net/forum?id=gFKPmwu2b4](https://openreview.net/forum?id=gFKPmwu2b4) [↑](#footnote-ref-6)
    
8.  Wieland, D., Leyh, N., & Ahrens, F. (2026). _From Prompts to Probes: How Large Language Models Improve Response Quality in Open-Ended Survey Research_. Hawaii International Conference on System Sciences. [https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189](https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189) [↑](#footnote-ref-7)
    
9.  PMC. (2026, March 5). _Are we reporting well enough? A systematic survey of missing data handling in RCTs_. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12961827/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12961827/) [↑](#footnote-ref-8)
    
10.  medRxiv. (2026, February 17). _A Comparative Study of DAE, SAITS, and MICE+LightGBM for Imputing Missing Data_. [https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full](https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full) [↑](#footnote-ref-9)
     
11.  Sherman, L., et al. (2026, February 17). _Global high-resolution estimates of the UN Human Development Index_. Nature Communications. [https://www.nature.com/articles/s41467-026-68805-6](https://www.nature.com/articles/s41467-026-68805-6) [↑](#footnote-ref-10)
     
12.  Phys.org. (2026, February 17). _Satellite imagery and AI reveal development needs hidden by national statistics_. [https://phys.org/news/2026-02-satellite-imagery-ai-reveal-hidden.html](https://phys.org/news/2026-02-satellite-imagery-ai-reveal-hidden.html) [↑](#footnote-ref-11)
     
13.  Das, S., Furceri, D., Patel, N., & Peralta-Alva, A. (2026, March 6). _AI Meets Fiscal Policy: Mapping Government Spending Actions Across 64 Countries_. IMF Working Paper WP/26/43. [https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286](https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286) [↑](#footnote-ref-12)
     
14.  Sturgis, P., Fung, L., & Roberts, C. (2025). _Using Large Language Models to measure and classify occupations in surveys_. First Workshop on Bridging NLP and Survey Science. [https://openreview.net/forum?id=gFKPmwu2b4](https://openreview.net/forum?id=gFKPmwu2b4) [↑](#footnote-ref-6)
     
15.  Wieland, D., Leyh, N., & Ahrens, F. (2026). _From Prompts to Probes: How Large Language Models Improve Response Quality in Open-Ended Survey Research_. Hawaii International Conference on System Sciences. [https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189](https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189) [↑](#footnote-ref-7)
     
16.  medRxiv. (2026, February 17). _A Comparative Study of DAE, SAITS, and MICE+LightGBM for Imputing Missing Data_. [https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full](https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full) [↑](#footnote-ref-9)
     
17.  Sherman, L., et al. (2026, February 17). _Global high-resolution estimates of the UN Human Development Index_. Nature Communications. [https://www.nature.com/articles/s41467-026-68805-6](https://www.nature.com/articles/s41467-026-68805-6) [↑](#footnote-ref-10)
     
18.  Das, S., Furceri, D., Patel, N., & Peralta-Alva, A. (2026, March 6). _AI Meets Fiscal Policy: Mapping Government Spending Actions Across 64 Countries_. IMF Working Paper WP/26/43. [https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286](https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286) [↑](#footnote-ref-12)
     
19.  Triantafyllopoulos, I., & Ipeirotis, P. (2026, March 2). _Learning to Pay Attention: Unsupervised Modeling of Attentive and Inattentive Respondents in Survey Data_. arXiv:2603.02427. [https://arxiv.org/abs/2603.02427](https://arxiv.org/abs/2603.02427) [↑](#footnote-ref-5)
     
20.  UNECE. (2026, March). _HLG-MOS Work Programme for 2026_. [https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf](https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf) [↑](#footnote-ref-2)
     
21.  UNSD. (2026, February 27). _AI-readiness for Official Data and Statistics: Friday Seminar on Emerging Issues, 57th Statistical Commission_. [https://unstats.un.org/UNSDWebsite/events-details/un57sc-ai-readiness-for-official-data-and-statistics-27Feb2026/](https://unstats.un.org/UNSDWebsite/events-details/un57sc-ai-readiness-for-official-data-and-statistics-27Feb2026/) [↑](#footnote-ref-13)
     
22.  UNSD. (2026, February 27). _AI-readiness for Official Data and Statistics: Friday Seminar on Emerging Issues, 57th Statistical Commission_. [https://unstats.un.org/UNSDWebsite/events-details/un57sc-ai-readiness-for-official-data-and-statistics-27Feb2026/](https://unstats.un.org/UNSDWebsite/events-details/un57sc-ai-readiness-for-official-data-and-statistics-27Feb2026/) [↑](#footnote-ref-13)
     
23.  UNECE. (2025, September). _Generative AI for Official Statistics (HLG-MOS Report 2025)_. [https://unece.org/sites/default/files/2026-03/05\_HLG-MOS%20Report2025.pdf](https://unece.org/sites/default/files/2026-03/05_HLG-MOS%20Report2025.pdf) [↑](#footnote-ref-14)
     
24.  UNECE. (2026, March). _HLG-MOS Work Programme for 2026_. [https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf](https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf) [↑](#footnote-ref-2)
     
25.  Eurostat. (2026, February 10). _64% of 16-24-year-olds used AI in 2025_. [https://ec.europa.eu/eurostat/web/products-eurostat-news/w/edn-20260210-1](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/edn-20260210-1) [↑](#footnote-ref-15)
     
26.  Federal Reserve. (2026, February 17). _Speech by Governor Barr on artificial intelligence and the labor market_. [https://www.federalreserve.gov/newsevents/speech/barr20260217a.htm](https://www.federalreserve.gov/newsevents/speech/barr20260217a.htm) [↑](#footnote-ref-16)
     
27.  Bernama. (2026, March 9). _Malaysia Reinforces Global Statistical Role At UNSC57_. [https://www.bernama.com/en/region/news.php/world/news.php?id=2532130](https://www.bernama.com/en/region/news.php/world/news.php?id=2532130) [↑](#footnote-ref-17)
     
28.  Azevedo, J.P. (2026, March). _The future of household surveys is being shaped now!_ LinkedIn post on UNSC57 side event. [https://www.linkedin.com/posts/jpazvd\_unsc57-mics-officialstatistics-activity-7434623220462403584-fWJB](https://www.linkedin.com/posts/jpazvd_unsc57-mics-officialstatistics-activity-7434623220462403584-fWJB) [↑](#footnote-ref-18)

---

## 🇫🇷 Français

# Mise à jour hebdomadaire : l'IA dans la recherche par sondage et les enquêtes auprès des ménages

_Semaine du 9 mars 2026_

**Auteur :** Manus AI

## Résumé

Cette mise à jour hebdomadaire passe en revue les développements les plus récents dans l'application de l'intelligence artificielle (IA) à la recherche par sondage et aux enquêtes auprès des ménages, couvrant l'ensemble du cycle de vie, de la conception du questionnaire et de la collecte des données au traitement, à l'analyse et à la diffusion. La période de référence a été particulièrement active, coïncidant avec la 57e session de la Commission de statistique des Nations Unies (UNSC57, 3-6 mars 2026) à New York, où la préparation à l'IA pour les données et statistiques officielles était un thème central. Les points saillants incluent un nouveau programme de travail HLG-MOS de la CEE-ONU pour 2026 qui lance des projets dédiés à la diffusion prête pour l'IA et à la confiance ; un séminaire de haut niveau de l'ONU sur la préparation à l'IA pour les statistiques officielles ; un nouveau document de travail du FMI utilisant GPT-4.1 pour construire une base de données mondiale sur la politique budgétaire ; une étude de Nature Communications combinant le machine learning et l'imagerie satellite pour estimer l'Indice de Développement Humain à l'échelle subnationale ; et une nouvelle prépublication arXiv proposant un cadre non supervisé pour détecter les répondants inattentifs aux enquêtes. Le thème général est une transition de l'expérimentation à l'institutionnalisation : les ONS passent des projets pilotes à l'intégration de l'IA dans les flux de production statistique essentiels, tout en faisant face aux défis de gouvernance, de confiance et de capacité.

## 1. L'IA dans la collecte de données et le travail de terrain

### 1.1. Machine Learning pour l'échantillonnage d'enquête et la conception adaptative

L'utilisation du machine learning pour optimiser l'échantillonnage des enquêtes gagne du terrain. En automatisant les processus de contrôle qualité, le machine learning renforce la robustesse de la sélection des échantillons et des procédures de collecte de données, permettant des ajustements en temps réel des stratégies d'échantillonnage basés sur les données entrantes [\[1\]](#footnote-1). Cette approche, souvent appelée conception d'enquête adaptative, permet aux gestionnaires d'enquête de réaffecter dynamiquement les ressources de terrain, en ciblant les zones ou les sous-groupes où les taux de réponse sont faibles ou la qualité des données est médiocre.

Le HLG-MOS de la CEE-ONU a reconnu l'importance stratégique de ce domaine et lance une nouvelle activité en 2026 sur **"L'avancement de la collecte de données rentable à l'aide de paradata et de la conception d'enquêtes adaptatives"**, proposée par l'Australian Bureau of Statistics (ABS). L'initiative vise à consolider les développements méthodologiques au sein des ONS et à élaborer un plan pour accroître l'utilisation des paradata — des données sur le processus de collecte de données lui-même — afin d'optimiser la qualité des enquêtes et l'allocation des ressources. Cela s'appuie directement sur les résultats du projet ASCENT (Advanced Survey Cost-Effectiveness with Nonresponse Treatment) et reflète l'importance croissante de l'exploitation des données opérationnelles pour une conception d'enquête basée sur des preuves [\[2\]](#footnote-2).

### 1.2. Travail de terrain assisté par l'IA et soutien aux enquêteurs

L'IA est de plus en plus intégrée aux systèmes d'interview assistée par ordinateur (CAPI) et d'interview téléphonique assistée par ordinateur (CATI). Les outils d'IA peuvent surveiller les performances des enquêteurs en temps réel, signaler les erreurs ou incohérences potentielles et fournir des invites dynamiques aux enquêteurs lorsqu'une réponse d'un répondant nécessite des éclaircissements. Dans les contextes de recherche qualitative, l'IA est utilisée pour présélectionner des centaines de profils de répondants et identifier les candidats les plus qualifiés, tout en automatisant les tâches de transcription et de traduction qui causaient auparavant des retards importants [\[3\]](#footnote-ref-3).

Une étude récente publiée dans JMIR Human Factors a examiné les effets de mode entre les interviews téléphoniques et web, constatant que les interviews CATI entraînaient un plus grand nombre de symptômes rapportés par rapport aux modes web, une découverte ayant des implications importantes pour la conception d'enquêtes en mode mixte et l'interprétation des effets de mode dans le contexte de l'interview assistée par l'IA [\[4\]](#footnote-ref-4).

### 1.3. Détection des répondants inattentifs et de la fraude aux enquêtes

Un défi important dans la recherche par sondage est la détection des répondants inattentifs ou frauduleux qui fournissent des réponses aléatoires ou peu élaborées. Les mesures de protection traditionnelles, telles que les contrôles d'attention, sont souvent coûteuses, réactives et incohérentes. Une nouvelle prépublication soumise à arXiv le 2 mars 2026 propose un cadre unifié et sans étiquette pour la détection de l'inattention qui évalue la cohérence des réponses à l'aide de deux approches non supervisées complémentaires : la reconstruction géométrique via des Autoencoders et la modélisation de la dépendance probabiliste via des arbres de Chow-Liu [\[5\]](#footnote-ref-5).

"Le cadre fournit aux plateformes d'enquête un outil de diagnostic évolutif et indépendant du domaine qui relie directement la qualité des données à la conception de l'instrument, permettant l'audit sans charge supplémentaire pour le répondant." — Triantafyllopoulos & Ipeirotis (2026) [\[6\]](#footnote-ref-5)

La principale conclusion de l'étude est que l'efficacité de la détection est moins déterminée par la complexité du modèle que par la structure de l'enquête : les instruments avec des batteries d'items cohérentes et superposées présentent des schémas de covariance forts qui permettent même aux modèles linéaires de séparer de manière fiable les répondants attentifs des inattentifs. Cela révèle un "Alignement Psychométrique-ML" critique : les mêmes principes de conception qui maximisent la fiabilité de la mesure maximisent également la détectabilité algorithmique.

## 2. L'IA dans le traitement et l'analyse des données

### 2.1. Codage automatisé des réponses ouvertes

Le codage automatisé des réponses ouvertes aux enquêtes — y compris les titres de profession, les descriptions d'industrie et les réponses en texte libre — a longtemps été un objectif pour les bureaux de statistique cherchant à réduire les coûts de traitement manuel. L'avènement des puissants LLM a rendu cet objectif réalisable. Des recherches présentées lors du First Workshop on Bridging NLP and Survey Science démontrent le potentiel des LLM à coder avec précision les titres de poste et d'autres données textuelles, avec un LLM intégré directement dans un logiciel de script de questionnaire pour rechercher des détails pertinents supplémentaires sur les tâches et l'industrie avant de coder selon une classification professionnelle standard [\[7\]](#footnote-ref-6).

Une étude complémentaire publiée en 2026 examine comment le sondage contextuel basé sur les LLM peut améliorer la qualité des réponses ouvertes aux enquêtes, fournissant une validation expérimentale systématique selon laquelle les invites contextuelles basées sur les LLM augmentent le nombre et la profondeur des sujets abordés dans les réponses des répondants [\[8\]](#footnote-ref-7). Ces développements sont appelés à avoir un impact majeur sur la production de statistiques officielles, permettant une analyse plus détaillée et plus rapide de la dynamique du marché du travail.

### 2.2. Édition, imputation et contrôle qualité des données

Des outils basés sur l'IA sont en cours de développement pour relever les défis de l'édition des données, de l'imputation des données manquantes et du contrôle qualité global des données. Les modèles de deep learning peuvent être entraînés pour identifier et corriger les erreurs dans les données d'enquête, tandis que les techniques d'imputation avancées basées sur le machine learning s'avèrent plus efficaces que les méthodes traditionnelles pour gérer les valeurs manquantes. Une enquête systématique publiée dans PMC en mars 2026 évalue la manière dont les données manquantes sur les résultats rapportés par les patients sont traitées dans les essais contrôlés randomisés, constatant une variation significative dans la qualité des rapports et la sophistication des méthodes d'imputation employées [\[9\]](#footnote-ref-8).

Une étude comparative publiée dans medRxiv en février 2026 évalue trois méthodologies d'imputation des données manquantes — Denoising Autoencoders (DAE), Self-Attention-based Imputation for Time Series (SAITS) et MICE+LightGBM — constatant que les approches de deep learning offrent des avantages dans la gestion des schémas de données manquantes complexes [\[10\]](#footnote-ref-9). Ces résultats ont une pertinence directe pour les enquêtes auprès des ménages, où la non-réponse aux items et la non-réponse des unités sont des défis persistants.

### 2.3. Machine Learning pour l'analyse de la pauvreté et du bien-être

L'IA permet aux chercheurs de combiner les données d'enquêtes traditionnelles auprès des ménages avec de nouvelles sources de données, telles que l'imagerie satellite haute résolution, pour produire des estimations plus granulaires et plus opportunes de la pauvreté et du bien-être. Une étude historique co-écrite par le Bureau du Rapport sur le Développement Humain (HDRO) du PNUD, publiée dans Nature Communications le 17 février 2026, démontre comment l'imagerie satellite et le machine learning peuvent étendre l'Indice de Développement Humain (IDH) des moyennes nationales à des estimations très localisées [\[11\]](#footnote-ref-10). La recherche rapporte des résultats pour 61 530 municipalités et comtés dans le monde et évalue également les différences en utilisant des tuiles de grille de 10 kilomètres sur 10 kilomètres.

"Presque toutes les données que nous avons sur le monde sont collectées à partir d'enquêtes auprès des ménages qui sont ensuite agrégées jusqu'à une zone administrative pratique... [cette étude] révèle des disparités au sein des pays que les statistiques nationales peuvent manquer." — Résumé de Phys.org de l'étude de Sherman et al. (2026) [\[12\]](#footnote-ref-11)

L'étude est co-écrite avec des collaborateurs universitaires de la Stanford Doerr School of Sustainability, de Caltech et de l'Université de la Colombie-Britannique, et reflète l'investissement du HDRO dans l'innovation des métriques de développement humain grâce à des partenariats avec des institutions de recherche de premier plan. Les estimations sont conçues pour compléter — et non remplacer — les rapports officiels nationaux sur l'IDH.

### 2.4. L'IA pour l'analyse fiscale et économique

Un nouveau document de travail du FMI (WP/26/43), publié le 6 mars 2026, démontre l'utilisation de l'IA pour le traitement de données économiques à grande échelle. Le document construit la première base de données narrative trimestrielle mondiale des actions discrétionnaires de dépenses publiques en appliquant une invite GPT-4.1 fixe aux rapports par pays de l'Economist Intelligence Unit (EIU), couvrant un panel déséquilibré de 64 pays du T1 1952 au T4 2023 [\[13\]](#footnote-ref-12). La série résultante identifie les chocs de dépenses exogènes pour l'analyse des multiplicateurs budgétaires, et les auteurs valident la base de données en reproduisant le codage narratif d'experts et en montrant que les chocs identifiés prédisent les mouvements ultérieurs des dépenses publiques mesurées. Cela représente une avancée significative dans l'utilisation des LLM pour les approches "texte-comme-donnée" en économie et en statistiques officielles.

Le tableau suivant résume les principales applications de l'IA dans le traitement et l'analyse des données d'enquête :

Domaine d'application

Technologie d'IA

Développement clé (2026)

Source

Codage des professions

LLM (classe GPT)

SOCbot intègre LLM dans le script CAPI pour un codage en temps réel

Sturgis et al. (2025) [\[14\]](#footnote-ref-6)

Analyse des réponses ouvertes

LLM

Le sondage contextuel améliore la profondeur des réponses et la couverture des sujets

Wieland et al. (2026) [\[15\]](#footnote-ref-7)

Imputation des données manquantes

Autoencoders, SAITS

Le deep learning surpasse MICE pour les données manquantes complexes

medRxiv (2026) [\[16\]](#footnote-ref-9)

Cartographie de la pauvreté

Imagerie satellite + ML

IDH estimé pour 61 530 municipalités dans le monde

Sherman et al., Nature Comms (2026) [\[17\]](#footnote-ref-10)

Analyse de la politique budgétaire

GPT-4.1

Base de données narrative mondiale des chocs de dépenses, 64 pays

FMI WP/26/43 [\[18\]](#footnote-ref-12)

Détection des répondants inattentifs

Autoencoders, arbres de Chow-Liu

Cadre non supervisé reliant la qualité des données à la conception de l'instrument

Triantafyllopoulos & Ipeirotis (2026) [\[19\]](#footnote-ref-5)

## 3. L'IA dans la diffusion et le reporting

### 3.1. Diffusion prête pour l'IA : une nouvelle priorité du HLG-MOS

Le concept de diffusion "prête pour l'IA" apparaît comme une priorité absolue pour la communauté statistique internationale. Le programme de travail 2026 du HLG-MOS lance un projet dédié intitulé **"Diffusion prête pour l'IA — Optimisation des produits statistiques pour la consommation par l'IA tierce."** Le projet reconnaît qu'à mesure que les services d'IA tels que les chatbots deviennent de plus en plus des points d'accès primaires à l'information, il est essentiel que les organisations statistiques optimisent leurs pratiques de diffusion pour garantir que leurs données restent découvrables, interprétables et fiables lorsqu'elles sont consommées par les systèmes d'IA [\[20\]](#footnote-ref-2).

Le projet est organisé autour de quatre groupes de travail : (1) partage des connaissances et études de cas ; (2) cadres de qualité pour les données statistiques prêtes pour l'IA, y compris un cadre de maturité ou un tableau de bord de préparation à l'IA ; (3) approches techniques pour les données statistiques prêtes pour l'IA, y compris l'utilisation de SDMX, Data Commons, et des protocoles émergents tels que les serveurs Model Context Protocol (MCP) ; et (4) communication avec les acteurs externes, y compris les développeurs de modèles d'IA et les fournisseurs de services.

### 3.2. Le séminaire de la Commission de statistique des Nations Unies sur la préparation à l'IA

La 57e session de la Commission de statistique des Nations Unies (UNSC57) a organisé un séminaire historique du vendredi sur les questions émergentes le 27 février 2026, intitulé **"Préparation à l'IA pour les données et statistiques officielles."** Le séminaire a réuni des statisticiens de haut niveau, des experts en technologie et des décideurs politiques pour discuter des défis et des opportunités de rendre les statistiques officielles prêtes pour l'IA [\[21\]](#footnote-ref-13).

Le séminaire a défini l'objectif de la préparation à l'IA comme suit :

"L'objectif de la préparation à l'IA des données et statistiques officielles est de fournir aux utilisateurs qui recherchent et accèdent aux données et statistiques via l'IA des données et métadonnées officielles correctes, opportunes, cohérentes, compréhensibles par l'homme et contextuellement pertinentes, avec une indication claire de leur provenance et de leur millésime." — UNSD, 2026 [\[22\]](#footnote-ref-13)

Le séminaire était organisé autour de quatre sessions couvrant : (1) le défi et l'opportunité pour les statistiques officielles à l'ère de l'IA ; (2) rendre les données et métadonnées lisibles et compréhensibles par les machines ; (3) la gouvernance des données, les cadres de licence et les capacités ; et (4) une table ronde de clôture avec les chefs d'Eurostat, de la Banque mondiale, de Statistics South Africa et de l'Office fédéral de la statistique suisse. Un message clé du séminaire était que les ONS doivent embrasser à la fois un rôle technique (assurer la qualité des données, la lisibilité par les machines et l'interopérabilité) et un rôle de gestion (gouverner l'écosystème de l'IA et établir des garde-fous pour l'utilisation des données officielles).

### 3.3. L'IA générative pour le reporting statistique

Le HLG-MOS de la CEE-ONU a publié son rapport sur "L'IA générative pour les statistiques officielles" en septembre 2025, qui continue d'être largement référencé à mesure que le domaine évolue. Le rapport explore comment l'IA générative remodèle la production, l'utilisation et la communication des statistiques officielles, et fournit un cadre aux ONS pour évaluer et adopter de manière responsable les outils d'IA générative [\[23\]](#footnote-ref-14). S'appuyant sur ce travail, le programme 2026 comprend une exploration continue de la manière dont les LLM peuvent être utilisés pour automatiser la génération de récits statistiques et de communiqués de presse, tout en garantissant l'exactitude et le respect des normes de qualité.

## 4. L'IA dans les offices statistiques nationaux et internationaux

### 4.1. CEE-ONU HLG-MOS : IA responsable et quantification de l'incertitude

Le groupe HLG-MOS "Applying Data Science and Modern Methods" (ADSaMM) finalise deux livrables majeurs début 2026. Le premier est un document d'orientation sur la **Quantification de l'incertitude (UQ)**, fournissant des recommandations pratiques aux organisations statistiques pour intégrer l'UQ comme composante routinière de la mesure lors de l'utilisation de modèles de machine learning ou d'IA, renforçant ainsi la fiabilité et l'assurance des statistiques officielles. Le second est un programme de formation sur l'**IA responsable (RAI)**, comprenant des modules sur les fondements de l'IA responsable, les MLOps et LLMOps, et l'IA explicable (XAI), conçus pour réduire les biais, améliorer la transparence et protéger la vie privée [\[24\]](#footnote-ref-2).

### 4.2. Eurostat : Mesurer l'adoption de l'IA

Eurostat surveille activement l'adoption de l'IA dans l'Union européenne. Un rapport publié le 10 février 2026 a révélé que 63,8 % des jeunes âgés de 16 à 24 ans dans l'UE ont utilisé des outils d'IA générative en 2025 — près du double de la proportion de la population adulte globale [\[25\]](#footnote-ref-15). Une étude distincte d'Eurostat sur les types de technologies d'IA a montré que le machine learning, l'analyse prédictive, les assistants conversationnels et la vision par ordinateur sont les technologies d'IA les plus largement utilisées par les entreprises de l'UE. Ces données fournissent un contexte crucial pour les ONS lorsqu'ils envisagent comment interagir avec un public de plus en plus habitué à interagir avec l'IA.

### 4.3. U.S. Census Bureau : Mesurer l'IA dans les enquêtes auprès des entreprises

Le U.S. Census Bureau a pris des mesures concrètes pour mesurer l'impact de l'IA sur l'économie américaine en ajoutant des questions spécifiques à l'IA à son **Business Trends and Outlook Survey (BTOS)** et à l'**Annual Business Survey**. En décembre 2025, 17 % des entreprises interrogées dans le BTOS déclarent utiliser l'IA dans leurs fonctions commerciales, selon un discours du gouverneur de la Réserve fédérale, Barr [\[26\]](#footnote-ref-16). Un groupe bipartisan de sénateurs a demandé des données encore plus détaillées sur l'impact de l'IA, reflétant l'intérêt croissant des politiques pour comprendre l'adoption de l'IA dans l'économie.

### 4.4. Malaisie et autres ONS à l'UNSC57

Lors de la 57e Commission de statistique des Nations Unies, la Malaisie a souligné son adoption de solutions basées sur l'IA, y compris AgroBot sur la plateforme TaniStats 2.0, pour améliorer la collecte de données agricoles et la réactivité des utilisateurs [\[27\]](#footnote-ref-17). C'est l'un des nombreux exemples de pays en développement où les ONS commencent à exploiter les outils d'IA pour moderniser leurs processus de production statistique, même dans des environnements aux ressources limitées. Le cadre de préparation à l'IA de PARIS21 pour les ONS fournit des orientations aux offices statistiques des pays en développement sur la manière de renforcer les capacités nécessaires pour adopter l'IA de manière responsable.

### 4.5. UNICEF et l'avenir des enquêtes auprès des ménages

À l'UNSC57, l'UNICEF a organisé un événement parallèle axé sur l'avenir des enquêtes auprès des ménages, avec un accent particulier sur le programme d'enquêtes en grappes à indicateurs multiples (MICS). L'événement a mis en évidence le rôle croissant de l'IA dans la définition de l'avenir de la conception, de la collecte et de l'analyse des données d'enquêtes auprès des ménages, et a exploré comment l'IA peut être utilisée pour réduire le coût et le temps nécessaires à la production de données d'enquêtes auprès des ménages de haute qualité dans les pays à revenu faible et intermédiaire [\[28\]](#footnote-ref-18).

## 5. Conclusion

La semaine du 9 mars 2026 a été une période marquante pour l'IA dans la recherche par sondage et les statistiques officielles. La convergence de la 57e Commission de statistique des Nations Unies, la publication du programme de travail 2026 du HLG-MOS de la CEE-ONU et une vague de nouvelles publications de recherche signalent que le domaine entre dans une nouvelle phase de maturité. Les ONS passent d'expériences isolées à une intégration systématique de l'IA dans leurs flux de production statistique essentiels. Les principaux défis à venir ne sont pas principalement techniques mais institutionnels : construire les cadres de gouvernance, les normes de qualité et les capacités humaines nécessaires pour déployer l'IA de manière responsable et maintenir la confiance du public dans les statistiques officielles.

Le tableau suivant résume les principaux développements couverts dans cette mise à jour :

Développement

Organisation

Date

Signification

Séminaire sur la préparation à l'IA à l'UNSC57

UNSD

27 février 2026

Définit l'agenda pour les statistiques officielles prêtes pour l'IA à l'échelle mondiale

Programme de travail HLG-MOS 2026

CEE-ONU

Mars 2026

Lance les projets "AI-Ready Dissemination" et "Trust Matters"

GPT-4.1 pour la base de données de politique budgétaire

FMI

6 mars 2026

Démontre le LLM pour l'analyse de texte-comme-donnée à grande échelle

Estimation de l'IDH à partir de l'imagerie satellite

PNUD/Stanford/Caltech/UBC

17 février 2026

Cartographie de la pauvreté subnationale à l'aide du ML

Détection non supervisée des répondants inattentifs

NYU/Cornell

2 mars 2026

Outil d'IA évolutif pour la qualité des données d'enquête

LLM pour le codage des professions (SOCbot)

Université de Southampton

2025

Automatise le codage ISCO dans les systèmes CAPI

Questions sur l'IA dans le BTOS et l'Annual Business Survey

U.S. Census Bureau

2025–2026

Mesure l'adoption de l'IA dans l'économie américaine

63,8 % des jeunes de l'UE utilisent l'IA générative

Eurostat

10 février 2026

Contextualise la littératie en IA pour l'engagement des ONS

AgroBot pour la collecte de données agricoles

Statistics Malaysia

2026

Adoption de l'IA dans les ONS des pays en développement

## Références

1.  SAE International. (2026, February 22). _How Machine Learning is Changing Survey Sampling_. [https://sae2025.org/how-machine-learning-is-changing-survey-sampling/](https://sae2025.org/how-machine-learning-is-changing-survey-sampling/) [↑](#footnote-ref-1)
    
2.  UNECE. (2026, March). _HLG-MOS Work Programme for 2026_. [https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf](https://unece.org/sites/default/files/2026-03/HLG-MOS%20Work%20Programme%20for%202026.pdf) [↑](#footnote-ref-2)
    
3.  The Logit Group. (2026, March 5). _How AI Is Transforming Qualitative Fieldwork_. [https://logitgroup.com/ai-qualitative-fieldwork/](https://logitgroup.com/ai-qualitative-fieldwork/) [↑](#footnote-ref-3)
    
4.  JMIR Human Factors. (2026, March 6). _Mode Effects Between Telephone and Web Interviews in the Post-Pandemic Era_. [https://humanfactors.jmir.org/2026/1/e80631](https://humanfactors.jmir.org/2026/1/e80631) [↑](#footnote-ref-4)
    
5.  Triantafyllopoulos, I., & Ipeirotis, P. (2026, March 2). _Learning to Pay Attention: Unsupervised Modeling of Attentive and Inattentive Respondents in Survey Data_. arXiv:2603.02427. [https://arxiv.org/abs/2603.02427](https://arxiv.org/abs/2603.02427) [↑](#footnote-ref-5)
    
6.  Triantafyllopoulos, I., & Ipeirotis, P. (2026, March 2). _Learning to Pay Attention: Unsupervised Modeling of Attentive and Inattentive Respondents in Survey Data_. arXiv:2603.02427. [https://arxiv.org/abs/2603.02427](https://arxiv.org/abs/2603.02427) [↑](#footnote-ref-5)
    
7.  Sturgis, P., Fung, L., & Roberts, C. (2025). _Using Large Language Models to measure and classify occupations in surveys_. First Workshop on Bridging NLP and Survey Science. [https://openreview.net/forum?id=gFKPmwu2b4](https://openreview.net/forum?id=gFKPmwu2b4) [↑](#footnote-ref-6)
    
8.  Wieland, D., Leyh, N., & Ahrens, F. (2026). _From Prompts to Probes: How Large Language Models Improve Response Quality in Open-Ended Survey Research_. Hawaii International Conference on System Sciences. [https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189](https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189) [↑](#footnote-ref-7)
    
9.  PMC. (2026, March 5). _Are we reporting well enough? A systematic survey of missing data handling in RCTs_. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12961827/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12961827/) [↑](#footnote-ref-8)
    
10.  medRxiv. (2026, February 17). _A Comparative Study of DAE, SAITS, and MICE+LightGBM for Imputing Missing Data_. [https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full](https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full) [↑](#footnote-ref-9)
     
11.  Sherman, L., et al. (2026, February 17). _Global high-resolution estimates of the UN Human Development Index_. Nature Communications. [https://www.nature.com/articles/s41467-026-68805-6](https://www.nature.com/articles/s41467-026-68805-6) [↑](#footnote-ref-10)
     
12.  Phys.org. (2026, February 17). _Satellite imagery and AI reveal development needs hidden by national statistics_. [https://phys.org/news/2026-02-satellite-imagery-ai-reveal-hidden.html](https://phys.org/news/2026-02-satellite-imagery-ai-reveal-hidden.html) [↑](#footnote-ref-11)
     
13.  Das, S., Furceri, D., Patel, N., & Peralta-Alva, A. (2026, March 6). _AI Meets Fiscal Policy: Mapping Government Spending Actions Across 64 Countries_. IMF Working Paper WP/26/43. [https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286](https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286) [↑](#footnote-ref-12)
     
14.  Sturgis, P., Fung, L., & Roberts, C. (2025). _Using Large Language Models to measure and classify occupations in surveys_. First Workshop on Bridging NLP and Survey Science. [https://openreview.net/forum?id=gFKPmwu2b4](https://openreview.net/forum?id=gFKPmwu2b4) [↑](#footnote-ref-6)
     
15.  Wieland, D., Leyh, N., & Ahrens, F. (2026). _From Prompts to Probes: How Large Language Models Improve Response Quality in Open-Ended Survey Research_. Hawaii International Conference on System Sciences. [https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189](https://scholarspace.manoa.hawaii.edu/items/6c969f15-23f3-41b8-ba54-88e2c8791189) [↑](#footnote-ref-7)
     
16.  medRxiv. (2026, February 17). _A Comparative Study of DAE, SAITS, and MICE+LightGBM for Imputing Missing Data_. [https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full](https://www.medrxiv.org/content/10.64898/2026.02.10.26345979v2.full) [↑](#footnote-ref-9)
     
17.  Sherman, L., et al. (2026, February 17). _Global high-resolution estimates of the UN Human Development Index_. Nature Communications. [https://www.nature.com/articles/s41467-026-68805-6](https://www.nature.com/articles/s41467-026-68805-6) [↑](#footnote-ref-10)
     
18.  Das, S., Furceri, D., Patel, N., & Peralta-Alva, A. (2026, March 6). _AI Meets Fiscal Policy: Mapping Government Spending Actions Across 64 Countries_. IMF Working Paper WP/26/43. [https://www.imf.org/en/publications/wp/issues/2026/03/07/ai-meets-fiscal-policy-mapping-government-spending-actions-across-64-countries-574286](https://www.imf.org/en/publications/