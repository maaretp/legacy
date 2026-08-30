# Getting the full LinkedIn posts via the Member Data Portability API

The regular **Settings → Data privacy → Get a copy of your data** export (even the
"larger data archive") did not include a `Shares.csv` in the 2026-08-29 dump —
only `Rich_Media.csv`, which preserved text for just the last ~month of
photo-posts.

LinkedIn's **Member Data Portability (Member)** API — built for the EU Digital
Markets Act — is the supported way to pull your *own* full history, including
every feed post. This is a self-serve developer flow, not a support ticket.

- Docs entry point:
  <https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/member-data-portability-member/?view=li-dma-data-portability-2026-05>
- The post history lives in the **`MEMBER_SHARE_INFO`** snapshot domain:
  "all shared or re-shared posts, including date, URL, shared comments, and
  visibility status" — i.e. the `Shares.csv` equivalent.

## Eligibility

> "At this time, this feature is available only for LinkedIn members located in
> the European Economic Area and Switzerland."

Finland qualifies.

## One-time setup (Developer Portal)

1. **Create a developer app** at <https://www.linkedin.com/developers/apps/>.
   - When it asks for a **LinkedIn Company Page**, use the shared page
     **"Member Data Portability (Member) Default Company"**
     (<https://www.linkedin.com/company/member-data-portability-member-default-company>).
   - **Do not create a new Company Page** — access to the API product is only
     granted to apps built against that specific default page.
   - Fill in app name, the default page, a logo, accept the API Terms.

2. **Request the API product.** In the app's **Products** tab, click
   **Request access** for **Member Data Portability API (Member)**, accept the
   terms. For self-serve member use this is granted immediately.

3. **Generate an access token.** Developer Portal → **Docs and tools** →
   **OAuth Token Tools** → **Create token**.
   - Select the app from step 1.
   - Select the scope **`r_dma_portability_self_serve`**.
   - **Request access token** → log in → **Allow** the consent screen
     ("share your LinkedIn data with your application").
   - Copy the token. (Tokens are time-limited; if a later run 401s, mint a new
     one the same way.)

   > Consenting here is also what makes LinkedIn **start processing your
   > historical data**. The Snapshot data — `MEMBER_SHARE_INFO` especially — is
   > collated offline and can take minutes to hours to be complete. If the first
   > run returns nothing or looks short, wait and re-run.

## Pull the data

The API endpoint is versioned and only accepts `Linkedin-Version: 202312`.

```
GET https://api.linkedin.com/rest/memberSnapshotData?q=criteria&domain=MEMBER_SHARE_INFO
Authorization: Bearer <access_token>
Linkedin-Version: 202312
Content-Type: application/json
```

Quick check with curl:

```sh
export LI_TOKEN="<access_token>"
curl -s --get 'https://api.linkedin.com/rest/memberSnapshotData' \
  --data-urlencode 'q=criteria' \
  --data-urlencode 'domain=MEMBER_SHARE_INFO' \
  -H "Authorization: Bearer $LI_TOKEN" \
  -H 'Linkedin-Version: 202312' \
  -H 'Content-Type: application/json' | head -c 2000
```

Response shape: `elements[0].snapshotData` is a list of records;
`paging.links[rel=next]` points to the next page (`start` is a page index, not an
offset). `paging.total` can under-report — keep paging until the API says
"No data found for this memberId".

### Script

`fetch_member_snapshot.py` (in this folder) handles pagination, retries, and
writes both JSON and flattened CSV per domain. No dependencies (stdlib only).

```sh
export LI_TOKEN="<access_token>"

# just the posts
python3 fetch_member_snapshot.py

# posts + articles + comments + reactions + polls + reposts + rich media
python3 fetch_member_snapshot.py --content

# specific domains
python3 fetch_member_snapshot.py --domains MEMBER_SHARE_INFO ARTICLES

# everything documented
python3 fetch_member_snapshot.py --all --out snapshot
```

Output lands in `snapshot/MEMBER_SHARE_INFO.json` and `.csv`, etc.

### Relevant domains for "my content"

| Domain | Contents |
| --- | --- |
| `MEMBER_SHARE_INFO` | All posts / re-shares: date, URL, commentary, visibility |
| `ARTICLES` | Long-form articles authored |
| `ALL_COMMENTS` | Comments made (excludes group posts) |
| `ALL_LIKES` | Reaction type per post |
| `ALL_VOTES` | Polls created and voted on |
| `INSTANT_REPOSTS` | Repost date, time, link |
| `RICH_MEDIA` | URLs to photos/videos/documents shared (what the old export gave) |

Full domain list:
<https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/shared/snapshot-domain?view=li-dma-data-portability-2026-05>

## Also available: Member Changelog API

Separately, once you have consented, the **Member Changelog API** streams new
activity (posts, comments, reactions) going forward, queryable for the **last 28
days** only. Not needed for a one-time history pull, but it is the way to keep an
archive current.
<https://learn.microsoft.com/en-us/linkedin/dma/member-data-portability/shared/member-changelog-api?view=li-dma-data-portability-2026-05>
