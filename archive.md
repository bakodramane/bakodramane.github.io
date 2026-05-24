---
layout: page
title: Archive
permalink: /archive/
description: "Chronological archive of AI for Official Statistics posts by Dramane Bako."
lang: en
---

<p class="page-lede">A chronological view of all posts in the AI for Official Statistics knowledge hub, including English and French updates.</p>

<div class="archive-toolbar" aria-label="Archive browsing options">
  <div>
    <p class="eyebrow">Browse</p>
    <h2>Chronological archive</h2>
  </div>
  <div class="archive-toolbar__links">
    <a href="{{ '/en/' | relative_url }}" hreflang="en">English posts</a>
    <a href="{{ '/fr/' | relative_url }}" hreflang="fr">Articles en français</a>
    <a href="{{ '/feed.xml' | relative_url }}">RSS feed</a>
  </div>
</div>

<div class="filter-placeholder">
  <strong>Future filtering area.</strong>
  <span>Phase 2 can add topic, language and search filters once the taxonomy is refined.</span>
</div>

<div class="archive-list archive-list--cards">
  {% for post in site.posts %}
    {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" %}
  {% endfor %}
</div>
