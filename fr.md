---
layout: page
title: Français
permalink: /fr/
description: "Articles en français sur les outils d'IA pour les enquêtes, les recensements, les données administratives et les statistiques officielles."
lang: fr
---

<p class="page-lede">Tous les articles en français, du plus récent au plus ancien.</p>

<div class="archive-list archive-list--cards">
  {% assign french_posts = site.posts | where: "lang", "fr" %}
  {% for post in french_posts %}
    {% include post-card.html post=post excerpt_limit=210 tag_limit=4 read_label="Lire la suite" date_format="%d/%m/%Y" heading_level="h2" %}
  {% endfor %}
</div>
