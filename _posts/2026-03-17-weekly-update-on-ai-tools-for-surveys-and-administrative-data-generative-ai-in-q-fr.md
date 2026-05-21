---
layout: post
title: "IA generative dans la conception des questionnaires"
date: 2026-03-17
author: Dramane Bako
description: "L'intégration de l'Intelligence Artificielle (IA) dans la recherche par sondage et les statistiques officielles s'est accélérée de manière significative..."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2026-03-17-weekly-update-on-ai-tools-for-surveys-and-administrative-data-generative-ai-in-q
permalink: /fr/2026/03/17/weekly-update-on-ai-tools-for-surveys-and-administrative-data-generative-ai-in-q/
---

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Période couverte : 16–22 mars 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes auprès des ménages, analyse des données

Résumé

L'intégration de l'Intelligence Artificielle (IA) dans la recherche par sondage et les statistiques officielles s'est accélérée de manière significative début 2026. Les Offices Nationaux de Statistique (ONS) et les institutions de recherche dépassent les phases expérimentales pour déployer opérationnellement des outils d'IA sur l'ensemble du cycle de vie des données d'enquête — de la conception du questionnaire et de la collecte des données à l'édition, l'analyse et la diffusion. Les développements clés de cette semaine incluent le lancement par le FMI de StatGPT pour l'interrogation structurée des statistiques officielles [1], le déploiement par le MoSPI indien d'un chatbot IA et d'un serveur de protocole de contexte de modèle (MCP) pour sa plateforme statistique nationale [2], et la publication d'un nouveau modèle d'imputation basé sur les transformeurs (NAIM) surpassant les méthodes d'apprentissage automatique classiques sur les données d'enquête tabulaires [3]. L'Open Agentic Survey Interview System (OASIS) est apparu comme un outil open-source significatif permettant des entretiens conversationnels basés sur l'IA à grande échelle [4]. Parallèlement, des organismes de gouvernance tels que l'UNECE renforcent les cadres pour une utilisation responsable de l'IA dans les statistiques officielles, tandis que le programme de formation 2026 d'Eurostat étend le renforcement des capacités en IA et apprentissage automatique pour les statisticiens [5].

En un coup d'œil : Développements clés cette semaine

## **Collecte de données et conception de questionnaires**

Les méthodes traditionnelles de collecte de données d'enquête — l'interview assistée par ordinateur en face à face (CAPI) et l'interview téléphonique assistée par ordinateur (CATI) — sont augmentées et, dans certains contextes de recherche, remplacées par des agents conversationnels basés sur l'IA. L'Open Agentic Survey Interview System (OASIS), lancé début 2026, représente une étape significative dans cette direction [4]. Construit sur les principes FAIR (Facile à trouver, Accessible, Interopérable, Réutilisable), OASIS est une plateforme entièrement open-source et auto-hébergée qui permet aux chercheurs de déployer des intervieweurs basés sur l'IA capables de mener des entretiens semi-structurés et entièrement ouverts à grande échelle. Le système prend en charge à la fois les conversations vocales en temps réel (utilisant OpenAI Realtime ou Gemini Live) et le chat textuel, avec une exploration adaptative configurable et des protocoles structurés téléchargeables via CSV ou JSON [4].

L'importance d'OASIS pour les statistiques officielles réside dans son potentiel à combler le compromis de longue date entre la profondeur et l'échelle dans la collecte de données qualitatives. La récente étude d'entretien mondial d'Anthropic auprès de 81 000 personnes — décrite comme la plus grande étude qualitative et multilingue jamais réalisée — a démontré ce potentiel, en utilisant des classificateurs basés sur Claude pour catégoriser et analyser les réponses dans 159 pays et 70 langues [6]. Pour les ONS menant des enquêtes auprès des ménages dans des environnements multilingues ou cherchant à compléter des instruments quantitatifs avec des données qualitatives plus riches, de tels outils offrent un complément méthodologique convaincant.

L'IA générative dans le développement de questionnaires

L'IA générative est de plus en plus appliquée dans la phase de conception des instruments d'enquête. Des études récentes démontrent la capacité des LLM à aider à l'élaboration d'éléments d'échelle d'enquête, à l'adaptation d'instruments validés existants et à la génération de sondes d'entretien cognitif [7]. Une recherche publiée dans Frontiers in Digital Health (2025) soutient que l'analyse sémantique basée sur l'IA peut éclairer de manière significative les méthodes qualitatives telles que l'entretien cognitif, améliorant ainsi la précision et la convivialité des éléments de questionnaire pour les répondants [8]. Le cadre de conception de questionnaire adaptatif utilisant des agents IA, développé pour le profilage des personnes, illustre en outre comment les agents IA peuvent sélectionner dynamiquement le contenu de l'enquête en fonction des caractéristiques des répondants, réduisant ainsi la longueur du questionnaire et la charge des répondants [9].

## **Édition, nettoyage et traitement des données**

Imputation basée sur les transformeurs pour les données d'enquête tabulaires

Les données manquantes restent l'un des défis les plus persistants dans l'analyse des enquêtes auprès des ménages, résultant de la non-réponse unitaire et par item, de l'attrition dans les études de panel et de la corruption des données. Une contribution méthodologique significative publiée en 2026 est NAIM (Not Another Imputation Method), un modèle basé sur les transformeurs conçu spécifiquement pour les ensembles de données tabulaires avec des valeurs manquantes [3]. Contrairement aux approches conventionnelles qui nécessitent des ensembles de données complets ou reposent sur une imputation de prétraitement, NAIM intègre des embeddings spécifiques aux caractéristiques et un mécanisme d'auto-attention masqué qui n'apprend qu'à partir des informations disponibles. Une nouvelle technique de régularisation masque aléatoirement chaque échantillon à chaque époque d'entraînement, permettant au modèle de généraliser à partir de données incomplètes. Testé par rapport à six modèles d'apprentissage automatique classiques et cinq bases de référence d'apprentissage profond sur cinq ensembles de données de classification accessibles au public, NAIM a démontré des performances supérieures, signalant un changement de paradigme dans la manière dont les données d'enquête manquantes peuvent être traitées [3].

Priorisation de l'édition des données dans les enquêtes sur les finances des ménages

Les bureaux de statistique sont confrontés à des contraintes de ressources pour examiner manuellement de grands volumes d'enregistrements d'enquête. Des approches d'apprentissage automatique sont appliquées pour développer des fonctions de score qui classent les enregistrements en fonction de leur probabilité de contenir des erreurs, permettant ainsi aux éditeurs de concentrer leur attention là où elle est le plus nécessaire [10]. Cette approche, appliquée aux enquêtes sur les finances des ménages, réduit le coût de l'édition des données tout en maintenant ou en améliorant la qualité globale des données. La méthodologie s'aligne sur le principe plus large de l'édition sélective, qui a été une priorité dans les statistiques officielles pendant des décennies, mais qui est maintenant opérationnalisée par la priorisation basée sur l'apprentissage automatique.

LLM pour le codage des réponses ouvertes aux enquêtes

Le codage des réponses ouvertes aux enquêtes — l'attribution d'étiquettes catégorielles aux réponses en texte libre — est un processus laborieux qui a historiquement nécessité des équipes de codeurs humains formés. Les LLM démontrent maintenant des performances compétitives dans ce domaine. Une recherche publiée dans Emerald Insight (2026) a révélé qu'un LLM local (Llama 3.2/3.3) pouvait classer 604 réponses ouvertes aux enquêtes avec une précision comparable à celle des codeurs humains, en utilisant des étiquettes de sentiment comme référence [11]. Séparément, des études sur la détection de la réponse à effort insuffisant (IER) montrent que les LLM peuvent identifier de manière fiable les réponses de faible qualité — telles que le texte aléatoire ou les réponses copier-coller — dans les questions ouvertes des enquêtes, améliorant ainsi la validité des ensembles de données d'enquête avant l'analyse [12].

Pour les ONS menant des enquêtes auprès des ménages à grande échelle avec des modules ouverts (par exemple, sur les raisons de la pauvreté, les comportements de recherche de soins de santé ou les expériences sur le marché du travail), ces outils offrent une voie évolutive vers un traitement systématique des données qualitatives.

## **Analyse et estimation des données**

Apprentissage automatique pour la cartographie de la pauvreté et l'estimation du bien-être

L'utilisation de l'apprentissage automatique pour estimer les indicateurs de bien-être à partir des données d'enquête — et pour combler les lacunes entre les cycles d'enquête — est un domaine actif de développement méthodologique. Un récent document de travail de la Banque mondiale évalue Random Forest comme méthodologie pour prédire la pauvreté en combinant les données actuelles de l'enquête sur la population active (EPA) avec les données précédentes de l'enquête sur les dépenses des ménages (EDM) [13
