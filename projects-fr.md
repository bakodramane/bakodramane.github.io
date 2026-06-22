---
layout: page
title: Projets
permalink: /projects-fr/
description: "Projets professionnels de Dramane Bako : Programme mondial de recensement de l'agriculture (WCA 2030) de la FAO et l'Initiative 50x2030."
lang: fr
---

<p class="page-lede">Programmes professionnels sur lesquels je travaille à la FAO, couvrant la méthodologie du recensement agricole et les systèmes d'enquêtes intégrées pour la production des indicateurs ODD 2.</p>

<p><em>TODO: traduction — voir la <a href="{{ '/projects/' | relative_url }}">version anglaise</a> pour le contenu complet.</em></p>

<div class="project-section" id="wca-2030-fr">
  <p class="eyebrow">FAO</p>
  <h2>Programme mondial de recensement de l'agriculture (WCA 2030)</h2>
  <p>Le Programme mondial de recensement de l'agriculture (WCA 2030) de la FAO établit le cadre méthodologique international pour les recensements agricoles nationaux du cycle 2030. Mes travaux couvrent la conception des enquêtes intégrées, la méthodologie du recensement, la tabulation et les outils facilitant l'application des directives.</p>

  <h3>Publications et outils connexes</h3>

  <div class="project-outputs" aria-label="Publications et outils connexes">
    <a href="{{ '/publications/#census-integrated-surveys' | relative_url }}">Publications : Recensement agricole et enquêtes intégrées</a>
    <a href="{{ '/publications/#survey-methodology' | relative_url }}">Publications : Méthodologie et échantillonnage</a>
    <a href="{{ '/apps-fr/#wca-2030-explorer' | relative_url }}">Application : WCA 2030 Explorer</a>
    <a href="{{ '/apps-fr/#pipeline-ac-mr-tmr' | relative_url }}">Application : Revue de métadonnées et tableaux des principaux résultats</a>
  </div>

  {% assign wca_posts_fr = site.posts | where: "lang", "fr" | where_exp: "p", "p.tags contains 'wca-2030'" %}
  {% if wca_posts_fr.size > 0 %}
    <h3>Articles connexes</h3>
    <div class="post-grid post-grid--topic">
      {% for post in wca_posts_fr limit: 6 %}
        {% include post-card.html post=post excerpt_limit=170 tag_limit=3 %}
      {% endfor %}
    </div>
  {% else %}
    <h3>Articles connexes</h3>
    <p class="empty-state">Les articles sur le WCA 2030 apparaîtront ici au fur et à mesure de leur publication. Consultez la <a href="{{ '/weekly-monitor/' | relative_url }}">Veille hebdomadaire</a> pour les mises à jour connexes.</p>
  {% endif %}
</div>

<div class="project-section" id="50x2030-fr">
  <p class="eyebrow">Initiative multipartenaires</p>
  <h2>L'Initiative 50x2030</h2>
  <p>L'Initiative 50x2030 est un effort multipartenaires visant à combler le déficit de données agricoles dans 50 pays d'ici 2030 grâce à des systèmes de données agricoles intégrés et fondés sur des enquêtes. Mes contributions portent sur l'approche de collecte de données, les orientations en matière d'échantillonnage et la production des indicateurs ODD 2.</p>

  <h3>Publications connexes</h3>

  <div class="project-outputs" aria-label="Publications connexes">
    <a href="{{ '/publications/#census-integrated-surveys' | relative_url }}">Publications : Recensement agricole et enquêtes intégrées</a>
    <a href="{{ '/publications/#survey-methodology' | relative_url }}">Publications : Méthodologie et échantillonnage</a>
  </div>

  {% assign x2030_posts_fr = site.posts | where: "lang", "fr" | where_exp: "p", "p.tags contains '50x2030'" %}
  {% if x2030_posts_fr.size > 0 %}
    <h3>Articles connexes</h3>
    <div class="post-grid post-grid--topic">
      {% for post in x2030_posts_fr limit: 6 %}
        {% include post-card.html post=post excerpt_limit=170 tag_limit=3 %}
      {% endfor %}
    </div>
  {% else %}
    <h3>Articles connexes</h3>
    <p class="empty-state">Les articles sur l'Initiative 50x2030 apparaîtront ici au fur et à mesure de leur publication. Consultez la <a href="{{ '/weekly-monitor/' | relative_url }}">Veille hebdomadaire</a> pour les mises à jour connexes.</p>
  {% endif %}
</div>
