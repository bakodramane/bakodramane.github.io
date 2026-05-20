---
layout: default
title: Home
description: "Weekly practical updates on AI tools, survey methodology, administrative data, agricultural statistics, and official statistics."
---

<section class="hero">
  <div class="hero__content">
    <p class="eyebrow">AI, surveys, administrative data</p>
    <h1>Practical AI insights for official statistics.</h1>
    <p class="hero__lede">
      Weekly updates for statisticians, data scientists, national statistical offices, researchers, and development practitioners working at the intersection of AI, surveys, censuses, administrative data, and agricultural statistics.
    </p>
    <div class="hero__actions">
      <a class="button button--primary" href="#latest-posts">Read latest posts</a>
      <a class="button" href="{{ '/about/' | relative_url }}">About Dramane</a>
    </div>
  </div>
  <div class="hero__panel" aria-label="Blog focus areas">
    <span>Survey methodology</span>
    <span>Official statistics</span>
    <span>Administrative data</span>
    <span>Responsible AI</span>
  </div>
</section>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Topics</p>
    <h2>What this blog covers</h2>
  </div>
  <div class="topic-grid">
    <article class="topic-card">
      <h3>AI for Surveys and Censuses</h3>
      <p>Tools and methods for questionnaire design, data collection, respondent interaction, quality control, coding, data processing and cleaning, tabulation and data analysis, reporting and dissemination..</p>
    </article>
    <article class="topic-card">
      <h3>Administrative Data</h3>
      <p>Practical applications of AI and machine learning for data integration, editing, validation, and production systems.</p>
    </article>
    <article class="topic-card">
      <h3>Official Statistics</h3>
      <p>Insights for national statistical offices on governance, transparency, methodological quality, and responsible innovation.</p>
    </article>
  </div>
</section>

<section class="section" id="latest-posts">
  <div class="section__heading section__heading--inline">
    <div>
      <p class="eyebrow">Latest</p>
      <h2>Recent posts</h2>
    </div>
    <a class="rss-link" href="{{ '/feed.xml' | relative_url }}">RSS feed</a>
  </div>

  <div class="post-grid">
    {% for post in site.posts limit:6 %}
      <article class="post-card">
        <p class="post-card__meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d, %Y" }}</time>
          {% if post.categories.size > 0 %}
            <span>{{ post.categories | first }}</span>
          {% endif %}
        </p>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description | default: post.excerpt | strip_html | strip | truncate: 170 }}</p>
        {% if post.tags.size > 0 %}
          <div class="tag-list" aria-label="Post tags">
            {% for tag in post.tags limit:3 %}
              <span>{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}
      </article>
    {% endfor %}
  </div>
</section>
