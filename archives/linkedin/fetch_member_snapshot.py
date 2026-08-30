#!/usr/bin/env python3
"""Fetch LinkedIn Member Snapshot data (DMA Member Data Portability API).

This pulls your *own* historical LinkedIn data — including every post you wrote
on your feed — which the regular "Download your data" archive does not include.

Prerequisites (see README section "Member Data Portability API"):
  1. You are a LinkedIn member in the EEA or Switzerland (required by LinkedIn).
  2. You created a developer app tied to the "Member Data Portability (Member)
     Default Company" page and were granted the
     "Member Data Portability API (Member)" product.
  3. You generated an access token in the Developer Portal OAuth Token Tool with
     the scope  r_dma_portability_self_serve  and consented.

Usage:
  export LI_TOKEN="<access_token>"
  python3 fetch_member_snapshot.py                 # posts only (MEMBER_SHARE_INFO)
  python3 fetch_member_snapshot.py --domains MEMBER_SHARE_INFO ARTICLES ALL_COMMENTS ALL_LIKES ALL_VOTES INSTANT_REPOSTS
  python3 fetch_member_snapshot.py --all           # every documented domain
  python3 fetch_member_snapshot.py --out snapshot  # output directory (default: snapshot)

Output:
  snapshot/<DOMAIN>.json   raw snapshotData records for that domain
  snapshot/<DOMAIN>.csv    same records flattened (union of keys as columns)

Notes:
  * The endpoint only accepts  Linkedin-Version: 202312 . Anything else 426s.
  * After you first consent, historical data is processed offline. Some domains
    (MEMBER_SHARE_INFO in particular) can take minutes to hours to fully appear.
    Re-run later if a domain comes back empty or short.
  * Pagination "total" can under-report; this script keeps paging until the API
    reports no more data.
"""

import argparse
import csv
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

BASE = "https://api.linkedin.com/rest/memberSnapshotData"
VERSION = "202312"


def make_ssl_context():
    """Build an SSL context with a CA bundle that works on macOS python.org builds
    (whose bundled OpenSSL does not read the system keychain)."""
    for candidate in (os.environ.get("SSL_CERT_FILE"), "/etc/ssl/cert.pem"):
        if candidate and os.path.exists(candidate):
            try:
                return ssl.create_default_context(cafile=candidate)
            except Exception:
                pass
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except Exception:
        return ssl.create_default_context()


SSL_CTX = make_ssl_context()

# Domains most people want for "my content". Full list is in the docs:
# https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/shared/snapshot-domain
CONTENT_DOMAINS = [
    "MEMBER_SHARE_INFO",   # all posts / re-shares: date, URL, commentary, visibility
    "ARTICLES",            # long-form articles you authored
    "ALL_COMMENTS",        # comments you made (excl. group posts)
    "ALL_LIKES",           # your reactions
    "ALL_VOTES",           # polls created and voted on
    "INSTANT_REPOSTS",     # reposts: date, time, link
    "RICH_MEDIA",          # URLs to photos/videos/documents you shared
]

ALL_DOMAINS = CONTENT_DOMAINS + [
    "PROFILE", "POSITIONS", "EDUCATION", "SKILLS", "CERTIFICATIONS", "COURSES",
    "HONORS", "PUBLICATIONS", "PROJECTS", "ORGANIZATIONS", "LANGUAGES",
    "VOLUNTEERING_EXPERIENCES", "CAUSES_YOU_CARE_ABOUT", "TEST_SCORES", "PATENTS",
    "RECOMMENDATIONS", "ENDORSEMENTS", "CONNECTIONS", "CONTACTS",
    "MEMBER_FOLLOWING", "COMPANY_FOLLOWS", "GROUPS", "INVITATIONS",
    "EVENTS", "MARKETPLACE_ENGAGEMENTS", "MARKETPLACE_PROVIDERS",
    "MARKETPLACE_OPPORTUNITIES", "REVIEWS", "ACTOR_SAVE_ITEM",
    "REGISTRATION", "ACCOUNT_HISTORY", "LOGIN", "EMAIL_ADDRESSES",
    "PHONE_NUMBERS", "INBOX", "SEARCHES", "ADS_CLICKED", "AD_TARGETING",
    "ADS_LAN", "INFERENCE_TAKEOUT", "PROFILE_SUMMARY", "LEARNING",
    "SAVED_JOBS", "SAVED_JOB_ALERTS", "JOB_APPLICATIONS", "JOB_POSTINGS",
    "JOB_SEEKER_PREFERENCES", "RECEIPTS", "RECEIPTS_LBP", "PREMIUM_NOTES",
]


def fetch_page(token, domain, start):
    url = f"{BASE}?q=criteria&start={start}"
    if domain:
        url += f"&domain={domain}"
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
            if e.code == 429:
                wait = 10 * (attempt + 1)
                print(f"    429 rate limited, sleeping {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            return None, f"HTTP {e.code}: {body[:500]}"
        except urllib.error.URLError as e:
            wait = 5 * (attempt + 1)
            print(f"    network error {e.reason}, retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    return None, "gave up after retries"


def collect_domain(token, domain, max_pages=1000):
    records = []
    start = 0
    while start < max_pages:
        page, err = fetch_page(token, domain, start)
        if err:
            low = err.lower()
            if "no data found" in low or err.startswith("HTTP 400"):
                break  # normal end-of-data signal
            print(f"  ! {domain} stopped at start={start}: {err}", file=sys.stderr)
            break
        elements = page.get("elements") or []
        page_records = []
        for el in elements:
            page_records.extend(el.get("snapshotData") or [])
        if not page_records:
            break
        records.extend(page_records)
        print(f"  {domain}: start={start} -> +{len(page_records)} (total {len(records)})")

        nxt = None
        for link in page.get("paging", {}).get("links", []):
            if link.get("rel") == "next":
                nxt = link
        if nxt:
            start += 1
        else:
            # docs warn total under-reports; probe one more page, then stop
            start += 1
            probe, perr = fetch_page(token, domain, start)
            if perr or not (probe.get("elements") or []):
                break
            extra = []
            for el in probe.get("elements", []):
                extra.extend(el.get("snapshotData") or [])
            if not extra:
                break
            records.extend(extra)
            print(f"  {domain}: start={start} -> +{len(extra)} (total {len(records)})")
            start += 1
        time.sleep(0.5)
    return records


def write_csv(path, records):
    keys = []
    seen = set()
    for r in records:
        for k in r:
            if k not in seen:
                seen.add(k)
                keys.append(k)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
        w.writeheader()
        for r in records:
            w.writerow(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domains", nargs="+", metavar="DOMAIN",
                    help="specific domains to fetch (default: MEMBER_SHARE_INFO)")
    ap.add_argument("--all", action="store_true", help="fetch every documented domain")
    ap.add_argument("--content", action="store_true",
                    help="fetch the 'my content' set: " + ", ".join(CONTENT_DOMAINS))
    ap.add_argument("--out", default="snapshot", help="output directory (default: snapshot)")
    ap.add_argument("--token", help="access token (else env LI_TOKEN)")
    args = ap.parse_args()

    token = args.token or os.environ.get("LI_TOKEN")
    if not token:
        token_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".li_token")
        if os.path.exists(token_file):
            with open(token_file, encoding="utf-8") as f:
                token = f.read().strip()
    if not token:
        sys.exit("No token. Set LI_TOKEN env var, pass --token, or write it to .li_token")

    if args.all:
        domains = ALL_DOMAINS
    elif args.content:
        domains = CONTENT_DOMAINS
    elif args.domains:
        domains = args.domains
    else:
        domains = ["MEMBER_SHARE_INFO"]

    os.makedirs(args.out, exist_ok=True)
    summary = {}
    for d in domains:
        print(f"== {d}")
        recs = collect_domain(token, d)
        summary[d] = len(recs)
        if not recs:
            print(f"  (not ready — LinkedIn still processing this domain; re-run later)")
            continue
        with open(os.path.join(args.out, f"{d}.json"), "w", encoding="utf-8") as f:
            json.dump(recs, f, ensure_ascii=False, indent=2)
        # Some domains (ARTICLES) return an HTML document split one line per record.
        if recs and list(recs[0].keys()) == ["<html>"]:
            html = "<html>\n" + "\n".join(str(r["<html>"]) for r in recs)
            with open(os.path.join(args.out, f"{d}.html"), "w", encoding="utf-8") as f:
                f.write(html)
            print(f"  wrote {d}.html ({len(recs)} lines)")
        else:
            write_csv(os.path.join(args.out, f"{d}.csv"), recs)

    print("\n== summary ==")
    for d, n in summary.items():
        print(f"  {d}: {n} records")
    print(f"\nWritten to {os.path.abspath(args.out)}/")


if __name__ == "__main__":
    main()
