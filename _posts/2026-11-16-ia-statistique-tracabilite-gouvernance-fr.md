---
layout: post
title: "IA et statistique officielle : tracer les traitements et proportionner les contrôles"
description: "Une proposition de la CEE-ONU sur l’évaluation des systèmes d’IA et de nouveaux outils de traçabilité et de contrôle d’accès : rendre les traitements assistés par IA vérifiables."
date: 2026-11-16
lang: fr
translation_key: weekly-ai-update-2026-11-16
permalink: /fr/ia-statistique-tracabilite-gouvernance/
categories: [statistique-officielle, intelligence-artificielle]
tags: [IA, enquetes, donnees-administratives, qualite, gouvernance]
---

## Synthèse

Sept évolutions publiées du 9 au 13 novembre 2026 mettent en lumière une exigence concrète pour les instituts de statistique : pouvoir examiner les traitements assistés par IA, depuis les données d'entrée jusqu'aux résultats diffusés. Une proposition de la CEE-ONU vise à élaborer des orientations communes pour évaluer les systèmes d'IA en statistique officielle, notamment les agents ayant accès à des microdonnées confidentielles. De nouvelles fonctions permettent le classement de documents par lots, la conservation de résultats intermédiaires, la traçabilité des tables, l'investigation des anomalies et la restriction des accès. Leur maturité varie. Aucune de ces annonces ne prouve qu'une méthode produit des estimations sans biais, protège à elle seule les données confidentielles ou convient déjà à la production statistique. [1–3]

## Vue d'ensemble

| Évolution | Étape du cycle statistique | Maturité | Usage envisageable |
|---|---|---|---|
| Proposition de la CEE-ONU sur les systèmes d'IA, 13 novembre | Conception ; gouvernance | Proposition émergente | Définir l'évaluation et la supervision avant un essai d'agents |
| API asynchrone AI Functions de Databricks, 9 novembre | Acquisition ; codification | Bêta | Traiter par lots l'extraction et le classement de textes |
| Résultats nettoyés des fonctions d'IA, 9 novembre | Contrôle ; validation | Préversion publique | Séparer valeurs, erreurs et réponses brutes |
| Traçabilité des tables BigQuery, 12 novembre | Intégration ; audit | Disponibilité générale | Suivre les tables administratives jusqu'aux produits dérivés |
| Genie ZeroOps de Databricks, 12 novembre | Suivi ; validation | Bêta | Soumettre les anomalies de traitement à une enquête humaine |
| Règles ABAC `DENY` pour les objets d'IA, 12 novembre | Confidentialité ; gouvernance | Bêta | Restreindre modèles, services d'agents et compétences |
| Requêtes fédérées BigQuery, 13 novembre | Acquisition ; intégration | Préversion | Interroger des bases opérationnelles sans copie complète initiale |

## Conception et collecte : définir les preuves attendues

**Vers une évaluation commune des systèmes d'IA.** Un projet du groupe « Applying Data Science and Modern Methods » de la CEE-ONU propose un guide pratique couvrant l'évaluation de la qualité, les risques, la supervision humaine, le suivi et la confidentialité. Il décrit des applications de codification des professions et des branches d'activité déjà en production dans certains instituts, tandis que les agents travaillant sur des microdonnées confidentielles restent généralement au stade de la recherche ou de l'expérimentation. Le guide envisagé traiterait de l'évaluation répétée des systèmes à plusieurs étapes et de tests d'attaque sur des microdonnées synthétiques. Il s'agit d'une *proposition*, ni d'une norme publiée ni d'une certification. Pour un recensement agricole, ces questions peuvent déjà structurer un essai de codification : codes de référence, erreurs selon la culture et la langue, seuils d'escalade et responsable statistique désigné. [1]

**L'accès fédéré aux données administratives exige un contrôle de qualité.** BigQuery a annoncé le 13 novembre, en préversion, des connexions et des requêtes fédérées vers MySQL, Oracle et PostgreSQL. Un institut pourrait explorer une source fiscale, un répertoire d'entreprises ou des permis agricoles sur place avant de décider quelles données intégrer pour un appariement. Il s'agit d'une infrastructure utile à l'IA, et non d'un modèle d'IA. Il faut vérifier les changements de schéma, les unités, les dates de référence, les droits d'accès, la reproductibilité et les performances avant d'alimenter un traitement. La fédération ne corrige ni les défauts de couverture ni les questions relatives à la base juridique de l'utilisation statistique. [2]

## Traitement, contrôle et validation : conserver les résultats intermédiaires

**Le traitement par lots est disponible en bêta.** Annoncée le 9 novembre, l'API asynchrone AI Functions de Databricks accepte un lot JSONL de 50 000 requêtes au maximum, provenant d'un volume Unity Catalog, pour `ai_parse_document`, `ai_extract` ou `ai_classify`, et produit un résultat par requête. Un essai circonscrit pourrait codifier des réponses libres sur les professions ou les cultures, ou extraire des champs de documents administratifs. Il faut conserver un identifiant stable, le texte ou l'image d'origine, la version de la nomenclature et un échantillon de référence vérifié ; puis mesurer les erreurs et le temps de correction par langue et catégorie rare. La taille admise des lots ne renseigne pas sur la qualité statistique. [3]

**Séparer les valeurs des échecs facilite la révision.** Une fonction de Lakeflow Designer, en préversion publique depuis le 9 novembre, place les valeurs extraites, les messages d'erreur et les réponses brutes des fonctions d'IA prises en charge dans des colonnes distinctes. On peut ainsi éviter qu'un échec d'extraction devienne silencieusement une valeur manquante ou plausible. Les échecs de lecture et les valeurs logiquement impossibles devraient suivre des circuits de révision différents ; les réponses brutes et corrections humaines doivent rester consultables. Cette fonction ne met pas elle-même en œuvre les règles de contrôle d'un questionnaire. [3]

**L'investigation des incidents assistée par IA reste consultative.** Genie ZeroOps est passé en bêta le 12 novembre. Le service surveille tâches, pipelines et tables, repère des défaillances ou des problèmes de qualité, en recherche la cause probable et suggère une correction. Dans une chaîne de traitement d'enquête, une chute du nombre d'enregistrements après un appariement pourrait justifier une investigation. Toute correction proposée doit toutefois être comparée aux totaux sources, aux domaines, aux poids et aux exécutions antérieures avant validation par un agent habilité. [3]

## Intégration, confidentialité et diffusion : tracer et limiter

**La traçabilité renforce la piste d'audit.** Le suivi de la filiation des données au niveau des tables dans les pipelines BigQuery est en disponibilité générale depuis le 12 novembre. Lorsqu'une source administrative est révisée, l'équipe peut identifier les tables en amont et les produits en aval d'un indicateur assisté par IA. Cette filiation au niveau des tables n'explique cependant pas une décision du modèle pour un enregistrement particulier : versions du modèle ou des instructions, code, appariements et interventions humaines doivent être documentés séparément. [2]

**Les restrictions d'accès s'étendent aux objets d'IA.** En bêta, les règles de contrôle d'accès fondé sur les attributs ABAC `DENY` de Databricks peuvent désormais viser les services de modèles, de fournisseurs de modèles, MCP et d'agents, ainsi que les compétences, et s'attacher à des objets particuliers. Un institut pourrait empêcher un agent généraliste d'appeler un service de microdonnées confidentielles ou une compétence non approuvée. Il faut tester les droits effectifs de chaque rôle et identité de service, y compris lors d'appels indirects. Ces restrictions complètent le contrôle des sorties, la protection contre la divulgation et les tests d'injection d'instructions. [3]

## Conséquences pour les instituts de statistique

La question commune est celle de la provenance : pouvoir reconstituer quelles versions d'une source, d'un classificateur, d'une instruction, d'une règle de contrôle et d'une décision humaine ont contribué à une estimation ou à un commentaire public. Les fonctions généralement disponibles peuvent aider à tracer les opérations ; les services en préversion ou en bêta nécessitent une évaluation opérationnelle distincte. Avant tout transfert de données identifiantes vers un service hébergé, vérifier contrats, durée de conservation, lieu de traitement, journaux d'accès et règles de confidentialité. Comparer la qualité statistique à une méthode de référence tenant compte du plan de sondage et mesurer l'incidence des corrections automatiques sur les estimations. Le cadre existant de la CEE-ONU sur l'IA responsable fournit des principes utiles en attendant le guide proposé sur les agents. [1, 4]

## Prochaines actions

1. Choisir un lot limité de réponses à codifier ou de documents à analyser, puis constituer un échantillon de référence arbitré par des agents, avec catégories rares et plusieurs langues si nécessaire.
2. Conserver identifiants des sources, versions des modèles et instructions, réponses brutes, erreurs et corrections humaines pour chaque observation de l'essai.
3. Rapprocher chaque lot et chaque table dérivée des totaux d'entrée, des domaines de sondage et des indicateurs de qualité connus.
4. Tester les droits d'accès et les risques de divulgation par requêtes successives sur des microdonnées synthétiques avant tout essai sur des données confidentielles.
5. Désigner un responsable statistique pour approuver les changements, suivre les dérives et décider du passage éventuel au-delà des services en préversion ou en bêta.

## Sources

1. CEE-ONU, [projet de guide commun sur les agents d'IA pour la statistique officielle](https://unece.org/sites/default/files/2026-11/HLG2026%20ActivityProposal2027_ADSaMM_Agents%20of%20OS.pdf), répertorié le 13 novembre 2026. Proposition, et non guide achevé.
2. Google Cloud, [notes de version de BigQuery](https://docs.cloud.google.com/bigquery/docs/release-notes), annonces des 12 et 13 novembre 2026 (filiation des tables et requêtes fédérées en préversion).
3. Databricks, [notes de version de novembre 2026 pour AWS](https://docs.databricks.com/aws/en/release-notes/product/2026/november), annonces des 9 et 12 novembre 2026 (API asynchrone, résultats nettoyés, Genie ZeroOps et règles ABAC `DENY`). Déploiement progressif et disponibilité selon l'environnement cloud.
4. CEE-ONU, [cadre pour une IA responsable en statistique officielle](https://unece.org/statistics/documents/2025/10/reports/responsible-ai-official-statistics-framework), 2025. Référence de gouvernance antérieure à cette semaine.
