---
layout: page
title: English
permalink: /en/
description: "English posts on AI tools for surveys, censuses, administrative data and official statistics."
lang: en
---

# Latest posts

<p class="archive-intro">All English posts in reverse chronological order.</p>

<div class="archive-list">
  {% assign english_posts = site.posts | where: "lang", "en" %}
  {% for post in english_posts %}
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
        <div class="tag-list" aria-label="Tags">
          {% for tag in post.tags limit:4 %}
            <span>{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
      <p><a class="read-more" href="{{ post.url | relative_url }}">Read more</a></p>
    </article>
  {% endfor %}
</div>
