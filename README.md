# Dramane Bako — professional and academic portfolio

Public portfolio and bilingual knowledge hub hosted with Jekyll on GitHub Pages.

- **Website:** https://bakodramane.github.io/
- **English professional homepage:** `/`
- **French professional homepage:** `/fr/accueil/`
- **English/French articles:** `/en/` and `/fr/` (preserved)
- **Publications:** source data in `_data/publications.yml`, rendered using the shared catalogue include
- **Apps:** source data in `_data/apps.yml`, rendered using the shared app include
- **Topic translations:** `_data/topics_fr.yml`
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
- `_includes/post-summary.html` — card summary for posts: the `description` front matter, falling back to the first paragraph. Every new post should still set `description` (it also feeds search snippets).

## Content maintenance

- Preserve existing blog post URLs, paired `translation_key` values and weekly-monitor automation.
- Pair portfolio pages using `translation_en` and `translation_fr`.
- Edit publication citations and app descriptions in their YAML source files.
- Keep professional claims and academic credentials accurate and distinguish author roles from institutional publications.
- Do not insert fabricated photos, unavailable demos, performance metrics or unverified scholarly IDs.
- See `docs/content-guidelines.md` and `docs/portfolio-content-review.md`.

## Personal disclaimer

All views expressed are personal and do not represent FAO or another organisation.

## Planned blog migration (gated)

The migration PR must **not** be merged before the separate blog repository and GitHub Pages project site are live. Legacy article and section URLs are forwarded by HTML meta refresh and JavaScript, not server-side 301 redirects. The original 125 post sources remain as Git backups, but published pages forward instead of repeating the articles. The previous Atom feed becomes a one-entry migration notice; existing subscribers must re-subscribe to the new blog feed. Update the weekly bilingual publishing automation to the new repository before merging.
