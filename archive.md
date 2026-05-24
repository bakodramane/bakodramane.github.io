---
layout: page
title: Archive
permalink: /archive/
description: "Chronological archive of AI for Official Statistics posts by Dramane Bako."
lang: en
---

<p class="page-lede">A chronological view of all posts in the AI for Official Statistics knowledge hub, including English and French updates.</p>

<div class="archive-toolbar" aria-label="Archive browsing options">
  <div>
    <p class="eyebrow">Browse</p>
    <h2>Chronological archive</h2>
  </div>
  <div class="archive-toolbar__links">
    <a href="{{ '/en/' | relative_url }}" hreflang="en">English posts</a>
    <a href="{{ '/fr/' | relative_url }}" hreflang="fr">Articles en français</a>
    <a href="{{ '/topics/' | relative_url }}">Topics</a>
    <a href="{{ '/feed.xml' | relative_url }}">RSS feed</a>
  </div>
</div>

<div class="archive-search" role="search" aria-label="Search archive">
  <label for="archive-search-input">Search posts</label>
  <input id="archive-search-input" type="search" placeholder="Search by title, excerpt, tag or category">
  <label for="archive-language-filter">Language</label>
  <select id="archive-language-filter">
    <option value="all">All languages</option>
    <option value="en">English</option>
    <option value="fr">Français</option>
  </select>
  <p id="archive-search-status" class="archive-search__status" aria-live="polite"></p>
</div>

<div class="archive-list archive-list--cards" id="archive-results">
  {% for post in site.posts %}
    {% include post-card.html post=post excerpt_limit=210 tag_limit=4 heading_level="h2" %}
  {% endfor %}
</div>

<script>
  (function () {
    var input = document.getElementById('archive-search-input');
    var language = document.getElementById('archive-language-filter');
    var status = document.getElementById('archive-search-status');
    var cards = Array.prototype.slice.call(document.querySelectorAll('#archive-results .post-card'));

    function updateArchive() {
      var query = input.value.trim().toLowerCase();
      var selectedLanguage = language.value;
      var visible = 0;

      cards.forEach(function (card) {
        var matchesQuery = !query || (card.getAttribute('data-search') || '').indexOf(query) !== -1;
        var matchesLanguage = selectedLanguage === 'all' || card.getAttribute('data-lang') === selectedLanguage;
        var show = matchesQuery && matchesLanguage;
        card.hidden = !show;
        if (show) visible += 1;
      });

      status.textContent = visible + ' post' + (visible === 1 ? '' : 's') + ' shown';
    }

    input.addEventListener('input', updateArchive);
    language.addEventListener('change', updateArchive);
    updateArchive();
  }());
</script>
