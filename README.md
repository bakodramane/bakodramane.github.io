# Dramane Bako — professional and academic portfolio

Bilingual (English/French) professional portfolio, built with Jekyll on GitHub Pages.

- **Website:** https://bakodramane.github.io/
- **English professional homepage:** `/`
- **French professional homepage:** `/fr/accueil/`
- **AI blog:** separate repository, see [AI blog](#ai-blog) below
- **Publications:** source data in `_data/publications.yml`, rendered using the shared catalogue include
- **Apps:** source data in `_data/apps.yml`, rendered using the shared app include
- **Publication topic translations:** `_data/publication_topics_fr.yml`
- **Bilingual navigation:** `_data/navigation.yml`
- **Site styling:** `assets/main.scss`

## Local development

Requires Ruby and Bundler compatible with the `github-pages` gem.

```sh
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000/`. Before opening or merging a PR, run:

```sh
bundle exec jekyll build
python3 scripts/check_site_links.py _site
```

The CI workflow runs these checks on pull requests and updates to `main`.

`Gemfile.lock` lists both the Windows (`x64-mingw-ucrt`) and Linux (`x86_64-linux`) platforms so the same lockfile installs locally and in CI. On another platform (for example macOS), run `bundle lock --add-platform <platform>` once and commit the result.

## Shared includes

- `_includes/featured-publications.html` — featured research on both home pages and the publications pages; edit the marker list there to change the selection.
- `_includes/publication-citation.html` — renders a citation and highlights the author's name.
- `_includes/blog-latest.html` — the latest three blog articles on each home page, read from the blog's feed in the browser, with a static link panel as fallback.

## Content maintenance

- Pair portfolio pages using `translation_en` and `translation_fr`.
- Edit publication citations and app descriptions in their YAML source files.
- Keep professional claims and academic credentials accurate and distinguish author roles from institutional publications.
- Do not insert fabricated photos, unavailable demos, performance metrics or unverified scholarly IDs.
- See `docs/content-guidelines.md` and `docs/portfolio-content-review.md`.

## Personal disclaimer

All views expressed are personal and do not represent FAO or another organisation.

## AI blog

The AI for Official Statistics blog is a separate site: [bakodramane/ai-official-statistics](https://github.com/bakodramane/ai-official-statistics), published at https://bakodramane.github.io/ai-official-statistics/. Its posts, weekly automation and post guidelines live there.

This repository keeps only small forwarding stubs for the former blog URLs, in `_legacy/`. GitHub Pages cannot send server-side 301 redirects, so each stub is an HTML page with a meta refresh, a script redirect that keeps any `#anchor`, and a canonical link to the new address. `/feed.xml` is a one-entry notice pointing subscribers to the new feed, `robots.txt` lists the blog sitemap, and `404.html` offers the same path on the blog.
