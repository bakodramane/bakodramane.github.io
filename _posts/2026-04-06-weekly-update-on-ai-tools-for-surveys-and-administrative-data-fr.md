---
layout: post
title: "Adoption de l'IA, evaluation des LLM et StatGPT"
date: 2026-04-06
author: Dramane Bako
description: "L’adoption de l’IA dans l’économie américaine croît rapidement : Les données d’enquêtes auprès des entreprises du Census Bureau montrent qu’environ 18 %..."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2026-04-06-weekly-update-on-ai-tools-for-surveys-and-administrative-data
permalink: /fr/2026/04/06/weekly-update-on-ai-tools-for-surveys-and-administrative-data/
---

Cet article fait partie des mises à jour hebdomadaires sur les nouvelles avancées dans l’utilisation des méthodes et outils d’IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives destinées aux statistiques officielles.

Période couverte : 30 mars – 5 avril 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes ménages, méthodes statistiques, analyse de données

Points clés à retenir

L’adoption de l’IA dans l’économie américaine croît rapidement : Les données d’enquêtes auprès des entreprises du Census Bureau montrent qu’environ 18 % des entreprises ont adopté l’IA fin 2025, avec des variations significatives selon la taille et le secteur d’activité.

L’IA générative transforme la conception des enquêtes mais nécessite une supervision humaine : Bien que les outils d’IA puissent accélérer la rédaction des enquêtes et produire des brouillons solides, ils sous-estiment souvent la charge imposée aux répondants et génèrent des options de réponse erronées, rendant indispensable une revue experte.

Il est crucial d’évaluer les LLMs sur des données statistiques complexes : Les organisations doivent mettre en œuvre des cadres d’évaluation structurés pour tester les performances des LLM dans des workflows analytiques multietapes assistés par outils, car le raisonnement autonome est insuffisant pour les travaux statistiques appliqués.

Le FMI introduit StatGPT pour les statistiques officielles : StatGPT exploite les LLM pour générer des requêtes structurées via les API des agences statistiques officielles, garantissant aux utilisateurs l’accès aux chiffres publiés exacts tout en bénéficiant de l’interaction en langage naturel.

## **Traitement du langage naturel et LLM pour la conception des enquêtes**

Les chatbots d’IA générative sont de plus en plus utilisés par les chercheurs UX pour déployer rapidement des enquêtes. Lorsqu’on leur fournit un objectif de recherche clair et les meilleures pratiques de conception d’enquête, des outils comme ChatGPT et Claude peuvent générer un premier brouillon solide en quelques secondes [1]. Cependant, ces outils sous-estiment souvent la charge du répondant et peuvent produire des options de réponse défectueuses, telles que l’omission de l’option « Autre » ou la création d’échelles de notation sémantiquement déséquilibrées [1]. Par conséquent, l’expertise humaine reste essentielle pour la supervision, et les tests pilotes avec des personnes réelles sont cruciaux pour révéler des confusions ou des frictions indétectables par l’IA [1].

## **Apprentissage automatique et IA pour l’analyse, le pondération et l’estimation des données d’enquête**

À mesure que les organisations intègrent les grands modèles de langage (LLM) dans leurs workflows analytiques, il est essentiel d’évaluer leurs performances sur des données statistiques complexes. Un cadre d’évaluation récent a testé les performances des LLM dans des workflows analytiques multietapes assistés par outils utilisant des données d’enquête complexes [2]. Les résultats ont montré que l’exécution de code est fondamentale ; lorsqu’ils se limitent au seul raisonnement, les taux d’erreur sont élevés, mais la précision augmente considérablement lorsque les modèles peuvent accéder aux données et exécuter du code [2]. De plus, la compétence statistique varie significativement selon les modèles, en particulier pour les tâches d’inférence causale, ce qui souligne la nécessité de cadres d’évaluation structurés basés sur des données réelles et un usage contrôlé des outils [2].

## **IA dans les statistiques officielles et les enquêtes ménages**

L’adoption de l’IA dans l’économie américaine est étroitement suivie via diverses enquêtes. Les données d’enquêtes auprès des entreprises du Census Bureau indiquent qu’environ 18 % des entreprises ont adopté l’IA fin 2025 [3]. L’enquête Real-Time Population Survey rapporte que l’adoption de l’IA générative liée au travail atteint environ 41 % en novembre 2025 [3]. Ces enquêtes révèlent également une hétérogénéité considérable selon la taille des entreprises et les secteurs, avec une adoption robuste dans les secteurs des services à forte valeur ajoutée, suggérant que l’utilisation actuelle de l’IA est la plus répandue dans les tâches cognitives et analytiques [3].

Dans le domaine des statistiques officielles, le FMI a lancé StatGPT, une initiative qui exploite les LLM pour générer des requêtes structurées via les API des agences statistiques officielles [4]. Cette approche garantit que les utilisateurs reçoivent les chiffres publiés exacts tout en bénéficiant d’une interaction en langage naturel, surpassant les limitations des applications GenAI prêtes à l’emploi qui fournissent fréquemment des chiffres erronés [4].

Par ailleurs, le Committee on National Statistics, le Federal Committee on Statistical Methodology et le National Institute of Statistical Sciences organisent un second AI Day pour les statistiques fédérales le 30 avril 2026 [5]. Cet atelier explorera les implications de l’IA pour les statistiques fédérales, offrant des opportunités de formation, de renforcement des capacités et de partage des meilleures pratiques pour utiliser l’IA afin d’améliorer l’efficacité gouvernementale et moderniser la main-d’œuvre fédérale [5].

Références

[1] AI Can Help with Survey Writing, But It Still Requires Human Expertise. Nielsen Norman Group. https://www.nngroup.com/articles/ai-survey-writing/

[2] Trusting your LLM: AI’s handling of complex statistical data. Mathematica. https://www.mathematica.org/blogs/trusting-your-llm

[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

[4] StatGPT: AI for Official Statistics. International Monetary Fund. https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[5] AI Day for Federal Statistics 2026. Population Association of America. https://www.populationassociation.org/events/event-description?CalendarEventKey=f26dfb08-99f4-42fa-921a-019cb515a57b&Home=%2Fhome

Contact: bakodramane@gmail.com
