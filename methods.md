---
layout: page
title: Methods
permalink: /methods/
description: "Methods for responsible and survey-aware AI use in official statistics."
lang: en
---

<p class="page-lede">Practical methods for applying AI and machine learning in official statistics while respecting survey design, quality, transparency and governance requirements.</p>

<div class="resource-grid">
  <section class="resource-card" id="survey-aware-machine-learning">
    <h2>Survey-aware machine learning</h2>
    <p>Models that account for survey weights, stratification, clusters, nonresponse and population inference.</p>
    <a class="read-more" href="{{ '/topics/#survey-methodology-machine-learning' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="editing-imputation">
    <h2>Editing, imputation and validation</h2>
    <p>AI-assisted data editing, anomaly detection, imputation, statistical checks and human review loops.</p>
    <a class="read-more" href="{{ '/topics/#data-cleaning-editing-imputation-validation' | relative_url }}">Related topic</a>
  </section>
  <section class="resource-card" id="quality-assurance">
    <h2>Quality assurance</h2>
    <p>Source-grounded validation, documentation, monitoring, auditability and quality gates for statistical production.</p>
    <a class="read-more" href="{{ '/resources/#responsible-ai-checklist' | relative_url }}">Responsible AI checklist</a>
  </section>
  <section class="resource-card" id="reproducible-workflows">
    <h2>Reproducible workflows</h2>
    <p>Versioned analysis, transparent prompts, documented assumptions and replicable data science workflows.</p>
    <a class="read-more" href="{{ '/tools/#workflow-tools' | relative_url }}">Related tools</a>
  </section>
</div>

{% assign methods_topic = site.data.topics | where: "slug", "survey-methodology-machine-learning" | first %}
<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Related posts</p>
      <h2>Survey methodology and machine learning</h2>
    </div>
    <a class="section-link" href="{{ '/topics/#survey-methodology-machine-learning' | relative_url }}">Topic group</a>
  </div>
  {% include topic-posts.html topic=methods_topic limit=6 lang="en" %}
</section>

{% assign cleaning_topic = site.data.topics | where: "slug", "data-cleaning-editing-imputation-validation" | first %}
<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Quality methods</p>
    <h2>Cleaning, editing, imputation and validation</h2>
  </div>
  {% include topic-posts.html topic=cleaning_topic limit=4 lang="en" %}
</section>
