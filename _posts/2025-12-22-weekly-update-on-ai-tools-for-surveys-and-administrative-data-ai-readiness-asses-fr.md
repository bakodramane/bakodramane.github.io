---
layout: post
title: "Boite a outils d'evaluation de la preparation a l'IA pour les ONS"
date: 2025-12-22
author: Dramane Bako
description: "La mise à jour de cette semaine sur l'intelligence artificielle dans la recherche par sondage met en lumière des avancées significatives tout au long du..."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2025-12-22-weekly-update-on-ai-tools-for-surveys-and-administrative-data-ai-readiness-asses
permalink: /fr/2025/12/22/weekly-update-on-ai-tools-for-surveys-and-administrative-data-ai-readiness-asses/
---

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

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

## **Conclusion**

Les développements de la semaine dernière démontrent une tendance claire et accélérée : l'IA n'est plus une technologie périphérique dans la recherche par sondage, mais devient un composant essentiel de la collecte, du traitement et de l'analyse des données modernes. De la restauration des données historiques à la création de nouveaux indicateurs en temps réel et à l'assurance de la qualité des données, l'IA remodèle le domaine. Pour les chercheurs et les offices statistiques, le principal défi n'est plus de savoir s'il faut adopter l'IA, mais comment le faire de manière responsable, éthique et efficace.

Références

[1] Mun, S., Lee, D., Yoo, J., & Lee, S. (2025). Reweaving the Threads of Korean History: AI-Driven Restoration of the Daegu-bu Household Registers (1681–1876). Scientific Data. https://www.nature.com/articles/s41597-025-06299-5

[2] Jaworski, K. (2025). Measuring Inflation Expectations Using Artificial Intelligence. Computational Economics. https://link.springer.com/article/10.1007/s10614-025-11231-5

[3] Martherus, J., Podkul, A., Cook, E., & Liebowitz, R. (2025). How to Detect AI-assisted
