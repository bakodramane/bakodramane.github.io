---
layout: page
title: Weekly Monitor
permalink: /weekly-monitor/
description: "Weekly monitor updates on AI tools, methods and governance for official statistics."
lang: en
---

<p class="page-lede">The weekly monitor tracks practical developments in AI tools, methods and governance for surveys, censuses, administrative data and official statistics.</p>

<section class="callout callout--compact">
  <div>
    <p class="eyebrow">Follow</p>
    <h2>Subscribe to new updates</h2>
    <p>Use the RSS feed to follow each new weekly monitor entry as it is published.</p>
  </div>
  <a class="button button--primary" href="{{ '/feed.xml' | relative_url }}">RSS feed</a>
</section>

<div class="archive-list archive-list--cards">
  {% assign english_posts = site.posts | where: "lang", "en" %}
  {% for post in english_posts limit: 12 %}
    {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" %}
  {% endfor %}
</div>
