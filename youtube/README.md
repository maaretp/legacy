# My YouTube Transcripts

Over the years I have shown up to talk about testing, and many of those talks
live on video. This folder keeps text transcripts of them — from my own YouTube
channel and from conference / meetup / podcast channels run by other people — so
the words are searchable, reusable under the repo's Creative Commons Attribution
license, and available as raw material when I turn a talk into a written article.

My channel: <https://www.youtube.com/channel/UCrTlIKuIS-LmRk-aAbcxTKg>
Talks on other channels are listed in `extra-videos.txt`.

Transcripts come from YouTube's auto-generated captions, so they have **no
punctuation or casing** and the odd misheard word ("marek pujarvi" for "Maaret
Pyhäjärvi"). They are a starting point, not a clean edit. Talks with no English
captions (some Finnish-language ones) are kept as a stub with no transcript.

## Contents

* `transcripts/<YYYYMMDD>-<slug>.md` — one file per talk: YAML frontmatter
  (title, video id, url, upload date, duration, channel, tags), the video
  description, then the cleaned transcript.
* `video-index.csv` — id, upload date, duration, title, url for every video.
* `extra-videos.txt` — video ids/URLs for talks on other people's channels.
* `fetch_transcripts.py` — regenerates everything from YouTube.

## Regenerating

```sh
brew install yt-dlp        # one-time; no API key or login needed
python3 fetch_transcripts.py               # my channel + extra-videos.txt, keep existing
python3 fetch_transcripts.py --no-channel  # only the extra-videos.txt list
python3 fetch_transcripts.py --force       # re-fetch and overwrite all
python3 fetch_transcripts.py --url <id>    # just one video
```

Last downloaded: August 30th 2026 — 48 videos: 12 from my channel plus 36
talks/interviews on other channels. 42 have transcripts. Three have no
captions on YouTube at all (Scan Agile 2015, one "Learning through Osmosis"
recording, a Finnish career-story talk); one (The Automationist's Gambit,
EuroSTAR 2021) was rate-limited on this run — re-run `--url 7VaodpFN1Dg`
to fill it in.
