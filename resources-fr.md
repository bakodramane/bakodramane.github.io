---
layout: page
title: "Ressources"
permalink: /resources-fr/
description: "Références, listes de contrôle et ressources pratiques pour l'IA responsable en statistique officielle."
lang: fr
translation_en: /resources/
translation_fr: /resources-fr/
---
<p class="page-lede">Guides, listes de contrôle, références et conseils pratiques pour l'utilisation responsable de l'IA dans les statistiques officielles.</p>
<div class="resource-grid">
  <section class="resource-card" id="responsible-ai-checklist"><h2>Liste de contrôle pour une IA responsable</h2><p>Préciser les objectifs, contrôler la qualité des données et la confidentialité, évaluer les biais, documenter les limites et assurer une supervision humaine.</p><a class="read-more" href="{{ '/topics-fr/#ai-governance-ethics-quality' | relative_url }}">Thème connexe →</a></section>
  <section class="resource-card" id="source-grounding"><h2>Veille fondée sur des sources fiables</h2><p>Suivre les évolutions de l'IA grâce aux publications originales, aux méthodes documentées et aux références institutionnelles.</p><a class="read-more" href="{{ '/fr/' | relative_url }}">Lire la veille →</a></section>
  <section class="resource-card" id="quality-template"><h2>Documentation de l'assurance qualité</h2><p>Consigner les hypothèses, les contrôles de validation, les limites connues et les mesures de surveillance.</p><a class="read-more" href="{{ '/methods-fr/#quality-assurance' | relative_url }}">Méthode connexe →</a></section>
  <section class="resource-card" id="rss"><h2>Abonnement RSS</h2><p>Suivre les mises à jour sur les outils, les méthodes et la gouvernance de l'IA en statistique officielle.</p><a class="read-more" href="{{ '/feed.xml' | relative_url }}">S'abonner →</a></section>
</div>
{% assign topic = site.data.topics | where: "slug", "ai-governance-ethics-quality" | first %}
<section class="section"><div class="section__heading"><p class="eyebrow">Gouvernance et qualité</p><h2>IA responsable et assurance qualité</h2></div>{% include topic-posts.html topic=topic limit=6 lang="fr" %}</section>
