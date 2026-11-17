#!/usr/bin/env python3
"""Check the portfolio-to-blog migration after a Jekyll build.

Every stub in _legacy/ must produce a page at its old permalink that forwards
to the same path on the independent blog; the old feed must be a move notice;
and the professional homepage must still be the portfolio.
"""
from pathlib import Path
import re
import sys

BLOG_BASE = "https://bakodramane.github.io/ai-official-statistics"

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
failures: list[str] = []

feed = (site / "feed.xml").read_text(encoding="utf-8")
if "feed moved" not in feed or f"{BLOG_BASE}/feed.xml" not in feed:
    failures.append("feed.xml must be a move notice that names the new feed URL.")

home = (site / "index.html").read_text(encoding="utf-8")
if "portfolio-hero" not in home:
    failures.append("index.html is no longer the professional homepage.")

stubs = sorted(Path("_legacy").rglob("*.md"))
if not stubs:
    failures.append("No legacy stubs found in _legacy/.")

for stub in stubs:
    match = re.search(r"^permalink:\s*(\S+)\s*$", stub.read_text(encoding="utf-8"), re.M)
    if not match:
        failures.append(f"{stub}: missing permalink")
        continue
    route = match.group(1)
    target = site / route.lstrip("/") / "index.html" if route.endswith("/") else site / route.lstrip("/")
    if not target.exists():
        failures.append(f"{stub}: nothing built at {route}")
        continue
    html = target.read_text(encoding="utf-8")
    expected = BLOG_BASE + route
    if 'http-equiv="refresh"' not in html or f'content="0;url={expected}"' not in html:
        failures.append(f"{route}: does not forward to {expected}")
    if 'name="robots" content="noindex' not in html:
        failures.append(f"{route}: forwarding page should be noindex")

sitemap = (site / "sitemap.xml").read_text(encoding="utf-8")
leaked = [s for s in re.findall(r"<loc>([^<]+)</loc>", sitemap) if "/ai-official-statistics/" in s]
if leaked:
    failures.append(f"sitemap.xml lists {len(leaked)} blog URLs")

for public in ("README.md", "docs", "scripts"):
    if (site / public).exists():
        failures.append(f"{public} is published; exclude it in _config.yml")

if failures:
    print("\n".join(failures), file=sys.stderr)
    raise SystemExit(1)
print(f"Verified {len(stubs)} legacy URLs forward to the blog, the feed notice and the portfolio homepage.")
