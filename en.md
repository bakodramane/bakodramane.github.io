---
layout: page
title: English Updates
permalink: /en/
description: "English posts on AI tools for surveys, censuses, administrative data and official statistics."
lang: en
---

<p class="page-lede">All English posts in reverse chronological order.</p>

<div class="archive-list archive-list--cards">
  {% assign english_posts = site.posts | where: "lang", "en" %}
  {% for post in english_posts %}
    {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" %}
  {% endfor %}
</div>
