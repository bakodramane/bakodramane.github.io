# AI for Official Statistics — Independent bilingual blog

**Planned publication address:** https://bakodramane.github.io/ai-official-statistics/

This source branch prepares a separate GitHub Pages project site for [Dramane Bako](https://bakodramane.github.io/). It contains the full original bilingual AI article archive, Weekly Monitor, methodological knowledge hub, resources, topic pages and RSS feed. The professional portfolio remains at the root site.

**Repository target:** `bakodramane/ai-official-statistics` (requires creation in GitHub before deployment).

## Deployment

1. Create a **public empty repository** named `ai-official-statistics` in the same GitHub account.
2. Push this branch's **files** to that repository's `main` branch. If creating a clean-history repository, use the instructions in the migration PR rather than merging this branch into the portfolio.
3. In the new repository: Settings → Pages → Deploy from a branch → `main` / `/(root)`.
4. Confirm the blog at `https://bakodramane.github.io/ai-official-statistics/`.
5. Validate EN/FR URLs, article translation switches, RSS and archives before redirecting the original site.
6. Update the scheduled bilingual blog publishing task's repository and branch target to the new `ai-official-statistics` repository.

`_config.yml` uses `url: https://bakodramane.github.io` and `baseurl: /ai-official-statistics`. Keep this when using the default GitHub Pages project URL; change both only when a custom domain is actually configured.

## Local validation

```bash
bundle install
bundle exec jekyll build
python3 scripts/check_site_links.py _site --baseurl /ai-official-statistics
```

## Publishing compatibility

Keep paired `translation_key`, `lang` and French `/fr/` permalinks on all posts. Existing weekly content format and source citation conventions are preserved. The website may not be live until the new repository is created and Pages enabled.

All statements and commentary are personal, not institutional.
