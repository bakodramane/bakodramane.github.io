---
layout: page
title: Français
permalink: /fr/
description: "Articles en français sur les outils d'IA pour les enquêtes, les recensements, les données administratives et les statistiques officielles."
lang: fr
---

# Articles récents

<p class="archive-intro">Tous les articles en français, du plus récent au plus ancien.</p>

<div class="archive-list">
  {% assign french_posts = site.posts | where: "lang", "fr" %}
  {% for post in french_posts %}
    <article class="archive-item">
      <p class="post-card__meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d/%m/%Y" }}</time>
        {% if post.categories.size > 0 %}
          <span>{{ post.categories | first }}</span>
        {% endif %}
      </p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.description | default: post.excerpt | strip_html | strip | truncate: 190 }}</p>
      {% if post.tags.size > 0 %}
        <div class="tag-list" aria-label="Mots-clés">
          {% for tag in post.tags limit:4 %}
            <span>{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
      <p><a class="read-more" href="{{ post.url | relative_url }}">Lire la suite</a></p>
    </article>
  {% endfor %}
</div>
