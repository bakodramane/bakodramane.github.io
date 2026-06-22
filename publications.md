---
layout: page
title: Publications
permalink: /publications/
description: "Selected publications and communications by Dramane Bako, organised by topic."
lang: en
---

<p class="page-lede">Selected publications and communications organised by topic. Types (journal article, working paper, guideline, conference paper, and so on) are labelled within each section.</p>

<nav class="taxonomy-overview" aria-label="Jump to topic">
  {% for topic in site.data.publications.topics %}
    <a href="#{{ topic.id }}">{{ topic.title }}</a>
  {% endfor %}
</nav>

<div class="pub-sections">
  {% for topic in site.data.publications.topics %}
    <section class="pub-section" id="{{ topic.id }}">
      <p class="eyebrow">Topic</p>
      <h2>{{ topic.title }}</h2>
      {% if topic.description %}
        <p>{{ topic.description }}</p>
      {% endif %}
      {% assign sorted_pubs = topic.publications | sort: "year" | reverse %}
      <ul class="pub-list" aria-label="Publications in {{ topic.title }}">
        {% for pub in sorted_pubs %}
          <li class="pub-item">
            <span class="pub-type-badge">{{ pub.type }}</span>
            {% if pub.url %}
              <p>{{ pub.citation }} <a class="pub-doi-link" href="{{ pub.url }}">Link &rarr;</a></p>
            {% else %}
              <p>{{ pub.citation }}</p>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </section>
  {% endfor %}
</div>

<p class="pub-note"><em>Selected publications and communications. Some items are cross-cutting and listed under their primary topic.</em></p>
