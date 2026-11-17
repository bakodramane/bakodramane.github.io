#!/usr/bin/env python3
"""Check a staged portfolio-to-blog migration after a Jekyll build."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
feed = (site / "feed.xml").read_text(encoding="utf-8")
if "feed moved" not in feed or "ai-official-statistics/feed.xml" not in feed:
    raise SystemExit("Old Atom feed must be a migration notice with the new feed URL.")

home = (site / "index.html").read_text(encoding="utf-8")
if "Dramane" not in home or "portfolio-hero" not in home:
    raise SystemExit("Professional homepage has been lost or replaced.")

for page in ["en/index.html", "fr/index.html", "weekly-monitor/index.html",
             "knowledge-hub/index.html", "topics/index.html", "methods/index.html"]:
    html = (site / page).read_text(encoding="utf-8")
    if 'http-equiv="refresh"' not in html or "ai-official-statistics/" not in html:
        raise SystemExit(f"Missing forwarding page at {page}")

redirects = 0
for html_file in site.rglob("*.html"):
    html = html_file.read_text(encoding="utf-8")
    if 'http-equiv="refresh"' in html and 'ai-official-statistics/' in html:
        redirects += 1

posts_count = len(list(Path("_posts").glob("*.md")))
if redirects < posts_count:
    raise SystemExit(f"Only {redirects} redirect pages for {posts_count} legacy posts.")

print(f"Verified {redirects} forwarding pages, portfolio homepage, and Atom migration notice.")
