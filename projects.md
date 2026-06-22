---
layout: page
title: Projects
permalink: /projects/
description: "Professional projects by Dramane Bako: FAO World Programme for the Census of Agriculture (WCA 2030) and the 50x2030 Initiative."
lang: en
---

<p class="page-lede">Professional programmes I work on at FAO, covering agricultural census methodology and the integrated survey systems that produce SDG 2 food security and agricultural indicators.</p>

<div class="project-section" id="wca-2030">
  <p class="eyebrow">FAO</p>
  <h2>World Programme for the Census of Agriculture (WCA 2030)</h2>
  <p>The FAO World Programme for the Census of Agriculture (WCA 2030) sets the international methodological framework for national agricultural censuses in the 2030 round. My work spans integrated survey design, census methodology, tabulation, and tools that make census guidelines easier to apply.</p>

  <h3>Related outputs</h3>

  <div class="project-outputs" aria-label="Related publications and tools">
    <a href="{{ '/publications/#census-integrated-surveys' | relative_url }}">Publications: Agricultural census &amp; integrated survey systems</a>
    <a href="{{ '/publications/#survey-methodology' | relative_url }}">Publications: Survey methodology &amp; sampling</a>
    <a href="{{ '/apps/#wca-2030-explorer' | relative_url }}">App: WCA 2030 Explorer</a>
    <a href="{{ '/apps/#pipeline-ac-mr-tmr' | relative_url }}">App: AC Metadata Review &amp; Tables of Main Results</a>
  </div>

  {% assign wca_posts = site.posts | where_exp: "post", "post.tags contains 'wca-2030'" | where: "lang", "en" %}
  {% if wca_posts.size > 0 %}
    <h3>Related articles</h3>
    <div class="post-grid post-grid--topic">
      {% for post in wca_posts limit: 6 %}
        {% include post-card.html post=post excerpt_limit=170 tag_limit=3 %}
      {% endfor %}
    </div>
  {% else %}
    <h3>Related articles</h3>
    <p class="empty-state">Articles on WCA 2030 will appear here as they are published. See the <a href="{{ '/weekly-monitor/' | relative_url }}">Weekly Monitor</a> for related updates.</p>
  {% endif %}
</div>

<div class="project-section" id="50x2030">
  <p class="eyebrow">Multi-partner initiative</p>
  <h2>The 50x2030 Initiative</h2>
  <p>The 50x2030 Initiative is a multi-partner effort to close the agricultural data gap in 50 countries by 2030 through integrated, survey-based agricultural data systems. My contributions cover the data-collection approach, sampling guidance, and the production of SDG 2 indicators.</p>

  <h3>Related outputs</h3>

  <div class="project-outputs" aria-label="Related publications">
    <a href="{{ '/publications/#census-integrated-surveys' | relative_url }}">Publications: Agricultural census &amp; integrated survey systems</a>
    <a href="{{ '/publications/#survey-methodology' | relative_url }}">Publications: Survey methodology &amp; sampling</a>
  </div>

  {% assign x2030_posts = site.posts | where_exp: "post", "post.tags contains '50x2030'" | where: "lang", "en" %}
  {% if x2030_posts.size > 0 %}
    <h3>Related articles</h3>
    <div class="post-grid post-grid--topic">
      {% for post in x2030_posts limit: 6 %}
        {% include post-card.html post=post excerpt_limit=170 tag_limit=3 %}
      {% endfor %}
    </div>
  {% else %}
    <h3>Related articles</h3>
    <p class="empty-state">Articles on the 50x2030 Initiative will appear here as they are published. See the <a href="{{ '/weekly-monitor/' | relative_url }}">Weekly Monitor</a> for related updates.</p>
  {% endif %}
</div>
