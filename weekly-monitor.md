---
layout: page
title: Weekly Monitor
permalink: /weekly-monitor/
description: "Weekly monitor updates on AI tools, methods and governance for official statistics."
lang: en
---

<p class="page-lede">The Weekly Monitor tracks new AI tools, methods, reports and governance developments relevant to surveys, censuses, administrative data and official statistics.</p>

<section class="callout callout--compact">
  <div>
    <p class="eyebrow">Follow</p>
    <h2>Subscribe to new updates</h2>
    <p>Use the RSS feed to follow each new weekly monitor entry as it is published.</p>
  </div>
  <a class="button button--primary" href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a>
</section>

<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">English</p>
      <h2>Latest monitor updates</h2>
    </div>
    <a class="section-link" href="{{ '/en/' | relative_url }}">All English posts</a>
  </div>
  <div class="archive-list archive-list--cards">
    {% assign english_posts = site.posts | where: "lang", "en" %}
    {% for post in english_posts limit: 12 %}
      {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" %}
    {% endfor %}
  </div>
</section>

<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Français</p>
      <h2>Dernières mises à jour</h2>
    </div>
    <a class="section-link" href="{{ '/fr/' | relative_url }}">Tous les articles en français</a>
  </div>
  <div class="archive-list archive-list--cards">
    {% assign french_posts = site.posts | where: "lang", "fr" %}
    {% for post in french_posts limit: 6 %}
      {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" date_format="%d/%m/%Y" %}
    {% endfor %}
  </div>
</section>
