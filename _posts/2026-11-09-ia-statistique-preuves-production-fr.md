---
layout: post
title: "IA et statistique officielle : de l’extraction documentaire à une production maîtrisée"
date: 2026-11-09
lang: fr
translation_key: weekly-ai-update-2026-11-09
permalink: /fr/ia-statistique-preuves-production/
categories: [statistique-officielle, intelligence-artificielle]
tags: [IA, enquetes, traitement-des-donnees, imputation, gouvernance]
---

## Synthèse

Cette édition examine sept évolutions annoncées du 19 octobre au 6 novembre 2026. Des fonctions désormais disponibles pour l’analyse de documents et l’inspection d’images peuvent aider les instituts de statistique à traiter des fichiers administratifs et des questionnaires numérisés. Des fonctions bêta pourraient rendre l’extraction plus reproductible et faciliter l’examen des définitions. Les travaux récents de l’Office for National Statistics (ONS) et de la Commission économique des Nations Unies pour l’Europe (CEE-ONU) rappellent cependant que la mesure de l’IA et l’imputation par apprentissage automatique posent aussi des questions méthodologiques. La disponibilité commerciale **ne vaut pas** validation statistique : chaque usage proposé exige une comparaison contrôlée avec les méthodes établies.

## Vue d’ensemble

| Évolution | Étape du cycle | Maturité | Utilisation envisageable |
|---|---|---|---|
| BigQuery `AI.PARSE_DOCUMENT` (2 novembre) | Ingestion ; structuration | Stable (disponibilité générale) | Extraire la structure en JSON et contrôler les valeurs |
| Tâches AI Function de Databricks (4 novembre) | Nettoyage ; codification | Bêta | Traiter les nouveaux fichiers avec révision humaine |
| Inspection TIFF de Google (2 novembre) | Protection ; validation | Fonction publiée | Repérer les données sensibles dans les scans |
| Wikis Unity Catalog (6 novembre) | Intégration ; documentation | Bêta | Consigner définitions, sources et usages autorisés |
| Compétences dans Agent Registry (6 novembre) | Gouvernance ; audit | Registre stable ; chiffrement en préversion | Versionner et examiner les instructions des agents |
| Programme de mesure de l’IA de l’ONS (4–5 novembre) | Enquête ; analyse | Méthode émergente | Améliorer les questions sur l’adoption et les comptes thématiques |
| Réunion CEE-ONU sur l’édition et l’imputation (19–21 octobre) | Contrôle ; imputation | Éléments émergents | Éprouver l’inférence après imputation par apprentissage automatique |

## Collecte, intégration et documentation

**L’analyse des documents devient plus facile à intégrer aux traitements.** Le 2 novembre, Google a annoncé la disponibilité générale de `AI.PARSE_DOCUMENT` dans BigQuery. La fonction transforme en JSON les éléments de structure d’un document, notamment paragraphes, listes, tableaux et images. Pour un recensement, elle pourrait préparer le traitement de formulaires anciens ou de documents administratifs. Il faudrait toutefois comparer les valeurs extraites à un échantillon saisi et vérifié indépendamment, conserver les références aux pages et transmettre les cas atypiques aux agents. Extraire une structure ne suffit pas à déterminer le sens statistique d’une variable. [1]

**Les métadonnées peuvent être examinées au plus près des données.** Databricks a lancé en bêta les wikis Unity Catalog le 6 novembre. Les responsables de données peuvent y décrire la signification, l’usage prévu et les sources d’une table ; les utilisateurs autorisés peuvent proposer des corrections. Pour relier les bases de sondage des recensements de la population et de l’agriculture, ce dispositif pourrait documenter unités statistiques, dates de référence et règles d’appariement. Les métadonnées approuvées et leur historique doivent toutefois faire autorité. [2]

## Contrôle, codification, imputation et analyse

**Le traitement incrémental par IA peut être planifié, mais reste en bêta.** Depuis le 4 novembre, les tâches AI Function de Databricks peuvent analyser, extraire ou classer les nouveaux fichiers ou enregistrements modifiés, puis écrire les résultats dans une table régie par Unity Catalog. Un essai pourrait codifier les réponses libres sur les cultures ou les professions, en conservant texte d’origine, version du modèle, score de confiance et décision de l’agent. Il convient de mesurer précision et rappel selon la langue, la région et les catégories rares, puis de rapprocher chaque exécution du registre des entrées. [3]

**L’inférence après imputation par apprentissage automatique mérite une évaluation distincte.** La réunion d’experts de la CEE-ONU des 19–21 octobre comprenait une intervention de David Haziza sur l’inférence en présence d’une telle imputation, ainsi qu’une contribution de l’institut espagnol de statistique sur le contrôle sélectif surveillé des données catégorielles. Ces communications ne démontrent pas l’existence d’une méthode universellement prête pour la production. Dans une enquête agricole, il faudrait comparer biais, variance et couverture des intervalles à une méthode de référence tenant compte du plan de sondage, préserver les poids et documenter les hypothèses sur les non-réponses. [4]

**Mesurer l’IA devient lui-même un chantier statistique.** Dans une conférence du 4 novembre publiée le 5, l’ONS a relevé des lacunes concernant l’identification des producteurs d’IA, les applications achetées ou développées en interne, l’investissement dans les données, les changements de qualité et l’intensité d’utilisation. L’institut prévoit de poursuivre ses travaux sur un compte thématique et ses enquêtes. Un module destiné aux entreprises devrait distinguer adoption, fréquence, dépenses, développement pour compte propre et résultats observés, puis faire l’objet d’essais cognitifs. Cette conférence présente un programme de recherche, pas une nouvelle série de statistiques officielles. [5]

## Confidentialité, sécurité et diffusion responsable

**Une nouvelle possibilité de filtrage concerne les documents scannés.** Depuis le 2 novembre, Google Sensitive Data Protection peut inspecter les images TIFF, y compris les fichiers multipages de 50 pages au maximum, dans plusieurs modes d’inspection et de découverte. Cela pourrait aider à repérer des renseignements personnels dans des questionnaires de recensement numérisés avant tout accès élargi. La détection restant imparfaite, il faut tester les noms locaux, les écritures manuscrites et les langues pertinentes, puis maintenir contrôles d’accès et examen du risque de divulgation. [6]

**Les instructions réutilisables des agents disposent de contrôles renforcés.** Le 6 novembre, Google a annoncé la disponibilité générale des compétences autonomes d’Agent Registry : enregistrement, révisions immuables et informations sur l’éditeur. L’analyse de sécurité et les règles de contrôle sont également annoncées ; le chiffrement des contenus par clés gérées par le client reste en préversion. Un institut pourrait versionner les instructions approuvées pour la validation ou la diffusion et limiter l’accès aux outils. Ces contrôles ne valident pas les résultats statistiques et ne suppriment pas les risques liés aux instructions malveillantes contenues dans les documents sources. [7]

## Conséquences pour les instituts de statistique

Ces nouveautés se prêtent à des essais circonscrits et mesurables. Il faut distinguer la réussite technique — document analysé ou tâche achevée — de la qualité statistique : unités, codes, estimations et incertitude corrects. Conserver sources, versions des transformations et décisions de révision. Avant tout transfert de microdonnées confidentielles vers un service, vérifier lieu de traitement, conservation, clauses contractuelles et droits d’accès. Les chiffres publiés et leur commentaire doivent toujours relever d’un responsable statistique identifié et de contrôles reproductibles.

## Prochaines actions

1. Choisir un lot limité de documents ou de réponses libres et constituer un échantillon de référence validé par des agents.
2. Évaluer extraction ou codification par langue, sous-groupe et catégorie rare ; mesurer aussi le temps de correction et le coût total.
3. Documenter définitions, appariements et usages permis pour une intégration de données administratives.
4. Tester la détection de données sensibles sur des TIFF locaux et vérifier manuellement le risque résiduel de divulgation.
5. Concevoir un module de mesure de l’IA avec essais cognitifs, en séparant adoption et usage intensif.

## Sources

1. Google Cloud, [notes de version du 2 novembre 2026](https://docs.cloud.google.com/release-notes) — disponibilité de `AI.PARSE_DOCUMENT`.
2. Databricks, [notes de version de novembre 2026, 6 novembre](https://docs.databricks.com/gcp/en/release-notes/product/2026/november) — wikis Unity Catalog en bêta.
3. Databricks, [notes de version de novembre 2026, 4 novembre](https://docs.databricks.com/gcp/en/release-notes/product/2026/november) — tâches AI Function en bêta.
4. CEE-ONU, [réunion d’experts sur l’édition statistique, 19–21 octobre 2026](https://unece.org/statistics/events/SDE2026) — programme et communications.
5. ONS, [conférence Deane-Stone de James Benford, 4 novembre 2026](https://www.ons.gov.uk/news/news/jamesbenford2026deanestonelecturenationalinstituteofeconomicandsocialresearch4november2026), publiée le 5 novembre.
6. Google Cloud, [notes de version de Sensitive Data Protection, 2 novembre 2026](https://docs.cloud.google.com/sensitive-data-protection/docs/release-notes) — inspection TIFF.
7. Google Cloud, [notes de version du 6 novembre 2026](https://docs.cloud.google.com/release-notes) — compétences d’Agent Registry et contrôles de sécurité.
