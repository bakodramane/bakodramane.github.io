---
layout: page
title: Archive
permalink: /archive/
description: "All posts from Dramane Bako's blog on AI tools, surveys, administrative data and official statistics."
---

# All posts

Browse all posts in reverse chronological order.

<div class="archive-list">
  {% for post in site.posts %}
    <article class="archive-item">
      <p class="post-card__meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
        {% if post.categories.size > 0 %}
          <span>{{ post.categories | first }}</span>
        {% endif %}
      </p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.description | default: post.excerpt | strip_html | strip | truncate: 190 }}</p>
      {% if post.tags.size > 0 %}
        <div class="tag-list" aria-label="Post tags">
          {% for tag in post.tags limit:4 %}
            <span>{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
    </article>
  {% endfor %}
</div>
