---
layout: page
title: Applications
permalink: /apps-fr/
description: "Applications et outils open source de Dramane Bako pour les recensements agricoles, le nettoyage des données d'enquête, l'estimation pour petits domaines et la recherche dans les directives."
lang: fr
---

<p class="page-lede">Outils open source, principalement hors connexion, que je développe pour les statistiques officielles — recensements agricoles, nettoyage des données d'enquête, estimation pour petits domaines et recherche dans les directives. Le code source, et une démonstration en ligne le cas échéant, sont accessibles sous chaque outil.</p>

<p><em>TODO: traduction — voir la <a href="{{ '/apps/' | relative_url }}">version anglaise</a> pour les descriptions complètes de chaque application.</em></p>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Outils de statistique</p>
    <h2>Outils pour les statistiques agricoles et la méthodologie des enquêtes</h2>
  </div>

  <div class="app-grid">

    <div class="app-card" id="wca-2030-explorer">
      <h2><a href="https://github.com/bakodramane/WCA_2030_Explorer">WCA 2030 Explorer</a></h2>
      <p>Application web progressive hors connexion pour interroger les directives FAO WCA 2030. Les réponses sont du texte extrait verbatim avec références de section et de page — jamais généré.</p>
      <div class="app-card__tech">
        <span>Vite</span>
        <span>Transformers.js (WASM)</span>
        <span>MiniSearch BM25</span>
        <span>PWA</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/WCA_2030_Explorer">Voir sur GitHub</a>
      </div>
    </div>

    <div class="app-card" id="pipeline-ac-mr-tmr">
      <h2><a href="https://github.com/bakodramane/PIPELINE_AC_MR_TMR">Revue de métadonnées et tableaux des principaux résultats (PIPELINE_AC_MR_TMR)</a></h2>
      <p>Application de bureau pour les équipes de méthodologie du recensement FAO WCA 2020. Génère des Revues de métadonnées (15 sections) et des Tableaux des principaux résultats (23 sous-tableaux) à partir de documents de recensement agricoles nationaux.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>API LLM</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/PIPELINE_AC_MR_TMR">Voir sur GitHub</a>
      </div>
    </div>

    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/DATA_CLEANING_SYNTAX_APP">Application de syntaxe de nettoyage de données</a></h2>
      <p>Outil open source hors connexion pour les statisticiens d'enquête. Convertit les dictionnaires de données et métadonnées en syntaxe de nettoyage, validation et imputation pour SPSS, Stata, R et Python.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>Hors connexion</span>
        <span>SPSS</span>
        <span>Stata</span>
        <span>R</span>
        <span>Python</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/DATA_CLEANING_SYNTAX_APP">Voir sur GitHub</a>
      </div>
    </div>

    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/SAE_Syntax_Generator">Générateur de syntaxe SAE</a></h2>
      <p>Application web progressive hors connexion pour statisticiens. Importez un dictionnaire de données d'enquête, choisissez parmi 16 méthodes d'estimation pour petits domaines, et téléchargez des scripts R et Stata prêts à l'emploi, commentés.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>PWA</span>
        <span>R</span>
        <span>Stata</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/SAE_Syntax_Generator">Voir sur GitHub</a>
      </div>
    </div>

  </div>
</section>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Autres projets</p>
    <h2>Portfolio de science des données</h2>
  </div>
  <div class="app-grid">
    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/PIMA_Diabetes_Prediction">Prédiction du diabète PIMA</a></h2>
      <p>Modèle prédictif classifiant la probabilité de diabète à partir d'attributs de santé (jeu de données PIMA Indians Diabetes). Projet de portfolio de science des données illustrant un pipeline complet d'apprentissage automatique.</p>
      <div class="app-card__tech">
        <span>Python</span>
        <span>Apprentissage automatique</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/PIMA_Diabetes_Prediction">Voir sur GitHub</a>
      </div>
    </div>
  </div>
</section>
