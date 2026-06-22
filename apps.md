---
layout: page
title: Apps
permalink: /apps/
description: "Open-source apps and tools by Dramane Bako for agricultural census methodology, survey data cleaning, small area estimation and guideline search."
lang: en
---

<p class="page-lede">Open-source, mostly offline-first tools I build for official statistics — for agricultural census methodology, survey data cleaning, small area estimation and guideline search. Source code, and a live demo where available, is linked under each tool.</p>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Statistics tools</p>
    <h2>Tools for agricultural statistics and survey methodology</h2>
  </div>

  <div class="app-grid">

    <div class="app-card" id="wca-2030-explorer">
      <h2><a href="https://github.com/bakodramane/WCA_2030_Explorer">WCA 2030 Explorer</a></h2>
      <p>Offline progressive web app for querying the FAO WCA 2030 guidelines. Answers are verbatim extracted text with section and page citations — never generated. Useful for census methodology teams who need precise, citable references to the guidelines without an internet connection.</p>
      <div class="app-card__tech">
        <span>Vite</span>
        <span>Transformers.js (WASM)</span>
        <span>MiniSearch BM25</span>
        <span>PWA</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/WCA_2030_Explorer">View on GitHub</a>
      </div>
    </div>

    <div class="app-card" id="pipeline-ac-mr-tmr">
      <h2><a href="https://github.com/bakodramane/PIPELINE_AC_MR_TMR">AC Metadata Review &amp; Tables of Main Results (PIPELINE_AC_MR_TMR)</a></h2>
      <p>Desktop app for FAO WCA 2020 census methodology staff. Generates Metadata Reviews (15 sections) and Tables of Main Results (23 sub-tables) from national agricultural census documents using LLM APIs — reducing manual processing time for census assessments.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>LLM APIs</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/PIPELINE_AC_MR_TMR">View on GitHub</a>
      </div>
    </div>

    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/DATA_CLEANING_SYNTAX_APP">Data Cleaning Syntax App</a></h2>
      <p>Offline-first, open-source tool for survey statisticians. Turns codebooks and metadata into transparent data-cleaning, validation and imputation syntax for SPSS, Stata, R, and Python — making cleaning workflows reproducible and auditable without proprietary tools.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>Offline-first</span>
        <span>SPSS</span>
        <span>Stata</span>
        <span>R</span>
        <span>Python</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/DATA_CLEANING_SYNTAX_APP">View on GitHub</a>
      </div>
    </div>

    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/SAE_Syntax_Generator">SAE Syntax Generator</a></h2>
      <p>Offline-first progressive web app for statisticians. Upload a survey codebook, choose from 16 area-level and unit-level small area estimation methods, and download ready-to-run, commented R and Stata scripts — lowering the barrier to applying SAE in national statistical offices.</p>
      <div class="app-card__tech">
        <span>TypeScript</span>
        <span>PWA</span>
        <span>R</span>
        <span>Stata</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/SAE_Syntax_Generator">View on GitHub</a>
      </div>
    </div>

  </div>
</section>

<section class="section">
  <div class="section__heading">
    <p class="eyebrow">Other projects</p>
    <h2>Data science portfolio</h2>
  </div>

  <div class="app-grid">

    <div class="app-card">
      <h2><a href="https://github.com/bakodramane/PIMA_Diabetes_Prediction">PIMA Diabetes Prediction</a></h2>
      <p>A predictive model that classifies whether a patient is likely to have diabetes from health attributes (PIMA Indians Diabetes Dataset). A data-science portfolio project demonstrating end-to-end machine learning — from exploratory analysis to model evaluation.</p>
      <div class="app-card__tech">
        <span>Python</span>
        <span>Machine learning</span>
      </div>
      <div class="app-card__actions">
        <a class="button button--primary" href="https://github.com/bakodramane/PIMA_Diabetes_Prediction">View on GitHub</a>
      </div>
    </div>

  </div>
</section>

<section class="section callout callout--compact" aria-label="GitHub profile">
  <div>
    <p class="eyebrow">Source code</p>
    <h2>All repos on GitHub</h2>
    <p>All source code is publicly available under open-source licences. Contributions and feedback are welcome.</p>
  </div>
  <a class="button button--primary" href="https://github.com/bakodramane">View GitHub profile</a>
</section>
