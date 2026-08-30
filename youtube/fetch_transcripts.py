#!/usr/bin/env python3
"""Fetch transcripts for every talk on my YouTube channel.

This enumerates the channel with yt-dlp, downloads the English caption track and
video metadata for each video, and writes one Markdown file per talk into
`youtube/transcripts/` with YAML frontmatter (title, video id, url, upload date,
duration, tags) followed by the cleaned transcript text.

The channel only has auto-generated captions, so transcripts have no punctuation
or casing ("marek pujarvi" rather than "Maaret Pyhajarvi"). They are still useful
as a searchable record and a starting point for turning talks into articles.

Prerequisites:
  * yt-dlp on PATH.  Install with:  brew install yt-dlp
    (no API key or login is needed for public videos with public captions)

It also reads `youtube/extra-videos.txt` (one id/URL per line) for talks and
interviews that live on other people's channels, and processes those too.

Usage:
  python3 fetch_transcripts.py                 # channel + extra-videos.txt, skip existing
  python3 fetch_transcripts.py --no-channel    # only extra-videos.txt
  python3 fetch_transcripts.py --force         # re-fetch and overwrite all
  python3 fetch_transcripts.py --keep-vtt      # also keep the raw .vtt files
  python3 fetch_transcripts.py --url <video>   # just one video (id or full URL)
  python3 fetch_transcripts.py --list          # print the channel video list only

Output:
  youtube/transcripts/<YYYYMMDD>-<slug>.md     one file per talk
  youtube/video-index.csv                      id, date, duration, title, url
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys
import tempfile

CHANNEL_URL = "https://www.youtube.com/channel/UCrTlIKuIS-LmRk-aAbcxTKg/videos"

HERE = os.path.dirname(os.path.abspath(__file__))
TRANSCRIPTS_DIR = os.path.join(HERE, "transcripts")
INDEX_CSV = os.path.join(HERE, "video-index.csv")
# Talks/interviews on other people's channels, one id or URL per line.
EXTRA_FILE = os.path.join(HERE, "extra-videos.txt")

# Caption tracks to try, in order of preference. "en-orig" is the original
# English auto-caption; "en" is the (identical, for English talks) default.
SUB_LANGS = "en-orig,en"


def run(cmd):
    """Run a command, returning (returncode, stdout, stderr)."""
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def require_yt_dlp():
    rc, out, _ = run(["yt-dlp", "--version"])
    if rc != 0:
        sys.exit("yt-dlp not found. Install it with:  brew install yt-dlp")
    return out.strip()


def list_videos(url=CHANNEL_URL):
    """Return [{id, title, upload_date?}] for every video, newest first."""
    rc, out, err = run(
        ["yt-dlp", "--flat-playlist", "--dump-single-json", url]
    )
    if rc != 0:
        sys.exit(f"Could not list channel videos:\n{err}")
    data = json.loads(out)
    entries = data.get("entries") or []
    videos = []
    for e in entries:
        if not e.get("id"):
            continue
        videos.append({"id": e["id"], "title": e.get("title") or e["id"]})
    return videos


def video_id(s):
    """Pull a bare 11-char video id out of an id or any YouTube URL."""
    s = s.strip()
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", s)
    if m:
        return m.group(1)
    return s.split("&")[0].split("?")[0]


def read_extra_ids():
    if not os.path.exists(EXTRA_FILE):
        return []
    ids = []
    with open(EXTRA_FILE, encoding="utf-8") as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if line:
                ids.append(video_id(line))
    return ids


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "video"


_TAG_RE = re.compile(r"<[^>]+>")
_UNESCAPE = (("&amp;", "&"), ("&#39;", "'"), ("&quot;", '"'),
             ("&lt;", "<"), ("&gt;", ">"), ("&nbsp;", " "))


def clean_vtt(path):
    """Turn a YouTube auto-caption .vtt file into de-duplicated plain text.

    Auto-captions scroll: each cue repeats the previous line and adds one new
    line, and carries per-word <timestamp> tags. We strip the tags and keep a
    line only when it differs from the last line already emitted.
    """
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    lines = []
    for block in raw.split("\n\n"):
        for line in block.splitlines():
            if line.startswith("WEBVTT") or line.startswith("Kind:") \
                    or line.startswith("Language:") or "-->" in line:
                continue
            line = _TAG_RE.sub("", line)
            for a, b in _UNESCAPE:
                line = line.replace(a, b)
            line = line.strip()
            if not line:
                continue
            if lines and lines[-1] == line:
                continue
            lines.append(line)
    return "\n".join(lines).strip()


def find_sub_file(workdir, vid):
    for lang in ("en-orig", "en"):
        cand = os.path.join(workdir, f"{vid}.{lang}.vtt")
        if os.path.exists(cand):
            return cand
    # fall back to whatever .vtt landed
    for name in sorted(os.listdir(workdir)):
        if name.endswith(".vtt"):
            return os.path.join(workdir, name)
    return None


def fetch_one(vid, force=False, keep_vtt=False):
    """Fetch metadata + transcript for one video id; write the .md file.

    Returns a dict row for the index, or None if skipped/failed.
    """
    url = f"https://www.youtube.com/watch?v={vid}"

    with tempfile.TemporaryDirectory() as workdir:
        outtmpl = os.path.join(workdir, "%(id)s.%(ext)s")
        # Metadata first, on its own, so a rate-limited caption download does
        # not cost us the whole entry.
        rc, _, err = run([
            "yt-dlp", "--skip-download", "--write-info-json",
            "-o", outtmpl, url,
        ])
        info_path = os.path.join(workdir, f"{vid}.info.json")
        if rc != 0 or not os.path.exists(info_path):
            print(f"  ! {vid}: yt-dlp failed\n{err.strip()}")
            return None
        # Captions in a second call; tolerate failure (429, none available).
        rc2, _, err2 = run([
            "yt-dlp", "--skip-download",
            "--write-auto-subs", "--write-subs",
            "--sub-langs", SUB_LANGS, "--sub-format", "vtt",
            "-o", outtmpl, url,
        ])
        if rc2 != 0:
            print(f"  ~ {vid}: caption download failed ({err2.strip().splitlines()[-1] if err2.strip() else 'unknown'})")

        with open(info_path, encoding="utf-8") as fh:
            info = json.load(fh)

        date = info.get("upload_date") or "00000000"
        title = info.get("title") or vid
        slug = slugify(title)
        md_path = os.path.join(TRANSCRIPTS_DIR, f"{date}-{slug}.md")

        row = {
            "id": vid,
            "upload_date": date,
            "duration": info.get("duration_string") or "",
            "title": title,
            "url": info.get("webpage_url") or url,
        }

        if os.path.exists(md_path) and not force:
            print(f"  = {os.path.basename(md_path)} (exists, skipping)")
            return row

        sub_path = find_sub_file(workdir, vid)
        transcript = clean_vtt(sub_path) if sub_path else ""
        if not transcript:
            print(f"  ! {vid}: no caption track found")

        if keep_vtt and sub_path:
            os.replace(sub_path, os.path.join(
                TRANSCRIPTS_DIR, f"{date}-{slug}.vtt"))

        tags = ", ".join(info.get("tags") or [])
        description = (info.get("description") or "").strip()

        front = [
            "---",
            f'title: "{title.replace(chr(34), chr(39))}"',
            f"video_id: {vid}",
            f"url: {row['url']}",
            f"upload_date: {date}",
            f"duration: {row['duration']}",
            f"channel: {info.get('channel') or ''}",
            f'tags: [{tags}]',
            "---",
            "",
            f"# {title}",
            "",
        ]
        if description:
            front.append("> " + description.replace("\n", "\n> "))
            front.append("")
        front.append("## Transcript")
        front.append("")
        front.append("_Auto-generated captions from YouTube; no punctuation or "
                     "casing. Lightly de-duplicated._")
        front.append("")
        front.append(transcript if transcript else "_(no transcript available)_")
        front.append("")

        with open(md_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(front))
        print(f"  + {os.path.basename(md_path)}")
        return row


def write_index(rows):
    """Merge the rows from this run into video-index.csv (keyed by id)."""
    fields = ["id", "upload_date", "duration", "title", "url"]
    merged = {}
    if os.path.exists(INDEX_CSV):
        with open(INDEX_CSV, newline="", encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                merged[r["id"]] = r
    for r in rows:
        merged[r["id"]] = {k: r.get(k, "") for k in fields}
    out = sorted(merged.values(),
                 key=lambda r: r.get("upload_date", ""), reverse=True)
    with open(INDEX_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f"\nWrote {INDEX_CSV} ({len(out)} videos)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true",
                    help="re-fetch and overwrite existing transcript files")
    ap.add_argument("--keep-vtt", action="store_true",
                    help="also keep the raw .vtt caption file next to the .md")
    ap.add_argument("--url", metavar="VIDEO",
                    help="fetch a single video (id or URL) instead of the channel")
    ap.add_argument("--no-channel", action="store_true",
                    help="skip the channel; only process extra-videos.txt")
    ap.add_argument("--list", action="store_true",
                    help="just print the channel video list and exit")
    args = ap.parse_args()

    print("yt-dlp", require_yt_dlp())
    os.makedirs(TRANSCRIPTS_DIR, exist_ok=True)

    if args.list:
        for v in list_videos():
            print(f"{v['id']}  {v['title']}")
        return

    if args.url:
        videos = [{"id": video_id(args.url), "title": video_id(args.url)}]
    else:
        videos = [] if args.no_channel else list_videos()
        if not args.no_channel:
            print(f"Channel has {len(videos)} videos")
        seen = {v["id"] for v in videos}
        extra = [i for i in read_extra_ids() if i not in seen]
        if extra:
            print(f"+ {len(extra)} extra videos from extra-videos.txt")
            videos += [{"id": i, "title": i} for i in extra]
        print()

    rows = []
    for i, v in enumerate(videos, 1):
        print(f"[{i}/{len(videos)}] {v['title']}")
        row = fetch_one(v["id"], force=args.force, keep_vtt=args.keep_vtt)
        if row:
            rows.append(row)

    if rows and not args.url:
        write_index(rows)


if __name__ == "__main__":
    main()
