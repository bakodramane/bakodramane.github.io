---
layout: post
title: "Weekly update on AI tools for surveys and administrative data: Generative AI in Questionnaire Development"
date: 2026-03-17
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, statistics, official-statistics, bilingual]
lang: en
---

## 🇬🇧 English

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Prepared by: Dramane Bako, Statistician/Data scientist (FAO Statistics Division, Rome, Italy)

Coverage Period: 16–22 March 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, data analysis

Executive Summary

The integration of Artificial Intelligence (AI) into survey research and official statistics has accelerated markedly in early 2026. National Statistical Offices (NSOs) and research institutions are moving beyond experimental phases into operational deployment of AI tools across the entire survey data lifecycle — from questionnaire design and data collection through editing, analysis, and dissemination. Key developments this week include the IMF's launch of StatGPT for structured querying of official statistics [1], India's MoSPI deploying an AI chatbot and Model Context Protocol (MCP) server for its national statistical platform [2], and the release of a new transformer-based imputation model (NAIM) outperforming classical machine learning methods on tabular survey data [3]. The Open Agentic Survey Interview System (OASIS) has emerged as a significant open-source tool enabling AI-powered conversational interviewing at scale [4]. Concurrently, governance bodies such as UNECE are reinforcing frameworks for responsible AI use in official statistics, while Eurostat's 2026 training programme expands capacity-building in AI and machine learning for statisticians [5].

At a Glance: Key Developments This Week

1. Data Collection and Questionnaire Design

Traditional survey data collection methods — Computer-Assisted Personal Interviewing (CAPI) and Computer-Assisted Telephone Interviewing (CATI) — are being augmented and, in some research contexts, replaced by AI-driven conversational agents. The Open Agentic Survey Interview System (OASIS), launched in early 2026, represents a significant step in this direction [4]. Built on FAIR principles (Findable, Accessible, Interoperable, Reusable), OASIS is a fully open-source, self-hosted platform that allows researchers to deploy AI-powered interviewers capable of conducting semi-structured and fully open-ended interviews at scale. The system supports both real-time voice-to-voice conversations (using OpenAI Realtime or Gemini Live) and text-based chat, with configurable adaptive follow-up probing and structured protocols uploadable via CSV or JSON [4].

The significance of OASIS for official statistics lies in its potential to bridge the longstanding tradeoff between depth and scale in qualitative data collection. Anthropic's recent 81,000-person global interview study — described as the largest and most multilingual qualitative study ever conducted — demonstrated this potential, using Claude-powered classifiers to categorize and analyze responses across 159 countries and 70 languages [6]. For NSOs conducting household surveys in multilingual environments or seeking to supplement quantitative instruments with richer qualitative data, such tools offer a compelling methodological complement.

Generative AI in Questionnaire Development

Generative AI is increasingly applied in the design phase of survey instruments. Recent studies demonstrate the capability of LLMs to assist in crafting survey scale items, adapting existing validated instruments, and generating cognitive interview probes [7]. Research published in Frontiers in Digital Health (2025) argues that AI-driven semantic analysis can meaningfully inform qualitative methods such as cognitive interviewing, thereby improving the precision and respondent-friendliness of questionnaire items [8]. The Adaptive Questionnaire Design Using AI Agents framework, developed for people profiling, further illustrates how AI agents can dynamically select survey content based on respondent characteristics, reducing questionnaire length and respondent burden [9].

2. Data Editing, Cleaning, and Processing

Transformer-Based Imputation for Tabular Survey Data

Missing data remains one of the most persistent challenges in household survey analysis, arising from unit and item non-response, attrition in panel studies, and data corruption. A significant methodological contribution published in 2026 is NAIM (Not Another Imputation Method), a transformer-based model designed specifically for tabular datasets with missing values [3]. Unlike conventional approaches that require complete datasets or rely on preprocessing imputation, NAIM integrates feature-specific embeddings and a masked self-attention mechanism that learns only from available information. A novel regularization technique randomly masks each sample at every training epoch, enabling the model to generalize from incomplete data. Tested against six classical machine learning models and five deep learning baselines across five publicly available classification datasets, NAIM demonstrated superior performance, signalling a paradigm shift in how missing survey data may be handled [3].

Prioritizing Data Editing in Household Finance Surveys

Statistical offices face resource constraints in manually reviewing large volumes of survey records. Machine learning approaches are being applied to develop score functions that rank records by their likelihood of containing errors, thereby enabling editors to focus their attention where it is most needed [10]. This approach, applied to household finance surveys, reduces the cost of data editing while maintaining or improving overall data quality. The methodology aligns with the broader principle of selective editing, which has been a priority in official statistics for decades but is now being operationalized through ML-based prioritization.

LLMs for Coding Open-Ended Survey Responses

The coding of open-ended survey responses — assigning categorical labels to free-text answers — is a labour-intensive process that has historically required teams of trained human coders. LLMs are now demonstrating competitive performance in this domain. Research published in Emerald Insight (2026) found that a local LLM (Llama 3.2/3.3) could classify 604 open-ended survey responses with accuracy comparable to human coders, using sentiment labels as a baseline [11]. Separately, studies on Insufficient Effort Responding (IER) detection show that LLMs can reliably identify low-quality responses — such as random text or copy-paste answers — in open-ended survey questions, improving the validity of survey datasets before analysis [12].

For NSOs conducting large-scale household surveys with open-ended modules (e.g., on reasons for poverty, health-seeking behaviour, or labour market experiences), these tools offer a scalable path to systematic qualitative data processing.

3. Data Analysis and Estimation

Machine Learning for Poverty Mapping and Welfare Estimation

The use of machine learning to estimate welfare indicators from survey data — and to bridge gaps between survey rounds — is an active area of methodological development. A recent World Bank working paper evaluates Random Forest as a methodology for predicting poverty by combining current Labour Force Survey (LFS) data with previous Household Expenditure Survey (HES) data [13]. The approach accurately reproduces official poverty statistics in data-scarce environments, offering a practical solution for countries that cannot afford frequent household expenditure surveys.

Complementing this, multimodal poverty mapping techniques are integrating features extracted from high-resolution satellite imagery, social media, and crowdsourced geographic information to estimate wealth indices at the village cluster level [14]. This approach, tested on 545 georeferenced clusters, demonstrates that geospatial AI can serve as a cost-effective complement to traditional household surveys for small area estimation and sub-national poverty monitoring.

Synthetic Data Generation for Survey Research

Synthetic data — artificial datasets generated to replicate the statistical properties of real survey data — is gaining traction across the research and official statistics communities. A 2025 study published in the ACM KDD proceedings evaluated four generative approaches for synthetic survey data, assessing both data utility and privacy preservation [15]. The findings indicate that well-calibrated synthetic datasets can approximate real-world results for structured, factual, and behavior-based questions, making them suitable for early-stage concept screening, persona development, and scenario modeling.

However, a 2026 analysis by Leger Research highlights important limitations: synthetic data tends to reflect average or mainstream patterns, with extreme or emotionally charged responses underrepresented; it is highly dependent on the quality and recency of training data; and traditional significance testing and confidence intervals are not directly applicable, requiring alternative validation approaches [16]. For official statistics, these limitations reinforce the view that synthetic data should complement rather than replace primary survey data collection.

4. Reporting and Dissemination

StatGPT: LLMs for Structured Querying of Official Statistics

The International Monetary Fund (IMF) has introduced StatGPT, an initiative by the IMF Statistics Department that leverages LLMs not to generate statistics, but to generate structured queries that retrieve officially published data [1]. This distinction is critical: rather than allowing an AI to fabricate statistical estimates, StatGPT interprets natural language user requests and translates them into precise database queries, directing users to authoritative sources. The initiative addresses a growing concern that conversational AI tools may produce plausible-sounding but inaccurate statistical figures, undermining public trust in official data [1].

Taylor Wilson, a commentator on NSO data lifecycles, notes that while dissemination and data access are important entry points, the real transformative potential of AI for official statistics lies in applying it throughout the entire value chain — from data collection through to analysis and reporting [17].

India's AI-Driven Statistical Ecosystem

India's MoSPI has undertaken a comprehensive AI-driven transformation of its statistical and data ecosystem, announced in March 2026 [2]. The key initiatives include:

MCP Server on e-Sankhyiki: A beta Model Context Protocol server enabling users to query 21 statistical products with over 136 million records directly through their own AI tools, without downloading large files [2].

Semantic Search: A natural language interface for the e-Sankhyiki dashboard, allowing users to explore datasets through conversational prompts [2].

Legacy Data Unlocking: AI tools to make historical statistical data accessible and searchable [2].

Singapore's DOS AI and Generative AI Playbook

The Department of Statistics Singapore (DOS) published its AI and Generative AI Playbook in February 2026, providing guidance on practical applications of AI in statistics and data analytics [18]. The playbook outlines DOS's AI journey and key considerations for responsible AI use in an official statistics context, serving as a model for other NSOs developing their own AI governance frameworks.

5. Governance, Privacy, and Responsible AI

Statistical Disclosure Control and Differential Privacy

The UNECE's SDC 2025 Report, released in March 2026, addresses the intersection of statistical disclosure control and modern privacy-enhancing technologies [19]. A key finding is that even small differential privacy budgets (below 1) may still lead to high disclosure risk in certain survey microdata contexts, underscoring the need for careful calibration of privacy parameters when releasing household survey data. The report reflects ongoing work within the international statistical community to develop practical guidance on applying differential privacy to official statistics without compromising data utility.

Responsible AI Framework for Official Statistics

The UNECE's Responsible AI for Official Statistics Framework (2025) provides a comprehensive, principle-based approach to governing the use of AI and machine learning in NSOs [20]. The framework addresses key concerns including algorithmic transparency, bias detection, human oversight, and the need for explainable AI in high-stakes statistical applications. As AI tools become embedded in core statistical production processes, adherence to such frameworks will be essential for maintaining public trust in official statistics.

6. Capacity Building and Training

Eurostat's 2026 Training Programme

Eurostat's European Statistical Training Programme (ESTP) for 2026 reflects a significant investment in AI and data science capacity for official statisticians [5]. Relevant courses include:

Artificial Intelligence and Machine Learning for Official Statistics (AIML4OS): A dedicated course covering ML techniques and their applications in official statistics, including classification, clustering, and predictive modelling.

Basic Python for Official Statistics: A five-day course in Cologne providing foundational programming skills for statistical applications.

Algorithms, Evidence and Data Science: A three-day course in The Hague covering algorithmic approaches to evidence generation.

Statistical Disclosure Control — Intermediate: A course covering privacy-preserving techniques for statistical microdata.

These offerings signal a strategic commitment by the European Statistical System to systematically build AI and data science competencies across member state NSOs.

Spotlight: Anthropic's 81,000-Person AI Interview Study

"For the first time, AI has enabled us to collect rich, open-ended interviews at extraordinary scale. We heard from people across 159 countries in 70 languages."

— Anthropic, March 2026 [6]

Anthropic's deployment of Claude as an AI conversational interviewer to conduct 80,508 interviews in one week represents a landmark demonstration of AI-enabled qualitative research at scale. The study used Claude-powered classifiers to categorize responses across multiple dimensions, and employed AI to extract representative quotes — with all responses de-identified before analysis [6]. For survey methodologists, this study raises important questions about the comparability of AI-conducted interviews with traditional human-administered surveys, the potential for response bias when respondents know they are speaking with an AI, and the appropriate use of such methods in official statistics contexts.

Resources and Tools

References

[1] StatGPT: AI for Official Statistics. (2026, March 10). International Monetary Fund. https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[2] AI-Driven Transformation of India's Statistical and Data Ecosystem. (2026, March 20). Press Information Bureau, Government of India. https://www.pib.gov.in/PressReleasePage.aspx?PRID=2242853

[3] Caruso, C. M., et al. (2026). Not another imputation method: A transformer-based model for missing values in tabular datasets. AI Open, ScienceDirect. https://www.sciencedirect.com/science/article/pii/S2666651026000057

[4] OASIS: Open Agentic Survey Interview System. (2026). https://oasis-surveys.github.io/

[5] ESTP Programme 2026. (2026). Eurostat CROS. https://cros.ec.europa.eu/book-page/estp-programme-2026

[6] What 81,000 people want from AI. (2026, March). Anthropic. https://www.anthropic.com/81k-interviews

[7] Can Generative AI Craft Variable Questions? A Mixed-Method Study on AI's Capability to Adopt, Adapt, and Create New Scales. (2025). Computers in Human Behavior. https://www.sciencedirect.com/science/article/pii/S2590291125004267

[8] Rethinking survey development in health research with AI-driven methodologies. (2025). Frontiers in Digital Health. https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2025.1636333/full

[9] Adaptive Questionnaire Design Using AI Agents for People Profiling. (2025). Semantic Scholar. https://pdfs.semanticscholar.org/6e88/bf656e0b5e20a18fd7844e4eedad0dda7604.pdf

[10] A score function to prioritize editing in household survey data: a machine learning approach. (2024). Journal of Official Statistics. https://journals.sagepub.com/doi/abs/10.1177/0282423X241309971

[11] Leveraging Local-LLM for sentiment analysis to enhance text classification of open-ended survey responses. (2026). The Electronic Library, Emerald Insight. https://www.emerald.com/el/article/doi/10.1108/EL-08-2025-0354/1348847/

[12] Using Large Language Models to Detect Insufficient Effort Responding in Open-Ended Survey Questions. (2025). ACM Digital Library. https://dl.acm.org/doi/abs/10.1145/3780045.3780059

[13] Is Random Forest a Superior Methodology for Predicting Poverty? (2026). World Bank Open Knowledge Repository. https://openknowledge.worldbank.org/entities/publication/a7fd997c-1162-52c9-8c5b-5a47c1e8513d

[14] Jung, W., et al. (2026). Multimodal poverty mapping and geographic transfer allocation. Sustainable Cities and Society, ScienceDirect. https://www.sciencedirect.com/science/article/abs/pii/S2210670726001356

[15] Jiang, Y., Liang, S., & Choi, J. (2025). Synthetic Survey Data Generation and Evaluation. ACM KDD. https://dl.acm.org/doi/abs/10.1145/3690624.3709421

[16] The Strengths and Weaknesses of Synthetic Data. (2026, March 5). Leger. https://leger360.com/market-intelligence-the-strengths-and-weaknesses-of-synthetic-data/

[17] Wilson, T. J. (2026, March). NSO Data Lifecycle Impacted by AI Tools. LinkedIn. https://www.linkedin.com/posts/taylorjameswilson_statgpt-ai-for-official-statistics-activity-7438196557495091200-EZSa

[18] DOS AI and Generative AI Playbook. (2026, February 26). Department of Statistics Singapore. https://www.singstat.gov.sg/publication-resources/dos-ai-and-generative-ai-playbook

[19] SDC 2025 Report. (2026, March). UNECE. https://unece.org/sites/default/files/2026-03/SDC%202025%20Report.pdf

[20] Modernstat — Modernization and Innovation. (2026). UNECE. https://unece.org/statistics/modernstats

This briefing is produced weekly. All developments are verified against primary sources. Feedback and contributions from the statistical community are welcome.

Contact: bakodramane@gmail.com

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d'IA pour les enquêtes et les données administratives : L'IA générative dans le développement de questionnaires**

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Préparé par : Dramane Bako, Statisticien/Scientifique des données (Division des statistiques de la FAO, Rome, Italie)

Période couverte : 16–22 mars 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes auprès des ménages, analyse des données

Résumé

L'intégration de l'Intelligence Artificielle (IA) dans la recherche par sondage et les statistiques officielles s'est accélérée de manière significative début 2026. Les Offices Nationaux de Statistique (ONS) et les institutions de recherche dépassent les phases expérimentales pour déployer opérationnellement des outils d'IA sur l'ensemble du cycle de vie des données d'enquête — de la conception du questionnaire et de la collecte des données à l'édition, l'analyse et la diffusion. Les développements clés de cette semaine incluent le lancement par le FMI de StatGPT pour l'interrogation structurée des statistiques officielles [1], le déploiement par le MoSPI indien d'un chatbot IA et d'un serveur de protocole de contexte de modèle (MCP) pour sa plateforme statistique nationale [2], et la publication d'un nouveau modèle d'imputation basé sur les transformeurs (NAIM) surpassant les méthodes d'apprentissage automatique classiques sur les données d'enquête tabulaires [3]. L'Open Agentic Survey Interview System (OASIS) est apparu comme un outil open-source significatif permettant des entretiens conversationnels basés sur l'IA à grande échelle [4]. Parallèlement, des organismes de gouvernance tels que l'UNECE renforcent les cadres pour une utilisation responsable de l'IA dans les statistiques officielles, tandis que le programme de formation 2026 d'Eurostat étend le renforcement des capacités en IA et apprentissage automatique pour les statisticiens [5].

En un coup d'œil : Développements clés cette semaine

1. Collecte de données et conception de questionnaires

Les méthodes traditionnelles de collecte de données d'enquête — l'interview assistée par ordinateur en face à face (CAPI) et l'interview téléphonique assistée par ordinateur (CATI) — sont augmentées et, dans certains contextes de recherche, remplacées par des agents conversationnels basés sur l'IA. L'Open Agentic Survey Interview System (OASIS), lancé début 2026, représente une étape significative dans cette direction [4]. Construit sur les principes FAIR (Facile à trouver, Accessible, Interopérable, Réutilisable), OASIS est une plateforme entièrement open-source et auto-hébergée qui permet aux chercheurs de déployer des intervieweurs basés sur l'IA capables de mener des entretiens semi-structurés et entièrement ouverts à grande échelle. Le système prend en charge à la fois les conversations vocales en temps réel (utilisant OpenAI Realtime ou Gemini Live) et le chat textuel, avec une exploration adaptative configurable et des protocoles structurés téléchargeables via CSV ou JSON [4].

L'importance d'OASIS pour les statistiques officielles réside dans son potentiel à combler le compromis de longue date entre la profondeur et l'échelle dans la collecte de données qualitatives. La récente étude d'entretien mondial d'Anthropic auprès de 81 000 personnes — décrite comme la plus grande étude qualitative et multilingue jamais réalisée — a démontré ce potentiel, en utilisant des classificateurs basés sur Claude pour catégoriser et analyser les réponses dans 159 pays et 70 langues [6]. Pour les ONS menant des enquêtes auprès des ménages dans des environnements multilingues ou cherchant à compléter des instruments quantitatifs avec des données qualitatives plus riches, de tels outils offrent un complément méthodologique convaincant.

L'IA générative dans le développement de questionnaires

L'IA générative est de plus en plus appliquée dans la phase de conception des instruments d'enquête. Des études récentes démontrent la capacité des LLM à aider à l'élaboration d'éléments d'échelle d'enquête, à l'adaptation d'instruments validés existants et à la génération de sondes d'entretien cognitif [7]. Une recherche publiée dans Frontiers in Digital Health (2025) soutient que l'analyse sémantique basée sur l'IA peut éclairer de manière significative les méthodes qualitatives telles que l'entretien cognitif, améliorant ainsi la précision et la convivialité des éléments de questionnaire pour les répondants [8]. Le cadre de conception de questionnaire adaptatif utilisant des agents IA, développé pour le profilage des personnes, illustre en outre comment les agents IA peuvent sélectionner dynamiquement le contenu de l'enquête en fonction des caractéristiques des répondants, réduisant ainsi la longueur du questionnaire et la charge des répondants [9].

2. Édition, nettoyage et traitement des données

Imputation basée sur les transformeurs pour les données d'enquête tabulaires

Les données manquantes restent l'un des défis les plus persistants dans l'analyse des enquêtes auprès des ménages, résultant de la non-réponse unitaire et par item, de l'attrition dans les études de panel et de la corruption des données. Une contribution méthodologique significative publiée en 2026 est NAIM (Not Another Imputation Method), un modèle basé sur les transformeurs conçu spécifiquement pour les ensembles de données tabulaires avec des valeurs manquantes [3]. Contrairement aux approches conventionnelles qui nécessitent des ensembles de données complets ou reposent sur une imputation de prétraitement, NAIM intègre des embeddings spécifiques aux caractéristiques et un mécanisme d'auto-attention masqué qui n'apprend qu'à partir des informations disponibles. Une nouvelle technique de régularisation masque aléatoirement chaque échantillon à chaque époque d'entraînement, permettant au modèle de généraliser à partir de données incomplètes. Testé par rapport à six modèles d'apprentissage automatique classiques et cinq bases de référence d'apprentissage profond sur cinq ensembles de données de classification accessibles au public, NAIM a démontré des performances supérieures, signalant un changement de paradigme dans la manière dont les données d'enquête manquantes peuvent être traitées [3].

Priorisation de l'édition des données dans les enquêtes sur les finances des ménages

Les bureaux de statistique sont confrontés à des contraintes de ressources pour examiner manuellement de grands volumes d'enregistrements d'enquête. Des approches d'apprentissage automatique sont appliquées pour développer des fonctions de score qui classent les enregistrements en fonction de leur probabilité de contenir des erreurs, permettant ainsi aux éditeurs de concentrer leur attention là où elle est le plus nécessaire [10]. Cette approche, appliquée aux enquêtes sur les finances des ménages, réduit le coût de l'édition des données tout en maintenant ou en améliorant la qualité globale des données. La méthodologie s'aligne sur le principe plus large de l'édition sélective, qui a été une priorité dans les statistiques officielles pendant des décennies, mais qui est maintenant opérationnalisée par la priorisation basée sur l'apprentissage automatique.

LLM pour le codage des réponses ouvertes aux enquêtes

Le codage des réponses ouvertes aux enquêtes — l'attribution d'étiquettes catégorielles aux réponses en texte libre — est un processus laborieux qui a historiquement nécessité des équipes de codeurs humains formés. Les LLM démontrent maintenant des performances compétitives dans ce domaine. Une recherche publiée dans Emerald Insight (2026) a révélé qu'un LLM local (Llama 3.2/3.3) pouvait classer 604 réponses ouvertes aux enquêtes avec une précision comparable à celle des codeurs humains, en utilisant des étiquettes de sentiment comme référence [11]. Séparément, des études sur la détection de la réponse à effort insuffisant (IER) montrent que les LLM peuvent identifier de manière fiable les réponses de faible qualité — telles que le texte aléatoire ou les réponses copier-coller — dans les questions ouvertes des enquêtes, améliorant ainsi la validité des ensembles de données d'enquête avant l'analyse [12].

Pour les ONS menant des enquêtes auprès des ménages à grande échelle avec des modules ouverts (par exemple, sur les raisons de la pauvreté, les comportements de recherche de soins de santé ou les expériences sur le marché du travail), ces outils offrent une voie évolutive vers un traitement systématique des données qualitatives.

3. Analyse et estimation des données

Apprentissage automatique pour la cartographie de la pauvreté et l'estimation du bien-être

L'utilisation de l'apprentissage automatique pour estimer les indicateurs de bien-être à partir des données d'enquête — et pour combler les lacunes entre les cycles d'enquête — est un domaine actif de développement méthodologique. Un récent document de travail de la Banque mondiale évalue Random Forest comme méthodologie pour prédire la pauvreté en combinant les données actuelles de l'enquête sur la population active (EPA) avec les données précédentes de l'enquête sur les dépenses des ménages (EDM) [13
