# visible-quality

A local, thematic archive of every post from ***A Seasoned Tester's Crystal Ball***
by Maaret Pyhäjärvi — <https://visible-quality.blogspot.com>.

## Ingestion

| | |
|---|---|
| **Last ingested** | **2026-08-28** |
| **Source** | https://visible-quality.blogspot.com (Blogger post feed, full content) |
| **Method** | `playwright-cli` — feed pages fetched through a real browser; every in-post image downloaded via `playwright-cli` network capture |
| **Posts** | 952 |
| **Date range** | 2009-05-08 → 2026-08-28 |
| **Images** | 438 downloaded into [`_images/`](./_images/); 3 originals no longer reachable (LinkedIn CDN, a dead domain, a Mastodon emoji) are left as their original remote URLs |

Every in-post `<img>` was rewritten to `../_images/<file>`; `<a>` links that
pointed straight at a now-local image were rewritten too. `data:` image URIs
were left inline. To refresh this archive, re-run the ingestion and update the
date above.

## Structure

```
visible-quality/
├── README.md                     ← this file
├── _images/                      ← all post images, referenced as ../_images/<file>
└── <theme>/
    ├── README.md                 ← chronological index of the theme's posts
    └── YYYY-MM-DD-<post-slug>.md  ← one Markdown file per post
```

Each post file has YAML front matter (`title`, `date`, `updated`, `theme`,
`labels`, `source`) followed by the post body converted from HTML to Markdown.
The original post URL is kept in every file.

## Themes

| Theme | Posts | Covers |
|---|---:|---|
| [Ensemble & Pair Testing](./ensemble-and-pair-testing/) | 79 | Mob/ensemble programming and testing, strong-style pairing, driver/navigator practice. |
| [Public Speaking & Conferences](./public-speaking-and-conferences/) | 76 | Talks, keynotes, abstracts, CFP/selection, conference organising and volunteering. |
| [Test Automation](./test-automation/) | 63 | Automation strategy, CI/CD, continuous delivery, unit testing, approval testing, tooling. |
| [Exploratory Testing](./exploratory-testing/) | 80 | Session-based management, charters, note-taking, heuristics, test documentation and mindmaps. |
| [Career & Recruiting](./career-and-recruiting/) | 21 | Hiring and interviewing, job changes, contracting, salaries, titles, Tester of the Year. |
| [Programming & Technical](./programming-and-technical/) | 54 | Learning to code, developer skills, code literacy, code review, technical practice. |
| [Leadership & Management](./leadership-and-management/) | 17 | Management, coaching and mentoring, quality coaching, strategy and metrics. |
| [Community, Diversity & Voice](./community-diversity-and-voice/) | 13 | Gender and diversity in tech, psychological safety, speaking up, being heard. |
| [Agile, Teams & Process](./agile-teams-and-process/) | 74 | Scrum, definition of done, cross-functional teams, ways of working, retrospectives, community. |
| [Testing Craft & Skills](./testing-craft-and-skills/) | 214 | Bugs and bug reporting, test strategy, quality thinking, skills and learning the craft. |
| [General & Reflections](./general-and-reflections/) | 261 | Experience reports and opinion pieces that don't sit under one narrow theme. |

### How posts were assigned

Blogger labels exist on only ~338 of the 952 posts
(11 distinct labels), so themes were derived primarily from the **post title**
(keyword rules), falling back to the Blogger label, and finally to **General & Reflections**
for posts that matched nothing specific. Each post lives in exactly one theme folder.
The mapping is heuristic — a post may touch several themes; `labels:` in the front
matter preserves the author's own tags.

Original Blogger labels and their counts:

- Exploratory Testing — 78
- Agile — 65
- Public Speaking — 60
- Mobbing — 53
- Test Automation — 33
- Pairing — 23
- Recruiting — 9
- Programming — 9
- Approval Testing — 4
- Crowdsourcing — 3
- Services — 1
