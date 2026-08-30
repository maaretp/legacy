#!/usr/bin/env python3
"""Tidy the generated entry files and (re)generate the README.md index tables.

Run after fetch_contributions.py. First trims trailing site-chrome / "more
episodes" noise from every entry file, then scans their frontmatter and rewrites
each folder's README.md with an index table.
"""
import os
import re

REPO = os.environ.get(
    "LEGACY_REPO",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# A whole line equal to (or, for the few marked with a trailing space, starting
# with) one of these ends the useful content — the rest is navigation, a comment
# section, or a list of other episodes/articles. Kept deliberately conservative:
# these must never plausibly appear inside real prose.
CUT_MARKERS = [
    "Log In or Register to post comments", "User Comments", "Community Sponsor",
    "Lets Hang!", "Featured Resources", "Leave a Reply", "Leave a Comment",
    "Post navigation", "Related Posts", "Related Episodes", "More Episodes",
    "You might also like", "Recent Posts", "Recent Episodes",
    "Oh, here is more", "Explore our resources",
    "May I Ask You For a Favor", "SUBSCRIBE & DOWNLOAD",
    "This site uses Akismet to reduce spam",
    "Sign up to receive insightful content",
]


def tidy(path):
    txt = open(path, encoding="utf-8").read()
    head, sep, body = txt.partition("\n---\n\n")
    if not sep:
        head, sep, body = txt.partition("\n---\n")
    lines = body.splitlines()
    cut = len(lines)
    for i, ln in enumerate(lines):
        s = ln.strip().lstrip("#").strip()
        if any(s == m or (m.endswith(" ") and s.startswith(m)) for m in CUT_MARKERS):
            cut = i
            break
    new_body = re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:cut]).rstrip())
    out = head + sep + new_body + "\n"
    if out != txt and len(new_body) > 0:
        open(path, "w", encoding="utf-8").write(out)


def parse(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", txt, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    body = txt[m.end():] if m else txt
    # retrieval note
    note = ""
    nm = re.search(r"> Retrieval note: (.+?)\.?\n", txt)
    if nm:
        note = nm.group(1)
    # rough word count of captured text (after the --- separator)
    parts = txt.split("\n---\n", 2)
    captured = parts[2] if len(parts) > 2 else ""
    wc = len(captured.split())
    has_text = "No readable text could be retrieved" not in captured and wc > 40
    return fm, note, wc, has_text


def build(folder, title, blurb, col):
    d = os.path.join(REPO, folder)
    files = sorted([f for f in os.listdir(d) if f.endswith(".md")
                    and f != "README.md"], reverse=True)
    rows = []
    n_text = 0
    for f in files:
        tidy(os.path.join(d, f))
        fm, note, wc, has_text = parse(os.path.join(d, f))
        if has_text:
            n_text += 1
        date = fm.get("date", "")
        rows.append((date, fm.get("title", f), col and fm.get(col, ""),
                     f, "yes (~%d words)" % wc if has_text else "link only",
                     fm.get("url", ""), note))

    lines = [
        f"# {title}",
        "",
        blurb,
        "",
        f"**{len(files)} entries — {n_text} with captured text, "
        f"{len(files) - n_text} link-only.** "
        "Each entry is a Markdown file with YAML frontmatter (title, "
        f"{'show' if folder == 'podcasts' else 'publication'}, date, url, "
        "retrieval note) followed by whatever readable text the source "
        "exposed. Where the text came from the Wayback Machine or a PDF/DOCX "
        "the frontmatter `source_retrieved` records that.",
        "",
        "Regenerate: `python3 fetch_contributions.py` then "
        "`python3 gen_readme.py` (both scripts live in `podcasts/`). "
        "Source of record: <https://maaretp.com/contributions/>.",
        "",
        f"| Date | {'Show' if folder == 'podcasts' else 'Publication'} | "
        "Title | Text | File |",
        "|------|------|-------|------|------|",
    ]
    for date, ttl, plat, fn, txt, url, note in rows:
        ttl = ttl.replace("|", "\\|")
        lines.append(f"| {date} | {plat} | [{ttl}]({url}) | {txt} | "
                     f"[`{fn}`](./{fn}) |")
    lines.append("")
    open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(
        "\n".join(lines))
    print(f"wrote {folder}/README.md  ({len(files)} entries, {n_text} w/ text)")


build("external-articles",
      "External Articles",
      "Articles and papers I contributed to other people's platforms — "
      "blogs, magazines, books and conference proceedings — collected from "
      "<https://maaretp.com/contributions/> so the text survives the "
      "platforms. Everything here is my own writing; licensed CC BY like the "
      "rest of this repo. Some sources are gone or paywalled and are kept as "
      "link-only records.",
      "publication")

build("podcasts",
      "Podcast Appearances",
      "Podcast episodes, recorded panels and live conversations I took part "
      "in, collected from <https://maaretp.com/contributions/>. Most are "
      "audio-only with no published transcript, so each file holds the show "
      "notes / description the episode page carried, not a transcript. The "
      "YouTube-hosted ones carry the video description (still not a "
      "transcript).",
      "show")
