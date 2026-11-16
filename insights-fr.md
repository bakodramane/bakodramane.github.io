---
layout: page
title: "Analyses et ressources"
description: "Analyses bilingues, veille sur l'IA et ressources pratiques consacrées à la statistique officielle."
permalink: /insights-fr/
lang: fr
translation_en: /insights/
translation_fr: /insights-fr/
---
<p class="page-lede">Analyses, méthodes pratiques et veille bilingue sur les évolutions de l'IA pour la statistique officielle. Le hub de connaissances et les archives existants sont conservés.</p>
<div class="portfolio-grid portfolio-grid--three">
  <article class="portfolio-tile"><h2>Veille hebdomadaire</h2><p>Actualités sélectionnées, sources et implications pratiques de l'IA pour les statistiques.</p><a class="text-action" href="{{ '/fr/' | relative_url }}">Consulter la veille →</a></article>
  <article class="portfolio-tile"><h2>Hub de connaissances</h2><p>Guides organisés autour des méthodes, de la qualité, de la gouvernance et des outils.</p><a class="text-action" href="{{ '/knowledge-hub-fr/' | relative_url }}">Explorer le hub →</a></article>
  <article class="portfolio-tile"><h2>Archives et RSS</h2><p>Recherche d'articles, filtre par langue et abonnement aux mises à jour.</p><a class="text-action" href="{{ '/archive/' | relative_url }}">Parcourir les archives →</a></article>
</div>
<h2>Derniers articles en français</h2>
<div class="portfolio-grid portfolio-grid--two">
{% assign french_posts = site.posts | where: "lang", "fr" %}{% for post in french_posts limit: 6 %}{% include post-card.html post=post heading_level="h2" excerpt_limit=180 date_format="%d/%m/%Y" %}{% endfor %}
</div>
<p><a class="text-action" href="{{ '/fr/' | relative_url }}">Tous les articles en français →</a> &nbsp; <a class="text-action" href="{{ '/en/' | relative_url }}">English articles →</a></p>
