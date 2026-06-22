---
layout: post
title: "Rendre interrogeables les directives du PMRA 2030 : construire un explorateur hors ligne"
lang: fr
translation_key: wca-2030-offline-explorer
date: 2026-06-22
permalink: /fr/2026/06/22/pmra-2030-explorateur-hors-ligne/
categories: [projects]
tags: [wca-2030]
published: false
description: "Pourquoi j'ai construit un explorateur hors ligne, fondé sur la citation, pour les directives du Programme mondial du recensement de l'agriculture 2030 de la FAO, et ce que cela signifie pour les équipes de méthodologie du recensement."
key_takeaways:
  - "Les directives du PMRA 2030 constituent la norme internationale pour le cycle de recensement 2026–2035 ; le problème concret du méthodologue est de localiser et de citer la recommandation exacte, et non l'absence d'orientation."
  - "L'Explorateur PMRA 2030 renvoie le texte mot pour mot, accompagné de sa référence de section et de page, et ne génère ni ne reformule jamais une réponse : la norme est citée plutôt qu'approchée."
  - "Le concevoir « hors ligne d'abord » permet à un méthodologue d'un institut national de statistique de l'utiliser sans connexion, sans transmettre de documents de recensement à un service externe, et sans coût par requête."
why_it_matters: >
  Un recensement de l'agriculture est un engagement décennal. Les directives qui le façonnent méritent un
  outil qui fasse remonter la formulation exacte dont un méthodologue a besoin pour défendre un choix de
  conception, avec une référence attachée, afin que les revues et les audits reposent sur la source plutôt
  que sur la mémoire.
practical_action: >
  Si votre institut prépare le cycle 2030, traitez les directives comme une référence que l'on interroge
  en continu plutôt que comme un document que l'on lit une seule fois. Une couche de recherche fondée sur
  la citation, posée sur la norme, raccourcit les revues de conception et ancre les adaptations nationales
  au texte international.
---

<!-- NOTE : vérifier que ces clés de front matter correspondent à un article existant avant publication. Passer `published` à true lorsque l'article est prêt. -->

Le Programme mondial du recensement de l'agriculture 2030 de la FAO fixe la norme méthodologique internationale pour les recensements agricoles nationaux du onzième cycle décennal, qui couvre la période de 2026 à 2035. Il porte des décennies de pratique accumulée : un dénombrement complet des éléments structurels au moins une fois par décennie, complété par des enquêtes intercensitaires régulières qui utilisent le recensement comme base de sondage, ainsi que des orientations élargies sur le géoréférencement, la collecte assistée par ordinateur, l'observation de la Terre, et le rôle de l'intelligence artificielle dans les opérations de recensement.

Il est aussi volumineux. Un méthodologue national qui s'installe pour concevoir un recensement a rarement besoin du document entier. Il a besoin d'une chose précise : la définition recommandée d'une exploitation du secteur non ménager, les conditions d'application d'un plan à double base de sondage, l'approche révisée de la mesure des rôles selon le genre au sein de l'exploitation, ou le seuil exact qu'attache une notion. Trouver ce paragraphe précis, puis le citer fidèlement dans une note de conception, voilà où se loge la véritable friction.

## La friction que j'ai vue se répéter

Dans les équipes de statistique agricole avec lesquelles je travaille, le schéma se répète. Quelqu'un rédige un plan de sondage ou une spécification de tableaux, se souvient que les directives disent quelque chose de pertinent, et passe vingt minutes à parcourir un PDF de plusieurs centaines de pages pour le retrouver. Une fois le passage trouvé, il le reformule de mémoire dans sa note, et la paraphrase s'éloigne silencieusement de la source. Au moment de la revue, le relecteur débat de la paraphrase plutôt que de la norme.

Pour un document normatif, c'est cette dérive qu'il vaut la peine de résoudre. Une norme de recensement ne fonctionne que si les personnes qui l'appliquent peuvent la citer exactement et indiquer où elle se trouve.

## Ce que j'ai construit

L'[Explorateur PMRA 2030](https://github.com/bakodramane/WCA_2030_Explorer) est un petit outil à la promesse délibérément étroite. Vous posez une question en langage courant, et il renvoie des passages des directives mot pour mot, chacun étiqueté de sa section et de sa page. Il ne résume pas, ne reformule pas, et ne compose pas de réponse de son cru. Le texte que vous lisez est le texte de la norme, et la référence vous indique où le vérifier.

Deux choix de conception définissent l'outil.

**Mot pour mot et référencé, par construction.** L'Explorateur ne génère jamais de prose. C'est une contrainte que j'ai intégrée plutôt qu'une limite que j'ai tolérée. Lorsqu'il s'agit d'une norme internationale, une réponse plausible mais qui reformule subtilement la règle est pire que pas de réponse du tout, car elle invite un méthodologue à agir sur une version de l'orientation que le document ne contient pas. Renvoyer la formulation exacte, avec sa page, maintient l'humain en position d'interpréter la source plutôt que de se fier à un intermédiaire.

**Hors ligne d'abord.** L'Explorateur est une application web progressive qui s'exécute entièrement dans le navigateur, sans appel à un serveur une fois chargée. C'est déterminant pour les instituts les plus susceptibles de l'utiliser. Un méthodologue qui prépare un recensement à Ouagadougou, Bamako, Monrovia ou Freetown ne devrait pas dépendre d'une connexion stable, ni d'une autorisation d'envoyer des projets de documents à un service externe, pour consulter une recommandation. L'exécution locale signifie aussi l'absence de coût par requête, ce qui garde l'outil utilisable par toute une équipe au lieu d'être rationné.

## Le fonctionnement, sous le capot

La couche de recherche combine deux méthodes complémentaires. Un index lexical construit avec MiniSearch et un classement BM25 traite les requêtes où l'utilisateur connaît déjà le bon vocabulaire, ce qui est fréquent chez les statisticiens cherchant un terme défini. À ses côtés, des plongements sémantiques générés dans le navigateur avec Transformers.js, compilé en WebAssembly, captent les requêtes formulées en langage courant qui ne correspondent pas à la terminologie du document. L'ensemble est empaqueté avec Vite et livré sous forme de fichiers statiques.

L'objectif technique, tout au long, était de garder le modèle honnête sur ses limites. Les plongements décident quels passages sont les plus pertinents ; ils n'écrivent jamais la réponse.

## Leçons pour les équipes de méthodologie du recensement

Quelques constats se sont dégagés en construisant cet outil et dépassent l'outil lui-même.

Une norme ne vaut que par sa facilité d'accès. Investir dans la manière dont les équipes trouvent et citent les directives se rembourse à chaque revue de conception d'un cycle de recensement. Traiter le document comme une infrastructure interrogeable change la fréquence à laquelle on le consulte réellement.

Les références sont un mécanisme de confiance, et non une formalité. Lorsque chaque passage porte sa source, une revue de conception avance vite, car personne ne discute pour savoir si l'orientation dit vraiment ce dont quelqu'un se souvient. La conversation reste centrée sur l'adaptation nationale, là où le jugement est réellement nécessaire.

Les contraintes inspirent la confiance. En refusant de générer du texte, l'outil renonce à une fonctionnalité qui aurait paru impressionnante en démonstration, et gagne quelque chose de plus précieux pour ce public : la garantie que ce que vous lisez est la norme.

## La suite

Le cycle 2030 s'étend sur une décennie, et la plupart des pays participants sont encore en phase de planification et de conception. <!-- TODO : nommer le ou les instituts nationaux de statistique où vous avez réellement testé ou présenté l'Explorateur, et une recherche concrète qui a fait gagner du temps. S'en tenir à ce qui est vérifiable. --> Un outil de ce genre est le plus utile tôt, pendant que les choix de conception sont arrêtés et documentés, et il complète plutôt qu'il ne remplace l'appui de fond que la FAO apporte aux pays.

Si vous préparez le cycle de recensement 2030 et souhaitez l'essayer, le code source est sur [GitHub](https://github.com/bakodramane/WCA_2030_Explorer). <!-- TODO : ajouter ici l'URL de la démo en ligne si l'application est déployée. -->

J'inscris ce travail dans un fil plus large : construire de petits outils transparents qui mettent les méthodes de la statistique officielle à portée de main des personnes qui les appliquent. Les travaux de programme associés figurent sur la page [Projets](/projects-fr/), et les publications méthodologiques sur la page [Publications](/publications-fr/).
