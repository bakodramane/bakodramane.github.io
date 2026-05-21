---
layout: post
title: "IA et recherche par sondage : publications et developpements cles"
date: 2026-03-13
author: Dramane Bako
description: "La semaine dernière a été marquée par une recrudescence notable d'activités à l'intersection de l'intelligence artificielle et de la recherche par..."
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: 2026-03-13-weekly-update-on-ai-tools-for-surveys-and-administrative-data-notable-surge-of-a
permalink: /fr/2026/03/13/weekly-update-on-ai-tools-for-surveys-and-administrative-data-notable-surge-of-a/
---

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Période couverte : 09–15 mars 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes auprès des ménages, analyse de données

Résumé

La semaine dernière a été marquée par une recrudescence notable d'activités à l'intersection de l'intelligence artificielle et de la recherche par sondage. Des publications phares du FMI, d'Eurostat et du ministère indien des Statistiques, ainsi que des études évaluées par des pairs sur l'imputation basée sur les LLM et la détection de robots d'enquête, signalent collectivement que le domaine passe de l'expérimentation exploratoire au déploiement opérationnel. Parallèlement, la 57e Commission de statistique des Nations Unies et la Réunion d'experts de la CEE-ONU sur l'éthique dans les statistiques officielles ont placé la gouvernance, la confiance et l'IA responsable fermement au centre des agendas institutionnels. Ce rapport organise les développements clés de la semaine à travers le cycle de vie complet des données d'enquête.

## **Conception d'enquêtes et élaboration de questionnaires**

1.1 Conception d'instruments assistée par l'IA

Les outils d'IA générative sont de plus en plus utilisés pour rédiger, adapter et pré-tester les questionnaires d'enquête. Des chercheurs d'Unisanté ont présenté une feuille de route pour les enquêtes assistées par l'IA lors d'un colloque début mars 2026, arguant que les outils d'IA peuvent désormais être appliqués à chaque étape du processus de recherche par sondage – de la revue de la littérature et de la conception de l'étude au pré-test du questionnaire, à la collecte et à l'analyse des données [1]. La feuille de route identifie l'interrogation adaptative, où l'IA ajuste dynamiquement le routage des questions en fonction des réponses précédentes, comme une application particulièrement précieuse pour les systèmes d'entretien personnel assisté par ordinateur (CAPI) et d'entretien téléphonique assisté par ordinateur (CATI).

Séparément, une étude publiée dans le Journal of Medical Internet Research a examiné l'IA dans le développement de questionnaires médicaux, constatant que l'IA accélère considérablement le cycle de développement des instruments tout en maintenant la validité psychométrique, à condition que l'examen par des experts humains soit conservé comme étape de validation finale [2].

1.2 Le problème de la contamination par les robots d'IA

L'un des défis méthodologiques les plus pressants de la période actuelle est la contamination des panels d'enquêtes en ligne par des réponses générées par l'IA. Une correspondance publiée dans Nature en mars 2026 rapporte qu'un outil de raisonnement basé sur l'IA a été utilisé pour construire un robot qui, en 6 700 tests, a réussi les questions de vérification d'attention standard avec un taux de réussite de 99,8 % [3]. Les auteurs soutiennent que ce développement ne crée pas un nouveau problème de qualité des données, mais rend plutôt impossible d'ignorer un problème existant – celui des répondants humains négligents ou frauduleux.

Une étude distincte publiée dans l'International Journal of Social Research Methodology a examiné une attaque de robot réelle sur une enquête éducative, documentant les protocoles de nettoyage des données nécessaires pour filtrer les réponses automatisées par des robots et recommandant une approche multifacette combinant des paradata comportementales, une analyse temporelle et une vérification d'identité [4]. Parallèlement, un cadre publié dans le Journal of Consumer Research suggère que le taux réel de contamination par l'IA sur les plateformes dotées d'une vérification d'identité robuste (telles que Prolific) pourrait actuellement être proche de zéro, ce qui indique que les contrôles au niveau de la plateforme peuvent être efficaces [5].

Les implications pour les enquêtes auprès des ménages menées via des panels web sont importantes. Les offices statistiques qui s'appuient sur la collecte de données via le web devraient envisager les stratégies d'atténuation suivantes :

## **Édition et nettoyage des données**

2.1 LLM pour l'imputation des données manquantes : une évaluation à grande échelle

Une étude comparative historique soumise à arXiv le 20 mars 2026 fournit l'évaluation la plus complète à ce jour des LLM pour l'imputation des données manquantes dans les ensembles de données tabulaires [6]. L'étude, menée par Mangussi et al., a comparé cinq LLM largement utilisés à six références d'imputation de pointe sur 29 ensembles de données selon trois mécanismes de données manquantes standard : Missing Completely at Random (MCAR), Missing at Random (MAR) et Missing Not at Random (MNAR), avec des taux de données manquantes allant jusqu'à 20 %.

Les principales conclusions sont les suivantes. Sur des ensembles de données open source réels, les LLM de premier plan – en particulier Gemini 3.0 Flash et Claude 4.5 Sonnet – ont constamment surpassé les méthodes traditionnelles. Cependant, sur des ensembles de données synthétiques, les méthodes traditionnelles telles que MICE (Multiple Imputation by Chained Equations) ont conservé leur supériorité. L'étude conclut que l'efficacité des LLM en matière d'imputation estTirée du contexte sémantique et des connaissances spécifiques au domaine absorbées lors du pré-entraînement, plutôt que d'une reconstruction purement statistique. Cela signifie que les LLM sont plus précieux lorsque le modèle de données manquantes est lié à la signification substantielle des variables – une situation courante dans les enquêtes auprès des ménages couvrant le revenu, la santé et l'emploi [6].

Un compromis critique est identifié : si les LLM excellent en qualité d'imputation sur les données réelles, ils entraînent des temps de calcul et des coûts monétaires nettement plus élevés que les méthodes classiques. Pour les offices statistiques traitant des enquêtes auprès des ménages à grande échelle, ce compromis coût-qualité nécessite une évaluation minutieuse.

« Les LLM sont des imputeurs prometteurs basés sur la sémantique pour les données tabulaires complexes, mais leur avantage est étroitement lié à l'exposition préalable des modèles à des modèles spécifiques au domaine appris lors du pré-entraînement sur des corpus à l'échelle d'Internet. »

— Mangussi et al. (2026) [6]

Une étude complémentaire sur l'apprentissage en contexte pour l'imputation de données d'enquête, présentée lors d'un atelier reliant le traitement du langage naturel et les statistiques d'enquête, a démontré que les LLM peuvent être utilisés pour l'imputation multiple – générant plusieurs valeurs imputées plausibles pour tenir compte correctement de l'incertitude associée aux données manquantes – une exigence clé pour une inférence statistique valide [7].

2.2 Codage automatisé des réponses ouvertes

Le codage manuel des réponses ouvertes aux enquêtes a longtemps été un goulot d'étranglement dans le traitement des enquêtes. Les plateformes natives d'IA utilisant le traitement du langage naturel sont désormais capables d'identifier des thèmes, d'évaluer le sentiment et de corréler des résultats qualitatifs avec des variables quantitatives sur des milliers de réponses en quelques secondes. Les analyses de l'industrie suggèrent que l'IA peut réduire le cycle de codage des réponses ouvertes de cinq à sept semaines à quelques heures [8]. Pour les offices statistiques nationaux qui incluent des questions ouvertes dans les enquêtes auprès des ménages – telles que des questions sur le bien-être subjectif, les raisons de la non-participation au marché du travail ou les obstacles à l'accès aux soins de santé – cela représente un gain d'efficacité transformateur.

## **Traitement des données et analyse statistique**

3.1 Évaluation des LLM sur des microdonnées d'enquête complexes

La question de savoir si les outils d'IA peuvent générer des résultats statistiquement défendables à partir de microdonnées d'enquête complexes a été directement abordée par Mathematica dans une étude publiée le 18 mars 2026 [9]. En utilisant l'échantillon de microdonnées à usage public de l'American Community Survey, l'équipe a construit 35 tâches analytiques validées couvrant des estimations de population pondérées et des méthodes d'inférence causale, puis a comparé les résultats du modèle à des estimations de référence validées dans deux conditions : raisonnement uniquement (pas d'accès aux données) et exécution de code activée.

Les résultats sont instructifs pour toute organisation envisageant une analyse d'enquête assistée par l'IA :

L'exécution de code est fondamentale. Dans les conditions de raisonnement uniquement, les taux
