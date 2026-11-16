---
layout: page
title: "Insights & Knowledge Hub"
description: "Bilingual insights, weekly AI monitoring and practical resources on official statistics, surveys, data science and responsible AI."
permalink: /insights/
lang: en
translation_en: /insights/
translation_fr: /insights-fr/
---
<p class="page-lede">Analysis, practical methods and bilingual monitoring on developments in AI for official statistics. The established knowledge hub and archive are preserved.</p>
<div class="portfolio-grid portfolio-grid--three">
  <article class="portfolio-tile"><h2>Weekly Monitor</h2><p>Curated developments, evidence and practical implications of AI for official statistics.</p><a class="text-action" href="{{ '/weekly-monitor/' | relative_url }}">Browse monitor →</a></article>
  <article class="portfolio-tile"><h2>Knowledge Hub</h2><p>Organised guides on statistical methods, quality, governance and useful tools.</p><a class="text-action" href="{{ '/knowledge-hub/' | relative_url }}">Explore hub →</a></article>
  <article class="portfolio-tile"><h2>Archives &amp; RSS</h2><p>Search past articles, filter by language and subscribe to updates.</p><a class="text-action" href="{{ '/archive/' | relative_url }}">Search archive →</a></article>
</div>
<h2>Latest articles in English</h2>
<div class="portfolio-grid portfolio-grid--two">
{% assign english_posts = site.posts | where: "lang", "en" %}{% for post in english_posts limit: 6 %}{% include post-card.html post=post heading_level="h2" excerpt_limit=180 %}{% endfor %}
</div>
<p><a class="text-action" href="{{ '/en/' | relative_url }}">All English articles →</a> &nbsp; <a class="text-action" href="{{ '/fr/' | relative_url }}">Articles en français →</a></p>
