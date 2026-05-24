---
title: "Home"
layout: default
description: "AI for Official Statistics: practical insights on AI tools, methods and governance for surveys, censuses, administrative data and agricultural statistics."
lang: en
---

{% assign english_posts = site.posts | where: "lang", "en" %}
{% assign latest_english = english_posts | first %}

<section class="hero hub-hero">
  <div class="hero__content">
    <p class="eyebrow">Personal knowledge hub</p>
    <h1>AI for Official Statistics</h1>
    <p class="hero__lede">
      Practical, source-grounded insights on AI tools, methods and governance for surveys, censuses, administrative data and agricultural statistics.
    </p>
    <p class="hero__positioning">
      A personal knowledge hub by Dramane Bako on responsible AI, data science and official statistics.
    </p>
    <div class="hero__actions" aria-label="Homepage actions">
      {% if latest_english %}
        <a class="button button--primary" href="{{ latest_english.url | relative_url }}">Read latest update</a>
      {% else %}
        <a class="button button--primary" href="{{ '/archive/' | relative_url }}">Read latest update</a>
      {% endif %}
      <a class="button" href="{{ '/topics/' | relative_url }}">Browse by topic</a>
      <a class="button" href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a>
    </div>
  </div>
  <div class="hero__panel" aria-label="Site focus">
    <span>Responsible AI governance</span>
    <span>Survey, census and administrative data methods</span>
    <span>Agricultural statistics and WCA 2030</span>
    <div class="hero__languages">
      <a href="{{ '/en/' | relative_url }}" hreflang="en">English updates</a>
      <a href="{{ '/fr/' | relative_url }}" hreflang="fr">Mises à jour en français</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Who this is for</p>
    <h2>Practical AI thinking for statistical work</h2>
  </div>
  <div class="audience-grid">
    <article class="audience-card audience-card--offices">
      <h3>For statistical offices</h3>
      <p>Responsible AI, quality assurance, governance, administrative data and dissemination.</p>
    </article>
    <article class="audience-card audience-card--practitioners">
      <h3>For survey and census practitioners</h3>
      <p>AI-supported questionnaire design, field operations, editing, imputation, tabulation and quality control.</p>
    </article>
    <article class="audience-card audience-card--science">
      <h3>For data scientists</h3>
      <p>LLMs, machine learning pipelines, survey-aware modelling and reproducible workflows.</p>
    </article>
  </div>
</section>

<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Topics</p>
      <h2>Browse the knowledge hub</h2>
    </div>
    <a class="section-link" href="{{ '/topics/' | relative_url }}">All topics</a>
  </div>
  <div class="topic-grid topic-grid--compact">
    <a class="topic-card" href="{{ '/topics/#surveys-censuses' | relative_url }}">
      <h3>AI for surveys and censuses</h3>
      <p>Questionnaires, field operations, processing and production workflows.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#administrative-data' | relative_url }}">
      <h3>Administrative data</h3>
      <p>Quality control, linkage, classification and reuse of administrative sources.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#agricultural-statistics-wca-2030' | relative_url }}">
      <h3>Agricultural statistics and WCA 2030</h3>
      <p>Emerging AI use cases for agricultural census and survey systems.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#governance-ethics' | relative_url }}">
      <h3>AI governance and ethics</h3>
      <p>Responsible adoption, transparency, risk management and institutional readiness.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#quality-editing-imputation' | relative_url }}">
      <h3>Data quality, editing and imputation</h3>
      <p>Methods for validation, anomaly detection, cleaning and missing data treatment.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#dissemination-access' | relative_url }}">
      <h3>Dissemination, chatbots and data access</h3>
      <p>AI-assisted publishing, user support and responsible data access.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#survey-aware-ml' | relative_url }}">
      <h3>Survey-aware machine learning</h3>
      <p>Models that respect weights, designs, sampling structure and population inference.</p>
    </a>
    <a class="topic-card" href="{{ '/topics/#tools-platforms' | relative_url }}">
      <h3>Tools and platforms</h3>
      <p>Practical tools, platforms and reproducible workflows for statistical teams.</p>
    </a>
  </div>
</section>

<section class="section start-section">
  <div class="section__heading">
    <p class="eyebrow">Start here</p>
    <h2>Useful entry points</h2>
  </div>
  <div class="start-grid">
    <a class="start-link" href="{{ '/use-cases/#survey-census-operations' | relative_url }}">AI tools for survey and census operations</a>
    <a class="start-link" href="{{ '/resources/#responsible-ai-checklist' | relative_url }}">Responsible AI checklist for official statistics</a>
    <a class="start-link" href="{{ '/methods/#survey-aware-machine-learning' | relative_url }}">Survey-aware machine learning: practical guide</a>
    <a class="start-link" href="{{ '/use-cases/#administrative-data-quality' | relative_url }}">AI for administrative data quality control</a>
    <a class="start-link" href="{{ '/use-cases/#wca-2030-ai' | relative_url }}">WCA 2030 and AI: emerging use cases</a>
  </div>
</section>

<section class="section">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Latest posts</p>
      <h2>Recent weekly monitor updates</h2>
    </div>
    <a class="section-link" href="{{ '/archive/' | relative_url }}">View archive</a>
  </div>
  <div class="post-grid">
    {% for post in site.posts limit: 6 %}
      {% include post-card.html post=post excerpt_limit=175 tag_limit=3 %}
    {% endfor %}
  </div>
</section>

<section class="section callout callout--rss">
  <div>
    <p class="eyebrow">RSS</p>
    <h2>Follow the weekly AI for official statistics monitor</h2>
    <p>Subscribe via RSS to follow new updates on AI tools, methods and governance for official statistics.</p>
  </div>
  <a class="button button--primary" href="{{ '/feed.xml' | relative_url }}">Subscribe via RSS</a>
</section>
