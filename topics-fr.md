---
layout: page
title: "Thèmes du hub de connaissances"
permalink: /topics-fr/
description: "Huit groupes thématiques en français sur l'IA et la statistique officielle."
lang: fr
translation_en: /topics/
translation_fr: /topics-fr/
---
<p class="page-lede">Huit groupes thématiques pour explorer les applications de l'IA dans les enquêtes, les recensements, le traitement des données et la statistique officielle.</p>
<nav class="taxonomy-overview" aria-label="Sommaire des thèmes">
{% for topic in site.data.topics %}<a href="#{{ topic.slug }}">{{ site.data.topics_fr[topic.slug].title | default: topic.title }}</a>{% endfor %}
</nav>
<div class="topic-sections">
{% for topic in site.data.topics %}
<section class="topic-section" id="{{ topic.slug }}">
  <div class="section__heading section__heading--inline"><div><p class="eyebrow">Thème</p><h2>{{ site.data.topics_fr[topic.slug].title | default: topic.title }}</h2></div><a class="section-link" href="{{ '/fr/' | relative_url }}">Articles en français →</a></div>
  <p>{{ site.data.topics_fr[topic.slug].description | default: topic.description }}</p>
  <h3>Articles connexes</h3>
  {% include topic-posts.html topic=topic limit=4 lang="fr" %}
</section>
{% endfor %}
</div>
