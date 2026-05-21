---
layout: post
title: "Qualite des enquetes par IA au-dela des garanties traditionnelles"
date: 2026-03-06
author: Dramane Bako
description: "Cette mise à jour hebdomadaire passe en revue les développements les plus récents dans l'application de l'intelligence artificielle (IA) à la recherche..."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2026-03-06-weekly-update-on-ai-tools-for-surveys-and-administrative-data-traditional-safegu
permalink: /fr/2026/03/06/weekly-update-on-ai-tools-for-surveys-and-administrative-data-traditional-safegu/
---

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Période couverte : 02–08 mars 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes auprès des ménages

Résumé exécutif

Cette mise à jour hebdomadaire passe en revue les développements les plus récents dans l'application de l'intelligence artificielle (IA) à la recherche par sondage et aux enquêtes auprès des ménages, couvrant l'ensemble du cycle de vie, de la conception du questionnaire et de la collecte des données au traitement, à l'analyse et à la diffusion. La période de référence a été particulièrement active, coïncidant avec la 57e session de la Commission de statistique des Nations Unies (UNSC57, 3–6 mars 2026) à New York, où la préparation à l'IA pour les données et statistiques officielles était un thème central. Les points saillants incluent un nouveau programme de travail du HLG-MOS de la CEE-ONU pour 2026 qui lance des projets dédiés à la diffusion et à la confiance prêtes pour l'IA ; un séminaire de haut niveau des Nations Unies sur la préparation à l'IA pour les statistiques officielles ; un nouveau document de travail du FMI utilisant GPT-4.1 pour construire une base de données mondiale sur la politique budgétaire ; une étude de Nature Communications combinant l'apprentissage automatique et l'imagerie satellitaire pour estimer l'Indice de développement humain à l'échelle infranationale ; et un nouveau prépublication arXiv proposant un cadre non supervisé pour détecter les répondants inattentifs aux enquêtes. Le thème général est une transition de l'expérimentation à l'institutionnalisation : les ONS passent des projets pilotes à l'intégration de l'IA dans les flux de travail de production statistique de base, tout en étant confrontés aux défis de la gouvernance, de la confiance et des capacités.

## **L'IA dans la collecte de données et le travail de terrain**

1.1. Apprentissage automatique pour l'échantillonnage d'enquête et la conception adaptative

L'utilisation de l'apprentissage automatique pour optimiser l'échantillonnage d'enquête gagne du terrain. En automatisant les processus de contrôle qualité, l'apprentissage automatique renforce la robustesse de la sélection des échantillons et des procédures de collecte de données, permettant des ajustements en temps réel des stratégies d'échantillonnage basées sur les données entrantes. Cette approche, souvent appelée conception d'enquête adaptative, permet aux gestionnaires d'enquête de réaffecter les ressources de terrain de manière dynamique, en ciblant les zones ou les sous-groupes où les taux de réponse sont faibles ou la qualité des données est médiocre.

Le HLG-MOS de la CEE-ONU a reconnu l'importance stratégique de ce domaine et lance une nouvelle activité en 2026 sur "Faire progresser la collecte de données rentable en utilisant les paradata et la conception d'enquête adaptative", proposée par le Bureau australien des statistiques (ABS). L'initiative vise à consolider les développements méthodologiques entre les ONS et à élaborer un plan pour accroître l'utilisation des paradata – données sur le processus de collecte de données lui-même – afin d'optimiser la qualité des enquêtes et l'allocation des ressources. Cela s'appuie directement sur les résultats du projet ASCENT (Advanced Survey Cost-Effectiveness with Nonresponse Treatment) et reflète l'importance croissante de l'exploitation des données opérationnelles pour une conception d'enquête fondée sur des preuves.

1.2. Travail de terrain assisté par l'IA et soutien aux enquêteurs

Une étude récente publiée dans JMIR Human Factors a examiné les effets de mode entre les entretiens téléphoniques et web, constatant que les entretiens CATI entraînaient un nombre plus élevé de symptômes rapportés par rapport aux modes web, une constatation ayant des implications importantes pour la conception d'enquêtes en mode mixte et l'interprétation des effets de mode dans le contexte des entretiens assistés par l'IA.

1.3. Détection des répondants inattentifs et de la fraude aux enquêtes

Un défi important dans la recherche par sondage est la détection des répondants inattentifs ou frauduleux qui fournissent des réponses aléatoires ou peu élaborées. Les mesures de protection traditionnelles, telles que les contrôles d'attention, sont souvent coûteuses, réactives et incohérentes. Une nouvelle prépublication soumise à arXiv le 2 mars 2026 propose un cadre unifié et sans étiquette pour la détection de l'inattention qui évalue la cohérence des réponses à l'aide de deux approches non supervisées complémentaires : la reconstruction géométrique via des Autoencodeurs et la modélisation de la dépendance probabiliste via des arbres de Chow-Liu.

"Le cadre fournit aux plateformes d'enquête un outil de diagnostic évolutif et indépendant du domaine qui lie directement la qualité des données à la conception de l'instrument, permettant un audit sans charge supplémentaire pour le répondant." — Triantafyllopoulos & Ipeirotis (2026)

La principale conclusion de l'étude est que l'efficacité de la détection est moins déterminée par la complexité du modèle que par la structure de l'enquête : les instruments avec des batteries d'éléments cohérentes et qui se chevauchent présentent de solides schémas de covariance qui permettent même aux modèles linéaires de séparer de manière fiable les répondants attentifs des inattentifs. Cela révèle un "alignement psychométrique-ML" critique : les mêmes principes de conception qui maximisent la fiabilité de la mesure maximisent également la détectabilité algorithmique.

## **L'IA dans le traitement et l'analyse des données**

2.1. Codage automatisé des réponses ouvertes

Le codage automatisé des réponses ouvertes aux enquêtes – y compris les titres de profession, les descriptions d'industrie et les réponses en texte libre – a longtemps été un objectif pour les bureaux de statistique cherchant à réduire les coûts de traitement manuel. L'avènement des puissants LLM a rendu cet objectif réalisable. Des recherches présentées lors du premier atelier sur le rapprochement du PNL et de la science des enquêtes démontrent le potentiel des LLM à coder avec précision les titres de poste et d'autres données textuelles, avec un LLM intégré directement dans le logiciel de script de questionnaire pour sonder des détails pertinents supplémentaires sur les tâches professionnelles et l'industrie avant de coder selon une classification professionnelle standard.

Une étude complémentaire publiée en 2026 examine comment le sondage contextuel basé sur les LLM peut améliorer la qualité des réponses ouvertes aux enquêtes, fournissant une validation expérimentale systématique selon laquelle les invites contextuelles basées sur les LLM augmentent le nombre et la profondeur des sujets abordés dans les réponses des répondants. Ces développements sont sur le point d'avoir un impact majeur sur la production de statistiques officielles, permettant une analyse plus détaillée et plus rapide de la dynamique du marché du travail.

2.2. Édition, imputation et contrôle qualité des données

Une étude comparative publiée dans medRxiv en février 2026 évalue trois méthodologies d'imputation des données manquantes – Denoising Autoencoders (DAE), Self-Attention-based Imputation for Time Series (SAITS) et MICE+LightGBM – constatant que les approches d'apprentissage profond offrent des avantages dans la gestion des schémas de données manquantes complexes. Ces résultats ont une pertinence directe pour les enquêtes auprès des ménages, où la non-réponse à des éléments et la non-réponse unitaire sont des défis persistants.

2.3. Apprentissage automatique pour l'analyse de la pauvreté et du bien-être

"Presque toutes les données que nous avons sur le monde sont collectées à partir d'enquêtes auprès des ménages qui sont ensuite agrégées à une zone administrative pratique... [cette étude] révèle des disparités au sein des pays que les statistiques nationales peuvent manquer." — Résumé de Phys.org de l'étude de Sherman et al. (2026)

L'étude est co-écrite avec des collaborateurs universitaires de la Stanford Doerr School of Sustainability, de Caltech et de l'Université de la Colombie-Britannique, et reflète l'investissement du Bureau du Rapport sur le Développement Humain (BRDH) dans l'innovation des indicateurs de développement humain grâce à des partenariats avec des institutions de recherche de premier plan. Les estimations sont conçues pour compléter – et non remplacer – les rapports officiels nationaux sur l'IDH.

2.4. L'IA pour l'analyse budgétaire et économique

Un nouveau
