# Maaret Pyhäjärvi on LinkedIn: Themes

A thematic classification of the text posts recoverable from a personal LinkedIn
data export (`archives/linkedin/Rich_Media.csv`).

## Scope and caveat

- `Rich_Media.csv` has 50 rows: every image, video, and document uploaded to
  LinkedIn between **March 2018 and August 2026**.
- Only **25 rows carry post text** — all of them "feed photo" uploads dated
  **July 30 to August 28, 2026**, a single ~30-day window.
- The other 25 rows (2018–2025) are media links only: 3 videos, 1 document,
  2 article covers, 2 profile background images, 17 older feed/photo images,
  with no caption preserved.
- This file therefore analyses **25 posts from one month of 2026**. It is not a
  representative sample of the full LinkedIn history. The complete picture needs
  `Shares.csv` from the larger data archive, which this export did not include.
- Posts routinely span three or four themes; counts below overlap.

## Shape of these 25 posts

| Attribute | Observation |
| --------- | ----------- |
| Language | ~21 English, ~4 Finnish (fully-Finnish posts on test levels, MCP pair-study, and training ROI) |
| Trigger | Most open from an external prompt — a podcast, a person's post, a meetup, a paired session, a news cycle |
| Structure | Personal anecdote → generalised principle → open question to the audience |
| Media | Each is a text post with an attached image: a slide from 2008, a mindmap, a `git log`, a screenshot, a photo |
| Links | Frequently close with a shortened `lnkd.in` link — usually the text-field exercise or the blog |
| Hashtags | Sparse: `#ExploratoryTesting`, `#research`. Far less tag-driven than the Mastodon archive |
| People named | Marko Rintamäki, Ru Cindrea, Pia Kiviranta, Elizabeth Ayer, Ashley Hunsberger, Anne-Marie Charrett, Lisa Crispin, Janet Gregory, Grace Hopper — community-dense |
| Self-reference | Constant: a 2003 academic article, a 2008 slide, an 11-year-old mindmap, "4 years since I last ran this workshop", a 5-year gap |

## Core themes

### 1. AI in testing and software work — ~22 of 25 posts

The dominant thread; nearly every post touches it. It splits into distinct
sub-conversations rather than one message.

- **AI as a learning and levelling tool.** "The best of genAI is removal of
  shame, allowing for time to do things we never did before." The blockers named
  are *time* and *shame*. People build complex Excel sheets and Jira dashboards
  they never learned to; "we start our 10x from very different points".
- **Task expansion.** From a session with Lisa Crispin and Janet Gregory: AI as
  "external imagination", lowering the entry bar to trying something new. For
  testers this means reporting bugs *with* pull requests, and moving from prompt
  engineering (individual) to context engineering (team knowledge), with fewer
  handoffs between test designer, executor, and automator.
- **Agentic workflows and "botsitting".** Leaving an agent to read a site for 30
  minutes of unattended time; the new challenge of "filling the freed time";
  setting work up "more as botsitting" than as prompting.
- **AI safety, sandboxing, security literacy.** Sandbox awareness taught "from
  the very first vibe coding workshop"; "Yolo should not be the option — but do
  you know if it is, for your environment?"; a sandbox on the network is poorly
  isolated; "telling AI not to do something and it forgets" is a misread of the
  technology. Recurring point: we assign the agency of humans' bad decisions to
  the AI.
- **AI reshaping the tester profession.** Workforce transformation "hits tester
  profession in an interesting way, since tester profession is one of the least
  homogenous masses" — the developer frame versus the knowledge-worker frame,
  divided by the tools you live in (git-first vs WYSIWYG).
- **AI tooling, hands-on.** Jira and Figma MCPs, Playwright CLI vs MCP, token-use
  monitoring; injecting an agentic Playwright framework into an exploratory
  project.
- **AI and loneliness.** "I feel lonely for talking with AI. I used to have these
  conversations with people." Won't post AI-generated text ("anyone can generate
  it from the prompt"); "a newfound love for figuring out the questions people
  care to ask".
- **AI quirks noticed in passing.** Generated demo data that assumed TEST lagged
  DEV; one request re-doing five years of manual blog categorisation.

### 2. What testing is — testing craft and philosophy — ~10 posts

- "Is testing really that hard? Honestly, I don't know." Sustained, open
  self-questioning about why testing resists explanation.
- The **four-leaf-clover metaphor**: testing is not "kicking tires" that anyone
  with care and time could do; it is a hunt where targets exist whether or not
  you find them, with techniques for directing attention and continuous
  adaptation while tracking coverage.
- Against teaching testing as easy: "**pizza box teams**" where the tester's job
  has degraded to pointing at obvious trash; the first job there is the
  conversation that builds a foundational culture of quality.
- **Test levels mean less than assumed.** Reprising her first academic article
  (2003): unit / integration / system (end-to-end) / acceptance are V-model
  waterfall pairings that should be cut differently, so testing is not a
  theatre-laden phase at the end. Integration testing already contains
  implementation and incremental system testing; "end-to-end" quietly grows
  larger than promised; acceptance testing is really two acceptances.

### 3. Teaching, training, and workshop practice — ~8 posts

- **Do we need injected bugs to teach testing?** Her theory of teaching says no —
  "our production versions are target rich enough without injecting anything."
- The **evolution and decay of training**: "many of the games and exercises
  around agile are no longer around, as they lived with their instructors";
  modern training "feels a lot like recorded talks available on a platform, and
  competition of platforms". Four years since running a small-batch test-design
  workshop.
- **Two kinds of training**: one "makes me competent" (CPACC, ISTQB Advanced Test
  Automation), one "raises my productivity" (one of two sales trainings did,
  the other did neither). A thought experiment that good teaching two days a
  month could take a lower-paid person to senior-level output.
- **ISTQB critique**: generating 35 essentially different input classes "is a
  hard problem, and it's not taught in ISTQB courses"; testing is too often
  "framed as ready answers from someone else".
- Vibe coding workshops as a teaching venue; collaborative teaching exchanges
  (an hour of teaching traded for an hour of help).

### 4. Exploratory testing in practice — ~7 posts

- A Friday-evening demonstration: spin up PrestaShop locally, fight Colima and
  redirects ("this part Narsu called 'ops', and I expect testers to be able to
  do this"), drop two Playwright tests as landmarks, tour the UI, then go
  deeper — "This is exploratory testing." Elapsed time per `git log`: under two
  hours.
- Coverage as an integral part of exploration; "**SOMEONE and EVERYONE
  coverage**"; sampling 6% of an organisation for a transformation assessment and
  refusing to freeze it into a snapshot because the analysis itself drives
  change.
- Taking control of test data early "because the defaults will hide all the
  interesting problems".

### 5. The text-field / e-primer exercise — 4 posts (recurring artifact)

A single concrete teaching tool that keeps reappearing (link
`lnkd.in/dNxry3id`):

- "One text field, all logic in frontend" — "37 inputs and the 65 bugs *that I
  know of*".
- Paired on *Capture the Bugs* with Ru Cindrea at Gamescom, adding a statistics
  page; a bug from putting the app in an iframe and not re-testing old features
  in the new frame; non-self-verifying test data.
- E-prime variant: real sentences with no "to be" verb; "you are" / "you're"
  side by side, one works and one finds a bug.
- Used as a **recruiting exercise**; the "18% coverage" benchmark from a
  professional tester framed as an "unsolvable puzzle", later reframed to focus
  on skill *after* learning rather than skill on entry.

### 6. Career, work identity, and industry economics — ~6 posts

- **Fractional and interim leadership.** "Comfort in concepts" — borrowing Pia
  Kiviranta's Interim/Fractional vocabulary to describe simultaneously being a
  fractional AI-enhanced application testing Director (team of 9), fractional QA-
  change bridge for two clients, interim + fractional Director of Consulting
  (team of 12 developers), and a per-gig consultant.
- **The consulting business model under pressure.** Professional testers are "a
  hard sell of extra testing when the client already buys teams where service
  promise includes it all"; over ten years "the client sector has moved to
  owning software development and acquiring services — they have control over
  this mix".
- Salary and training ROI, asked openly to the "LinkedIn wall" for other
  perspectives.

### 7. Leadership, agency, and change — ~5 posts

- **Radiating intent** (via Elizabeth Ayer, building on Grace Hopper): teams
  stall "waiting for someone else to decide"; doing something visibly is how work
  moves; "you will notice you are rarely being blocked for a conversation when
  you radiate intent" — written after getting pushback for picking up work that
  "wasn't mine, needs doing".
- **Onboarding as "the ultimate shift left"** (Anne-Marie Charrett); "water,
  water everywhere" — surrounded by information, little of it usable; became
  comfortable finding what to drink closer to two years; onboarding is as much
  how you ask to be fed information as how the org feeds it — "a whole lot more
  agency than people give credit for".
- Building systems "around AI for people to remain accountable".

### 8. Agile practices and their legacy — ~3 posts

- "Remembering also what agile gave us, even when we now no longer speak of it:
  smaller batches, smaller risk."
- The gap "built between increments and end-in-mind planning".
- Cost of errors: "we used to talk about the idea that cost of errors multiplies,
  but we know now that it is not true for most of errors" — a 25,000 €/year
  architecture mistake found during requirements work that "too could have been
  fixed later".

### 9. Speaking and conferences — ~2 posts

- The arithmetic of a promised talk: "16–18 hours of travel ... each direction",
  out-of-pocket money "usually compensated after the event", "a week away from
  work and family" — set against extending oneself to another community and being
  fully present for anyone there. (PNSQC, Portland, October 12–14.)
- Conference-linked conversations as post material (Agile Testing Fellow session).

### 10. Reflection and the human side — ~3 posts

- Public self-doubt as a stance: "I might be going about trying to make sense of
  it the wrong way."
- "**1:1 is powerful. Broadcasting from stages is illusion, as is broadcasting on
  socials.**" A colleague's "15 minutes with you changes how things are" is
  incomplete without "the stream of 15 minutes leading up to" it.

### 11. Blog, archive, and self-curation — 2 posts

- Re-reading and re-categorising years of blog posts on `#ExploratoryTesting`;
  "I did not find time to continue on side of work for *five years*", then "one
  request to update for today's scale" — the same archival work this repository
  holds.
- "Thanks robots, for 2.04M blog hits" — feeding a twitter extract to the
  crawlers deliberately.

## Cross-cutting observations

- **AI is the lens, testing is the subject.** Almost nothing here is about AI in
  the abstract; it is always AI *doing* testing, teaching, hiring, onboarding, or
  changing the profession's economics.
- **Coverage and metrics recur** as the vocabulary she returns to: 6% org
  sample, 18% tester benchmark, 37 inputs / 65 bugs, 35 input classes, SOMEONE vs
  EVERYONE.
- **The profession's status worries her.** Repeated notes that "ideas about
  testers are taking steps backwards" even as AI makes "everyone in dire need of
  testing".
- **Community is the method.** Posts credit named people, cite podcasts, and
  outsource open questions to Mastodon and the "LinkedIn wall" rather than
  asserting conclusions.
- **History as argument.** A 2003 paper, a 2008 slide, an 11-year-old mindmap
  brought forward to show both what has changed and what has not.

## Signature lines

- "This is exploratory testing." (after a two-hour PrestaShop session)
- "The best of genAI is removal of shame."
- "Yolo should not be the option. But do you know if it is, for your
  environment?"
- "Notice how we assign the agency of bad decisions by people to AI?"
- "Investing in onboarding is the ultimate shift left." (quoting Anne-Marie
  Charrett)
- "Our production versions are target rich enough without injecting anything."
- "We start our 10x from very different points."
- "1:1 is powerful. Broadcasting from stages is illusion, as is broadcasting on
  socials."
- "I feel lonely for talking with AI. I used to have these conversations with
  people."
- "Testing is more like [the] hunt of the four leaf clovers. They are there even
  when you don't find them."
