---
layout: page
title: Resources
permalink: /resources/
description: "Resource entry points for responsible AI, official statistics governance and practical statistical AI workflows."
lang: en
---

<p class="page-lede">Curated guides, checklists, references and starting points for responsible AI in official statistics. These resources are intentionally practical and can be expanded into fuller guides over time.</p>

<div class="resource-grid">
  <section class="resource-card" id="responsible-ai-checklist">
    <h2>Responsible AI checklist for official statistics</h2>
    <p>Start with purpose, data quality, privacy, bias, transparency, validation, human oversight, documentation and public trust.</p>
    <a class="read-more" href="{{ '/topics/#ai-governance-ethics-quality' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="source-grounding">
    <h2>Source-grounded monitoring</h2>
    <p>Track AI developments through original sources, methodological documentation, institutional guidance and reproducible notes.</p>
    <a class="read-more" href="{{ '/weekly-monitor/' | relative_url }}">Read the monitor</a>
  </section>
  <section class="resource-card" id="quality-template">
    <h2>Quality assurance template</h2>
    <p>A future place for documenting assumptions, validation checks, known limitations and operational controls.</p>
    <a class="read-more" href="{{ '/methods/#quality-assurance' | relative_url }}">Related method</a>
  </section>
  <section class="resource-card" id="rss">
    <h2>RSS subscription</h2>
    <p>Follow new updates on AI tools, methods and governance for official statistics.</p>
    <a class="read-more" href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a>
  </section>
</div>

{% assign governance_topic = site.data.topics | where: "slug", "ai-governance-ethics-quality" | first %}
<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Evidence and governance</p>
      <h2>Responsible AI and quality assurance</h2>
    </div>
    <a class="section-link" href="{{ '/topics/#ai-governance-ethics-quality' | relative_url }}">Topic group</a>
  </div>
  {% include topic-posts.html topic=governance_topic limit=6 lang="en" %}
</section>
