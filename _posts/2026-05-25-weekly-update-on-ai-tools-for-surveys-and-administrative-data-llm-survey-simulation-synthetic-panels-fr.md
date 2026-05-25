---
layout: post
title: "Simulation d'enquête LLM, panels synthétiques et IA tout au long du cycle de vie de l'enquête"
date: 2026-05-25
author: Dramane Bako
description: "Une nouvelle étude montre que les LLM correspondent aux moyennes des enquêtes mais échouent à reproduire l'hétérogénéité distributionnelle ; RTI décrit quatre applications de l'IA tout au long du cycle de vie de l'enquête ; l'Inde lance sa première Enquête Nationale sur le Revenu des Ménages."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2026-05-25-weekly-update-on-ai-tools-for-surveys-and-administrative-data-llm-survey-simulation-synthetic-panels
permalink: /fr/2026/05/25/weekly-update-on-ai-tools-for-surveys-and-administrative-data-llm-survey-simulation-synthetic-panels/
coverage_period: "19-25 mai 2026"
source_count: "6 développements majeurs"
key_takeaways:
  - "Une nouvelle étude démontre que les LLM peuvent correspondre aux réponses moyennes des grandes enquêtes auprès des ménages mais ne parviennent pas à reproduire l'hétérogénéité distributionnelle, les techniques de désapprentissage offrant un remède partiel."
  - "RTI International décrit quatre applications concrètes de l'IA tout au long du cycle de vie de l'enquête — codage, contrôle qualité, analyse des paradata et workflows agentiques — toutes évaluées selon le cadre Total Survey Error."
  - "Un preprint arXiv de l'Université de Floride présente un cadre d'intégration des LLM en cinq étapes pour les enquêtes de préparation aux catastrophes, montrant que l'imputation augmentée par récupération informée par la théorie surpasse les méthodes classiques."
  - "Research Live définit les panels synthétiques comme un complément, et non un substitut, à la recherche primaire, avec un consensus actuel que la technologie n'est pas encore assez mature pour des décisions à fort enjeu."
  - "Le NSO/MoSPI de l'Inde a lancé la première Enquête Nationale sur le Revenu des Ménages (NHIS) du pays, qui se déroulera d'avril 2026 à mars 2027."
  - "Un nouveau papier arXiv cartographie les perspectives des parties prenantes sur la gouvernance de l'IA à travers 10 068 contributions publiques au Plan d'action américain sur l'IA, constatant que les préoccupations des citoyens individuels sont sous-représentées."
why_it_matters: "Les développements de cette semaine relient la validité de la simulation LLM, l'intégration pratique de l'IA dans les opérations d'enquête et la gouvernance de l'IA de manière directement pertinente pour les systèmes de production statistique et les statisticiens officiels."
practical_action: "Utilisez le cadre RTI TSE comme liste de contrôle lors de l'évaluation des outils d'IA ; appliquez l'audit de biais stratifié par sous-groupes à tout flux de travail d'imputation augmenté par LLM ; et surveillez la méthodologie du NHIS indien pour en tirer des leçons sur la mesure à grande échelle des revenus des ménages."
last_updated: 2026-05-25
toc: true
---

# Simulation d’enquêtes LLM, panels synthétiques et IA tout au long du cycle de vie des enquêtes

Période de couverture : 19–25 mai 2026  
Mots-clés : outils IA, enquêtes, données administratives, large language models, statistiques officielles, panels synthétiques, simulation d’enquêtes, préparation aux catastrophes, gouvernance de l’IA, enquêtes auprès des ménages

## Principaux enseignements

- Une nouvelle étude montre que les LLM peuvent reproduire les réponses moyennes des grandes enquêtes auprès des ménages mais échouent à restituer l’hétérogénéité distributionnelle, les techniques d’« unlearning » apportant un remède partiel.  
- Le blog praticien de RTI International de mai 2026 détaille quatre applications concrètes de l’IA tout au long du cycle de vie des enquêtes — codage, contrôle qualité, analyse de paradata et workflows agentiques — toutes évaluées à l’aune du cadre Total Survey Error.  
- Un preprint de l’Université de Floride sur arXiv propose un cadre d’intégration en cinq étapes des LLM pour les enquêtes de préparation aux catastrophes, démontrant que l’imputation augmentée par récupération informée par la théorie surpasse les méthodes classiques, tout en mettant en garde contre le biais agrégé masquant des erreurs de sous-groupes.  
- Research Live définit et contextualise les panels synthétiques comme un complément — et non un substitut — à la recherche primaire, avec un consensus actuel qui considère la technologie encore immature pour des décisions à enjeux élevés.  
- Le National Statistical Office d’Inde (NSO/MoSPI) a lancé la première enquête nationale sur le revenu des ménages (NHIS), d’avril 2026 à mars 2027, visant à capter la distribution des revenus et à renforcer les politiques fondées sur les preuves.  
- Un nouvel article sur arXiv cartographie les points de vue des parties prenantes sur la gouvernance de l’IA à travers 10 068 contributions publiques au U.S. AI Action Plan, constatant une sous-représentation des préoccupations des citoyens par rapport à celles du secteur privé.

## Les LLM peuvent-ils imiter les enquêtes auprès des ménages ? Le défi distributionnel

Un working paper de Dalloul et Pfeifer (2026), résumé dans *Towards Data Science* le 20 mai 2026, évalue cinq large language models — Llama-3-8B, Llama-3-70B, Claude-3.7-Sonnet, DeepSeek-V3 et GPT-4o — sur trois grandes enquêtes d’attentes auprès des ménages : la Survey of Consumer Expectations (SCE), la Michigan Survey, et la Survey of Professional Forecasters. Le constat principal est frappant : si les LLM peuvent reproduire l’*espérance moyenne* d’inflation à un point de pourcentage près, ils compressent toute la distribution en un pic étroit. Dans les enquêtes humaines, 44 à 70 % des répondants fournissent des réponses à plus de trois points de pourcentage de la modalité dominante ; dans les échantillons LLM, cette part est quasiment nulle.

Les auteurs identifient la cause principale comme étant une fuite de données — les LLM ont mémorisé des tableaux du CPI et des agrégats d’enquêtes publiées dans leurs corpus d’entraînement, rendant les simulations incitées plus proches d’une récupération de statistiques mémorisées que d’une véritable simulation d’opinion. Deux stratégies d’« unlearning » — Gradient Ascent (GA) et Negative Preference Optimization (NPO) — sont testées comme remèdes. GA restaure substantiellement la précision distributionnelle (taux de précision dans les extrêmes passant de zéro à 97 % selon la référence SCE) et reproduit partiellement les effets de traitement dans un RCT répliqué sur les attentes d’inflation. NPO performe de manière comparable sur la distribution mais échoue à reproduire les effets de traitement.

L’implication pratique pour les chercheurs en enquêtes et statisticiens officiels est claire : les enquêtes synthétiques basées sur LLM doivent toujours rapporter le second moment en plus de la moyenne, et la précision distributionnelle ainsi que la fuite de données doivent être considérées comme des contraintes conjointes. L’article confirme que les LLM ne peuvent pas encore se substituer aux répondants réels dans les applications nécessitant une représentation hétérogène des croyances.

| Configuration LLM                        | Correspondance Mode Exacte | Précision Queue (>±3pp) | Séparation Traitement RCT |
|---------------------------------------|----------------------------|-------------------------|---------------------------|
| Baseline Llama-3                      | 92 %                      | 0 %                     | Non                       |
| Llama-3 + Gradient Ascent             | 24 %                      | 97 %                    | Oui (partiel)             |
| Llama-3 + Negative Preference Optimization | 37 %                      | 98 %                    | Non                       |
| Référence humaine SCE                 | —                         | 44 %                    | Oui                       |

## RTI International : quatre applications de l’IA tout au long du cycle de vie des enquêtes

Un blog d’expertise de RTI International publié le 22 mai 2026, signé Bollenbacher, Liao, Peytchev et Timbrook, offre un compte rendu à visée praticienne de l’intégration de l’IA dans le cycle de vie de la recherche par enquête. Le texte se distingue par son ancrage explicite dans le cadre Total Survey Error (TSE) — chaque application IA est évaluée selon son impact sur l’erreur de mesure, d’échantillonnage, de couverture, de non-réponse et de traitement avant mise en œuvre.

Les quatre cas d’usage décrits sont les suivants. D’abord, le codage assisté par IA via l’application SMART de RTI a réduit la charge de travail manuel sur la Survey of Earned Doctorates de la National Science Foundation d’environ 55 % (303 heures) entre 2022 et 2024, tout en maintenant une relecture humaine de chaque catégorie suggérée par l’IA. Ensuite, RTI QUINTET, une suite d’analyse audio par IA, a identifié 17 erreurs de formulation et une omission d’énoncé de consentement dans une enquête de santé, permettant au personnel qualité de prioriser les enregistrements problématiques sans écouter des heures d’audio. Troisièmement, l’analyse de paradata pilotée par IA permet des opérations d’enquête adaptatives — analysant en masse le timing des tentatives de contact, la durée des entretiens et les raisons de refus pour optimiser en temps réel les stratégies de sollicitation. Quatrièmement, des pilotes IA agentiques explorent des workflows multi-étapes dépassant l’assistance LLM mono-tâche, en s’appuyant sur des cadres agent commerciaux et open source pour automatiser des tâches analytiques complexes.

Le cadre humain-dans-la-boucle est mis en avant : des experts formés examinent les résultats IA, les corrigent au besoin, et affinent continuellement les modèles. Ce point de vue praticien complète la littérature méthodologique et propose un modèle pour les services statistiques envisageant l’intégration de l’IA.

## LLM tout au long du workflow d’enquête : la préparation aux catastrophes comme étude de cas

Un preprint publié sur arXiv le 19 mai 2026 (Wang, Guo et McCarty, Université de Floride) propose un cadre d’intégration en cinq étapes des LLM testé sur l’enquête de préparation à l’ouragan Milton 2024 en Floride (n=946). Les cinq étapes sont : conception du questionnaire, sélection de l’échantillon, tests pilotes, imputation des données manquantes, et analyse post-collecte. L’étude introduit un graphe de connaissances co-occurrence contraint par la Protection Motivation Theory (PMT) pour structurer la génération augmentée par récupération, testant sept configurations LLM.

Le résultat méthodologique clé est que le LLM informé par théorie marginale ancrée (A-TLM) surpasse trois méthodes classiques d’imputation — IPW/MI, MICE+PMM, et missForest — selon l’erreur quadratique moyenne (RMSE) sous conditions blocs de données manquantes non aléatoires pertinentes aux catastrophes (RMSE 1,439 contre 1,496 pour la méthode suivante), tout en obtenant un biais global proche de zéro (−0,121) comparé au plus grand biais absolu de −0,631 du random-forest imputer. Structurer la récupération autour de la causalité PMT et intégrer toute la preuve en un seul appel modèle dépasse la récupération non structurée par plus proches voisins et l’inférence séquentielle par étapes.

Un avertissement crucial est formulé : un biais agrégé proche de zéro peut masquer d’importantes erreurs opposées dans des sous-groupes. Les répondants vulnérables à facteurs combinés sont systématiquement sous-prédits dans toutes les configurations LLM. Les auteurs proposent un audit de biais stratifié par sous-groupes comme standard de rapport pour les workflows pertinents pour la politique. Un chatbot graphe de connaissances contraint par récupération démontre que le risque d’hallucination est gérable architecturale par refus fondé. Cette étude est directement pertinente pour les statisticiens officiels concevant des collectes de données augmentées par IA pour les populations difficiles à atteindre ou vulnérables.

## Panels synthétiques : complément, pas remplacement

Research Live (20 mai 2026) a publié un article explicatif sur les panels synthétiques dans sa série "Terms of Engagement". Les panels synthétiques utilisent des réponses générées par IA pour simuler les réponses humaines dans le but de modéliser, tester, prévoir ou augmenter les enquêtes. Trois approches techniques sont distinguées : génération LLM à partir d’informations publiques ; augmentation par machine learning d’un petit échantillon réel ; et IA formée sur des données propriétaires de réponses humaines pour des insights ciblés sur cohortes.

L’article souligne une distinction utile entre panels synthétiques (simulation d’un large échantillon de répondants virtuels) et personas synthétiques (représentation généralisée d’un segment de consommateurs). Hasdeep Sethi de Strat7 souligne que les données synthétiques doivent être considérées comme un complément — et non un substitut — à la recherche primaire avec des humains réels, surtout dans des enquêtes à enjeux élevés ou complexes où les risques commerciaux sont significatifs. Des tests de validation réguliers et une plus grande transparence méthodologique des fournisseurs sont identifiés comme prérequis à une adoption plus large. Ce cadrage rejoint les conclusions de Dalloul et Pfeifer (2026) et renforce la posture prudente adoptée par le groupe de travail sur l’IA responsable d’AAPOR.

## L’Inde lance la première enquête nationale sur le revenu des ménages

Le National Statistical Office indien (NSO), relevant du Ministry of Statistics and Programme Implementation (MoSPI), a annoncé le lancement de la première enquête nationale sur le revenu des ménages (NHIS), d’avril 2026 à mars 2027. L’enquête recueillera des revenus issus des salaires, de l’agriculture, des entreprises et des actifs, dans le but de renforcer l’élaboration de politiques fondées sur des preuves concernant la distribution des revenus et le bien-être. Un Technical Expert Group (TEG) a été constitué pour guider la méthodologie.

La NHIS constitue une expansion majeure de l’infrastructure d’enquêtes auprès des ménages en Inde, à un moment où les outils d’IA pour la collecte et le traitement des données se généralisent. MoSPI a également publié la bibliothèque Python eSankhyiki, permettant un accès programmatique aux indicateurs statistiques officiels sur l’emploi, les prix, l’industrie, le PIB, la santé, l’éducation, l’environnement et le commerce — un pas vers des flux statistiques plus ouverts et reproductibles.

## Gouvernance de l’IA et voix publique : quelles préoccupations sont reflétées ?

Un preprint sur arXiv (Karakanta et al., 21 mai 2026) analyse 10 068 lettres publiques soumises à l’Office of Science and Technology Policy des États-Unis dans le cadre de la consultation sur le U.S. AI Action Plan de l’administration Trump. Par modélisation de sujets et analyse de fréquences, les auteurs constatent que les citoyens individuels expriment de fortes préoccupations sur l’impact de l’IA sur la vie, l’emploi et les libertés civiles, tandis que d’autres groupes d’acteurs — le monde académique, le secteur privé, les associations — se concentrent davantage sur le développement de l’IA, la sécurité et les cadres politiques.

La comparaison des thèmes des parties prenantes avec le plan final révèle que celui-ci reflète principalement les préoccupations du secteur privé en matière de sécurité, développement et politique, les préoccupations individuelles étant moins représentées. Ce constat est directement pertinent pour la gouvernance des statistiques officielles : à mesure que les bureaux statistiques nationaux s’engagent dans des cadres de gouvernance de l’IA, il reste un défi critique d’assurer une représentation adéquate des préoccupations des personnes concernées par les données et des répondants aux enquêtes dans la conception des politiques. Le corpus et la chaîne de traitement sont disponibles publiquement, offrant une méthodologie réplicable pour l’analyse des consultations publiques sur l’IA dans d’autres contextes nationaux.

## Tableau récapitulatif : développements clés, 19–25 mai 2026

| Développement                                                        | Source                         | Pertinence                         |
|---------------------------------------------------------------------|--------------------------------|-----------------------------------|
| Les LLM reproduisent les moyennes d’enquête mais compressent les distributions ; l’unlearning restaure partiellement l’hétérogénéité | Dalloul & Pfeifer (2026), SSRN | Validité des enquêtes synthétiques, précision distributionnelle |
| RTI : quatre cas d’usage IA tout au long du cycle d’enquête évalués selon le cadre TSE | RTI International, 22 mai      | Intégration pratique de l’IA, contrôle qualité |
| Imputation LLM informée par théorie surpasse les méthodes classiques en enquête de catastrophe ; avertissement sur biais de sous-groupes | Wang et al. (2026), arXiv:2605.19229 | Données manquantes, populations vulnérables |
| Panels synthétiques définis comme complément, pas remplacement, de la recherche primaire | Research Live, 20 mai          | Simulation d’enquête, transparence fournisseurs |
| L’Inde lance la première National Household Income Survey (NHIS), avril 2026–mars 2027 | NSO/MoSPI                     | Infrastructure d’enquêtes auprès des ménages |
| U.S. AI Action Plan reflète plus les intérêts du secteur privé que ceux des individus dans 10 068 contributions publiques | Karakanta et al. (2026), arXiv:2605.22650 | Gouvernance IA, participation publique |
