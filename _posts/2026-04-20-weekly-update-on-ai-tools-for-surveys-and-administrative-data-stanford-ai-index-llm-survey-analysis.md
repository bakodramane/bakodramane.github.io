---
layout: post
title: "Weekly update on AI tools for surveys and administrative data: Stanford AI Index 2026, LLM-assisted survey analysis, and AI adoption in the US economy"
date: 2026-04-20
author: Dramane Bako
---

## 🇬🇧 English

**Weekly update on AI tools for surveys and administrative data: Stanford AI Index 2026, LLM-assisted survey analysis, and AI adoption in the US economy**

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms...) and administrative data for official statistics.

Prepared by: Dramane Bako, Statistician/Data scientist (FAO Statistics Division, Rome, Italy)

Coverage Period: 14 – 20 April 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis, AI adoption

### Key Takeaways

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

### References

[1] Inside the AI Index: 12 Takeaways from the 2026 Report. Stanford HAI. https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report
[2] Public Opinion | The 2026 AI Index Report. Stanford HAI. https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion
[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
[4] LAPS: Automating Hypothesis-Driven Statistical Analysis of Public Survey Using Large Language Models. ACM Digital Library. https://dl.acm.org/doi/full/10.1145/3772318.3791665
[5] Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions. arXiv. https://arxiv.org/html/2502.16761v2

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d'IA pour les enquêtes et les données administratives : Stanford AI Index 2026, analyse d'enquête assistée par LLM, et adoption de l'IA dans l'économie américaine**

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Préparé par : Dramane Bako, Statisticien/Data scientist (FAO Statistics Division, Rome, Italie)

Période couverte : 14 – 20 avril 2026

Mots clés : IA, recherche par enquête, statistiques officielles, apprentissage automatique, qualité des données, enquêtes ménages, méthodes statistiques, analyse de données, adoption de l'IA

### Points clés

- **Le rapport AI Index 2026 de Stanford** souligne que l'IA générative a atteint un taux d'adoption de 53 % au niveau de la population en seulement trois ans, avec 58 % des employés dans le monde déclarant utiliser l'IA au travail. Cependant, l'anxiété publique augmente, et le public américain fait état de la plus faible confiance dans son gouvernement pour réguler efficacement l'IA.
- **La Réserve fédérale** a publié une note sur le suivi de l'adoption de l'IA dans l'économie américaine, révélant que 18 % des entreprises ont adopté l'IA à la fin de l'année 2025, et que 78 % de la main-d'œuvre travaille dans des entreprises ayant adopté l'IA.
- **LAPS (LLM-Assisted Public Survey)**, un nouveau cadre automatisé, a été présenté pour soutenir une analyse statistique complète et pilotée par hypothèses des données d'enquête, réduisant la charge cognitive tout en garantissant l'autonomie du chercheur.
- **L'ajustement fin des modèles de langage sur des données d'enquête à grande échelle** (jeu de données SubPOP) démontre que le fine-tuning des LLM sur des données d'enquête structurées améliore significativement la prédiction des distributions d'opinion publique, réduisant l'écart LLM-humain jusqu'à 46 %.

### 1. Adoption de l'IA et opinion publique : enseignements du Stanford AI Index 2026

L'Institut Stanford pour l'IA centrée sur l'humain a publié en avril 2026 son très attendu **rapport AI Index 2026** [1], offrant un portrait complet et fondé sur les données du développement rapide de l'IA et de son impact sociétal. Le rapport révèle que l'IA générative a atteint un taux d'adoption de 53 % au niveau de la population en seulement trois ans, se diffusant plus rapidement que l'ordinateur personnel ou Internet.

Au travail, 58 % des employés dans le monde ont déclaré utiliser l'IA de manière semi-régulière ou régulière en 2025. Fait intéressant, l'utilisation de l'IA au travail est plus élevée dans plusieurs économies émergentes que dans de nombreux pays avancés ; dans des pays comme l'Inde, la Chine, le Nigeria, les Émirats arabes unis, l'Égypte et l'Arabie saoudite, la part dépasse 80 % [2].

Malgré cette adoption rapide, le sentiment public est complexe. Alors que 59 % des répondants mondiaux se montrent optimistes quant aux bénéfices de l'IA, 52 % rapportent que les produits d'IA les rendent nerveux. Aux États-Unis, 64 % des Américains s'attendent à ce que l'IA entraîne une diminution des emplois au cours des 20 prochaines années, et le public américain fait état de la plus faible confiance (31 %) dans son gouvernement pour réguler l'IA de manière responsable parmi tous les pays sondés [2].

### 2. Suivi de l'adoption de l'IA dans l'économie américaine

Une note récente de la Réserve fédérale a examiné les tendances d'adoption de l'IA dans l'économie américaine à partir de trois enquêtes publiques : l'enquête Business Trends and Outlook Survey (BTOS) du Census Bureau, la Real-Time Population Survey (RPS), et la Survey of Business Uncertainty (SBU) [3].

L'analyse a révélé qu'environ 18 % des entreprises américaines avaient adopté l'IA à la fin de 2025. Toutefois, pondérée par l'emploi, la SBU estime que 78 % de la main-d'œuvre travaille dans des entreprises ayant adopté l'IA, et environ 54 % dans des entreprises utilisant des modèles de langage de grande taille (LLM) [3]. Cela indique que si le nombre absolu d'entreprises adoptant l'IA est encore en croissance, les plus grands employeurs ont déjà intégré l'IA dans leurs opérations. Le rapport note également une adoption robuste de l'IA dans les secteurs de services à forte valeur ajoutée, tels que les services professionnels et la finance, suggérant que l'utilisation actuelle de l'IA est la plus répandue dans les travaux cognitifs et analytiques.

### 3. LAPS : automatisation de l'analyse statistique pilotée par hypothèses des enquêtes publiques

Un nouvel article présenté à la conférence CHI 2026 a introduit **LAPS**, un cadre automatisé assisté par LLM conçu pour soutenir une analyse statistique complète et pilotée par hypothèses des données d'enquête publique [4]. Les enquêtes publiques sont essentielles pour comprendre les dynamiques sociales, mais leur analyse impose souvent une lourde charge cognitive en raison de leur complexité structurelle.

LAPS se compose de quatre modules : Opérationnalisation, Planification, Exécution et Rapport. Il intègre des mécanismes humains dans la boucle pour équilibrer automatisation et autonomie utilisateur. Une étude utilisateur menée avec 12 chercheurs en sciences sociales a démontré que LAPS assure une stabilité analytique, réduit la charge cognitive dans le flux de travail d'analyse, et produit des résultats fiables et cohérents [4]. Cet outil représente une avancée majeure pour rendre l'analyse de données d'enquête complexes plus accessible et efficace pour les chercheurs.

### 4. Ajustement fin des LLM sur des données d'enquête à grande échelle pour la prédiction d'opinions

Des chercheurs de l'UC Berkeley et de Microsoft Research ont proposé une approche novatrice pour prédire les distributions d'opinion publique en ajustant directement les LLM sur des données d'enquête à grande échelle [5]. Ils ont constitué **SubPOP**, un jeu de données comprenant 3 362 questions et 70 000 paires sous-population-réponse issues d'enquêtes d'opinion publique bien établies.

Les méthodes antérieures tentaient de guider les LLM via l'ingénierie de prompt (en décrivant les sous-populations dans l'invite), mais ces approches peinaient à prédire fidèlement les distributions de réponses humaines. L'étude a montré que le fine-tuning sur le jeu de données SubPOP améliore considérablement la correspondance entre les prédictions des LLM et les réponses humaines à travers diverses sous-populations, réduisant l'écart LLM-humain jusqu'à 46 % par rapport aux méthodes de base [5]. Cette avancée souligne le potentiel du fine-tuning basé sur les enquêtes pour permettre des conceptions d'enquête plus efficaces et une prédiction précise des opinions pour des sous-populations diverses et réelles.

### Références

[1] Inside the AI Index: 12 Takeaways from the 2026 Report. Stanford HAI. https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report
[2] Public Opinion | The 2026 AI Index Report. Stanford HAI. https://hai.stanford.edu/ai-index/2026-ai-index-report/public-opinion
[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html
[4] LAPS: Automating Hypothesis-Driven Statistical Analysis of Public Survey Using Large Language Models. ACM Digital Library. https://dl.acm.org/doi/full/10.1145/3772318.3791665
[5] Language Model Fine-Tuning on Scaled Survey Data for Predicting Distributions of Public Opinions. arXiv. https://arxiv.org/html/2502.16761v2
