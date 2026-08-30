# My YouTube Transcripts

Over the years I have shown up to talk about testing, and some of those talks
live on video. This folder keeps text transcripts of the talks on my own
YouTube channel, so the words are searchable, reusable under the repo's
Creative Commons Attribution license, and available as raw material when I turn
a talk into a written article.

Channel: <https://www.youtube.com/channel/UCrTlIKuIS-LmRk-aAbcxTKg>

The channel only carries YouTube's auto-generated captions, so the transcripts
have **no punctuation or casing** and the odd misheard word ("marek pujarvi"
for "Maaret Pyhäjärvi"). They are a starting point, not a clean edit.

## Contents

* `transcripts/<YYYYMMDD>-<slug>.md` — one file per talk: YAML frontmatter
  (title, video id, url, upload date, duration, tags), the video description,
  then the cleaned transcript.
* `video-index.csv` — id, upload date, duration, title, url for every video.
* `fetch_transcripts.py` — regenerates everything from the live channel.

Two very short screen-recording clips have no spoken audio and therefore no
transcript.

## Regenerating

```sh
brew install yt-dlp        # one-time; no API key or login needed
python3 fetch_transcripts.py            # fetch new videos, keep existing
python3 fetch_transcripts.py --force    # re-fetch and overwrite all
python3 fetch_transcripts.py --url <id> # just one video
python3 fetch_transcripts.py --list     # list the channel without fetching
```

Last downloaded: August 30th 2026.
