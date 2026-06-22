---
layout: post
title: "Making the WCA 2030 guidelines searchable: building an offline explorer"
lang: en
translation_key: wca-2030-offline-explorer
date: 2026-06-22
categories: [projects]
tags: [wca-2030]
published: false
description: "Why I built an offline, citation-first explorer for the FAO World Programme for the Census of Agriculture 2030 guidelines, and what it means for census methodology teams."
key_takeaways:
  - "The WCA 2030 guidelines are the international standard for the 2026–2035 census round, and the practical problem for methodologists is locating and citing the exact recommendation, not the absence of guidance."
  - "The WCA 2030 Explorer returns verbatim text with section and page citations, and never generates or paraphrases an answer, so the standard is quoted rather than approximated."
  - "Building it offline-first means a methodologist in a national statistics office can use it without connectivity, without sending census documents to an external service, and without per-query costs."
why_it_matters: >
  A census of agriculture is a once-a-decade commitment. The guidelines that shape it deserve a tool
  that surfaces the exact wording a methodologist needs to defend a design decision, with a citation
  attached, so reviews and audits rest on the source rather than on memory.
practical_action: >
  If your office is preparing for the 2030 round, treat the guidelines as a reference you query
  constantly rather than a document you read once. A citation-first search layer over the standard
  shortens design reviews and keeps national adaptations anchored to the international text.
---

<!-- NOTE: confirm these front-matter keys match an existing post (e.g. a recent weekly-monitor entry) before publishing. Flip `published` to true when ready. -->

The FAO World Programme for the Census of Agriculture 2030 sets the international methodological standard for national agricultural censuses in the eleventh decennial round, covering the period from 2026 to 2035. It carries decades of accumulated practice: complete enumeration of structural items at least once a decade, complemented by regular inter-censal surveys that use the census as their frame, alongside expanded guidance on georeferencing, computer-assisted interviewing, Earth observation, and the role of artificial intelligence in census operations.

It is also long. A national methodologist sitting down to design a census rarely needs the whole document. They need one specific thing: the recommended definition of a non-household holding, the conditions under which a dual-frame design applies, the revised approach to measuring gender roles within the holding, or the exact threshold the guidelines attach to a concept. Finding that one paragraph, and then citing it precisely in a design note, is where the real friction sits.

## The friction I kept seeing

Across the agricultural statistics teams I work with, the pattern repeats. Someone is drafting a sampling plan or a tabulation specification, they remember that the guidelines say something relevant, and they spend twenty minutes scrolling a several-hundred-page PDF to find it. When they do, they paraphrase it into their note from memory, and the paraphrase quietly drifts from the source. By the time the design is reviewed, the reviewer is debating the paraphrase rather than the standard.

For a normative document, that drift is the problem worth solving. A census standard works only if the people applying it can quote it exactly and point to where it lives.

## What I built

The [WCA 2030 Explorer](https://github.com/bakodramane/WCA_2030_Explorer) is a small tool with a deliberately narrow promise. You ask it a question in plain language, and it returns passages from the guidelines verbatim, each tagged with its section and page. It does not summarise, rephrase, or compose an answer of its own. The text you read is the text in the standard, and the citation tells you where to verify it.

Two design choices define the tool.

**Verbatim and cited, by construction.** The Explorer never generates prose. This is a constraint I built in rather than a limitation I tolerated. When the subject is an international standard, an answer that sounds plausible but subtly restates the rule is worse than no answer, because it invites a methodologist to act on a version of the guidance that the document does not contain. Returning the exact wording, with a page reference, keeps the human in the position of interpreting the source rather than trusting an intermediary.

**Offline-first.** The Explorer is a progressive web app that runs entirely in the browser, with no server call once it has loaded. That matters for the offices most likely to use it. A methodologist preparing a census in Ouagadougou, Bamako, Monrovia, or Freetown should not depend on a stable connection, or on permission to send draft census materials to an external service, to look up a recommendation. Running locally also means there are no per-query costs, which keeps the tool usable across a whole team rather than rationed.

## How it works underneath

The retrieval layer combines two complementary methods. A lexical index built with MiniSearch and BM25 ranking handles the queries where the user already knows the right vocabulary, which is common among statisticians searching for a defined term. Alongside it, semantic embeddings generated in the browser with Transformers.js, compiled to WebAssembly, catch the queries phrased in everyday language that do not match the document's wording. The whole stack is bundled with Vite and ships as static assets.

The engineering goal throughout was to keep the model honest about its boundaries. The embeddings decide which passages are most relevant; they never write the answer.

## Lessons for census methodology teams

A few things became clear while building this that generalise beyond the tool itself.

A standard is only as useful as its retrievability. Investing in how teams find and cite the guidelines pays back across every design review in a census cycle. Treating the document as searchable infrastructure changes how often people actually consult it.

Citations are a trust mechanism, not a formality. When every passage carries its source, a design review moves quickly because nobody is arguing about whether the guidance really says what someone remembers it saying. The conversation stays on the national adaptation, which is where judgement is genuinely needed.

Constraints earn trust. By refusing to generate text, the tool gives up a feature that would have looked impressive in a demonstration, and gains something more valuable for this audience: a guarantee that what you read is the standard.

## Where this goes

The 2030 round runs for a decade, and most participating countries are still in the planning and design phase. <!-- TODO: name the national statistics office(s) where you have actually trialled or demonstrated the Explorer, and one concrete lookup that saved time. Keep it to what you can verify. --> A tool like this is most useful early, while design decisions are being made and documented, and it complements rather than replaces the substantive guidance FAO provides to countries.

If you are preparing for the 2030 census round and want to try it, the source is on [GitHub](https://github.com/bakodramane/WCA_2030_Explorer). <!-- TODO: add the live demo URL here if the PWA is deployed. -->

I see this as part of a wider thread in my work: building small, transparent tools that put official statistics methods within easy reach of the people who apply them. The related programme work sits on the [Projects](/projects/) page, and the methodological publications behind it are on the [Publications](/publications/) page.
