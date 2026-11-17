# Deploying the independent AI for Official Statistics blog

## Current state

This is the **standalone blog source branch**, **not** a pull request to the professional site. The main portfolio website remains at `https://bakodramane.github.io/`. The target blog website is `https://bakodramane.github.io/ai-official-statistics/`.

The complete 125-file bilingual `_posts/` archive and working Jekyll sources are already included. Automated CI has passed both the Jekyll build and the internal link checker under the `/ai-official-statistics` base path.

## One-time GitHub action

1. Go to https://github.com/new while logged in as `bakodramane`.
2. Set repository owner `bakodramane`, name `ai-official-statistics`, visibility **Public**.
3. Do **not** initialise a README, licence or .gitignore in the new repository. Create it empty.
4. Push the prepared blog branch into that repository as `main`.

### Transfer option A: simplest (preserves source Git history)

Run the following in Git Bash, using your authorised GitHub credentials:

```bash
git clone --branch ai-blog-standalone-2026-11-17 --single-branch https://github.com/bakodramane/bakodramane.github.io.git ai-blog-transfer
cd ai-blog-transfer
git remote add blog https://github.com/bakodramane/ai-official-statistics.git
git push blog HEAD:main
```

The new repository starts with the blog sources at its `main` branch but also inherits the old public Git history. Do **not** push the `main` branch from the professional portfolio as the blog.

### Transfer option B: clean independent repository history (recommended)

In Git Bash or a Unix shell:

```bash
git clone --branch ai-blog-standalone-2026-11-17 --single-branch https://github.com/bakodramane/bakodramane.github.io.git blog-source
mkdir ai-official-statistics-clean
cd blog-source
git archive HEAD | tar -x -C ../ai-official-statistics-clean
cd ../ai-official-statistics-clean
git init -b main
git add -A
git commit -m "Initial independent bilingual AI for Official Statistics blog"
git remote add origin https://github.com/bakodramane/ai-official-statistics.git
git push -u origin main
```

This creates a new source history with no portfolio commits or files.

## Publish and validate

1. In the new repository, go to **Settings → Pages → Build and deployment**.
2. Select **Deploy from a branch** using `main` and `/(root)`.
3. Open `https://bakodramane.github.io/ai-official-statistics/` and `https://bakodramane.github.io/ai-official-statistics/fr/accueil/`.
4. Confirm the two article listings under `/en/` and `/fr/`, a dated article in each language, language-switching, `/archive/`, `/knowledge-hub/`, and `/feed.xml`.
5. Check the repository **Actions** tab: the `AI blog — build and link checks` workflow must pass. It checks project-base links, generated feeds and bilingual index pages.
6. Keep the original professional portfolio unchanged until the new blog works.

## Switch weekly publication automation

Update the existing **Weekly bilingual AI blog update** scheduled task **only after the blog repository is live**. Replace:

- Repository: `https://github.com/bakodramane/bakodramane.github.io`
- New target repository: `https://github.com/bakodramane/ai-official-statistics`
- Website: `https://bakodramane.github.io/ai-official-statistics/`
- Branch naming, Monday schedule, source-quality requirements, EN/FR paired `translation_key`, `lang`, FR permalinks, human review and PR flow: **retain unchanged**.

Once an automated run has successfully opened its first PR against the new repository, proceed with the portfolio migration PR.

## Cut over the professional portfolio

The portfolio migration PR is tracked separately at https://github.com/bakodramane/bakodramane.github.io/pull/33.

After the blog is deployed and the scheduled task is migrated, review and merge that PR. It replaces the old article pages with HTML forwarding pages, moves the visible blog navigation to the new site, and leaves the professional portfolio intact.

These forwarding pages are **not HTTP 301 redirects**. Existing RSS subscribers need the new feed URL.

## Never change without verification

- Old public post URL patterns and paired EN/FR `translation_key` metadata.
- The `baseurl` unless actually configuring a domain.
- The personal/FAO disclaimer and source attribution.
- The weekly automation's publication dates, required source-quality conditions and review process.
