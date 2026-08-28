# GitHub REST API — collecting repository FILE contents for a CEL-based Elastic Agent integration

Research notes for a custom (never-published) integration that ingests advisory documents
stored as files under `advisories/` in the **private** repo `elastic/security-advisories`.

Scope: GitHub API mechanics only. Precedent found in the `elastic/integrations` monorepo is
in the companion file [`integrations-precedent.md`](./integrations-precedent.md).

**Verification legend**

- **[VERIFIED-DOC]** — stated in official GitHub documentation (link given).
- **[VERIFIED-LIVE]** — reproduced empirically against `api.github.com` during this research,
  using the sandbox's GitHub App installation token (`ghs_…`) against the public repo
  `elastic/integrations`. Commands are reproducible; raw doc captures are in `../temp/`.
- **[UNVERIFIED]** — could not confirm from an official source; reasoning or community source only.

---

## 1. GitHub REST API options for enumerating and reading repo files

### 1.1 Summary comparison

| API | Enumerate a directory? | Returns content? | Hard limits | Fit for `advisories/` |
| --- | --- | --- | --- | --- |
| Contents API (dir) | Yes | **No** (metadata only) | **1,000 files, silently truncated**; no pagination | Poor — silent data loss risk |
| Contents API (file) | n/a | Yes (base64 or raw) | 1 MB / 100 MB thresholds | Good for per-file fetch |
| Git Trees API | **Yes, recursively, in one call** | No (SHAs + sizes) | 100,000 entries / 7 MB documented; `truncated` flag | **Best for enumeration** |
| Git Blobs API | No | Yes (base64 or raw) | 100 MB | **Best for per-file fetch** (content-addressed) |
| `raw.githubusercontent.com` | No | Yes | n/a | Undocumented auth surface — avoid |
| Commits API | No (commit list only) | No | `files[]` absent from list responses | Weak for change detection |
| Compare API | Changed files only | No (only `patch`) | **300 files**, first page only | Usable, with caveats |
| Search code API | Yes (query) | No | **10 req/min**, 1,000 results | Not viable |

---

### 1.2 Contents API — `GET /repos/{owner}/{repo}/contents/{path}`

Docs: <https://docs.github.com/en/rest/repos/contents#get-repository-content>
(full capture: `../temp/github-contents-api-doc.txt`)

**Parameters**

| Parameter | In | Notes |
| --- | --- | --- |
| `owner` | path | required, case-insensitive |
| `repo` | path | required, without `.git` |
| `path` | path | required; omit to get the repo root |
| `ref` | query | commit SHA, branch, or tag name. Default: the repository's default branch |

**Media types** [VERIFIED-DOC]

- `application/vnd.github.raw+json` — raw file contents for files and symlinks.
- `application/vnd.github.html+json` — rendered HTML (Markup library).
- `application/vnd.github.object+json` — consistent object shape regardless of content type;
  a directory becomes an object with an `entries` array instead of a bare JSON array.
- Default (`application/vnd.github+json`) — JSON with base64 `content`.

**Size thresholds** [VERIFIED-DOC] — quoted verbatim from the docs:

> - 1 MB or smaller: All features of this endpoint are supported.
> - Between 1-100 MB: Only the `raw` or `object` custom media types are supported. Both will
>   work as normal, except that when using the `object` media type, the `content` field will
>   be an empty string and the `encoding` field will be `"none"`. To get the contents of these
>   larger files, use the `raw` media type.
> - Greater than 100 MB: This endpoint is not supported.

**Directory listing behaviour** [VERIFIED-LIVE]

A directory request returns an **array of metadata objects with no `content` field**. Each entry:

```json
{
  "name": "cel.yml.hbs",
  "path": "packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs",
  "sha": "3313c1ef1f43d8a606e226f6557c96e2a8fe28e3",
  "size": 2534,
  "url": "https://api.github.com/repos/elastic/integrations/contents/…?ref=main",
  "html_url": "https://github.com/elastic/integrations/blob/main/…",
  "git_url": "https://api.github.com/repos/elastic/integrations/git/blobs/3313c1ef…",
  "download_url": "https://raw.githubusercontent.com/elastic/integrations/main/…",
  "type": "file",
  "_links": { "self": "…", "git": "…", "html": "…" }
}
```

So enumerating a directory **always** requires a second request per file to get content.

**Single-file behaviour** [VERIFIED-LIVE] — adds `content` (base64), `encoding` (`"base64"`),
and keeps `size`. Confirmed against `packages/github/data_stream/security_advisories/manifest.yml`
(3,267 bytes): `keys: [name, path, sha, size, url, html_url, git_url, download_url, type, content, encoding, _links]`.

**The base64 `content` field is MIME-wrapped with embedded newlines every 60 characters.**
[VERIFIED-LIVE] Observed value began:

```
dGl0bGU6IENvbGxlY3QgR2l0SHViIFNlY3VyaXR5IEFkdmlzb3JpZXMgZGF0\nYSBmcm9tIEdpdEh1Yi…
```

This matters for CEL: mito's `base64_decode` is implemented with Go's
`base64.StdEncoding.DecodeString` (`../temp/mito/lib/crypto.go:443-454`), and Go's decoder
**ignores `\r` and `\n`**. Verified by compiling and running the decode against a
newline-wrapped string — it succeeded with no error. So no newline-stripping is needed.

**The 1,000-file directory cap is real and SILENT** [VERIFIED-LIVE] — this is the single most
important finding in this section. The docs say:

> This API has an upper limit of 1,000 files for a directory. If you need to retrieve more
> files, use the Git Trees API.

Tested against `packages/security_detection_engine/kibana/security_rule`, which actually
contains **5,733 files**:

- Contents API returned exactly **1,000 entries**, HTTP 200, **no `truncated` flag, no `Link`
  header, no warning of any kind**.
- The same directory via the Trees API returned all **5,733 entries** with `"truncated": false`.

**The Contents API directory listing does not paginate** [VERIFIED-LIVE]: requesting
`…/contents/packages?per_page=5&page=1` returned all **481** entries and emitted **no `Link`
header**. `per_page`/`page` are ignored.

**Other documented notes** [VERIFIED-DOC]

- `304 Not modified` is a documented response status for this endpoint (conditional requests work).
- "Download URLs expire and are meant to be used just once. To ensure the download URL does
  not expire, please use the contents API to obtain a fresh download URL for each download."

---

### 1.3 Git Trees API — `GET /repos/{owner}/{repo}/git/trees/{tree_sha}`

Docs: <https://docs.github.com/en/rest/git/trees#get-a-tree>

**Parameters**: `tree_sha` (path) is "The SHA1 value or ref (branch or tag) name of the tree";
`recursive` (query) — "Setting this parameter to any value returns the objects or subtrees
referenced by the tree". Note the doc's warning that `recursive=0` and `recursive=false` also
*enable* recursion; omit the parameter entirely to disable it.

**Response shape** — `{ "sha", "url", "tree": [...], "truncated": bool }`, where each `tree[]`
entry is:

| Field | Example | Notes |
| --- | --- | --- |
| `path` | `_dev/deploy` | Relative to the requested tree |
| `mode` | `100644` / `100755` / `040000` / `160000` / `120000` | blob / exec blob / tree / submodule / symlink |
| `type` | `blob` \| `tree` \| `commit` | |
| `sha` | `6408ae6b258e743cb…` | Git blob SHA — content hash |
| `size` | `2534` | Present for blobs only |
| `url` | `https://api.github.com/repos/{o}/{r}/git/blobs/{sha}` | Directly usable Blobs API URL |

**Truncation** [VERIFIED-DOC]:

> If `truncated` is `true` in the response then the number of items in the `tree` array
> exceeded our maximum limit. If you need to fetch more items, use the non-recursive method
> of fetching trees, and fetch one sub-tree at a time.
>
> Note: The limit for the `tree` array is 100,000 entries with a maximum size of 7 MB when
> using the `recursive` parameter.

**Observed discrepancy with the documented 7 MB size limit** [VERIFIED-LIVE]: a full recursive
tree of `elastic/integrations` at `main` returned **55,987 entries in an 18.4 MB uncompressed
response with `"truncated": false`**. Either the 7 MB figure applies to a compressed
representation or it is not enforced as documented. Treat the entry count (100,000) as the
reliable bound and **always check the `truncated` flag** rather than relying on the size figure.
[UNVERIFIED] as to which interpretation is correct.

**`{ref}:{path}` tree-ish syntax works and scopes enumeration to one subdirectory**
[VERIFIED-LIVE, but **[UNVERIFIED]** in the official docs — the doc only describes `tree_sha`
as a SHA1 or a branch/tag name]:

```
GET /repos/elastic/integrations/git/trees/main:packages%2Fgithub%2Fdata_stream%2Fsecurity_advisories?recursive=1
→ HTTP 200, 7,601 bytes, truncated: false, 26 entries
   first paths: ["_dev", "_dev/deploy", "_dev/deploy/docker"]
```

Both the URL-encoded colon (`%3A`, via `main:pack…` encoded) and a literal `:` returned HTTP 200.
Returned `path` values are **relative to the sub-tree**, not to the repo root.

This is the key capability for this integration: **one request enumerates the entire
`advisories/` directory with every file's path, size, and blob SHA**, with no 1,000-file cap
and an explicit truncation flag.

**The Trees API supports conditional requests** [VERIFIED-LIVE]:

```
etag: "6061b34db97a55ad5b8d62c04e3951cfd36fc4e7d04c1ca5fcf7a5390630fd62"
→ repeat with If-None-Match → HTTP/2 304, x-ratelimit-remaining unchanged
```

---

### 1.4 Git Blobs API — `GET /repos/{owner}/{repo}/git/blobs/{file_sha}`

Docs: <https://docs.github.com/en/rest/git/blobs#get-a-blob>

- Default media type `application/vnd.github+json` returns
  `{ "content", "encoding": "base64", "url", "sha", "size", "node_id" }`.
  The docs state: "The `content` in the response will always be Base64 encoded."
- `application/vnd.github.raw+json` returns the raw blob data.
- **"This endpoint supports blobs up to 100 megabytes in size."** [VERIFIED-DOC]
- Permission: **"Contents" repository permissions (read)**.

Because a blob is addressed by its **content hash**, a given blob URL is immutable — the same
SHA always yields the same bytes. That makes blob responses trivially cacheable and makes the
blob SHA a reliable change detector and natural document fingerprint. Each Trees API entry
already carries the ready-made blob `url`, so no path escaping is required.

---

### 1.5 `raw.githubusercontent.com`

**There is no official GitHub REST API documentation for `raw.githubusercontent.com` as an
authenticated API surface.** It appears in the REST docs only as the value of the Contents
API's `download_url` field. [VERIFIED-DOC — by absence]

What is documented [VERIFIED-DOC]: "Download URLs expire and are meant to be used just once."
For a private repo the `download_url` carries a short-lived `?token=…` query parameter
(distinct from the caller's PAT).

What community sources report [UNVERIFIED]: sending `Authorization: token <PAT>` (or `Bearer`)
as a **header** to `https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}` does return
private file contents, whereas putting the token in the URL as `?token=` or `https://TOKEN@raw…`
does not. Sources:
<https://stackoverflow.com/questions/57780240/how-to-access-github-via-personal-access-token-in-url>,
<https://stackoverflow.com/questions/77054807/how-do-you-use-raw-githubusercontent-com-in-a-github-action>.

[VERIFIED-LIVE, partial] Both `Authorization: Bearer <token>` and `Authorization: token <token>`
returned HTTP 200 against a **public** repo path. The sandbox token has no access to any private
repo (`GET /repos/elastic/security-advisories` → **HTTP 404**), so the private-repo case could
not be reproduced here.

**Recommendation: do not use `raw.githubusercontent.com`.** It is an undocumented, unversioned
surface with no rate-limit headers, no `X-GitHub-Api-Version` contract, and no ETag guarantees
that GitHub commits to. The Contents API's `application/vnd.github.raw` media type gives the
identical bytes over the documented, versioned, rate-limit-instrumented API. Also note the
private-repo failure mode is a **404, not a 401/403** — GitHub returns 404 for private resources
the credential cannot see, so a misconfigured token looks identical to a missing file.

---

### 1.6 Commits API — `GET /repos/{owner}/{repo}/commits`

Docs: <https://docs.github.com/en/rest/commits/commits#list-commits>
(full capture: `../temp/github-commits-api-doc.txt`)

Relevant query parameters [VERIFIED-DOC]:

| Parameter | Notes |
| --- | --- |
| `sha` | SHA or branch to start listing commits from. Default: the repo's default branch |
| `path` | **Only commits containing this file path will be returned** |
| `since` | ISO 8601 `YYYY-MM-DDTHH:MM:SSZ`; only results last updated after this time |
| `until` | ISO 8601; only commits before this date |
| `per_page` | max 100, default 30 |
| `page` | default 1 |

**Critical limitation: `files[]` is NOT included in the list response** [VERIFIED-LIVE].
Observed top-level keys of a list entry:

```
['sha', 'node_id', 'commit', 'url', 'html_url', 'comments_url', 'author', 'committer', 'parents']
```

`'files' in commit → False`. To learn which files a commit touched you must call
`GET /repos/{owner}/{repo}/commits/{sha}` **once per commit**, which does include `files[]`
(verified: `has files[]: True`, 300 entries, keys
`[sha, filename, status, additions, deletions, changes, blob_url, raw_url, contents_url, patch]`).
This makes "commits since timestamp" an expensive change-detection strategy — see §2.

The list endpoint does paginate via `Link` [VERIFIED-LIVE]:

```
link: <https://api.github.com/repositories/202127068/commits?path=packages%2Fgithub&since=2026-01-01T00%3A00%3A00Z&per_page=3&page=2>; rel="next",
      <…&page=6>; rel="last"
```

Note that GitHub rewrites the `Link` URLs to the numeric `/repositories/{id}/` form. Following
them verbatim (rather than reconstructing) is the documented practice.

Also note `path` filters by an exact path or a directory prefix, and the "Get a commit" endpoint
caps its `files[]` at 300 by default, paginating up to 3,000 [VERIFIED-DOC]:

> If there are more than 300 files in the commit diff and the default JSON media type is
> requested, the response will include pagination link headers for the remaining files, up to
> a limit of 3000 files.

---

### 1.7 Compare API — `GET /repos/{owner}/{repo}/compare/{basehead}`

Docs: <https://docs.github.com/en/rest/commits/commits#compare-two-commits>

`basehead` is `BASE...HEAD` (three dots). Both may be branch names, tags, or commit SHAs.

**`files[]` is an array of `Diff Entry`** [VERIFIED-DOC + VERIFIED-LIVE]:

| Field | Type | Notes |
| --- | --- | --- |
| `sha` | string \| null | Blob SHA of the file **at head** |
| `filename` | string | Repo-root-relative path |
| `status` | enum | `added`, `removed`, `modified`, `renamed`, `copied`, `changed`, `unchanged` |
| `additions` / `deletions` / `changes` | integer | |
| `blob_url` / `raw_url` | uri | |
| `contents_url` | uri | Contents API URL **pinned to the head ref** — directly fetchable |
| `patch` | string | Present for text diffs; absent for binary |
| `previous_filename` | string | Present when `status == "renamed"` |

Top-level `status` is a separate enum: `diverged`, `ahead`, `behind`, `identical`.

**The 300-file cap** [VERIFIED-DOC]:

> When calling this endpoint without any paging parameter (`per_page` or `page`), the returned
> list is limited to 250 commits, and the last commit in the list is the most recent of the
> entire comparison.
>
> The list of changed files is only shown on the first page of results, and it includes up to
> 300 changed files for the entire comparison.

[VERIFIED-LIVE] A comparison spanning 40 commits of `elastic/integrations` returned
`total_commits: 40`, `status: "ahead"`, and **exactly `files count: 300`**
(`Counter({'modified': 246, 'added': 54})`) — the cap, hit silently.

**Critically: paginating does NOT get you more files.** `page=2` returns more *commits* but the
`files[]` array only appears on page 1 and is still capped at 300. There is no way to retrieve
files 301+ from this endpoint. Sample entry [VERIFIED-LIVE]:

```json
{
  "sha": "587e9baf520e3eb5c9401e334822b4a3bda0fb01",
  "filename": ".buildkite/pipeline.schedule-daily.yml",
  "status": "modified",
  "additions": 2, "deletions": 2, "changes": 4,
  "contents_url": "https://api.github.com/repos/elastic/integrations/contents/.buildkite%2Fpipeline.schedule-daily.yml?ref=e7090bd7b4b90774406bcd9e098b3eaf704ef727"
}
```

Two further operational risks: the `base` SHA must remain reachable (a force-push, branch
deletion, or history rewrite makes it unreachable and the compare 404s), and there is no
`path` filter — you get every changed file in the repo and must filter to `advisories/` client-side.

---

### 1.8 Search code API — `GET /search/code`

Docs: <https://docs.github.com/en/rest/search/search#search-code>

[VERIFIED-LIVE] `GET /search/code?q=repo:elastic/integrations+path:packages/github+cel`:

```
HTTP/2 200
x-ratelimit-limit: 10
x-ratelimit-remaining: 9
x-ratelimit-resource: code_search
{"total_count":8,"incomplete_results":false,"items":[{"name":"cel.yml.hbs","path":"…","sha":"…", …}]}
```

**Not viable.** It uses a separate `code_search` rate-limit bucket with a limit of **10 requests
per minute** (the `search` bucket is 30/min — both confirmed live via `GET /rate_limit`).

The documented restrictions compound the problem
(<https://docs.github.com/en/search-github/searching-on-github/searching-code#considerations-for-code-search>)
[VERIFIED-DOC]:

- "You must be signed into a personal account on GitHub to search for code" — **this rules out a
  GitHub App installation token outright**, independent of everything else.
- "Only the *default branch* is indexed for code search" — no `ref` pinning.
- "Only files smaller than 384 KB are searchable."
- "Up to 4,000 private repositories are searchable" (the most recently updated of the first
  10,000 you can access) — membership in that set is not something an integration can guarantee.
- "Only repositories that have had activity or have been returned in search results in the last
  year are searchable." A quiet advisories repo could silently drop out of the index.
- "Archived repositories are not searchable."
- "you must always include at least one search term" — you cannot ask for "every file under
  `advisories/`"; a bare `path:` qualifier is rejected.

On top of that, results carry an `incomplete_results` flag when the query times out, the search
index lags the repository by an unspecified delay, and the Search API caps total results at 1,000.

For an exhaustive, correctness-sensitive enumeration of a known directory this is strictly worse
than the Trees API in every dimension. Its only legitimate use would be ad-hoc content discovery,
which is not what this integration does.

---

## 2. Incremental collection strategies

Baseline assumption: **200–500 advisory files**, a poll `interval` of 1h, and a low change rate
(a handful of files per week). The CEL input persists an arbitrary JSON object in `state.cursor`
between runs and across restarts.

### Strategy A — Sub-tree ETag + persisted `path → blob SHA` map  ★ RECOMMENDED

Store in the cursor: the ETag of the `advisories/` sub-tree request, and a map of
`path → blob sha` from the last successful enumeration.

Each poll: conditional `GET /repos/{o}/{r}/git/trees/{ref}:advisories?recursive=1` with
`If-None-Match`. On 304, stop. On 200, diff the returned `tree[]` against the stored map and
fetch a blob only where the SHA is new or changed.

| Situation | API calls | Rate-limit units consumed |
| --- | --- | --- |
| Nothing changed (the common case) | 1 | **0** (304s are free) |
| 3 files changed | 1 + 3 = 4 | 4 |
| Initial backfill, 500 files | 1 + 500 = 501 | 501 |
| Steady state per day (24 polls, ~0 changes) | 24 | **~0** |

**Pros.** Cheapest possible steady state — a full day of polling can consume literally zero
rate-limit budget. Detection is *exact*: a git blob SHA is a content hash, so a changed SHA
means changed bytes, with no timestamp skew, no clock dependency, and no 300-file cap.
Deletions and renames are detected for free (a path vanishes from the tree). It is robust to
force-pushes and history rewrites because it compares *state*, not *history* — there is no
`base` ref that can become unreachable. It works on the very first run with an empty cursor.

**Cons.** The cursor is larger: ~500 entries × (~45-char path + 40-char SHA) ≈ **40–50 KB** of
JSON in the Filebeat registry. That is well within workable bounds but is the main cost.
(Storing only the sub-tree SHA instead would shrink the cursor to 40 bytes, but then any change
forces a re-fetch of all 500 files — see Strategy D.) The `{ref}:{path}` tree-ish syntax is
undocumented, so it carries a small compatibility risk; the documented fallback is two calls
(resolve the directory's tree SHA, then recurse into it).

### Strategy B — Last-seen commit SHA + Compare API

Store the default-branch head SHA. Each poll, read the current head, then
`GET /compare/{stored}...{current}` and filter `files[]` to `advisories/`.

| Situation | API calls |
| --- | --- |
| Nothing changed | 1 (head lookup; conditional, so possibly free) + 0 |
| 3 files changed | 1 + 1 + 3 = 5 |
| Initial backfill | Cannot bootstrap — no base SHA exists; needs Strategy A or D for run 1 |

**Pros.** Gives explicit `status` values (`added`/`modified`/`removed`/`renamed`) rather than
inferred ones, and each entry's `contents_url` is pre-pinned to the head ref.

**Cons.** **Hard 300-file cap with no pagination escape** — a bulk import, a mass reformat, or a
long agent outage silently loses changes past #300, with no flag to detect it. The stored base
SHA can become **unreachable** after a force-push or history rewrite, producing a 404 that
requires a full-resync fallback path anyway. There is no server-side `path` filter, so a busy
monorepo burns the 300-file budget on unrelated files. And it cannot bootstrap itself.

### Strategy C — Last-run timestamp + Commits API with `since` and `path`

Store an ISO 8601 timestamp. Each poll, `GET /commits?path=advisories&since={ts}`, then fetch
each commit to read its `files[]`, union the filenames, then fetch content.

| Situation | API calls |
| --- | --- |
| Nothing changed | 1 |
| 3 files changed across 3 commits | 1 (list) + **3 (per-commit detail)** + 3 (content) = 7 |
| A week's backlog, 40 commits | 1 + **40** + N |

**Pros.** Simple cursor (one timestamp). Server-side `path` filter genuinely narrows the result set.

**Cons.** The **N+1 problem is unavoidable and verified**: list responses omit `files[]`, so
every commit costs an extra request. Commit timestamps are *author/committer* timestamps, which
are client-supplied and can be backdated or skewed — a commit can be pushed *after* your cursor
timestamp while being *dated* before it, and it will be missed permanently. Rebases and squashes
rewrite dates. Cost scales with commit volume, not with the number of files you actually care
about.

### Strategy D — Full re-listing every interval + Elasticsearch `_id` dedup

Enumerate the tree, fetch all 200–500 files, and let Elasticsearch collapse duplicates by a
document `_id` fingerprinted from the file path or advisory ID.

| Situation | API calls |
| --- | --- |
| Every poll, 500 files | 501 |
| Per day at 1h interval | **12,024** |

**Cons.** At 501 calls/hour it consumes ~10% of the 5,000/hour budget continuously and
permanently, and it re-indexes all 500 documents every hour — every poll is a full-index
rewrite in Elasticsearch, inflating segment churn and version numbers for no informational gain.
It also makes deletions invisible unless separately reconciled. Its one virtue is that it is
self-healing and stateless.

**Verdict.** Strategy A is the clear recommendation. Its worst case (initial backfill, 501 calls)
equals Strategy D's *every* poll, and its steady state is free. A pragmatic implementation uses
A as the primary path with D's logic as an automatic fallback whenever the cursor is empty or
the tree response reports `truncated: true`.

---

## 3. Conditional requests, ETags, and rate limits

### 3.1 Conditional requests

Docs: <https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#use-conditional-requests>

> Most endpoints return an `etag` header, and many endpoints return a `last-modified` header…
> Making a conditional request does not count against your primary rate limit if a `304`
> response is returned **and the request was made while correctly authorized with an
> `Authorization` header**.

The authorization caveat is important: an unauthenticated 304 *does* consume budget.

**[VERIFIED-LIVE]** Reproduced end to end on the Contents API:

```
Request 1 (no conditional):
  HTTP/2 200
  etag: "c19818f32ae46601df3065646ec86717102106b6"
  last-modified: Fri, 28 Aug 2026 10:09:53 GMT
  x-ratelimit-limit: 5000
  x-ratelimit-remaining: 4942
  x-ratelimit-used: 58

Request 2 (If-None-Match: "c19818f32ae46601df3065646ec86717102106b6"):
  HTTP/2 304
  etag: "c19818f32ae46601df3065646ec86717102106b6"
  x-ratelimit-limit: 5000
  x-ratelimit-remaining: 4942     ← unchanged
  x-ratelimit-used: 58            ← unchanged
```

The 304 consumed **zero** rate-limit budget. The same was confirmed for the Trees API
(§1.3). Note the ETag value must be sent back **including its surrounding double quotes**.

`Last-Modified` / `If-Modified-Since` is also supported, using an HTTP-date
(`Wed, 25 Oct 2023 19:17:59 GMT`).

GitHub's guidance for maximising 304 hit rate: request only the data you need, use a stable
sort order (`sort=updated` reorders pages and defeats caching), and use identical parameters
on every poll — a different `per_page`, `page`, or filter yields a different ETag.

### 3.2 Primary rate limits

Docs: <https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api>

| Authentication method | Limit (per hour unless noted) |
| --- | --- |
| **Unauthenticated** (by originating IP) | **60** |
| **Personal access token** — classic *or* fine-grained | **5,000** |
| GitHub App / OAuth app acting on a user's behalf, app owned by a **GitHub Enterprise Cloud** org | **15,000** |
| **GitHub App installation access token** (baseline) | **5,000** |
| GitHub App installation, on a **GitHub Enterprise Cloud** org | **15,000** |
| GitHub App installation, scaling: >20 repos → +50/hr per repo; >20 org users → +50/hr per user | capped at **12,500** |
| OAuth app using client ID + secret for public data | **5,000** per app (15,000 if GHEC-owned) |
| `GITHUB_TOKEN` in GitHub Actions | **1,000 per repository** (15,000/hr/repo for GHEC resources) |
| Git LFS | 300/**min** unauthenticated, 3,000/**min** authenticated |
| Search (`search` resource) | **30/min** authenticated (10/min unauthenticated) |
| Code search (`code_search` resource) | **10/min** |

Note the sharing rule: a user's PAT requests and any app's requests made *on that user's behalf*
draw from the same 5,000 budget. Per the docs, "if an app with a 15,000 request limit makes
10,000 requests on your behalf, you will have exhausted the 5,000 request budget for your
personal access tokens."

**[VERIFIED-LIVE]** `GET /rate_limit` with the sandbox's GitHub App installation token:

```json
{
  "core":        { "limit": 5000, "used": 0, "remaining": 5000, "reset": 1787928277 },
  "search":      { "limit": 30,   "used": 0, "remaining": 30 },
  "graphql":     { "limit": 5000, "used": 0, "remaining": 5000 },
  "code_search": { "limit": 10,   "used": 0, "remaining": 10 }
}
```

`GET /rate_limit` does not count against the primary limit, but does count against secondary limits.

### 3.3 Secondary rate limits

| Constraint | Value |
| --- | --- |
| Concurrent requests | **no more than 100**, shared across REST and GraphQL |
| Points per minute, per REST endpoint | **900** (GraphQL endpoint: 2,000) |
| CPU time | no more than 90 s CPU per 60 s real time (≤60 s of it GraphQL) |
| Content creation | 80/min and 500/hr |
| OAuth access token requests | 2,000/hr |

Point costs: most REST `GET`, `HEAD`, `OPTIONS` = **1 point**; most `POST`, `PATCH`, `PUT`,
`DELETE` = **5 points**. "Some REST API endpoints have a different point cost that is not
shared publicly." Since this integration is read-only, the practical ceiling is 900 GETs/min
against one endpoint — far above anything the recommended strategy needs.

GitHub explicitly advises making requests **serially, not concurrently**, to stay under
secondary limits.

### 3.4 Rate-limit headers — exact names

| Header | Meaning |
| --- | --- |
| `x-ratelimit-limit` | Maximum requests per hour |
| `x-ratelimit-remaining` | Requests remaining in the current window |
| `x-ratelimit-used` | Requests made in the current window |
| `x-ratelimit-reset` | Window reset time, **UTC epoch seconds** |
| `x-ratelimit-resource` | Which bucket the request counted against (`core`, `search`, `code_search`, `graphql`, …) |
| `retry-after` | Seconds to wait; present on some secondary-limit responses |
| `x-poll-interval` | Minimum seconds before polling the same endpoint again, when present |

### 3.5 What a rate-limited response looks like

> If you exceed your primary rate limit, you will receive a `403` or `429` response, and the
> `x-ratelimit-remaining` header will be `0`. You should not retry your request until after the
> time specified by the `x-ratelimit-reset` header.
>
> If you exceed a secondary rate limit, you will receive a `403` or `429` response and an error
> message that indicates that you exceeded a secondary rate limit.

So **both 403 and 429 are possible for either limit type**, and the two are distinguished by the
response body message plus header state, not by status code:

1. If `retry-after` is present → wait that many seconds.
2. Else if `x-ratelimit-remaining` is `0` → wait until `x-ratelimit-reset` (epoch seconds).
3. Else → wait ≥60 s, then exponential backoff, and give up after a bounded number of retries.

**[VERIFIED-LIVE] A secondary rate limit was triggered accidentally during this research**, and
it is a perfect illustration of why branch 3 above is necessary. Re-running the verification
script issued two `/search/code` requests within a few minutes:

```
HTTP/2 429
x-ratelimit-limit: 10
x-ratelimit-remaining: 10     ← NOT zero
x-ratelimit-resource: code_search
```

The request was rejected with **429 while `x-ratelimit-remaining` was still 10** and no
`retry-after` header was present. A client that only checks `x-ratelimit-remaining == 0` would
conclude it had budget available and retry immediately, compounding the problem. Any rate-limit
handling must treat a 403/429 status as authoritative on its own, regardless of what the
remaining-count header says.

"Continuing to make requests while you are rate limited may result in the banning of your
integration."

One further trap for a private repo, documented under error handling: GitHub returns
**`404 Not Found` rather than `403 Forbidden`** when credentials do not grant access to a
private resource, "so a `404` does not always mean that the resource is absent."
[VERIFIED-LIVE] `GET /repos/elastic/security-advisories` with the sandbox token → **HTTP 404**,
even though the repository exists.

---

## 4. Authentication options for a private repo

### 4.1 Fine-grained personal access token  ★ RECOMMENDED

- **Create at**: Settings → Developer settings → Personal access tokens → Fine-grained tokens.
  Set *Resource owner* to `elastic`, *Repository access* to "Only select repositories" →
  `security-advisories`.
- **Required permission, named exactly**: **Repository permissions → "Contents" → Read-only**
  (API parameter name `contents`, access level `read`). This is the permission the docs list for
  *Get repository content*, *Get a tree*, and *Get a blob* alike.
- **Also required, granted automatically**: **"Metadata" → Read-only** (`metadata: read`).
  It is mandatory on every fine-grained token and is added implicitly; there is nothing to
  enable. [VERIFIED-DOC that `metadata` is a read-only-only permission; the "mandatory and
  automatic" characterisation is [UNVERIFIED] against a single official page, though it is
  consistent with GitHub's own `GITHUB_TOKEN` docs and the token-creation URL example in the
  PAT docs which pairs `contents:read` with `metadata:read`.]
- **Header**: `Authorization: Bearer <token>` (`Authorization: token <token>` also works).
- **Lifetime**: chosen at creation, **1–366 days**, or non-expiring — subject to an
  organization/enterprise maximum-lifetime policy. The `expires_in` parameter accepts
  "Integer between 1 and 366, or `none` for non-expiring"; default 30 days.
- **Caveats**: the token is tied to the creating user and "will become inactive if the user
  loses access to the resource" — a leaver breaks ingestion. Organization owners may need to
  approve fine-grained tokens targeting org-owned repositories.

Docs: <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>

### 4.2 Classic personal access token

- **Required scope**: **`repo`** ("Full control of private repositories"). There is no read-only
  scope for private repository contents — `repo` is all-or-nothing and also grants **write**.
- **Header**: `Authorization: Bearer <token>` or `Authorization: token <token>`.
- **Lifetime**: optional expiry, may be unlimited. "GitHub automatically removes personal access
  tokens that haven't been used in a year."
- **Caveats**: "Your personal access token (classic) can access every repository that you can
  access." Many organizations disable classic PATs entirely — "If you try to use a personal
  access token (classic) to access resources in an organization that has disabled personal
  access token (classic) access, your request will fail with a `403` response."

Works, but strictly worse than a fine-grained token for this use case: vastly over-privileged
for reading one directory.

### 4.3 GitHub App installation access token — **NOT PRACTICAL for a CEL integration**

The exchange is: build a JWT signed **RS256** with the app's PEM private key → `POST
/app/installations/{installation_id}/access_tokens` with `Authorization: Bearer <JWT>` →
receive an installation token that **expires after 1 hour**.

**A CEL program cannot do this.** [VERIFIED-LIVE against the mito source] mito's crypto library
(`../temp/mito/lib/crypto.go`) registers only `base64`, `base64_decode`, `base64_raw`,
`base64_raw_decode`, `md5`, `sha1`, `sha256`, `hmac`, `hex`, and `uuid`. **There is no RSA
signing primitive and no JWT builder** — only symmetric HMAC. Signing an RS256 JWT is therefore
impossible inside the CEL program, and the CEL input has no built-in GitHub App credential
provider (unlike its `auth.oauth2` support, which does not fit this flow).

The 1-hour token lifetime also rules out pasting a pre-minted installation token into the
integration config: it would break within the hour.

This is worth stating explicitly in the design doc, because "just use a GitHub App, it has
higher rate limits and better lifecycle" is the obvious reviewer question, and the answer is a
concrete technical blocker rather than a preference.

Docs: <https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation>

### 4.4 OAuth app

Requires an interactive browser authorization code flow to mint a user token. There is no
non-interactive path suited to an agent reading a static credential from config, and the
resulting token's rate limit is the user's shared 5,000/hr anyway. Not applicable.

### 4.5 GitHub Enterprise Server / GHES base URL

[VERIFIED-DOC] GHES REST API base URL is:

```
http(s)://HOSTNAME/api/v3
```

so endpoints become e.g. `https://ghes.example.com/api/v3/repos/{owner}/{repo}/git/trees/{tree_sha}`.
GitHub Enterprise **Cloud** with a dedicated data residency subdomain uses
`https://api.SUBDOMAIN.ghe.com`. Plain GHEC uses ordinary `https://api.github.com`.

Docs: <https://docs.github.com/en/enterprise-server@3.14/rest/quickstart>

The practical consequence for the integration is that the API base URL should be a
user-configurable variable defaulting to `https://api.github.com` rather than a hardcoded host —
which is exactly what every existing data stream in the `github` package already does
(see `integrations-precedent.md` §2).

### 4.6 Assessment for a CEL integration with a static credential

| Method | Static credential? | Least privilege? | Verdict |
| --- | --- | --- | --- |
| Fine-grained PAT, `Contents: Read-only` | Yes | **Yes** — one repo, read-only | ★ **Recommended** |
| Classic PAT, `repo` scope | Yes | No — read/write, all repos | Fallback only |
| GitHub App installation token | **No** — 1-hour expiry, needs RS256 signing | Yes | **Not feasible in CEL** |
| OAuth app | No — interactive flow | No | Not applicable |

---

## 5. Precedent in `elastic/integrations`

See the companion file: [`integrations-precedent.md`](./integrations-precedent.md).

---

## 6. Alternatives to the GitHub API

### 6.1 Scheduled `git clone` / `git pull` + `filestream` input over the working copy

**Pros.** Git handles incrementality natively and optimally — a `git pull` transfers only
changed objects over the pack protocol, which is far more efficient than any REST polling
scheme. Full history is available locally. No REST rate limits apply (Git operations are
governed separately).

**Cons.** This is decisive: **Elastic Agent has no git input and no mechanism to run a clone
on a schedule.** You would need an out-of-band cron job or sidecar to maintain the working
copy, which means the "integration" is only half the solution and the other half is undocumented
operational glue that Fleet cannot manage, monitor, or distribute. Every agent host needs a git
binary, credential storage on disk, and disk space for the checkout. `filestream` tails
*appends* to files; advisory files are *rewritten* in place, and a rewrite plus inode change on
checkout produces ambiguous re-read semantics. [VERIFIED-LIVE] No package in
`/workspace/packages` does this — the only match for `git clone` across all package manifests
and templates was `packages/fim/manifest.yml`, which is unrelated (file integrity monitoring).

### 6.2 CI job in the advisories repo pushing to `http_endpoint`, `aws-s3`, or `gcs`

**Pros.** Push beats poll: advisories arrive within seconds of merge, with zero steady-state
API cost and no rate-limit exposure at all. The CI job can pre-normalise or pre-validate the
advisory documents, simplifying the ingest pipeline. `aws-s3` and `gcs` inputs are mature and
widely used, and an object store gives durable replay. `http_endpoint` is well-precedented —
[VERIFIED-LIVE] 20+ packages use it, including `cloudflare_logpush`, `jamf_protect`,
`ping_one`, and `f5_bigip`.

**Cons.** It requires **write access to and a maintained workflow in `elastic/security-advisories`**,
which is a different team's repository and a different change-approval path — an organizational
dependency, not just a technical one. `http_endpoint` needs an agent reachable from GitHub
Actions runners, meaning a public ingress endpoint, TLS certificates, and a shared secret to
manage. There is no backfill: only advisories merged *after* the workflow ships are captured,
so an initial historical load still needs an API-based or manual path. And if the workflow
silently breaks, ingestion stops with no signal — a poll-based design fails loudly.

### 6.3 GitHub webhooks on push events

**Pros.** Near-real-time. The push payload includes `commits[].added`, `commits[].modified`,
and `commits[].removed` arrays, so the changed file list arrives for free.

**Cons.** The push payload contains **file paths only, never file contents**, so every webhook
still requires a follow-up Contents or Blobs API call — the GitHub API dependency and its
authentication requirement do not go away. The push event's commit arrays are capped at 20
commits, so a large push loses entries. Webhooks require a public HTTPS ingress with signature
verification (`X-Hub-Signature-256`), and delivery is at-least-once with no ordering guarantee,
so the consumer must be idempotent anyway. Missed deliveries during agent downtime require a
reconciliation path — which is Strategy A again. Configuring a repository webhook needs admin
rights on `elastic/security-advisories`.

### 6.4 Verdict

For a **custom, internal, never-published** integration, **CEL + GitHub API (Strategy A)** is
the right choice. It needs nothing from the `security-advisories` repository team beyond a
read-only token, it is entirely self-contained within Fleet, it backfills and self-heals, and
its steady-state cost is effectively zero rate-limit budget. The push-based alternatives are
better on latency but each introduces a cross-team dependency and a public ingress, and none of
them removes the need for an API-based backfill and reconciliation path.

If sub-minute latency ever becomes a requirement, the natural evolution is §6.2 (CI push to an
object store) *layered on top of* the CEL poller retained as the reconciliation mechanism —
not as a replacement for it.

---

## Gaps, open questions, and areas for further investigation

1. **`{ref}:{path}` tree-ish syntax is undocumented.** It works reliably today
   [VERIFIED-LIVE] but GitHub's Trees API documentation only describes `tree_sha` as "The SHA1
   value or ref (branch or tag) name of the tree". If this matters for long-term support, the
   documented two-call fallback (resolve the sub-tree SHA via the Contents API `object` media
   type, then `GET /git/trees/{that_sha}?recursive=1`) is equivalent at the cost of one extra
   request on cache misses.

2. **The Trees API 7 MB limit could not be reproduced.** An 18.4 MB response returned
   `truncated: false`. Whether the documented figure refers to a compressed size, is stale, or
   is simply not enforced is unresolved. Not material at 200–500 files, but worth knowing.

3. **`raw.githubusercontent.com` private-repo authentication is unverified.** The sandbox token
   has no private-repo access anywhere, so the community claim that an `Authorization` header
   works there could not be reproduced. The recommendation to avoid it stands regardless.

4. **The actual contents of `elastic/security-advisories/advisories/` are unknown.** The token
   available here returns 404 for that repository. Everything about file *format* — whether the
   advisories are Markdown with YAML front matter, OSV JSON, CSAF, or a bespoke schema — the
   file count, the naming convention, and the branch name remain open. Those determine the
   parsing approach and the document `_id` fingerprint source, and someone with repo access
   needs to answer them.

5. **CEL execution-budget interaction.** The CEL input's `max_executions` (default 1,000; the
   `github` package sets 5,000) bounds how many times a program can re-request via `want_more`.
   A 500-file initial backfill that fetches one blob per execution would need ~500 executions.
   Whether to batch multiple blob fetches per execution, and what that does to secondary rate
   limits, is an implementation question for the CEL-program author rather than a research
   finding — but the constraint is real and should be flagged to them.

6. **Repository-level GitHub-native security advisories** (`GET /repos/{owner}/{repo}/security-advisories`,
   fine-grained permission `repository_advisories: read`) is a *different* data source from
   files in an `advisories/` directory. [VERIFIED-LIVE] The endpoint exists and returns 200 for
   `elastic/integrations`. If `elastic/security-advisories` also publishes GitHub-native
   repository advisories that mirror the files, that endpoint would be a structured alternative
   worth comparing. Unknown without repo access.
