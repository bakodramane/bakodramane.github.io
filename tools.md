---
layout: page
title: Tools
permalink: /tools/
description: "AI tools and platforms relevant to survey, census, administrative data and official statistics workflows."
lang: en
---

<p class="page-lede">AI tools, platforms and libraries relevant to surveys, censuses, administrative data and official statistics. This page surfaces tool-oriented monitor updates while keeping detailed tool reviews for future expansion.</p>

<div class="resource-grid">
  <section class="resource-card" id="survey-tools">
    <h2>Survey and census tools</h2>
    <p>Questionnaire support, translation, interviewer assistance, field monitoring, coding and data collection quality checks.</p>
    <a class="read-more" href="{{ '/topics/#ai-surveys-censuses' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="administrative-data-tools">
    <h2>Administrative data tools</h2>
    <p>Classification, entity resolution, record linkage, anomaly detection and metadata-assisted quality assurance.</p>
    <a class="read-more" href="{{ '/topics/#administrative-data' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="dissemination-tools">
    <h2>Dissemination and access tools</h2>
    <p>Chatbots, natural language data access, dashboards, documentation support and user-facing statistical services.</p>
    <a class="read-more" href="{{ '/topics/#dissemination-dashboards-chatbots-data-access' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="workflow-tools">
    <h2>Workflow and reproducibility tools</h2>
    <p>LLM-assisted coding, reproducible analysis, pipeline documentation and transparent validation practices.</p>
    <a class="read-more" href="{{ '/methods/#reproducible-workflows' | relative_url }}">Related methods</a>
  </section>
</div>

{% assign tools_topic = site.data.topics | where: "slug", "tools-libraries-platforms" | first %}
<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Related posts</p>
      <h2>Tools, libraries and platforms</h2>
    </div>
    <a class="section-link" href="{{ '/topics/#tools-libraries-platforms' | relative_url }}">Topic group</a>
  </div>
  {% include topic-posts.html topic=tools_topic limit=6 lang="en" %}
</section>

{% assign dissemination_topic = site.data.topics | where: "slug", "dissemination-dashboards-chatbots-data-access" | first %}
<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Data access</p>
    <h2>Dissemination, dashboards and chatbots</h2>
  </div>
  {% include topic-posts.html topic=dissemination_topic limit=4 lang="en" %}
</section>
