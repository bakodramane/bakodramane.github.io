# Content Guidelines

This site is a personal knowledge hub on AI for Official Statistics. It should remain professional, practical and source-grounded, while clearly avoiding the appearance of an official institutional publication.

Use this disclaimer where appropriate:

> Views are personal and do not represent any institution.

## Front Matter

Recommended front matter for new posts:

```yaml
---
layout: post
title: "Post title"
date: YYYY-MM-DD
author: Dramane Bako
description: "One concise summary sentence for cards and SEO."
lang: en
translation_key: stable-shared-key-for-english-and-french
permalink: /fr/YYYY/MM/DD/stable-slug/ # French posts only, when preserving the /fr/ URL pattern.
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, official-statistics, administrative-data]
coverage_period: "Month D-D, YYYY"
source_count: "6 sources"
key_takeaways:
  - "First practical takeaway."
  - "Second practical takeaway."
  - "Third practical takeaway."
why_it_matters: "Why this matters for official statistics."
practical_action: "A concrete action for statistical offices or practitioners."
last_updated: YYYY-MM-DD
toc: true
---
```

French posts should use the paired values:

```yaml
categories: [IA, Recherche par sondage, Veille]
tags: [IA, enquetes, statistiques-officielles, donnees-administratives]
lang: fr
translation_key: same-key-as-the-english-post
```

## Translation Pairs

Pair English and French posts with the same `translation_key`. The current post layout and header language switch use this field to link translations.

Keep French post URLs under `/fr/YYYY/MM/DD/.../` using `permalink` when needed. Do not change existing post URLs unless there is a deliberate migration plan.

## Tags And Categories

Current tags are intentionally broad and should not be mass-renamed because they are already used across the archive:

- English tags: `AI`, `surveys`, `official-statistics`, `administrative-data`, plus older `statistics` and `bilingual`.
- French tags: `IA`, `enquetes`, `statistiques-officielles`, `donnees-administratives`.
- English categories: `AI`, `Survey Research`, `Weekly Update`.
- French categories: `IA`, `Recherche par sondage`, `Veille`.

For future posts, prefer the current canonical tags:

- English: `AI`, `surveys`, `official-statistics`, `administrative-data`.
- French: `IA`, `enquetes`, `statistiques-officielles`, `donnees-administratives`.

Use `_data/topics.yml` for the richer editorial taxonomy. Add a post's `translation_key` to a topic's `featured_posts` list when the broad tags are not specific enough.

## Topic Groups

The maintained topic groups are:

- AI for surveys and censuses
- Administrative data
- Agricultural statistics and WCA 2030
- AI governance, ethics and quality assurance
- Survey methodology and machine learning
- Data cleaning, editing, imputation and validation
- Dissemination, dashboards, chatbots and data access
- Tools, libraries and platforms

## Summary Boxes

Use the optional fields `coverage_period`, `source_count`, `key_takeaways`, `why_it_matters`, `practical_action`, `last_updated` and `toc` for long monitor posts. The layout will display them automatically when present.

## Tables

Use standard Markdown tables:

```markdown
| Column A | Column B |
|----------|----------|
| Value    | Notes    |
```

Keep table cells concise. Long tables will scroll horizontally on mobile through the global CSS.

## Source Sections

Prefer clear source headings such as:

- `## Sources used this week`
- `## References`
- `## Further reading`
- `## Official sources`
- `## Papers and reports`

Use source sections for official institutional pages, reports, academic papers, conference pages, tool documentation and credible organisational blogs. Do not invent sources.

## Editorial Tone

Write as a knowledgeable individual practitioner. Prefer practical implications, methodological caution and source-grounded synthesis. Avoid wording that implies the blog represents FAO, the UN, a government, or any institution.
