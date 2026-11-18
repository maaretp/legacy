#!/usr/bin/env python3
"""Fetch new LinkedIn activity from the Member Changelog API (DMA).

The Member Snapshot API (fetch_member_snapshot.py) gives history up to the time
you consented; the Changelog API gives everything since, but only for the last
28 days. Run this at least every four weeks or posts fall off the window.

Same token as fetch_member_snapshot.py (LI_TOKEN env var, --token, or .li_token).

Usage:
  export LI_TOKEN="<access_token>"
  python3 fetch_changelog.py                          # since the newest Shares_changelog_*.json here
  python3 fetch_changelog.py --since 2026-10-20       # since a date (UTC), clamped to 28 days by LinkedIn
  python3 fetch_changelog.py --rebuild Shares_changelog_20260921-20261005.json
                                                      # rewrite the CSV from a saved JSON, no API call

Output (dates are the first and last event captured, UTC):
  Changelog_<from>-<to>.json         every raw event (posts, comments, reactions, ...)
  Shares_changelog_<from>-<to>.json  raw events for your posts (resourceName ugcPosts)
  Shares_changelog_<from>-<to>.csv   one row per post, latest version, same columns
                                     as Shares.csv in the "Download your data" export

Notes:
  * The endpoint only accepts  Linkedin-Version: 202312 .
  * startTime is inclusive, so each page re-sends the last event; events are
    de-duplicated by id.
  * If the API returns nothing at all, check that changelog generation is on:
    python3 fetch_changelog.py --check-authorization
"""

import argparse
import csv
import datetime
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from fetch_member_snapshot import SSL_CTX, VERSION

BASE = "https://api.linkedin.com/rest"
COUNT = 10            # LinkedIn recommends 10
MAX_COUNT = 50        # the API rejects anything above this
WINDOW_DAYS = 28
SHARE_COLUMNS = ["Date", "ShareLink", "ShareCommentary", "SharedUrl", "MediaUrl", "Visibility"]
HERE = os.path.dirname(os.path.abspath(__file__))


def api_get(token, path, params):
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Linkedin-Version", VERSION)
    req.add_header("Content-Type", "application/json")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as resp:
                return json.loads(resp.read().decode("utf-8")), None
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code == 429 or e.code >= 500:
                wait = 10 * (attempt + 1)
                print(f"    HTTP {e.code}, sleeping {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            return None, f"HTTP {e.code}: {body[:500]}"
        except urllib.error.URLError as e:
            wait = 5 * (attempt + 1)
            print(f"    network error {e.reason}, retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    return None, "gave up after retries"


def collect_events(token, start_time, max_pages=2000):
    """Page forward by processedAt, as the docs recommend, until nothing new comes back."""
    events = {}
    count = COUNT
    for _ in range(max_pages):
        params = {"q": "memberAndApplication", "count": count}
        if start_time:
            params["startTime"] = start_time
        page, err = api_get(token, "memberChangeLogs", params)
        if err:
            sys.exit(f"  ! stopped at startTime={start_time}: {err}")
        elements = page.get("elements") or []
        new = [e for e in elements if e.get("id") not in events]
        if not new:
            if len(elements) >= count and start_time:
                # a full page all at one processedAt: widen to the API maximum, then step past it
                if count < MAX_COUNT:
                    count = MAX_COUNT
                else:
                    print(f"  ! over {MAX_COUNT} events at processedAt={start_time}; some may be missed",
                          file=sys.stderr)
                    start_time += 1
                continue
            break
        for e in new:
            events[e["id"]] = e
        start_time = max(e.get("processedAt") or 0 for e in new)
        count = COUNT
        print(f"  +{len(new)} events (total {len(events)}), next startTime={start_time}")
        time.sleep(0.5)
    return sorted(events.values(), key=lambda e: (e.get("capturedAt") or 0, e.get("id") or 0))


def utc(ms, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).strftime(fmt)


def share_row(event):
    activity = event.get("activity") or {}
    content = (activity.get("specificContent") or {}).get("com.linkedin.ugc.ShareContent") or {}
    media = content.get("media") or []
    created = (activity.get("created") or {}).get("time") or event.get("capturedAt")
    return {
        "Date": utc(created),
        "ShareLink": "https://www.linkedin.com/feed/update/"
                     + urllib.parse.quote(event["resourceId"], safe=""),
        "ShareCommentary": (content.get("shareCommentary") or {}).get("text", ""),
        "SharedUrl": next((m["originalUrl"] for m in media if m.get("originalUrl")), ""),
        "MediaUrl": media[0].get("media", "") if media else "",
        "Visibility": next(iter((activity.get("visibility") or {}).values()), ""),
    }


def share_rows(share_events):
    """One row per post: later events (edits) replace earlier ones, deletes drop the post."""
    latest = {}
    for e in share_events:
        if e.get("method") == "DELETE":
            latest.pop(e.get("resourceId"), None)
        elif e.get("activity"):
            latest[e["resourceId"]] = e
    rows = [share_row(e) for e in latest.values()]
    return sorted(rows, key=lambda r: r["Date"], reverse=True)


def write_shares_csv(path, share_events):
    rows = share_rows(share_events)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=SHARE_COLUMNS)
        w.writeheader()
        w.writerows(rows)
    print(f"  wrote {os.path.basename(path)} ({len(rows)} posts)")


def write_json(path, records):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print(f"  wrote {os.path.basename(path)} ({len(records)} events)")


def latest_saved_capture(folder):
    """Newest capturedAt in any Shares_changelog_*/Changelog_*.json already in the folder."""
    newest = 0
    for path in glob.glob(os.path.join(folder, "*hangelog_*.json")):
        with open(path, encoding="utf-8") as f:
            for e in json.load(f):
                newest = max(newest, e.get("capturedAt") or 0)
    return newest or None


def load_token(args):
    token = args.token or os.environ.get("LI_TOKEN")
    if not token:
        token_file = os.path.join(HERE, ".li_token")
        if os.path.exists(token_file):
            with open(token_file, encoding="utf-8") as f:
                token = f.read().strip()
    if not token:
        sys.exit("No token. Set LI_TOKEN env var, pass --token, or write it to .li_token")
    return token


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", metavar="YYYY-MM-DD",
                    help="fetch events from this UTC date (default: after the newest saved event)")
    ap.add_argument("--out", default=HERE, help="output directory (default: this folder)")
    ap.add_argument("--token", help="access token (else env LI_TOKEN)")
    ap.add_argument("--rebuild", metavar="JSON",
                    help="rewrite the shares CSV next to a saved Shares_changelog_*.json and exit")
    ap.add_argument("--check-authorization", action="store_true",
                    help="show whether LinkedIn is recording changelog events for you and exit")
    args = ap.parse_args()

    if args.rebuild:
        with open(args.rebuild, encoding="utf-8") as f:
            events = json.load(f)
        shares = [e for e in events if e.get("resourceName") == "ugcPosts"]
        write_shares_csv(os.path.splitext(args.rebuild)[0] + ".csv", shares)
        return

    token = load_token(args)

    if args.check_authorization:
        page, err = api_get(token, "memberAuthorizations", {"q": "memberAndApplication"})
        if err:
            sys.exit(err)
        for el in page.get("elements") or []:
            print(f"  recording since {utc(el['regulatedAt'])} UTC, scopes {el.get('memberComplianceScopes')}")
        if not page.get("elements"):
            print("  not recording — enable with: POST /rest/memberAuthorizations with body {}")
        return

    if args.since:
        since = datetime.datetime.strptime(args.since, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc)
        start_time = int(since.timestamp() * 1000)
    else:
        start_time = latest_saved_capture(args.out)
    window_start = int((time.time() - WINDOW_DAYS * 86400) * 1000)
    if start_time and start_time < window_start:
        print(f"  ! {utc(start_time)} is older than {WINDOW_DAYS} days — events before "
              f"{utc(window_start)} are no longer available", file=sys.stderr)
        start_time = window_start
    print(f"== memberChangeLogs since {utc(start_time) if start_time else f'{WINDOW_DAYS} days ago'}")

    events = collect_events(token, start_time)
    if not args.since and start_time:
        events = [e for e in events if (e.get("capturedAt") or 0) > start_time]  # already saved
    if not events:
        print("  no new events")
        return

    os.makedirs(args.out, exist_ok=True)
    span = f"{utc(events[0]['capturedAt'], '%Y%m%d')}-{utc(events[-1]['capturedAt'], '%Y%m%d')}"
    write_json(os.path.join(args.out, f"Changelog_{span}.json"), events)
    shares = [e for e in events if e.get("resourceName") == "ugcPosts"]
    if shares:
        write_json(os.path.join(args.out, f"Shares_changelog_{span}.json"), shares)
        write_shares_csv(os.path.join(args.out, f"Shares_changelog_{span}.csv"), shares)

    counts = {}
    for e in events:
        key = f"{e.get('resourceName')} {e.get('method')}"
        counts[key] = counts.get(key, 0) + 1
    print("\n== summary ==")
    for key, n in sorted(counts.items()):
        print(f"  {key}: {n}")


if __name__ == "__main__":
    main()
