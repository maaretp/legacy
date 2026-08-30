#!/usr/bin/env python3
"""Fetch a URL (with Wayback fallback) and print readable main-content text.

Usage: python3 extract.py <url> [--wayback] [--raw]
"""
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")


def curl(url):
    r = subprocess.run(
        ["curl", "-sL", "-A", UA, "--max-time", "40", "--compressed", url],
        capture_output=True)
    return r.stdout.decode("utf-8", "replace")


def _get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as fh:
                return fh.read().decode("utf-8", "replace")
        except Exception as e:
            if i == tries - 1:
                print(f"[net error {url[:80]}: {e}]", file=sys.stderr)
    return ""


def wayback_url(url, prefer_early=True):
    """Return a usable Wayback snapshot URL.

    Prefer the earliest HTTP-200 text/html capture from the CDX index (recent
    'closest' snapshots are often parked-domain or redirect stubs), then fall
    back to the availability API.
    """
    if prefer_early:
        cdx = ("http://web.archive.org/cdx/search/cdx?url="
               + urllib.parse.quote(url, "")
               + "&output=json&filter=statuscode:200&filter=mimetype:text/html"
               + "&collapse=digest&limit=8")
        raw = _get(cdx)
        try:
            rows = json.loads(raw) if raw else []
            if len(rows) > 1:
                ts = rows[1][1]
                return f"https://web.archive.org/web/{ts}/{url}"
        except Exception:
            pass
    raw = _get("http://archive.org/wayback/available?url="
               + urllib.parse.quote(url, ""))
    try:
        snap = json.loads(raw).get("archived_snapshots", {}).get("closest", {})
        if snap.get("available"):
            return snap["url"].replace("http://", "https://", 1)
    except Exception:
        pass
    return None


def looks_blocked(html):
    if len(html) < 1500:
        return True
    low = html[:4000].lower()
    return ("just a moment" in low or "enable javascript and cookies" in low
            or "captcha-delivery" in low or "attention required" in low)


def extract(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # If this is a Wayback page, drop their toolbar
    for sel in ["#wm-ipp-base", "#wm-ipp", "#donato", "script", "style",
                "noscript", "nav", "header", "footer", "aside", "form",
                ".sidebar", ".site-header", ".site-footer", ".nav",
                ".menu", ".cookie", ".newsletter", ".related-posts",
                ".share", ".social", ".comments", "#comments"]:
        for el in soup.select(sel):
            el.decompose()

    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True) or title

    # pick the densest container
    candidates = soup.select("article, main, [role=main], .post-content, "
                             ".entry-content, .article-content, .blog-post, "
                             ".post-body, .rich-text, .content, .post, "
                             ".episode-description, .show-notes, .shownotes, "
                             ".episode-content, .episode__description, "
                             "[itemprop=description], .single-content, "
                             ".elementor-widget-container, .fl-module-content")
    best = None
    best_len = 0
    for c in candidates:
        t = c.get_text(" ", strip=True)
        if len(t) > best_len:
            best, best_len = c, len(t)
    if best is None or best_len < 400:
        best = soup.body or soup

    lines = []
    for el in best.descendants:
        if el.name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            txt = el.get_text(" ", strip=True)
            if txt:
                lines.append("\n" + "#" * int(el.name[1]) + " " + txt + "\n")
        elif el.name == "li":
            txt = el.get_text(" ", strip=True)
            if txt:
                lines.append("- " + txt)
        elif el.name == "p":
            txt = el.get_text(" ", strip=True)
            if txt:
                lines.append(txt + "\n")
        elif el.name == "blockquote":
            txt = el.get_text(" ", strip=True)
            if txt:
                lines.append("> " + txt + "\n")
        elif el.name == "pre":
            txt = el.get_text("\n", strip=False)
            if txt.strip():
                lines.append("```\n" + txt.strip("\n") + "\n```\n")

    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    # Fallback: meta description / og:description when body text is thin
    if len(text) < 200:
        for sel, attr in [("meta[property='og:description']", "content"),
                          ("meta[name='description']", "content"),
                          ("meta[name='twitter:description']", "content")]:
            m = soup.select_one(sel)
            if m and m.get(attr) and len(m[attr].strip()) > len(text):
                text = m[attr].strip()
    return title, text


def main():
    args = sys.argv[1:]
    force_wb = "--wayback" in args
    raw = "--raw" in args
    url = [a for a in args if not a.startswith("--")][0]

    html = "" if force_wb else curl(url)
    src = url
    if force_wb or looks_blocked(html):
        wb = wayback_url(url)
        if wb:
            print(f"[using wayback: {wb}]", file=sys.stderr)
            html = curl(wb)
            src = wb
        elif force_wb:
            print("[no wayback snapshot found]", file=sys.stderr)

    if raw:
        print(html)
        return

    if looks_blocked(html):
        print(f"SOURCE: {src}\n\n[could not retrieve readable content — "
              f"blocked or empty]")
        return

    title, text = extract(html)
    print(f"SOURCE: {src}\nTITLE: {title}\n\n{text}")


if __name__ == "__main__":
    main()
