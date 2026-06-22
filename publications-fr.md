---
layout: page
title: Publications
permalink: /publications-fr/
description: "Sélection de publications et communications de Dramane Bako, organisées par thème."
lang: fr
---

<p class="page-lede">Sélection de publications et communications organisées par thème. Les types (article de revue, document de travail, directive, communication à conférence, etc.) sont indiqués dans chaque section.</p>

<p><em>TODO: traduction — les notices bibliographiques restent en anglais (références publiées) ; les titres de section et descriptions sont à traduire. Voir la <a href="{{ '/publications/' | relative_url }}">version anglaise</a> pour le contenu complet.</em></p>

<nav class="taxonomy-overview" aria-label="Aller à un thème">
  {% for topic in site.data.publications.topics %}
    <a href="{{ '/publications/' | relative_url }}#{{ topic.id }}">{{ topic.title }}</a>
  {% endfor %}
</nav>

<div class="callout callout--compact" style="margin-top: 24px;">
  <div>
    <p class="eyebrow">Version complète</p>
    <h2>Consulter la page Publications en anglais</h2>
    <p>La liste complète des publications, avec les notices bibliographiques et les liens, est disponible sur la page anglaise.</p>
  </div>
  <a class="button button--primary" href="{{ '/publications/' | relative_url }}">Publications (English)</a>
</div>

<p class="pub-note"><em>Sélection de publications et communications. Certains items sont transversaux et sont classés sous leur thème principal.</em></p>
