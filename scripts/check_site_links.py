#!/usr/bin/env python3
"""Check internal links in a built Jekyll site using only the Python standard library.

Supports custom domain/root hosting and index.html directory permalinks.
Checks that internal targets and same-page or cross-page anchors exist.
External links are deliberately excluded (they require separate live monitoring).
"""
from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

SITE_HOSTS = {"bakodramane.github.io"}

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag == "a" and a.get("href"):
            self.links.append((a["href"], self.getpos()[0]))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site_dir", type=Path, nargs="?", default=Path("_site"))
    parser.add_argument("--baseurl", default="", help="GitHub Pages project path, e.g. /ai-official-statistics")
    args = parser.parse_args()
    baseurl = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    site = args.site_dir.resolve()
    html = sorted(site.rglob("*.html"))
    if not html:
        print(f"No generated HTML found in {site}", file=sys.stderr)
        return 2

    pages: dict[Path, LinkParser] = {}
    for file in html:
        page = LinkParser()
        page.feed(file.read_text(encoding="utf-8"))
        pages[file] = page

    failures: list[str] = []
    checked = 0
    for file, page in pages.items():
        for href, line in page.links:
            parts = urlsplit(href.strip())
            if parts.scheme and parts.scheme not in ("http", "https"):
                continue
            if parts.netloc and parts.netloc not in SITE_HOSTS:
                continue
            if parts.scheme and not parts.netloc:
                continue
            target_path = unquote(parts.path)
            if baseurl and target_path.startswith("/"):
                if target_path == baseurl or target_path.startswith(baseurl + "/"):
                    target_path = target_path[len(baseurl):] or "/"
                elif parts.netloc in SITE_HOSTS:
                    # A fully qualified URL outside this project belongs to the portfolio.
                    continue
                else:
                    failures.append(f"{file.relative_to(site)}:{line}: root-relative URL lacks project baseurl: {href}")
                    continue
            if not target_path:
                target = file
            elif target_path.startswith("/"):
                target = site / target_path.lstrip("/")
            else:
                target = file.parent / target_path

            target = target.resolve()
            try:
                target.relative_to(site)
            except ValueError:
                failures.append(f"{file.relative_to(site)}:{line}: link outside site: {href}")
                continue

            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                failures.append(f"{file.relative_to(site)}:{line}: missing target: {href}")
                continue
            checked += 1
            if parts.fragment and target.suffix.lower() == ".html":
                anchor = unquote(parts.fragment)
                if target not in pages or anchor not in pages[target].ids:
                    failures.append(f"{file.relative_to(site)}:{line}: missing fragment: {href}")

    print(f"Checked {checked} internal links on {len(pages)} HTML pages.")
    if failures:
        for issue in failures[:100]:
            print(issue, file=sys.stderr)
        print(f"{len(failures)} broken internal link(s) detected.", file=sys.stderr)
        return 1
    print("All tested internal targets and anchors resolve.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
