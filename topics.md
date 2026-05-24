---
layout: page
title: Topics
permalink: /topics/
description: "Topic taxonomy for AI tools, methods and governance in official statistics."
lang: en
---

<p class="page-lede">A maintained topic taxonomy for the AI for Official Statistics knowledge hub. Existing post tags are intentionally preserved; these topic groups provide a clearer editorial layer above the current broad tags and categories.</p>

<div class="taxonomy-overview" aria-label="Topic overview">
  {% for topic in site.data.topics %}
    <a href="#{{ topic.slug }}">{{ topic.title }}</a>
  {% endfor %}
</div>

<div class="topic-sections">
  {% for topic in site.data.topics %}
    <section class="topic-section" id="{{ topic.slug }}">
      <div class="section__heading section__heading--inline">
        <div>
          <p class="eyebrow">Topic group</p>
          <h2>{{ topic.title }}</h2>
        </div>
        <a class="section-link" href="{{ '/archive/' | relative_url }}">Browse archive</a>
      </div>
      <p>{{ topic.description }}</p>

      <div class="topic-meta">
        <div>
          <strong>Mapped tags</strong>
          <div class="tag-list">
            {% for tag in topic.tags %}
              <span>{{ tag }}</span>
            {% endfor %}
          </div>
        </div>
        <div>
          <strong>Mapped categories</strong>
          <div class="meta-list">
            {% for category in topic.categories %}
              <span class="meta-badge">{{ category }}</span>
            {% endfor %}
          </div>
        </div>
      </div>

      <h3>Relevant posts</h3>
      {% include topic-posts.html topic=topic limit=4 lang="en" %}
    </section>
  {% endfor %}
</div>
