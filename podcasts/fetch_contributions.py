#!/usr/bin/env python3
"""Rebuild podcasts/ and external-articles/ from maaretp.com/contributions.

The entry lists (ARTICLES, PODCASTS below) are transcribed from
<https://maaretp.com/contributions/>. For each entry this fetches the source and
writes one Markdown file with YAML frontmatter + whatever readable text could be
recovered:

  * normal web pages   -> curl, main-content extraction (see extract.py)
  * dead / blocked host -> Wayback Machine (earliest 200 snapshot via CDX)
  * Google Drive PDF/DOCX -> pdftotext / python-docx
  * YouTube             -> yt-dlp metadata + video description (NOT a transcript)
  * audio-only players (Spotify, Apple, ...) with no notes -> link-only stub

Then run  gen_readme.py  to refresh the per-folder README.md index tables.

Usage:
  python3 fetch_contributions.py            # both folders
  python3 fetch_contributions.py articles   # external-articles/ only
  python3 fetch_contributions.py podcasts   # podcasts/ only

Needs: curl, yt-dlp, pdftotext (poppler), python3-bs4, python-docx.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request

# The two output folders (podcasts/, external-articles/) live next to this
# script's parent — i.e. the repo root.
REPO = os.environ.get(
    "LEGACY_REPO",
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/17.0 Safari/605.1.15")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract import curl, wayback_url, looks_blocked, extract  # noqa: E402


def gdrive_id(url):
    m = re.search(r"[?&]id=([\w-]+)", url) or re.search(r"/d/([\w-]+)", url)
    return m.group(1) if m else None


def _docx_text(path):
    try:
        import docx
    except ImportError:
        return None
    try:
        d = docx.Document(path)
    except Exception:
        return None
    out = []
    for p in d.paragraphs:
        t = p.text.strip()
        if t:
            style = (p.style.name or "").lower() if p.style else ""
            if "heading 1" in style:
                out.append("\n# " + t + "\n")
            elif "heading 2" in style:
                out.append("\n## " + t + "\n")
            elif "heading 3" in style:
                out.append("\n### " + t + "\n")
            else:
                out.append(t + "\n")
    txt = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", txt).strip() or None


def fetch_gdrive_pdf(url, tmp):
    fid = gdrive_id(url)
    if not fid:
        return None
    dl = f"https://drive.google.com/uc?export=download&id={fid}"
    subprocess.run(["curl", "-sL", "-A", UA, "--max-time", "60",
                    "-c", tmp + ".ck", "-o", tmp, dl], capture_output=True)
    with open(tmp, "rb") as fh:
        head = fh.read(400)
    if head[:2] == b"PK":  # zip -> likely docx/pptx
        d = _docx_text(tmp)
        if d:
            return d
    if not head.startswith(b"%PDF"):
        # confirm-token dance for large files
        try:
            txt = head.decode("utf-8", "replace") + open(
                tmp, "rb").read().decode("utf-8", "replace")
            tok = re.search(r"confirm=([\w-]+)", txt)
            if tok:
                dl2 = (f"https://drive.google.com/uc?export=download&"
                       f"confirm={tok.group(1)}&id={fid}")
                subprocess.run(["curl", "-sL", "-A", UA, "--max-time", "60",
                                "-b", tmp + ".ck", "-o", tmp, dl2],
                               capture_output=True)
        except Exception:
            pass
    with open(tmp, "rb") as fh:
        if not fh.read(4).startswith(b"%PDF"):
            return None
    r = subprocess.run(["pdftotext", "-layout", "-nopgbrk", tmp, "-"],
                       capture_output=True)
    out = r.stdout.decode("utf-8", "replace").strip()
    out = re.sub(r"\n{3,}", "\n\n", out)
    return out or None


def fetch_youtube(url):
    r = subprocess.run(
        ["yt-dlp", "--skip-download", "--dump-single-json", url],
        capture_output=True, text=True)
    if r.returncode != 0:
        return None
    try:
        d = json.loads(r.stdout)
    except Exception:
        return None
    bits = []
    if d.get("title"):
        bits.append(f"**{d['title']}**")
    meta = []
    if d.get("channel"):
        meta.append(f"Channel: {d['channel']}")
    if d.get("upload_date"):
        meta.append(f"Uploaded: {d['upload_date']}")
    if d.get("duration_string"):
        meta.append(f"Duration: {d['duration_string']}")
    if meta:
        bits.append("  \n".join(meta))
    if d.get("description"):
        bits.append("## Video description\n\n" + d["description"].strip())
    return "\n\n".join(bits) or None


def get_text(item, tmp):
    url = item["url"]
    if not url or url == "N/A":
        return None, url, "no public link on the contributions page"
    if item.get("linkonly"):
        return None, url, item["linkonly"]
    if item.get("force_wb"):
        wb = wayback_url(url)
        if wb:
            html = curl(wb)
            if not looks_blocked(html) and len(html) > 1200:
                title, text = extract(html)
                if len(text) >= 200:
                    return text, wb, "retrieved via the Wayback Machine " \
                                     "(original site is gone)"
        return None, url, "original site is gone; no usable archive snapshot"
    if "youtube.com" in url or "youtu.be" in url:
        t = fetch_youtube(url)
        if t:
            return t, url, "yt-dlp metadata + description (not a transcript)"
    if "drive.google.com" in url:
        t = fetch_gdrive_pdf(url, tmp)
        if t:
            return t, url, "text extracted from the Google Drive PDF"
        return None, url, "Google Drive file — could not download/extract"

    live_html = curl(url)
    live_text = ""
    if live_html and not looks_blocked(live_html) and len(live_html) > 1000:
        _, live_text = extract(live_html)

    best_text, best_src, best_note = live_text, url, "page text as published"

    # Try Wayback too; keep whichever gives more readable text
    if len(best_text) < 1500:
        wb = wayback_url(url)
        if wb:
            wb_html = curl(wb)
            if wb_html and not looks_blocked(wb_html) and len(wb_html) > 1000:
                _, wb_text = extract(wb_html)
                if len(wb_text) > len(best_text):
                    best_text, best_src, best_note = (
                        wb_text, wb, "retrieved via the Wayback Machine")

    if len(best_text) < 120:
        return None, best_src, "source is a JS-only player / dead link — no " \
                               "readable notes found"
    if len(best_text) < 400:
        return best_text, best_src, best_note + " (short blurb only — this " \
                                               "source publishes no written notes)"
    return best_text, best_src, best_note


def fm_escape(s):
    return s.replace('"', "'")


STUB = "No readable text could be retrieved"


def write_item(folder, item, tmp):
    date = item["date"]
    prefix = date.replace("-", "") if date else "0000"
    path = os.path.join(REPO, folder, f"{prefix}-{item['slug']}.md")

    # Never clobber an entry that already holds real recovered text (e.g. a
    # sign-in-walled Drive PDF that was fetched by hand) with a fresh stub.
    if os.path.exists(path):
        existing = open(path, encoding="utf-8").read()
        body = existing.split("\n---\n", 2)[-1]
        if STUB not in body and len(body.split()) > 400:
            probe, _, _ = get_text(item, tmp)
            if not probe or len(probe.split()) < len(body.split()):
                print(f"KEEP {folder}/{os.path.basename(path)}  <- existing "
                      f"text is longer; not overwriting")
                return os.path.basename(path), True, "kept existing"

    text, src, note = get_text(item, tmp)
    fm = [
        "---",
        f'title: "{fm_escape(item["title"])}"',
        f'{"show" if folder == "podcasts" else "publication"}: '
        f'"{fm_escape(item["platform"])}"',
        f"date: {date or 'unknown'}",
        f"url: {item['url']}",
        f"source_retrieved: {src if src != item['url'] else item['url']}",
        f"kind: {item['kind']}",
        f"language: {item.get('lang', 'en')}",
        "---",
        "",
        f"# {item['title']}",
        "",
        f"*{item['platform']}"
        + (f" — {date}*" if date else "*"),
        "",
        f"Source: <{item['url']}>",
        "",
        f"> Retrieval note: {note}.",
        "",
        "---",
        "",
    ]
    body = text if text else "_No readable text could be retrieved for this " \
                             "entry. The link above is the record of the " \
                             "appearance._"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(fm) + body + "\n")
    status = "OK  " if text else "MISS"
    print(f"{status} {folder}/{os.path.basename(path)}  <- {note}")
    return os.path.basename(path), bool(text), note


ARTICLES = [
    dict(slug="change-in-the-world-of-testing", title="Change in the World of Testing - New Misconceptions from Old Folklore", platform="BrowserStack blog", date="2022-02-11", kind="article", url="https://www.browserstack.com/blog/change-in-the-world-of-testing/"),
    dict(slug="experiencing-5x-transformation", title="Experiencing 5x Transformation", platform="Agile Thoughts Magazine", date="2021-06", kind="magazine article", url="https://www.agile-thoughts.com/magazine/jun-2021/", linkonly="published in the Jun 2021 issue of Agile Thoughts Magazine; only the issue landing page is online, not the article text"),
    dict(slug="contemporary-exploratory-testing", title="Contemporary Exploratory Testing", platform="testproject.io blog", date="2021-04-20", kind="article", url="https://blog.testproject.io/2021/04/20/contemporary-exploratory-testing/", force_wb=True),
    dict(slug="social-software-testing-approaches", title="Social Software Testing Approaches", platform="bbst.courses blog", date="2020-06-16", kind="article", url="https://bbst.courses/blog/social-software-testing-approaches/"),
    dict(slug="fighting-against-automation", title="Fighting against Automation isn't doing anyone a favor", platform="Around the World with 80 Software Testers (book)", date="2020-04", kind="book chapter", url="https://leanpub.com/AroundTheWorldWith80SoftwareTesters", linkonly="a chapter in the community Leanpub book; only the book landing page is public, not the chapter text"),
    dict(slug="exploratory-testing-essentials-qa", title="Exploratory Testing Essentials - Questions and Answers", platform="Xray blog", date="2020-04-21", kind="article", url="https://www.getxray.app/blog/exploratory-testing-essentials/"),
    dict(slug="test-automation-process-improvement-devops-nexta", title="Test Automation Process Improvement in a DevOps Team: Experience Report", platform="NEXTA 2020 (ICSE workshop)", date="2020", kind="research paper", url="https://drive.google.com/open?id=1soKIBGN5cunqVFoiBtSEB4pVwNJfD8TZ"),
    dict(slug="intersection-of-et-and-test-automation", title="Intersection of Exploratory Testing and Test Automation", platform="Quality Matters", date="2020", kind="magazine article", url="https://drive.google.com/open?id=1GzIUGBViMB2Kjq6tUOCSRPHpY95IeA9t"),
    dict(slug="mob-testing-introduction-experience-report", title="Mob Testing - an Introduction and Experience Report", platform="Ministry of Testing, The Testing Planet", date="2018-01", kind="article", url="https://dojo.ministryoftesting.com/lessons/mob-testing-an-introduction-experience-report"),
    dict(slug="making-teams-awesome", title="Making Teams Awesome", platform="Quality Matters", date="2018", kind="magazine article", url="https://www.quality-matters.org/", linkonly="published in the Autumn 2018 issue of Quality Matters magazine; only the magazine's generic page is online"),
    dict(slug="five-controversial-ideas-tester-impact", title="Five Controversial Ideas to Increase Your Impact as a Tester", platform="Women Testers", date="2017-08", kind="magazine article", url="https://drive.google.com/file/d/0B07e3JZGe_haVmRfOUFDLWRMcVU/view?usp=sharing"),
    dict(slug="amplified-learning-with-mob-testing", title="Amplified Learning with Mob Testing", platform="StickyMinds", date="2017-01", kind="article", url="https://www.stickyminds.com/article/amplified-learning-mob-testing"),
    dict(slug="how-to-explore-with-intent", title="How to Explore with Intent - Exploratory Testing Self-Management", platform="Ministry of Testing, The Testing Planet", date="2016-11", kind="article", url="https://dojo.ministryoftesting.com/lessons/how-to-explore-with-intent-exploratory-testing-self-management"),
    dict(slug="learning-programming-through-osmosis", title="Learning Programming through Osmosis", platform="Voxxed", date="2016-09", kind="article", url="https://www.voxxed.com/blog/2016/09/learning-programming-through-osmosis/", linkonly="Voxxed was merged into DZone and the original post is gone; no usable archive snapshot"),
    dict(slug="exploratory-testing-an-api", title="Exploratory Testing an API", platform="Ministry of Testing, The Testing Planet", date="2016-09", kind="article", url="https://dojo.ministryoftesting.com/lessons/exploratory-testing-an-api"),
    dict(slug="my-year-of-lessons-for-aspiring-speakers", title="My Year of Lessons for Aspiring Speakers", platform="Women Testers", date="2016-01", kind="magazine article", url="https://drive.google.com/open?id=0B07e3JZGe_haNC03UVF4c0Y2UkE"),
    dict(slug="turn-up-the-good-mob-programming", title="Turn up the Good. A Tester Meets Mob Programming", platform="Testing Trapeze", date="2015-08", kind="magazine article", url="https://drive.google.com/open?id=0B07e3JZGe_haY1VEdVdQQTdBUWM"),
    dict(slug="use-of-rapid-reporter-in-exploratory-testing", title="Use of Rapid Reporter in Exploratory Testing", platform="Testing Circus", date="2014-04", kind="magazine article", url="https://drive.google.com/open?id=0B07e3JZGe_haMjZPUXQwLThlbnM"),
    dict(slug="modern-testing-perspective-hicss-2003", title="Increasing Understanding of the Modern Testing Perspective in Software Product Development Projects", platform="Hawai'i International Conference on System Sciences (HICSS) Proceedings", date="2003", kind="research paper", url="https://drive.google.com/file/d/1JONa8kSIuJ7bCfYBp3eQurWMkSeHEGKK/view?usp=sharing"),
    dict(slug="tentative-framework-small-companies-hicss-2002", title="A Tentative Framework for Managing Software Product Development in Small Companies", platform="Hawai'i International Conference on System Sciences (HICSS) Proceedings", date="2002", kind="research paper", url="https://drive.google.com/open?id=0B07e3JZGe_haX0JyTGtuMDRHczg"),
]

PODCASTS = [
    dict(slug="maximize-potential-of-ai-in-qa", title="Maximize the potential of AI in Quality Assurance", platform="Qt Software Quality Forum Panel", date="2025-04-16", kind="panel discussion", url="https://www.qt.io/quality-assurance/resources/videos/panel-discussion-maximize-the-potential-of-ai-in-quality-assurance"),
    dict(slug="beyond-bugs-human-side-of-testing", title="Beyond Bugs: The Human Side of Testing", platform="BrowserStack Talks", date="2025-12-08", kind="podcast episode", url="https://open.spotify.com/episode/18oH0p7XdVSc7fr5j0CseF"),
    dict(slug="is-manual-testing-dead-ai-blind-spots", title="Is manual testing dead? Why is AI exposing our blind spots", platform="[Dev]olution Podcast", date="2025-12-03", kind="podcast episode", url="https://open.spotify.com/episode/3Fg7p3X90qJvl5sXmlxZOl"),
    dict(slug="tekoaly-tietoturva-ja-testaus", title="Tekoäly, tietoturva ja testaus", platform="CGI Teknologian takana", date="2025-12-04", kind="podcast episode", url="https://www.cgi.com/fi/fi/artikkeli/quality-engineering-and-testing/tekoaly-testaus-ja-tietoturva-rakentavat-luottamusta", lang="fi"),
    dict(slug="marya-vitaly-and-maaret-on-management", title="Marya, Vitaly and Maaret on Management", platform="Beyond Quality Podcast", date="2025-12-04", kind="podcast episode", url="https://www.youtube.com/watch?v=KJQpbYELBC0"),
    dict(slug="testing-in-the-modern-age", title="Maaret Pyhäjärvi on Testing in the Modern Age", platform="Semaphore podcast", date="2024-03-12", kind="podcast episode", url="https://semaphoreci.com/blog/maaret-pyhajarvi"),
    dict(slug="digital-crime-podcast", title="Digital Crime Podcast", platform="Digital Crime Podcast", date="2024", kind="podcast episode", url="N/A"),
    dict(slug="the-10x-tester-maximizing-your-impact-lt012", title="The 10x Tester, Maximizing Your Impact (LT012 Part 2)", platform="Liberated Tester Podcast", date="2023-03-30", kind="podcast episode", url="https://open.spotify.com/episode/4HBbv0iWmDuBuP0HOfPBMe"),
    dict(slug="paradox-of-tight-schedules-lt011", title="Paradox of Tight Schedules, Pull Systems, Ensemble Programming (LT011 Part 1)", platform="Liberated Tester Podcast", date="2023-03-13", kind="podcast episode", url="https://open.spotify.com/episode/77ecY6JsnWHEwRWBgkoVWm"),
    dict(slug="things-to-unlearn-with-maaret-and-shruti", title="Things to Unlearn with Maaret and Shruti", platform="LinkedIn event", date="2023-02-03", kind="live event", url="https://www.youtube.com/watch?v=szcfI69Dt-s"),
    dict(slug="exploratory-testing-qa-therapy", title="Exploratory Testing with Maaret Pyhäjärvi", platform="QA Therapy Podcast", date="2023-02-09", kind="podcast episode", url="https://anchor.fm/qa-therapy-podcast/episodes/S2-E13-Exploratory-Testing-e1umt2j", linkonly="the anchor.fm episode link is dead (anchor.fm folded into Spotify); the current QA Therapy show page only lists other episodes"),
    dict(slug="examining-the-nuances-of-software-testing", title="Examining the nuances of Software Testing", platform="glich Podcast", date="2022-12-22", kind="podcast episode", url="https://anchor.fm/glich/episodes/E23---Examining-the-nuances-of-Software-Testing-e1sfqf3", linkonly="the anchor.fm episode link is dead (anchor.fm folded into Spotify); the current glich show page only lists other episodes"),
    dict(slug="bandwidth-to-grow", title="Bandwidth to Grow: Supporting Growth and Change", platform="Quality Bits Podcast", date="2022-11-28", kind="podcast episode", url="https://www.buzzsprout.com/2037134/11705424"),
    dict(slug="exploratory-testing-quality-sense", title="Exploratory Testing", platform="Quality Sense Podcast (Abstracta)", date="2022-09-30", kind="podcast episode", url="https://abstracta.us/blog/podcast/maaret-pyhajarvi-exploratory-testing/"),
    dict(slug="yhteisohjelmoinnissa-tehdaan-yllattavia-asioita", title="Yhteisohjelmoinnissa tehdään yllättäviä asioita", platform="Koodarikuiskaaja", date="2022-08-28", kind="podcast episode", url="https://koodarikuiskaaja.fi/podcast/yhteisoohjelmoinnissa-tehdaan-yllattavia-asioita/", lang="fi"),
    dict(slug="ensemble-teaching-exploratory-testing-product-development", title="Ensemble Teaching, Exploratory Testing, and Product Development", platform="The Mob Mentality Show", date="2022-05", kind="podcast episode", url="https://www.youtube.com/watch?v=AjJF-0r5HMc"),
    dict(slug="women-in-testing-part-1", title="Women in Testing, Part 1", platform="The Testing Show (Qualitest)", date="2022-03", kind="podcast episode", url="https://qualitestgroup.com/insights/podcasts/the-testing-show-women-in-testing-part-1/"),
    dict(slug="women-in-testing-part-2", title="Women in Testing, Part 2", platform="The Testing Show (Qualitest)", date="2022-03", kind="podcast episode", url="https://qualitestgroup.com/insights/podcasts/the-testing-show-women-in-testing-part-2/"),
    dict(slug="data-challenges-in-software-testing", title="Data Challenges in Software Testing (Episode 28)", platform="Data Democratization Podcast (Mostly AI)", date="2022-03", kind="podcast episode", url="https://mostly.ai/data-democratization-podcast/data-challenges-in-testing/"),
    dict(slug="testaaminen-pinnan-alla", title="Testaaminen pinnan alla", platform="Koodia Pinnan Alla", date="2021-05-25", kind="podcast episode", url="https://koodiapinnanalla.fi/episodes/7-testaaminen-pinnan-alla-GQGlROtU", lang="fi"),
    dict(slug="exploratory-testing-reclaimed-quare-meetcast", title="Exploratory Testing Reclaimed with Maaret and Anne-Marie", platform="Quare Meetcast", date="2020-12-16", kind="podcast episode", url="https://open.spotify.com/episode/4zD1JdIBPCXeluxbIf9MAm"),
    dict(slug="conversation-with-maaret-code-her-stories", title="Conversation with Maaret Pyhäjärvi", platform="Code Her Stories", date="2020-12-05", kind="podcast episode", url="https://www.youtube.com/watch?v=S7GpUz_BNW8"),
    dict(slug="quality-coach-roadshow-episode-15", title="Quality Coach Roadshow, Episode 15: Maaret Pyhäjärvi", platform="Quality Coach Roadshow", date="2020-07-15", kind="podcast episode", url="https://www.spreaker.com/user/charrett/quality-coach-roadshow-episode-15-maaret"),
    dict(slug="learning-with-maaret-ab-testing-124", title="Learning with Maaret", platform="AB Testing", date="2020-07-13", kind="podcast episode", url="https://www.angryweasel.com/ABTesting/ab-testing-episode-124-learning-with-maaret/"),
    dict(slug="time-travel-to-the-past-developer-melange", title="Time Travel to the Past", platform="Developer Melange", date="2020-07-01", kind="podcast episode", url="https://developermelange.com/034-time-travel-to-the-past/"),
    dict(slug="interview-modern-agile-show", title="Interview with Maaret Pyhäjärvi", platform="Modern Agile Show", date="2020-04-22", kind="podcast episode", url="https://www.youtube.com/watch?v=IETVizs_x2M"),
    dict(slug="agile-without-product-owner-agilpodden", title="Agile without Product Owner", platform="Agilpodden", date="2020-04-30", kind="podcast episode", url="https://agilpodden.podbean.com/e/77-agile-without-product-owner-eng/"),
    dict(slug="react-finland-2-designkirjastot-ja-testaaminen", title="React Finland 2: Designkirjastot ja testaaminen", platform="Webbidevaus.fi", date="2019-05", kind="podcast episode", url="https://webbidevaus.fi/44", lang="fi"),
    dict(slug="learn-not-to-be-afraid-it-career-energizer", title="Learn Not to be Afraid of Doing Things Differently", platform="IT Career Energizer", date="2019-04", kind="podcast episode", url="https://podcasts.apple.com/us/podcast/learn-not-to-be-afraid-doing-things-differently-maaret/id1231387865?i=1000435108093"),
    dict(slug="working-together-is-hard-guilty-tester", title="Working Together is Hard", platform="The Guilty Tester", date="2018-09", kind="podcast episode", url="https://testingpodcast.com/the-guilty-tester-episode-4-maaret-pyhajarvi-working-together-is-hard/"),
    dict(slug="collaboration-between-testers-and-developers-cucumber", title="Collaboration between testers and developers", platform="Cucumber Podcast", date="2018-03", kind="podcast episode", url="https://soundcloud.com/cucumber-podcast/collaboration-between-testers-and-devs"),
    dict(slug="discussion-on-collaboration-two-points-of-view", title="Discussion on Collaboration", platform="Two Points of View at Two", date="2018-02", kind="podcast episode", url="https://testingpodcast.com/two-points-of-view-at-two-short-high-impact-talks-about-testing-with-maaret-pyhajarvi/"),
    dict(slug="testing-software-reflection-as-a-service", title="Maaret Pyhäjärvi on Testing Software", platform="Reflection as a Service", date="2017-02", kind="podcast episode", url="https://reflectionasaservice.com/2017/02/episode-36-maaret-pyhajarvi-testing-software/"),
    dict(slug="lead-change-from-the-back-of-the-room", title="How to lead change from the back of the room", platform="Scrum Master Toolbox Podcast", date="2017-01", kind="podcast episode", url="https://scrum-master-toolbox.org/2017/01/podcast/maaret-pyhajarvi-on-how-to-lead-change-from-the-back-of-the-room/"),
    dict(slug="always-one-more-thing-to-add-anti-pattern", title="The 'always one more thing to add' anti-pattern", platform="Scrum Master Toolbox Podcast", date="2017-01", kind="podcast episode", url="https://scrum-master-toolbox.org/2017/01/podcast/maaret-pyhajarvi-on-the-always-one-more-thing-to-add-anti-pattern/"),
    dict(slug="how-the-whole-team-can-work-together", title="How the whole team can work together", platform="Scrum Master Toolbox Podcast", date="2017-01", kind="podcast episode", url="https://scrum-master-toolbox.org/2017/01/podcast/maaret-pyhajarvi-explains-how-the-whole-team-can-work-together/"),
    dict(slug="anyone-can-take-up-the-role-of-scrum-master", title="How anyone in the team can take up the role of Scrum Master", platform="Scrum Master Toolbox Podcast", date="2017-01", kind="podcast episode", url="https://scrum-master-toolbox.org/2017/01/podcast/maaret-pyhajarvi-on-how-anyone-in-the-team-can-take-up-the-role-of-scrum-master/"),
    dict(slug="context-driven-testing-understanding-the-system", title="Context Driven testing and how that helps understand the system we work within", platform="Scrum Master Toolbox Podcast", date="2017-01", kind="podcast episode", url="https://scrum-master-toolbox.org/2017/01/podcast/maaret-pyhajarvi-on-context-driven-testing-and-how-that-helps-understand-the-system-we-work-within/"),
    dict(slug="testing-in-the-pub-testbash-philadelphia", title="Testing in the Pub at TestBash Philadelphia", platform="Testing in the Pub (Ministry of Testing)", date="2016", kind="podcast episode", url="https://www.ministryoftesting.com/dojo/lessons/maaret-and-greg-live-from-testing-in-the-pub-from-testbash-philadelphia"),
    dict(slug="we-talk-all-things-mob-testing", title="We Talk All Things Mob Testing", platform="Ministry of Testing Podcast", date="2016", kind="podcast episode", url="https://www.ministryoftesting.com/dojo/lessons/we-talk-all-things-mob-testing-with-maaret-pyhajarvi"),
    dict(slug="it-takes-two-lets-talk-about-tests-baby-61", title="Episode 61 / It Takes Two", platform="Let's Talk About Tests Baby", date="2016-08-06", kind="podcast episode", url="http://letstalkabouttests.xyz/index.php/2016/10/06/ep-61-takes-two/"),
    dict(slug="agile-lean-startup-mindsets-testtalks-115", title="Episode 115 / Agile, Lean Startup Mindsets", platform="TestTalks (Joe Colantonio)", date="2016-08-14", kind="podcast episode", url="https://joecolantonio.com/testtalks/115-agile-lean-startup-mindsets-maaret-pyhajarvi/"),
    dict(slug="enabling-voices-developer-on-fire-116", title="Episode 116 / Maaret Pyhäjärvi: Enabling Voices", platform="Developer on Fire", date="2016-03-28", kind="podcast episode", url="http://developeronfire.com/episode-116-maaret-pyhajarvi-enabling-voices"),
    dict(slug="mobbing-and-pairing-testing-in-the-pub-22", title="Episode 22 / Mobbing and Pairing", platform="Testing in the Pub", date="2015-11-20", kind="podcast episode", url="http://testinginthepub.co.uk/testinginthepub/podcast/testing-in-the-pub-episode-22-mobbing-and-pairing-with-maaret-pyhajarvi/"),
]


def build(folder, items):
    os.makedirs(os.path.join(REPO, folder), exist_ok=True)
    tmp = f"/tmp/gd_{folder}.pdf"
    rows = []
    for it in items:
        fn, ok, note = write_item(folder, it, tmp)
        rows.append((it, fn, ok, note))
        time.sleep(1.0)
    return rows


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("both", "articles"):
        build("external-articles", ARTICLES)
    if which in ("both", "podcasts"):
        build("podcasts", PODCASTS)
    print("\nDone. Now run:  python3 gen_readme.py")
