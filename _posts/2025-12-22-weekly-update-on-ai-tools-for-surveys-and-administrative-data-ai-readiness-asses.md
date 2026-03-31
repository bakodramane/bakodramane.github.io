---
layout: post
title: "Weekly update on AI tools for surveys and administrative data: AI Readiness Assessment Toolkit to help NSOs benchmark their progress"
date: 2025-12-22
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, statistics, official-statistics, bilingual]
lang: en
---

## 🇬🇧 English

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Prepared by: Dramane Bako, Statistician/Data scientist (FAO Statistics Division, Rome, Italy)

Coverage Period: 22–28 December 2025

Key words: AI, survey research, official statistics, machine learning, data quality, automation, household surveys, data analysis

Executive Summary

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

Conclusion

The developments of the past week demonstrate a clear and accelerating trend: AI is no longer a peripheral technology in survey research but is becoming a core component of modern data collection, processing, and analysis. From restoring historical data to creating new real-time indicators and ensuring data quality, AI is reshaping the field. For researchers and statistical offices, the key challenge is no longer whether to adopt AI, but how to do so responsibly, ethically, and effectively.

References

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

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d'IA pour les enquêtes et les données administratives : Kit d'évaluation de la préparation à l'IA pour aider les ONS à évaluer leurs progrès**

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Préparé par : Dramane Bako, Statisticien/Scientifique des données (Division des statistiques de la FAO, Rome, Italie)

Période couverte : 22–28 décembre 2025

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, automatisation, enquêtes auprès des ménages, analyse de données

Résumé

La mise à jour de cette semaine sur l'intelligence artificielle dans la recherche par sondage met en lumière des avancées significatives tout au long du cycle de vie de l'enquête, du nettoyage et de la collecte des données à l'analyse et à la diffusion. Les développements clés incluent l'utilisation de grands modèles linguistiques (LLM) pour la restauration des données et comme remplacement des méthodes d'enquête traditionnelles, de nouveaux cadres pour détecter les réponses d'enquête générées par l'IA, et la publication de guides complets de préparation à l'IA pour les offices nationaux de statistique. Ces tendances indiquent une maturation rapide des applications de l'IA dans le domaine, passant d'utilisations expérimentales à des systèmes intégrés de niveau production.

Une étude révolutionnaire publiée dans Nature Scientific Data démontre la puissance des modèles linguistiques masqués (MLM) comme BERT et RoBERTa pour la restauration de données historiques d'enquêtes auprès des ménages [1]. La recherche, axée sur les registres des ménages de Daegu-bu de 1681 à 1876, a utilisé une méthodologie en deux étapes impliquant un nettoyage complet des données suivi d'une analyse basée sur l'IA pour automatiser la reconstruction des valeurs manquantes et mal interprétées. Cette approche a des implications significatives pour la recherche par sondage moderne, offrant un cadre robuste pour la gestion des enregistrements d'enquête incomplets ou endommagés et l'automatisation des contrôles de qualité des données.

Une recherche publiée dans Computational Economics met en évidence le potentiel de l'IA à remplacer ou à augmenter entièrement les méthodes d'enquête traditionnelles [2]. L'étude utilise des LLM pour extraire les attentes d'inflation directement du discours public d'experts économiques sur les plateformes de médias sociaux comme Twitter. Cette approche basée sur l'IA permet une mesure en temps réel des indicateurs économiques sans avoir besoin d'enquêtes coûteuses et chronophages, offrant une actualité et une fréquence améliorées. La méthodologie est suffisamment sophistiquée pour distinguer les perceptions de l'inflation passée des véritables attentes prospectives, une limitation des techniques d'analyse de sentiment plus simples. Ce développement signale un changement de paradigme où l'IA peut générer des données équivalentes à celles d'une enquête à partir du discours en ligne existant, réduisant ainsi le fardeau des répondants et offrant une alternative rentable pour la collecte de données à haute fréquence.

Assurer la qualité des données à l'ère de l'IA

À mesure que l'IA devient plus performante, garantir la qualité et l'authenticité des données d'enquête est une préoccupation croissante. Une étude publiée dans Survey Practice a évalué la capacité de l'outil d'IA agentique d'OpenAI, Operator, à compléter des enquêtes en ligne et a étudié des méthodes pour détecter de telles réponses assistées par l'IA [3]. La recherche a révélé que si les méthodes traditionnelles comme les contrôles d'attention et les questions pièges sont largement inefficaces contre les agents d'IA modernes, d'autres indicateurs peuvent les identifier de manière fiable.

Ces résultats soulignent le besoin urgent pour les chercheurs en sondage et les offices statistiques de développer et d'adapter de nouveaux mécanismes de contrôle de la qualité pour l'ère de l'IA.

Préparation et adoption institutionnelle de l'IA

Reconnaissant l'importance croissante de l'IA, plusieurs organisations ont publié des directives et lancé des programmes pour promouvoir la préparation à l'IA.

PARIS21 a lancé un cadre complet pour aider les offices nationaux de statistique (ONS), en particulier dans les pays à revenu faible et intermédiaire, à devenir « prêts pour l'IA » [4]. Le cadre SPEED (State, Policy, Expertise, Engine, and Delivery) fournit une feuille de route pour une adoption responsable de l'IA, abordant des défis tels que les infrastructures faibles, les budgets limités et le besoin d'expertise technique. Il comprend un prochain kit d'évaluation de la préparation à l'IA pour aider les ONS à évaluer leurs progrès.

Aux États-Unis, le Bureau du recensement a mis à jour son enquête sur les tendances et les perspectives commerciales (BTOS) pour inclure de nouvelles questions fondamentales sur l'adoption de l'IA [8]. Cela représente le premier effort gouvernemental systématique et à grande échelle pour suivre l'impact économique de l'IA à travers les statistiques officielles. Les premières données montrent déjà une augmentation significative de l'utilisation de l'IA parmi les entreprises américaines, passant de 3,7 % fin 2024 à 10 % en septembre 2025.

Pendant ce temps, l'Office for National Statistics (ONS) du Royaume-Uni envisage de rendre certaines enquêtes auprès des ménages obligatoires pour lutter contre la baisse des taux de réponse [9]. Cette crise des données souligne l'urgence de méthodes améliorées par l'IA qui peuvent améliorer l'engagement et réduire le fardeau des répondants, offrant une solution plus durable que les mandats légaux.

Outils et plateformes d'IA émergents

Le marché des outils d'enquête basés sur l'IA se développe rapidement. Artemis, un nouvel assistant d'enquête IA de ngSurvey, illustre la tendance à l'automatisation de bout en bout [6]. Il offre des capacités couvrant l'ensemble du cycle de vie de l'enquête :

Analyse des données : Fournit des informations complètes, une analyse des tendances et un filtrage des données sans effort.

Informations sur le texte ouvert : Utilise une catégorisation approfondie et une analyse des sentiments pour extraire des informations exploitables de milliers de commentaires ouverts dans n'importe quelle langue.

Rapports : Génère des résumés exécutifs et des rapports prêts à être présentés en quelques minutes.

Les plateformes établies intègrent également l'IA. La revue de l'année 2025 de SurveyCTO met en évidence un changement majeur vers une plus grande automatisation et interopérabilité, stimulée par l'IA [10]. La plateforme propose désormais des transferts de données activés par API, des ensembles de données dynamiques basés sur le cloud et des capacités avancées pour la collecte de données géospatiales et la gestion des cas hors ligne.

IA préservant la confidentialité

Alors que l'accessibilité des données devient une priorité en vertu de nouvelles réglementations comme le U.S. Evidence Act, la protection de la vie privée des répondants est primordiale. Un article sur arXiv détaille le développement de CenSyn, un cadre d'apprentissage automatique pour la création d'échantillons de microdonnées à usage public (PUMS) synthétiques pour les enquêtes commerciales du Bureau du recensement des États-Unis [5]. Cette approche génère des données artificielles qui préservent les propriétés statistiques des données originales à usage restreint sans contenir d'enregistrements individuels ou commerciaux réels. Cela permet un accès public plus large à des données précieuses pour la recherche et l'élaboration des politiques tout en respectant des exigences strictes de confidentialité.

Conclusion

Les développements de la semaine dernière démontrent une tendance claire et accélérée : l'IA n'est plus une technologie périphérique dans la recherche par sondage, mais devient un composant essentiel de la collecte, du traitement et de l'analyse des données modernes. De la restauration des données historiques à la création de nouveaux indicateurs en temps réel et à l'assurance de la qualité des données, l'IA remodèle le domaine. Pour les chercheurs et les offices statistiques, le principal défi n'est plus de savoir s'il faut adopter l'IA, mais comment le faire de manière responsable, éthique et efficace.

Références

[1] Mun, S., Lee, D., Yoo, J., & Lee, S. (2025). Reweaving the Threads of Korean History: AI-Driven Restoration of the Daegu-bu Household Registers (1681–1876). Scientific Data. https://www.nature.com/articles/s41597-025-06299-5

[2] Jaworski, K. (2025). Measuring Inflation Expectations Using Artificial Intelligence. Computational Economics. https://link.springer.com/article/10.1007/s10614-025-11231-5

[3] Martherus, J., Podkul, A., Cook, E., & Liebowitz, R. (2025). How to Detect AI-assisted
