# Content guidelines

This repository is the professional and academic portfolio of Dramane Bako. The homepage, professional pages, publication catalogue and programme/project case studies must foreground verifiable contributions and distinguish personal views from institutional positions.

The **AI for Official Statistics** blog lives in its own repository, [bakodramane/ai-official-statistics](https://github.com/bakodramane/ai-official-statistics), which also holds the post-writing guidelines. Do not add posts here.

## Portfolio and bilingual pages

The main portfolio pages have parallel English and French versions. Every new professional page should define `lang`, `translation_en` and `translation_fr` in front matter. The bilingual publication catalogue is rendered from `_data/publications.yml` through `_includes/publications-catalog.html`; do not manually duplicate references in translated pages.

Professional assertions must be supported by CV/publication evidence. Attribute institutional outputs correctly; do not imply sole authorship or claim unmeasured outcomes. Add photographs, screenshots, downloadable CV files, ORCID/Google Scholar identifiers and project metrics only after confirmation. Never use invented placeholders as if they were real.

## Former blog URLs

`_legacy/` holds one small stub per former blog URL (120 posts and 16 section pages). Each builds a `noindex` page at the old address that forwards to the same path on the blog. Keep these files: they are what keeps old links and search results working. CI (`scripts/check_migration.py`) fails if a stub stops forwarding.

Use this disclaimer where appropriate:

> Views are personal and do not represent any institution.
