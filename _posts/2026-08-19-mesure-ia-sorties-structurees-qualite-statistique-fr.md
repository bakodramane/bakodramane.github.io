---
layout: post
title: "Mesure de l'IA, sorties structurées et qualité statistique"
date: 2026-08-19
author: Dramane Bako
description: "Nouveautés récentes sur la mesure de l'IA, la validation et la gouvernance pour les statistiques officielles."
categories: [IA, Enquêtes, Données administratives, Statistiques officielles]
tags: [outils IA, enquêtes, recensements, données administratives, statistiques officielles]
lang: fr
translation_key: weekly-ai-update-2026-08-19
permalink: /fr/2026/08/19/mesure-ia-sorties-structurees-qualite-statistique/
---

## **Résumé exécutif**

Les développements de la semaine montrent un déplacement concret : les organisations statistiques passent des discussions générales sur l'intelligence artificielle (IA) à la mesure de son adoption, aux sorties structurées, à la diffusion traçable et à des contrôles de validation plus solides. Les nouveautés sont pertinentes pour la conception d'enquêtes, les chaînes de données administratives et la diffusion publique, mais elles doivent être testées avec prudence avant tout usage en production statistique officielle.

## **Nouveautés de la semaine**

### Conception d'enquêtes et mesure

**Produits BTOS du U.S. Census Bureau sur l'usage de l'IA, publiés le 18 juin 2026**

Le U.S. Census Bureau a publié des produits de données et des visualisations du Business Trends and Outlook Survey (BTOS) à partir de questions supplémentaires sur l'utilisation de l'IA par les entreprises. Le module couvre l'adoption de l'IA selon la branche d'activité, la géographie, la taille de l'entreprise, la fonction opérationnelle et les tâches des travailleurs, dans le cadre d'une enquête bimensuelle auprès des entreprises employeuses.

Ce point est important parce que l'adoption de l'IA devient un objet de mesure statistique, et non seulement une question technologique interne. Un cas d'usage consiste à adapter les enquêtes auprès des entreprises, de la main-d'oeuvre ou des établissements pour mesurer l'usage de l'IA par processus, territoire et classe de taille. La mise en oeuvre doit documenter le libellé des questions, les périodes de référence, les effets de mode, la comparabilité temporelle et les règles de confidentialité avant d'utiliser les résultats pour le suivi des politiques publiques.

- **Sources :** [U.S. Census Bureau, publication des données BTOS](https://www.census.gov/newsroom/press-releases/2026/btos-june-18.html) ; [page de données BTOS](https://www.census.gov/hfp/btos/data).

**Analyse de l'ONS sur l'IA dans les entreprises britanniques, publiée le 20 juillet 2026**

L'Office for National Statistics (ONS) du Royaume-Uni a publié des statistiques officielles sur l'utilisation de l'IA dans les entreprises britanniques à partir du Business Insights and Conditions Survey. La publication décrit comment les entreprises appliquent l'IA, les facteurs qui influencent son adoption et les domaines où ses effets commencent à apparaître.

Pour les offices statistiques, cette publication illustre l'intégration de l'adoption de l'IA dans une enquête récurrente auprès des entreprises plutôt que dans une enquête technologique ponctuelle. Un cas d'usage consiste à comparer les modules sur l'IA entre enquêtes économiques et registres administratifs d'entreprises. La mise en oeuvre doit harmoniser les classifications, conserver les métadonnées par vague d'enquête et éviter d'interpréter les indicateurs d'adoption comme des effets sur la productivité ou le bien-être si ces liens ne sont pas mesurés séparément.

- **Sources :** [ONS, Artificial intelligence in UK businesses: 2023 to 2026](https://www.ons.gov.uk/releases/aiinukbusinesses) ; [GOV.UK, page de statistiques officielles](https://www.gov.uk/government/statistics/ai-in-uk-businesses).

### Édition et validation

**Great Expectations 1.20.0, publié le 7 août 2026**

Great Expectations a publié la version 1.20.0 de sa bibliothèque open source de validation des données. Cette version est surtout une mise à jour de maintenance et de fiabilité, avec des corrections concernant les contextes en système de fichiers en lecture seule, les alias de métriques SQL, les attentes non satisfaites lorsqu'une colonne n'a pas de quantiles, les métriques de quantile SQLite et la promotion de `ExpectColumnValuesToMatchStrftimeFormat` parmi les attentes prises en charge.

Cet outil est utile pour la production statistique car les règles de validation constituent souvent la première ligne de défense quand des données administratives, des paradonnées d'enquête ou des sorties de modèles entrent dans une chaîne de traitement. Un cas d'usage consiste à ajouter des attentes versionnées sur les formats d'identifiants, les dates, les plages de valeurs et les seuils de valeurs manquantes avant un codage ou une imputation assistés par IA. La mise en oeuvre doit figer les versions, relancer les suites de validation existantes et maintenir une revue des lignes en erreur distincte de toute correction automatisée.

- **Sources :** [Great Expectations sur PyPI](https://pypi.org/project/great-expectations/) ; [notes de version Great Expectations 1.20.0](https://github.com/fivetran/great_expectations/releases).

### Traitement et intégration

**Transformers 5.15.0 et documentation sur l'analyse des réponses, publiés le 10 août 2026**

Hugging Face Transformers 5.15.0 a été publié sur PyPI, et la documentation du projet décrit les modèles de réponse et `parse_response()`, qui transforment les générations brutes des modèles conversationnels en dictionnaires de messages structurés. La documentation couvre aussi l'analyse de réponses en flux et le typage des arguments d'appels d'outils à partir de JSON Schema.

Ce point est pertinent lorsque des organismes testent des grands modèles de langage (large language models, LLM) pour coder des réponses textuelles, extraire des métadonnées ou orienter des enregistrements vers une revue humaine. Un cas d'usage est une chaîne de recherche contrôlée qui transforme les sorties d'un LLM en champs prédéfinis pour évaluation manuelle, plutôt qu'en texte libre. La mise en oeuvre doit traiter ces sorties comme des éléments produits par machine à valider, conserver les consignes et versions de modèles lorsque la politique le permet, et tester les erreurs silencieuses d'analyse sur les cas limites et les réponses multilingues.

- **Sources :** [Transformers sur PyPI](https://pypi.org/project/transformers/) ; [documentation Hugging Face Transformers sur l'analyse des réponses](https://huggingface.co/docs/transformers/main/chat_response_parsing).

**Documentation Gemini API sur les sorties structurées, mise à jour le 17 août 2026**

Google a mis à jour la documentation de l'API Gemini sur les sorties structurées, qui explique comment configurer les modèles pour produire des réponses conformes à un JSON Schema. La documentation cite l'extraction de données, la classification structurée et les chaînes agentiques comme cas d'usage, tout en indiquant des limites, notamment la prise en charge partielle de JSON Schema et le rejet possible de schémas trop complexes.

Pour les statistiques officielles, les sorties contraintes par schéma sont utiles pour des expérimentations de classification, d'extraction de métadonnées et de services de diffusion contrôlés. Un cas d'usage consiste à extraire des variables normalisées de documents méthodologiques publics ou à classer les questions d'utilisateurs avant leur orientation. La mise en oeuvre doit valider le sens des résultats après validation du schéma, exclure les microdonnées confidentielles, maintenir une revue humaine pour les décisions statistiques et suivre les changements d'API dans les notes de version.

- **Sources :** [sorties structurées de l'API Gemini](https://ai.google.dev/gemini-api/docs/structured-output?lang=rest) ; [notes de version de l'API Gemini](https://ai.google.dev/gemini-api/docs/changelog).

### Rapportage et diffusion

**Projet UNECE AI-Ready Dissemination et documents sur les standards, actifs en 2026**

Le High-Level Group for the Modernisation of Official Statistics de l'UNECE mène en 2026 un projet AI-Ready Dissemination centré sur la capacité des produits statistiques officiels à être découverts, tracés et cités de manière transparente par des systèmes d'IA tiers. Les documents d'atelier de 2026 couvrent aussi les standards, la gestion des métadonnées, la diffusion prête pour l'IA, SDMX, les assistants de données et les architectures statistiques fondées sur des standards.

Ce sujet compte parce que la diffusion devient un problème de machine à machine autant qu'un problème de site web pour les utilisateurs humains. Un cas d'usage consiste à vérifier si les indicateurs clés exposent des identifiants persistants, des périodes de référence, des avertissements méthodologiques, des historiques de révision et des métadonnées lisibles par machine pour les systèmes de génération augmentée par récupération. La mise en oeuvre doit privilégier les API faisant autorité, les licences claires, les règles de citation et les tests comparatifs sur la manière dont des systèmes d'IA externes retrouvent les chiffres officiels.

- **Sources :** [projet UNECE HLG-MOS AI-Ready Dissemination](https://unece.org/ru/node/395050) ; [UNECE Workshop on Supporting Standards 2026](https://unece.org/statistics/events/Standards2026).

### Gouvernance, confidentialité et IA responsable

**Cartes de modèles Google DeepMind mises à jour pour Gemini, 13 août 2026**

Google DeepMind a mis à jour son index de cartes de modèles, avec notamment une mise à jour du 13 août 2026 pour Gemini 3.7 Flash et des mises à jour de juillet 2026 pour Gemini 3.6 Flash et Gemini 3.5 Flash-Lite. Les cartes de modèles fournissent des résumés structurés sur la conception et l'évaluation de modèles avancés d'IA.

Pour les offices statistiques, l'enseignement principal relève de la gouvernance plutôt que du choix d'un modèle particulier. Un cas d'usage consiste à exiger des cartes de modèles, ou une documentation équivalente, pour tout modèle externe utilisé dans la recherche, l'édition, le codage ou la communication publique. La mise en oeuvre doit enregistrer l'identité du modèle, l'usage prévu, les éléments d'évaluation, les limites, les conditions de traitement des données, les risques résiduels et les dates de dépréciation ; une carte de modèle ne remplace pas une validation locale sur des données statistiques.

- **Source :** [cartes de modèles Google DeepMind](https://deepmind.google/models/model-cards/).

**Synthèse des National Academies sur l'AI Day for Federal Statistics 2026, mise à jour le 22 juillet 2026**

Les National Academies des États-Unis ont publié une synthèse de l'AI Day for Federal Statistics 2026, consacrée aux expérimentations d'IA dans les agences statistiques fédérales et aux besoins de garde-fous, d'évaluation, d'éthique, de transparence, de reproductibilité et de confiance publique. L'article mentionne des exemples liés à la mise en oeuvre des enquêtes, au codage de réponses textuelles et au rôle des statisticiens dans le déploiement de l'IA.

Ce point est important parce qu'il présente l'IA comme un enjeu opérationnel et de gouvernance pour les systèmes statistiques, et non comme une simple mise à jour technique. Un cas d'usage consiste à créer un comité méthodologique ou un comité de revue de l'IA pour les pilotes de codage, d'édition et de diffusion. La mise en oeuvre doit définir les droits de décision, les seuils de preuve, les traces d'audit, les contrôles de confidentialité et les procédures de retour arrière avant de passer des pilotes à la production.

- **Source :** [National Academies, Federal Statistics Enters the Age of AI - Carefully](https://www.nationalacademies.org/news/federal-statistics-enters-the-age-of-ai-carefully).

## **Implications pour les offices statistiques**

Le fil conducteur est que la préparation à l'IA dépend de la mesure, des métadonnées et des contrôles. Les offices statistiques doivent mesurer l'adoption de l'IA dans l'économie, mais ils doivent aussi rendre leurs propres produits plus faciles à citer correctement par des systèmes d'IA et plus difficiles à séparer de leurs définitions, avertissements et historiques de révision.

Les outils présentés sont utiles, mais ils ne remplacent pas la gestion de la qualité statistique. Les sorties structurées facilitent la validation des résultats de LLM, les bibliothèques de qualité des données détectent plus tôt les défaillances de chaîne, et les cartes de modèles renforcent la gouvernance et les achats. Aucune de ces mesures ne supprime la nécessité de données représentatives, de méthodes transparentes, d'une revue humaine et d'une validation locale.

## **Prochaines actions**

- Vérifier si les enquêtes auprès des entreprises incluent des questions claires et comparables sur l'adoption et les usages de l'IA.
- Ajouter des suites de validation à l'entrée des données administratives, en particulier pour les dates, identifiants, classifications, plages de valeurs et valeurs manquantes.
- Tester les sorties de LLM contraintes par schéma uniquement sur des données non confidentielles ou approuvées pour la recherche, avec revue manuelle.
- Inventorier les indicateurs publics les plus susceptibles d'être retrouvés par des systèmes d'IA et renforcer les métadonnées, citations et notes de révision.
- Exiger des cartes de modèles ou une documentation équivalente avant tout pilote avec des modèles d'IA hébergés à l'extérieur.
- Définir les seuils de preuve et les procédures de retour arrière avant d'orienter des pilotes de codage ou de diffusion assistés par IA vers la production.

## **Sources**

- [U.S. Census Bureau, Business Trends and Outlook Survey Data Release - June 18, 2026](https://www.census.gov/newsroom/press-releases/2026/btos-june-18.html)
- [U.S. Census Bureau, page de données BTOS](https://www.census.gov/hfp/btos/data)
- [ONS, Artificial intelligence in UK businesses: 2023 to 2026](https://www.ons.gov.uk/releases/aiinukbusinesses)
- [GOV.UK, AI in UK businesses](https://www.gov.uk/government/statistics/ai-in-uk-businesses)
- [Great Expectations sur PyPI](https://pypi.org/project/great-expectations/)
- [Notes de version Great Expectations 1.20.0](https://github.com/fivetran/great_expectations/releases)
- [Transformers sur PyPI](https://pypi.org/project/transformers/)
- [Documentation Hugging Face Transformers sur l'analyse des réponses](https://huggingface.co/docs/transformers/main/chat_response_parsing)
- [Sorties structurées de l'API Gemini](https://ai.google.dev/gemini-api/docs/structured-output?lang=rest)
- [Notes de version de l'API Gemini](https://ai.google.dev/gemini-api/docs/changelog)
- [Projet UNECE HLG-MOS AI-Ready Dissemination](https://unece.org/ru/node/395050)
- [UNECE Workshop on Supporting Standards 2026](https://unece.org/statistics/events/Standards2026)
- [Cartes de modèles Google DeepMind](https://deepmind.google/models/model-cards/)
- [National Academies, Federal Statistics Enters the Age of AI - Carefully](https://www.nationalacademies.org/news/federal-statistics-enters-the-age-of-ai-carefully)
