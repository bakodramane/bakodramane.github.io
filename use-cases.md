---
layout: page
title: Use Cases
permalink: /use-cases/
description: "Practical AI use cases for surveys, censuses, administrative data, agricultural statistics and official statistics."
lang: en
---

<p class="page-lede">Concrete applications of AI across the statistical production lifecycle, from planning and fieldwork to processing, analysis, dissemination and user support.</p>

<div class="resource-grid">
  <section class="resource-card" id="survey-census-operations">
    <h2>Survey and census operations</h2>
    <p>Questionnaire drafting, translation support, field monitoring, adaptive follow-up, editing, imputation, tabulation and dissemination.</p>
    <a class="read-more" href="{{ '/topics/#ai-surveys-censuses' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="administrative-data-quality">
    <h2>Administrative data quality control</h2>
    <p>Automated checks, anomaly detection, classification review, linkage validation and source quality documentation.</p>
    <a class="read-more" href="{{ '/topics/#administrative-data' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="wca-2030-ai">
    <h2>WCA 2030 and AI</h2>
    <p>Emerging use cases for agricultural censuses, geospatial enrichment, frame quality, data processing and dissemination.</p>
    <a class="read-more" href="{{ '/topics/#agricultural-statistics-wca-2030' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="dissemination-chatbots">
    <h2>Dissemination and chatbots</h2>
    <p>Natural language access, metadata-aware assistants, statistical literacy support and responsible public information services.</p>
    <a class="read-more" href="{{ '/topics/#dissemination-dashboards-chatbots-data-access' | relative_url }}">Related topic</a>
  </section>
</div>

{% assign survey_topic = site.data.topics | where: "slug", "ai-surveys-censuses" | first %}
<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Production lifecycle</p>
    <h2>Survey and census operations</h2>
  </div>
  {% include topic-posts.html topic=survey_topic limit=4 lang="en" %}
</section>

{% assign agriculture_topic = site.data.topics | where: "slug", "agricultural-statistics-wca-2030" | first %}
<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Agricultural statistics</p>
    <h2>Agricultural statistics and WCA 2030</h2>
  </div>
  {% include topic-posts.html topic=agriculture_topic limit=4 lang="en" %}
</section>
