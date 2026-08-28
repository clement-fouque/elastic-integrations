# Research Brief: Elastic Security Advisories (ESA)

> **Generated:** 2026-08-28
> **Revised:** 2026-08-28 (review pass 2 — see `research-review.md`)
> **Researcher:** AI-assisted research via `/research-integration` skill
> **Status:** READY FOR REVIEW
> **Confidence:** MEDIUM-HIGH — collection mechanics, ECS mapping, and configuration are HIGH confidence and verified live against the GitHub API. The advisory files are now known to be **JSON**, but the **field names inside them remain UNVERIFIED** because the source repository is private. See §8, question 1.

---

## ⚠️ Read this first

The requested data source, `https://github.com/elastic/security-advisories/tree/main/advisories`, is a **private repository**. It is not readable from this research environment:

| Check | Result |
|---|---|
| `curl https://github.com/elastic/security-advisories` (unauthenticated) | **404** |
| `curl https://github.com/elastic/integrations` (control, same host) | 200 |
| `gh api repos/elastic/security-advisories` (sandbox token) | **404** |

The sandbox's GitHub credential is an App installation token scoped to `elastic/integrations` only. GitHub returns `404` rather than `403` for private resources a credential cannot see, so this is consistent with the repository existing but being inaccessible. Re-probed on the review pass: unchanged.

### What the review pass learned from outside this environment

A person with repository access supplied two facts that the research environment could not obtain. They are the most load-bearing new information in this brief:

| Fact | What it settles |
|---|---|
| A real file in the directory is named **`ESA-2026-0081.json`** | The on-disk format is **JSON**, not the Markdown-with-YAML-front-matter that pass 1 rated most likely. The files are keyed by ESA ID, and the ID is **zero-padded to four digits**. |
| The directory **may hold more than 1000 files** | The corpus is materially larger than the 200–500 advisories pass 1 estimated, and the enumeration strategy must not rely on the GitHub Contents API. |

**The file's contents were not supplied**, so the JSON's field names, and whether it is an ESA-native record or a rendering of some standard schema, are still unknown. That is now the only blocking unknown (§8, question 1). Everything about *how to collect* the files, *how to authenticate*, and *what to configure* is researched and verified live.

**Two consequences worth reading before anything else:**

1. **The ESA ID is rendered differently in the repository than in public.** The repository pads the sequence to four digits (`ESA-2026-0081`); every public rendering pads to a *minimum* of two and widens naturally (`ESA-2026-01`, `ESA-2026-81`, `ESA-2026-137`). The same advisory therefore has two different string forms, and `ESA-2026-0081` is the public `ESA-2026-81` — verified to exist (Elasticsearch, CVE-2026-72679, posted 2026-08-13). Any join to the public corpus, and any document `_id`, must key on the pair *(year, integer sequence)* rather than on either string. §4.5.
2. **A >1000-file corpus breaks one default.** The Filebeat `cel` input's `max_executions` defaults to 1,000, so a backfill that fetches one advisory per execution stalls partway. This turns out to be dissolvable rather than limiting — a single CEL evaluation can issue many HTTP requests, verified live against mito — but it must be a deliberate decision. §7.4.

A fully-specified, credential-free **alternative data source** that reproduces most of the same corpus from public endpoints is documented in §2.2. It is a legitimate primary design, not a degraded fallback.

### Accuracy of this revision

Pass 1's claims were independently re-derived in a four-track audit; the findings are consolidated in `research-review.md` and detailed in `references/review-*.md`. The empirical GitHub API work and the CVE-corpus analysis reproduced exactly and are trustworthy. A number of hand-counted advisory-body statistics did not, and are corrected in place below. Where a corrected figure appears in this brief it is the re-derived value, not pass 1's.

---

## 1. Product Overview

### 1.1 What is it?

An **Elastic Security Advisory (ESA)** is Elastic's official disclosure document for a security vulnerability in an Elastic product. Each advisory carries an `ESA-YYYY-NN` identifier, one or more CVE IDs, a CVSS v3.1 score and vector, the affected product and version ranges, the fixed versions, and remediation guidance. Elastic is an authorized CVE Numbering Authority (`CNA-2017-0011`), so first-party advisories also produce a CVE Record in the CVE Program.

The consumer of this integration is an organization running Elastic products that wants its own advisory feed indexed in Elasticsearch — for vulnerability tracking against deployed Stack versions, for alerting when a new advisory affects a version in use, and for reporting.

### 1.2 Vendor

- **Vendor name:** Elastic
- **Product name:** Elastic Security Advisories
- **Product category:** Vendor vulnerability disclosure / advisory feed
- **Vendor documentation portal:** <https://www.elastic.co/product-security> (`elastic.co/community/security` 301-redirects here)
- **Advisory portal:** <https://discuss.elastic.co/c/announcements/security-announcements/31>
- **Requested source:** `elastic/security-advisories`, directory `advisories/` (private)

### 1.3 Data generated

One document type: a vulnerability disclosure record. There are no runtime events, metrics, or telemetry. Volume is low and bursty, published in **release-train batches rather than continuously**: across 203 ESA-tagged forum topics there are only 52 distinct publication dates, and the largest single-day batch observed was **48 advisories on 2026-08-13**.

**Corpus size — the public record and the repository disagree, and the gap matters.**

| Measure | Value | Basis |
|---|---|---|
| Distinct **published** ESA IDs, 2016–2026 | **341** | Full Discourse crawl; spot-verified live for 2016, 2018, 2019, 2020, 2022 |
| **Allocated** upper bound from per-year maxima | **~386** | Sum of the highest sequence number seen in each year |
| Earliest ESA ID seen publicly | `ESA-2016-02` | Discourse search |
| Published in 2026 | **116** advisories, highest sequence **137** | 21 sequence numbers in 2026 were never published |
| 2026 publication rate | **~15/month** (116 over Jan–Aug) | ~5.7× the 2024–2025 rate |
| Files reported in `advisories/` | **>1000** | Supplied by a person with repo access |

So the public record accounts for at most ~386 ESA IDs ever minted, and the directory reportedly holds more than 1000 files. **Roughly 600+ files are unexplained by anything observable publicly.** Ranked explanations:

1. **The repository holds advisories that were never published** — internal-only, silently-fixed, embargoed, or withdrawn. This is the best-supported explanation: four-digit zero-padding provides capacity for 9,999 IDs per year against a published peak of 137, which is the signature of a series far denser than the public one. It also fits the observed 15% never-published rate in 2026.
2. **The count is recursive or includes non-advisory entries** — year subdirectories, a schema file, templates, a README. A recursive count over `advisories/**` would inflate a flat-file total.
3. **More than one file per advisory** — for example a source record plus an emitted CVE 5.x document.
4. **The ">1000" was a general caution rather than a measured count.** The phrasing given was "there could be more than 1000 files", offered as the *reason* to prefer the Git Trees API over the Contents API. It may be a warning about the API's cap rather than an observation about this directory.

**This ambiguity does not change the recommended design**, because the enumeration strategy chosen in §2.1 is already correct for any size from 1 to 100,000 files. It does change the sizing arithmetic (§6.3) and it raises a governance question that pass 1 never asked (§8, question 11): if most files are unpublished advisories, an integration that ingests the directory indiscriminately will index non-public vulnerability information.

**A correction to pass 1.** This brief previously said "roughly 200–500 advisories… growing by about 15 per month". The growth rate was right; the corpus size was a floor mistaken for a total, because the count only considered forum topics whose *title* carries an ESA ID. 106 further advisory-like topics from 2015–2025 predate that title convention and were missed. Pass 1 also stated "137 advisories in 2026 alone" in §4.6, conflating the highest sequence number with a count; the count is 116.

### 1.4 Existing Elastic coverage

**No integration collects Elastic's own security advisories.** There is a near-miss that a reviewer will ask about:

`packages/github/data_stream/security_advisories` calls `https://api.github.com/advisories` — the **global, public GitHub Advisory Database** of open-source package vulnerabilities. It is a different endpoint returning a different entity, and no parameter makes it return repository files or Elastic's ESAs. Its ingest pipeline is nonetheless the single best in-repo template for `vulnerability.*` ECS mapping, and its CEL program is the best template for GitHub API headers, token redaction, and error handling.

More broadly, **no package in `/workspace/packages` reads files from a git repository**, and none sends `If-None-Match` conditional requests. Both are new ground. Full precedent survey: `references/integrations-precedent.md`.

### 1.5 Market coverage

**N/A — deliberately skipped.** The requester specified this is a custom integration that will never be published and that competitive analysis is not needed. No IBM QRadar / Splunk / Sumo Logic comparison was performed.

---

## 2. Data Collection Method

### 2.1 Recommended method

- **Input type:** `cel`
- **APIs:** GitHub **Git Trees API** for enumeration, **Git Blobs API** for content, with **sub-tree ETag** conditional requests plus a persisted `path → blob SHA` map for change detection.
- **Rationale:** one request enumerates the entire `advisories/` directory with every file's path, size, and blob SHA; the steady-state poll then costs **zero rate-limit budget**.

**Why the Git Trees API and not the more obvious Contents API.** This was verified empirically twice, and the result is decisive:

> Against `packages/security_detection_engine/kibana/security_rule`, which contains **5,733 files**, the Contents API returned exactly **1,000 entries with HTTP 200, no `truncated` flag, no `Link` header, and no warning of any kind**. The Trees API returned all 5,733 with `"truncated": false`.

The Contents API's documented 1,000-file directory cap **truncates silently**. It also ignores `per_page`/`page` entirely and never includes `content` in a directory listing, so it costs a second request per file regardless. The Trees API has an explicit truncation flag, a 100,000-entry bound, and each entry carries a ready-made blob URL.

**With a reported >1000 files in `advisories/`, this stops being a theoretical preference and becomes the difference between a complete corpus and a silently truncated one.** A Contents-API implementation would have returned exactly 1,000 advisories with a success status and no indication that anything was missing. The person who supplied the file-count figure independently reached the same recommendation.

The `{ref}:{path}` tree-ish form — `GET /repos/{owner}/{repo}/git/trees/main:advisories?recursive=1` — scopes recursion to the one subdirectory in a single call. It works reliably but is **undocumented**; the documented two-call fallback is equivalent at the cost of one extra request.

**Fetch blob content as raw, not base64.** The Blobs endpoint honours `Accept: application/vnd.github.raw`, which returns the file bytes directly. Verified over 100 blobs: **916,962 bytes raw versus 1,292,920 base64**, a 29% saving, and it removes the base64 decode step entirely. The base64 path is still safe if used — see §3.2 — but raw is strictly better.

**Avoid `raw.githubusercontent.com`.** It is undocumented as an authenticated API surface, emits no rate-limit headers, and honours no `X-GitHub-Api-Version` contract. The `application/vnd.github.raw` media type returns identical bytes over the documented, versioned, instrumented API.

### 2.2 Alternative methods

| Method | Input type | Pros | Cons |
|---|---|---|---|
| **Git Trees + Blobs API** ★ | `cel` | Zero-cost steady state; exact content-hash change detection; self-backfilling; needs nothing from the advisories repo team beyond a read token | Requires a credential for a private repo; **file format unverified**; every misconfiguration returns an indistinguishable 404 |
| **Public Discourse + CVE Record 5.x** | `cel` | **No credential at all**; no 404 ambiguity; deployable by anyone; CVE records give genuinely structured version ranges and decomposed CVSS | No ETag support, so every poll transfers a full payload; requires Markdown/HTML section parsing; 25–30 items/page against 48-advisory batches makes page-walking mandatory; no ESA ID except via slug regex |
| Contents API | `cel` | Simpler mental model | **Silent 1,000-file truncation**; two requests per file anyway |
| Commits API + `since` | `cel` | Simple one-timestamp cursor | Verified N+1: list responses omit `files[]`, so one extra call per commit; commit timestamps are client-supplied and can be backdated past the cursor and lost permanently |
| Compare API from last-seen SHA | `cel` | Explicit `added`/`modified`/`removed` status | **Hard 300-file cap with no pagination escape**; stored base SHA becomes unreachable after a force-push; cannot bootstrap |
| Scheduled `git clone` + `filestream` | `filestream` | Git handles incrementality optimally | **Elastic Agent has no git input and cannot run a clone on a schedule.** Requires out-of-band cron that Fleet cannot manage or monitor |
| CI job in the advisories repo pushing to `http_endpoint` / `aws-s3` | various | Push beats poll; seconds of latency; zero API cost | Needs write access and a maintained workflow in another team's repository; requires public ingress; **no backfill** |
| GitHub push webhooks | `http_endpoint` | Near-real-time; payload lists changed paths | Payload carries **paths only, never contents**, so the API dependency remains; 20-commit cap; needs public ingress and repo admin rights |
| Search code API | `cel` | — | 10 req/min; requires a signed-in *personal* account; default branch only; **not viable** |

The **incremental strategy** comparison, for a 500-file corpus:

| Strategy | Steady-state poll | 3 files changed | Backfill (1,000 files) | Per day @ 1h |
|---|---|---|---|---|
| **ETag + blob-SHA map** ★ | 1 call, **0 units** | 4 | 1,001 | **~0 units** |
| Compare API | 1–2 | 5 | cannot bootstrap | low, but 300-file cap |
| Commits + `since` | 1 | 7 | n/a | low, but N+1 and clock-skew loss |
| Full re-listing + `_id` dedup | 1,001 | 1,001 | 1,001 | **24,024 calls** |

A 304 on an authorized conditional request consumes **zero** rate-limit budget — verified live twice, most recently by holding `x-ratelimit-used` at 999 across three consecutive `If-None-Match` 304s while three unconditional 200s advanced it to 1,000, 1,001, 1,002. Blob SHAs are content hashes, so detection is exact, immune to clock skew, and gives deletions for free.

**The strategy's largest untested assumption was checked and holds.** The sub-tree ETag changes if and only if something inside that sub-tree changes: it stayed stable across six unrelated repo-wide commits and took a distinct value for each of three commits that touched the directory. Had it been sensitive to unrelated commits, the zero-cost steady state would have collapsed into a full re-listing on every unrelated push.

The recommended implementation uses the ETag strategy as the primary path with full re-listing as an automatic fallback whenever the cursor is empty or the tree response reports `truncated: true`.

### 2.3 Vendor-side setup required

An operator must create a **fine-grained personal access token** with one permission: **Repository permissions → Contents → Read-only**. `Metadata: Read-only` is also required but is mandatory on every fine-grained token and granted implicitly.

Three gotchas, all verified, all of which produce a bare 404 that looks like an empty directory:

1. **The "Resource owner" selector defaults to your own user account and must be changed to the organization.** A user-owned token authenticates fine, reports a healthy 5,000/hr rate limit, and returns 404 for the org's private repo with no explanation.
2. **Organization owner approval is the default posture** for fine-grained tokens against org resources. An unapproved token sits `pending` and reads only public resources. Owners are notified by a **once-daily digest email**, so budget for that latency.
3. **The `elastic` organization has SAML SSO configured** — verified: `github.com/orgs/elastic/sso` returns HTTP 200 with a single-sign-on prompt, whereas the same path on organizations without SAML returns 404. This matters less than feared, because GitHub documents that fine-grained tokens are *"authorized during token creation"*; the separate "Configure SSO → Authorize" step applies only to **classic** PATs, and skipping it is the classic cause of "valid token, everything 404s".

Four completely different faults — wrong resource owner, nonexistent repo, wrong directory path, wrong branch — all return a **byte-identical** `{"message":"Not Found"}`. A four-step diagnostic ladder that isolates each one is in `references/deployment-and-setup.md` §1.8.

Full operator setup guide, including the classic-PAT comparison and token lifetime policy: `references/deployment-and-setup.md`.

---

## 3. Data Source Details

### 3.1 Connection and authentication

- **Base URL:** `https://api.github.com` (GitHub Enterprise Server: `https://HOSTNAME/api/v3`; GHEC with data residency: `https://api.SUBDOMAIN.ghe.com`)
- **API version:** `X-GitHub-Api-Version: 2022-11-28` (current is `2026-03-10`; `2022-11-28` still supported, verified live)
- **Rate limits:** see below
- **Documentation:** <https://docs.github.com/en/rest/git/trees>, <https://docs.github.com/en/rest/git/blobs>

**Authentication detail — API key / static Bearer token:**

- **Method:** Bearer token (fine-grained personal access token)
- **Header format:** `Authorization: Bearer <token>` (`Authorization: token <token>` also works)
- **Credential creation:** Settings → Developer settings → Personal access tokens → Fine-grained tokens. Set *Resource owner* to `elastic`, *Repository access* to "Only select repositories" → `security-advisories`.
- **Required permission:** **Contents → Read-only** (`contents=read`). Confirmed live: both the Trees and Blobs endpoints return `x-accepted-github-permissions: contents=read`.
- **Token lifetime:** 1–366 days or non-expiring, subject to organization policy. The org default caps fine-grained tokens at 366 days. **A non-compliant token is not revoked — it is silently rejected with a 404.**

**Why not a GitHub App installation token** (the obvious reviewer question): a CEL program **cannot mint one**. The flow requires signing an **RS256** JWT, and mito — the CEL library behind the Filebeat `cel` input — registers only `base64`, `md5`, `sha1`, `sha256`, `hmac`, `hex`, and `uuid`. There is no RSA signing primitive and no JWT builder, only symmetric HMAC. Pasting a pre-minted installation token into the config does not help either: it expires in one hour. This is a concrete technical blocker, not a preference.

**Rate limits:**

| Authentication | Limit |
|---|---|
| Unauthenticated (by IP) | 60/hr |
| Personal access token, classic or fine-grained | **5,000/hr** |
| GitHub App installation | 5,000/hr (15,000 on GHEC) |
| Secondary: points per minute per endpoint | 900 (a GET costs 1 point) |
| Secondary: concurrent requests | 100 |

Headers: `x-ratelimit-limit`, `x-ratelimit-remaining`, `x-ratelimit-used`, `x-ratelimit-reset` (UTC epoch seconds), `x-ratelimit-resource`, `retry-after`.

Two traps worth designing against. First, **the 5,000/hr limit is per *user*, not per token** — minting a second token buys nothing. Second, a secondary rate limit was triggered accidentally during this research and returned **HTTP 429 while `x-ratelimit-remaining` was still 10**, with no `retry-after` header. A client that only checks `remaining == 0` would conclude it had budget and retry immediately. **Status code must be treated as authoritative on its own.**

### 3.2 Endpoints / data paths

| Endpoint / Path | Method | Purpose | Returns |
|---|---|---|---|
| `/repos/{owner}/{repo}/git/trees/{branch}:{path}?recursive=1` | GET | Enumerate every advisory file under the directory | `tree[]` of `{path, mode, type, sha, size, url}` plus a `truncated` flag |
| `/repos/{owner}/{repo}/git/blobs/{sha}` | GET | Fetch one advisory file's content | `{content (base64), encoding, url, sha, size, node_id}` |
| `/repos/{owner}/{repo}` | GET | Diagnostic only — confirms access and returns `default_branch` | repository metadata |
| `/rate_limit` | GET | Diagnostic only — does not count against the primary limit | per-bucket limits |

The base64 `content` field is **MIME-wrapped with a newline every 60 characters**. This is safe: mito's `base64_decode` uses Go's `base64.StdEncoding.DecodeString`, which ignores `\r` and `\n`. Re-verified on the review pass by compiling and running the decode against a newline-wrapped value — no stripping needed. Note the precise scope of the guarantee: Go ignores `\r` and `\n` **and nothing else**, so the claim holds only because GitHub emits `\n` alone. Preferring `Accept: application/vnd.github.raw` (§2.1) sidesteps the question.

**Requesting a path that is a file rather than a directory returns HTTP 422**, not 404, with a distinct message. This is the one input error that is distinguishable from the others, and it is worth surfacing in diagnostics rather than collapsing into the generic 404 case.

### 3.3 Pagination

- **Mechanism:** **none.** Neither endpoint paginates. The Trees API returns the entire sub-tree in one response; the Blobs API returns exactly one blob.
- **Truncation indicator:** the Trees response's `truncated` boolean. Documented bound is 100,000 entries / 7 MB, though an 18.4 MB response returned `truncated: false` in testing, so treat the **entry count as the reliable bound and always check the flag**.
- **Consequence:** a `batch_size` / `page_size` configuration variable would be inert and is excluded (§6).

### 3.4 Time-based filtering

- **Not applicable.** The Trees API returns the **current state** of a directory, not a time-ordered feed. There is no `since` parameter and no time window.
- **Incremental collection strategy:** persist the sub-tree ETag and a `path → blob SHA` map in the CEL cursor. Send `If-None-Match`; on 304 stop; on 200 diff the tree against the stored map and fetch only new or changed SHAs.
- **Consequence:** an `initial_interval` variable has no meaning here and is excluded (§6). The first poll captures the entire corpus by construction.
- **Cursor size:** each entry costs roughly a 45-character path plus a 40-character SHA. Re-measured across the plausible corpus range:

| Corpus | Cursor size in the Filebeat registry |
|---|---|
| 500 files | ~62 KiB |
| 1,000 files | ~88 KiB |
| 3,000 files | ~185–264 KiB |

  This is the main cost of the strategy, and it is **3–6× the 40–50 KB pass 1 estimated**. It remains workable — a few hundred KiB of registry state is unremarkable — but it should be a known cost rather than a surprise, and the backfill should write the cursor incrementally after each batch so that an interrupted first run resumes rather than restarts.

### 3.5 Reference documentation

| Title | URL | Relevance |
|---|---|---|
| Git Trees API | <https://docs.github.com/en/rest/git/trees> | Primary enumeration endpoint |
| Git Blobs API | <https://docs.github.com/en/rest/git/blobs> | Primary content endpoint |
| Repository contents | <https://docs.github.com/en/rest/repos/contents> | Rejected alternative; documents the 1,000-file cap |
| REST API rate limits | <https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api> | Limits and headers |
| REST API best practices | <https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api> | Conditional requests; the "304 is free" guarantee |
| Managing personal access tokens | <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens> | Fine-grained token creation, permissions, lifetime |
| Authenticating as a GitHub App installation | <https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation> | Why the App path is infeasible in CEL |
| GHES REST quickstart | <https://docs.github.com/en/enterprise-server@3.14/rest/quickstart> | The `/api/v3` base URL form |
| Elastic Product Security | <https://www.elastic.co/product-security> | Advisory policy; names Discourse as the sole publication channel |
| Elastic Security Announcements | <https://discuss.elastic.co/c/announcements/security-announcements/31> | The public advisory corpus |
| Elastic advisory generator prompt | <https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder/agent-creation-prompt.md> | **Elastic's own advisory template** — the authoritative field list |
| CVE Record 5.x API | <https://cveawg.mitre.org/api/cve/CVE-2026-33461> | The structured twin of an ESA |
| CVE Program CNA list | <https://raw.githubusercontent.com/CVEProject/cve-website/dev/src/assets/data/CNAsList.json> | Confirms `CNA-2017-0011`, shortName `elastic` |

---

## 4. Data Format and Structure

### 4.1 Format overview

- **Wire format (transport):** JSON from the GitHub API, with the file body as base64 inside `content`, or as raw bytes when `Accept: application/vnd.github.raw` is used.
- **Wire format (file body):** **JSON.** Established by the reported filename `ESA-2026-0081.json`.
- **Filename convention:** `ESA-YYYY-NNNN.json`, sequence zero-padded to four digits. Casing of the extension and the presence of non-advisory files alongside the advisories are `[UNVERIFIED]`.
- **JSON field names:** **`[UNVERIFIED]`.** This is the remaining blocking unknown (§8, question 1).
- **Encoding:** UTF-8
- **Compression:** none
- **Envelope structure:** `{"sha", "url", "tree": [...], "truncated": bool}` for enumeration; `{"content", "encoding", "url", "sha", "size", "node_id"}` per blob.

### 4.2 Event types

There is **one** event type: a security advisory. Variants within it that a parser must handle:

| Variant | Description | Relative volume | Priority |
|---|---|---|---|
| First-party advisory | Elastic-assigned CVE, full CWE/CAPEC/CVSS detail | High | High |
| Third-party dependency advisory | `CWE-1395`, references an upstream CVE Elastic did not assign (e.g. ESA-2026-41) | Medium | High |
| Multi-product advisory | One advisory covering Beats + Elastic Agent + APM Server + Fleet Server (e.g. ESA-2023-16) | Low | Medium |
| Multi-ESA advisory | One forum topic carrying two ESA IDs — historical only, all 2025–2026 posts carry exactly one | Low | Low |
| "Living" advisory | Long-lived with a revision `Update Log`; ESA-2021-31 (Log4Shell) is 35 KB with nine revisions | Very low | Medium — the worst case for any parser |
| Rejected / withdrawn | 27 of 340 CVE records are in `REJECTED` state with `rejectedReasons` | Low | Low |

### 4.3 Field inventory

Elastic publishes its **own advisory template** in a public repo (linked in §3.5), which is the authoritative field list. A verbatim copy is at `references/elastic-advisory-generator-prompt-TEMPLATE.md`.

Frequencies below are re-derived across 53 real advisory bodies sampled from 2021–2026. **Pass 1's version of this table was materially wrong and misleading**, in a way worth understanding before using it: it counted only the *bold-label* spelling of each heading, then presented the result as if it measured whether the field was *present at all*. That turned a heading-style census into a false claim that 11 of 53 advisories omit `Affected Versions:`. In fact every advisory in the sample carries it. Two columns are separated below so the distinction is explicit.

#### Common fields

| Field | Where it appears | Bold-label form | Present in any form (of 53) |
|---|---|---|---|
| ESA ID | Topic title, usually in trailing parentheses | — | Yes (2023+) |
| `CVE ID:` | Body footer line | 47 | **53 — always** |
| `Severity:` (label + CVSS score + vector) | Body footer line | 44 | 50 (3 advisories carry no severity at all) |
| `Affected Versions:` | Bullet list keyed by major series | 39 (+12 ATX, +2 unmarked) | **53 — always** |
| `Solutions and Mitigations:` | Prose naming fix versions | 38 (+13 ATX, +2 unmarked) | **53 — always** |
| Advisory title (`<CWE Title> in <Product> Leading to <Impact>`) | First line of body | — | 2026+ consistently |
| Description paragraph | After the title | — | Yes |
| `Affected Configurations:` | Prose | 18 | 20 |
| `For Users that Cannot Upgrade:` | Workarounds, with `Self-Managed`/`Cloud` sub-blocks | 16 | 23 |
| `Problem Type:` (CWE ID + title) | Body footer line | 13 | 13 — modern advisories only |
| `Impact:` (CAPEC ID + title) | Body footer line | 13 | 13 — modern advisories only |
| `Indicators of Compromise (IOC)` | Detection guidance prose | 4 | 4 in sample (8 across all 57 bodies on disk) |
| `Elastic Cloud Serverless` | Boilerplate remediation statement | 4 | 4 in sample (8 across all 57) |
| `Acknowledgements:` | External reporter credit | **2** | 3 (one credits a reporter in prose with no heading) |
| `Update Log` / `Change log` / `Updates` | Revision history | 6 | 6 (1 `## Update Log`, 2 `### Change log`, 3 `### Updates`) |
| Publication date | **Envelope only, never the body** | — | Yes |

**The practical reading**: `CVE ID`, `Affected Versions` and `Solutions and Mitigations` are universal and a parser may treat them as required; `Severity` is near-universal but genuinely absent 3 times in 53; everything else is optional. Note this table describes the **published Discourse rendering**, which is the fallback data source. It constrains the repository JSON only insofar as both are renderings of the same advisory.

#### Structured fields available from the CVE Record 5.x twin

Every first-party ESA also exists as a CVE Record, which is genuinely structured and freely retrievable without authentication. Aggregate shape across all **340** Elastic-assigned records:

| CVE Record path | ESA equivalent |
|---|---|
| `cveMetadata.cveId` / `.datePublished` / `.dateUpdated` / `.dateReserved` | CVE ID; dates |
| `containers.cna.title` | Advisory title line |
| `containers.cna.descriptions[].value` | Description paragraph — **identical in 24 of 44 comparable pairs (55%)**, not "every case" as pass 1 claimed. Best in 2026 (13 of 18). Of the mismatches, 8 differ only because the ESA carries Markdown links the CVE record flattens, 6 are CVE text truncated relative to the ESA, and 6 are genuinely different prose. Do not treat the two as interchangeable. |
| `containers.cna.affected[].vendor` / `.product` / `.defaultStatus` | Product |
| `containers.cna.affected[].versions[]` | `Affected Versions:` as `{version, lessThan\|lessThanOrEqual, status, versionType}` |
| `containers.cna.metrics[].cvssV3_1` | `Severity:` — **fully decomposed metrics** plus `vectorString` and `baseScore` |
| `containers.cna.problemTypes[].descriptions[].cweId` | `Problem Type:` |
| `containers.cna.impacts[].capecId` | `Impact:` |
| `containers.cna.references[].url` | The `discuss.elastic.co` back-link — **this is the only CVE↔ESA join** |
| `containers.cna.credits[]` | `Acknowledgements:` (only 5 of 340 records) |
| `containers.cna.x_generator.engine` | Elastic's tooling fingerprint (§4.6) |

Container key counts: `affected` 313, `descriptions` 313, `references` 313, `problemTypes` 311, `x_generator` 204, `metrics` 203, `title` 193, `impacts` 129, `credits` 5. Metrics are `cvssV3_1` ×201 and `cvssV4_0` ×2 — **CVSS v3.1 is the norm, v4.0 a rare exception**.

**Critically, the CVE record does not carry the fixed version**, and there is **no ESA ID field anywhere** in it. Both exist only in the ESA prose.

### 4.4 Sample data

`references/sample-events/` holds nine verbatim real advisories plus machine-readable variants, each with a provenance header:

- `ESA-2026-24.md` — Kibana Fleet; the fullest modern template, every optional section present
- `ESA-2026-01.md` — Metricbeat; the advisory Elastic cites as the first output of its AI drafting pipeline
- `ESA-2026-02.md` — Packetbeat; `Acknowledgements:`, ATX headings, bare CVSS vector with no `CVSS:3.1/` prefix
- `ESA-2026-41.md` — Fleet Server; the third-party dependency (CWE-1395) variant
- `ESA-2026-128.md` — `Description:` label variant plus a genuine duplicated heading; a good malformed-input test
- `ESA-2025-14.md` — Elasticsearch/Tika; long multi-step workaround with inline code and API links
- `ESA-2024-01.md` — leaner 2024 template, no CWE/CAPEC/IOC/Serverless
- `ESA-2023-16.md` — multi-product, 2023 ATX-heading style
- `ESA-2021-31.md` — Log4Shell; a 35 KB living document with a nine-entry `Update Log`. The parser worst case.
- `ESA-2026-24.cve-record-5.1.json`, `ESA-2026-24.github-advisory.json`, `ESA-2025-20.osv.json`, `ESA-2026-128.discourse-topic.json`, `ESA-2026-128.discourse-rss-item.xml`, `discourse-category-topic-list.json`
- **`ESA-2026-24.mapped-ecs.json`** — the hand-written expected post-ingest document. The most useful single artifact for the integration builder.

Complete field inventory and heading-variant analysis: `references/esa-publication-landscape.md` §3. Raw artifacts — all 315 forum topics, 57 raw advisory bodies (53 of which form the sampled statistics set), all 340 CVE records, the full NVD response, 177 resolved CVE→ESA mappings — are in `temp/`.

#### Inline sample (ESA-2026-24, verbatim)

```
**Incorrect Authorization in Kibana Fleet Leading to Information Disclosure**

Incorrect Authorization (CWE-863) in Kibana can lead to information disclosure via Privilege Abuse
(CAPEC-122). A user with limited Fleet privileges can exploit an internal API endpoint to retrieve
sensitive configuration data, including private keys and authentication tokens, that should only be
accessible to users with higher-level settings privileges.

**Affected Versions:**

* 8.x: All versions from 8.0.0 up to and including 8.19.13
* 9.x:
  * All versions from 9.0.0 up to and including 9.2.7
  * All versions from 9.3.0 up to and including 9.3.2

**Affected Configurations:**

Deployments with Fleet enabled where users have been granted the Fleet Agents privilege without the
Fleet Settings.

**Solutions and Mitigations:**

The issue is resolved in versions 8.19.14, 9.2.8, and 9.3.3.

**For Users that Cannot Upgrade:**

* Review Fleet role assignments
* Rotate any proxy credentials (private keys, authentication tokens)

**Indicators of Compromise (IOC)**

Review Kibana audit logs for access to Fleet enrollment settings endpoints

**Elastic Cloud Serverless**

Due to our continuous deployment and patching model, the vulnerability described in this security
advisory was remediated in our Elastic Cloud Serverless offering before the public disclosure.

**Severity:** CVSSv3.1: High ( 7.7 ) \- CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
**CVE ID:** CVE-2026-33461
**Problem Type:** CWE-863 \- Incorrect Authorization
**Impact:** CAPEC-122 \- Privilege Abuse
```

### 4.5 Timestamp handling

- **Primary timestamp field:** the advisory publication date → `@timestamp`.
- **Format:** ISO 8601 / RFC 3339 with timezone.
- **Timezone:** UTC.
- **Three competing sources**, which differ by minutes. For ESA-2026-24: Discourse `created_at` is `2026-04-08T16:18:41.426Z`, CVE `datePublished` is `2026-04-08T16:41:27.335Z`. The advisory record's own published date is authoritative; fall back to the CVE date.
- **Secondary timestamps:** advisory last-updated, CVE `dateReserved` (~19 days before publication), CVE `dateUpdated` (changes when CISA ADP enriches, independently of Elastic), and the git last-commit date.
- **The ESA year and the publication date are independent.** `ESA-2024-20` was posted 2025-05-01. Nothing should derive one from the other.

#### The ESA identifier has two renderings, and they do not string-match

This is new in the review pass and it affects the natural key, every join, and the document `_id`.

| Context | Padding | Examples |
|---|---|---|
| **Repository filename** | Fixed width, **4 digits** | `ESA-2026-0081.json` |
| **Every public rendering** (forum title, slug, Elastic's own template, blog) | Minimum width **2**, widening naturally | `ESA-2024-01`, `ESA-2026-81`, `ESA-2026-137` |

Verified across 315 forum titles, 57 advisory bodies and 340 CVE records: the four-digit form appears **nowhere** publicly, and a bare single-digit form (`ESA-2026-1`) appears nowhere either — public IDs are zero-padded, just to a different width. `ESA-2026-0081` and `ESA-2026-81` are the same advisory.

Three consequences:

1. **Normalize to `(year, integer sequence)`.** This is the only representation that is stable across both renderings. Deriving an integer sequence handles `0081` → `81` naturally.
2. **Never string-compare or string-sort ESA IDs.** Public IDs sort incorrectly as strings above sequence 99 (`ESA-2026-137` sorts before `ESA-2026-24`); repository IDs sort correctly but will not match the public form. Fixed-width formatting to two digits also breaks above 99.
3. **Fingerprint the document `_id` over the normalized ID** (§5.6). If a raw filename ID is used and normalization is added later, every `_id` in the index changes and the entire corpus silently duplicates.

Whether the JSON's own internal ID field is padded, unpadded, or absent is `[UNVERIFIED]` — the filename is the only observation available.

### 4.6 Special parsing considerations

**The format is JSON. What remains unknown is the schema inside it.** Pass 1's inference table is superseded; the graded post-mortem of how well it predicted the answer is in `references/advisory-file-format.md`, and the short version is that it ranked the true answer (JSON) *below* the false one (YAML/Markdown). What survives is the reasoning that a **structured source of truth exists**, which was rated High and is now confirmed by the format itself:

- **Batched publication.** 48 advisories, 48 CVE records and a coordinated release train in one day is implausible by hand.
- **A bespoke publishing tool.** 204 of 340 CVE records carry an `x_generator`: 122 name **"Elastic CVE Publisher"** (74 × `0.0.1`, 48 × `1.0.0`) and 82 name the off-the-shelf Vulnogram they used earlier. A tool that emits valid CVE 5.x JSON must read structured input, and a JSON advisory record is the natural candidate for that input.
- **A reserved-then-published ID space with real gaps** — 21 unpublished sequence numbers in 2026, 5 in 2024. That is the signature of a registry, not a folder of hand-written documents.
- **A slot-filling template** with conditional blocks driven by a product lookup table, which is a template rendered over a data record.

#### Which JSON schema? Candidates, evaluated

| Candidate | Verdict | Evidence |
|---|---|---|
| **Bespoke Elastic schema** | **Most likely** | Nothing standard fits the filename and field requirements simultaneously. The ESA-keyed filename implies an ESA-native record. |
| CVE Record 5.x | **Unlikely as the whole document** | CVE 5.x records are conventionally keyed by **CVE** ID (`CVE-2026-33461.json`); this file is keyed by **ESA** ID. ESA↔CVE is also many-to-many, and dependency advisories have no Elastic-assigned CVE at all, so a CVE-keyed schema cannot be the primary record. CVE 5.x also has no slot for the ESA ID, fixed versions, affected configurations, workarounds, IOC guidance, or the Serverless statement. |
| OSV | **Ruled out** | Structurally the closest analogy — OSV databases are conventionally one JSON file per vulnerability ID — but `ESA` is not among OSV's 47 registered prefixes, OSV requires an `x_` prefix for local databases, and every `ESA-` ID returns 404 from `api.osv.dev`. |
| CSAF 2.0 | **Ruled out** | CSAF §5.1 mandates *lowercase* filenames; this file is uppercase. Elastic serves no `provider-metadata.json`, no `index.txt`, no `aggregator.json` and no `security.txt` at either location — all 404 against a control URL that returns 200. |
| ECS-shaped JSON | **Possible, weakly supported** | In 2020 Elastic's Product Security lead stated the plan was to publish advisories "in ECS format… allow the JSON to be downloaded". Against it: the promised ECS additions never landed, and ECS's `vulnerability.*` fieldset still has no fields for version ranges, fixed versions, CWE or CAPEC — so an ECS-shaped record could not represent an advisory without heavy custom extension. |

One useful negative: Elastic's public advisory-drafting pipeline (the Security Labs RAG/Agent Builder work) emits **Markdown, not JSON**, so it is not the producer of these files.

Two residual layout unknowns, neither of which affects the design: whether the directory is flat or year-nested (recursive enumeration handles both transparently, and >1000 files makes nesting more likely), and whether non-advisory JSON sits alongside the advisories (which is why the file-pattern default stays empty — §6.2).

#### The one thing that could get harder

If the JSON turns out to be a CVE-record rendering rather than an ESA superset, then **fixed versions, affected configurations, workarounds, IOC guidance and the Serverless statement have no source in the repository at all** — the CVE record carries none of them, and fixed versions in particular exist only in the ESA's `Solutions and Mitigations` prose. That would make the public Discourse path a required companion rather than an optional fallback (§7.3). The filename evidence argues against this outcome, but it is the single most consequential thing that one look at a real file would settle.

#### Markdown parsing hazards — now scoped to the fallback path only

The formatting hazards below apply to the **public Discourse rendering** (§2.2's alternative source), *not* to the GitHub JSON path. Pass 1 presented them as the central parsing risk; with a JSON source they are irrelevant unless the public path is built. They are retained because that path remains a live option.

- **Heading style is not stable.** Modern advisories use `**Bold Label:**`; 2023-era and some 2026 ones use ATX headings (`### Affected Versions:`). In the 53-advisory sample, 12 `Affected Versions:` and 13 `Solutions and Mitigations:` were ATX rather than bold.
- **The colon comes and goes:** `**CVE ID**: CVE-…` and `**CVE ID:** CVE-…` both occur.
- **Headings can be duplicated.** ESA-2026-128 has `**For Users that Cannot Upgrade:**` twice in a row.
- **The CVSS vector prefix is inconsistent.** Usually `CVSS:3.1/AV:N/…`, but ESA-2026-02 has a bare `AV:A/AC:L/…`.
- **Severity label and score ordering varies:** `Medium (6.5)`, `High ( 7.7 )` with spaces inside the parens, and `8.8(High)` score-first all appear.
- **Discourse emits escaped hyphens** (`\-`) for some separators.
- **A non-standard `MPR` environmental metric appears once**, spliced onto what is labelled a base vector (ESA-2025-14).
#### Data hazards that apply to *both* paths

These three are properties of the advisory data itself, not of its Markdown rendering, so they survive the move to JSON and must be handled regardless of source:

- **Version ranges are discontinuous per release branch.** `9.0.0–9.2.7` plus `9.3.0–9.3.2` is not one range; Elastic maintains parallel release branches and each gets its own bound. A series may also be listed with **no upper bound** (`7.x: All versions`), meaning the whole series is affected and unfixed. This is the reason the range array must be `nested` (§5.6).
- **Boundary inclusivity varies.** The modern form is inclusive (`up to and including`); older records are exclusive (`before`, `up to, but not including`). In the CVE corpus this surfaces as `lessThan` versus `lessThanOrEqual`, and the two must not be conflated. Distribution across 558 CVE version objects: `semver` 432, no `versionType` 120, `custom` 4, plus one each of the non-standard `1.x.x` and `8.x.x`.
- **Product naming is not normalised.** `Kibana`/`kibana`, `Elastic Cloud Enterprise`/`Elastic Cloud Enterprise (ECE)`, and `Elastic Enterprise Search`/`Enterprise Search`/`Enterprisesearch` all coexist. A normalisation table is needed.

---

## 5. ECS Mapping Analysis

Full analysis with the precedent survey, ECS existence verification, and the complete nine-part mapping table: `ecs-mapping-analysis.md`. Every ECS claim was checked against the generated ECS schema rather than recalled.

### 5.1 Categorization per event type

| Event type | event.kind | event.category | event.type | event.outcome |
|---|---|---|---|---|
| Security advisory | `enrichment` | `[vulnerability]` | `[info]` | unset |

`event.dataset: elastic_security_advisories.advisory`, `event.module: elastic_security_advisories`.

**The decisive precedent** is `packages/github/data_stream/security_advisories`, which ingests GitHub Security Advisory documents — a structural twin of an ESA (stable advisory ID, CVE ID, CVSS score and vector, CWE list, description, affected version ranges, credits, published/updated dates) — and sets exactly that triple at `elasticsearch/ingest_pipeline/default.yml:12-25`, verified line-exact. ECS reinforces it independently: `event.category: vulnerability` declares `expected_event_types: ["info"]`, so `[info]` is the only ECS-sanctioned pairing.

**Two corrections to how pass 1 argued this.** The conclusion stands; the supporting framing did not survive audit.

- The survey covered **75 vulnerability-touching streams across 58 packages**, not the "34 streams" pass 1 claimed. No reading of the criterion produces 34, and the tables actually enumerate about 30 — so this was never the exhaustive survey it was described as.
- The claimed "clean split" holds in **one direction only**. Of the asset-finding streams, *zero* use `enrichment` — that half is solid. But of the catalog/reference streams, only 4 use `enrichment`; the other 6 use `state`, `event` or `alert`. "Catalog streams lean `enrichment`" is false as an aggregate. Also, `ti_google_threat_intelligence/vulnerability_weaponization` was miscited as corroboration: it sets `event.category: threat` / `type: indicator`, so only the `kind` matches. Its sibling `vulnerability` stream does match exactly, as does `first_epss/vulnerability`.

The recommendation therefore rests on the structural twin plus ECS's own `expected_event_types`, not on a monorepo consensus that does not exist. That is still a strong basis. `event.kind: state` remains wrong here for a substantive reason: it is the CDR finding framing and arrives bundled with `resource.id`, `resource.name`, `host.name`, `package.version` — all of which need an evaluated asset that an advisory does not have.

**This is an event stream, not an entity stream.** Only one of the two required entity-classification signals holds. More importantly, the ECS `entity.type` allowed values are `bucket, database, container, function, queue, host, user, application, service, session, cloud, orchestrator` — an advisory is none of them, and `event.kind: asset` would drop disclosure records into entity-store views alongside users and hosts.

### 5.2 Field mappings

The `vulnerability.*` fieldset has exactly **13 members** at ECS v9.3.0, plus `vulnerability.status` added at v9.5.0 (beta). **Ten are usable** — pass 1 said nine here while its own companion table marked ten; the discrepancy was `vulnerability.scanner.vendor`, which is semantically loose but recommended, so it is counted below:

| Source field | ECS field | Notes |
|---|---|---|
| CVE ID | `vulnerability.id` | |
| ESA ID (normalized) | `vulnerability.report_id` | Secondary; the canonical home is the custom namespace. Must use the normalized ID (§4.5) |
| (constant `CVE`) | `vulnerability.enumeration` | |
| (constant `CVSS`) | `vulnerability.classification` | |
| Description paragraph | `vulnerability.description` (+ `.text`) | Identical to the CVE record's description in only 55% of cases — see §4.3. Prefer the advisory's own text |
| Severity label | `vulnerability.severity` | ECS declares no allowed values; documented example is Title Case |
| CVSS base score | `vulnerability.score.base` | **`float`** — fixed by ECS |
| CVSS version (`"3.1"`) | `vulnerability.score.version` | `keyword`, not numeric |
| `discuss.elastic.co` URL | `vulnerability.reference` | Also `event.reference`, `event.url`, `url.original`/`url.full` |
| (constant `Elastic`) | `vulnerability.scanner.vendor` | Judgement call for cross-integration query symmetry. Precedent: `ti_google_threat_intelligence/vulnerability` sets `Google`; counter-precedent: `github/security_advisories` omits it |

**Not usable:** `.score.temporal` and `.score.environmental` (Elastic publishes base metrics only), `.category` (a Qualys platform bucket — nothing maps), and `.status` (describes a finding on an asset; no asset exists, so do not bump the ECS pin to reach it).

Other ECS fields that do apply: `event.id` (ESA ID), `event.original` (the verbatim source file), `package.name` (affected product, array), `file.path`/`.name`/`.extension`/`.size` (git provenance), and `url.*` (the advisory link).

**The biggest gaps.** `vulnerability.*` has **no fixed-version field and no version-range field of any kind** — no bounds, no inclusivity flag, no version-type discriminator, and no way to express that Elastic's ranges are discontinuous per release branch. `package.*` does not help: its members describe one *installed* package instance, and `package.version` means "the version on this asset", so populating it from an advisory's lower bound would be a lie. `package.fixed_version` is a widely-copied CDR convention but is **not ECS** — it is a custom field in **12** packages (pass 1 said ten, turning its own "at least ten" lower bound into a precise count that was also low).

Also worth recording: `file.extension` for these records is **`json`**, not the `md` pass 1 assumed, and `file.name` follows the four-digit form (`ESA-2026-0081.json`).

Fields with no ECS home, needing `elastic_security_advisories.advisory.*`:

| Source field | Custom target | Why no ECS |
|---|---|---|
| ESA ID (canonical) | `…advisory.esa_id` | No ECS field for a vendor advisory ID |
| Advisory title | `…advisory.title` | **`vulnerability.title` does not exist.** Confirmed absent v9.3.0 → main |
| CVSS vector string | `…advisory.cvss.vector_string` | No ECS field for a CVSS vector |
| Decomposed CVSS metrics | `…advisory.cvss.attack_vector`, `.attack_complexity`, `.privileges_required`, `.user_interaction`, `.scope`, `.confidentiality_impact`, `.integrity_impact`, `.availability_impact` | Precedent: `hackerone/data_stream/report/fields/fields.yml:477-489`, `google_scc/data_stream/finding/fields/fields.yml:786-806` |
| CWE ID + title | `…advisory.cwe.id` / `.title` | **ECS has no CWE fieldset anywhere** |
| CAPEC ID + title | `…advisory.capec.id` / `.title` | **`threat.technique.*` is ATT&CK, not CAPEC — do not misuse it** |
| Affected version ranges | `…advisory.affected_versions` (**`nested`**) | §5.4 |
| Fixed versions | `…advisory.fixed_versions` | No ECS field; **absent from the CVE record entirely** |
| Affected configurations, workarounds, IOC guidance, Serverless statement | `…advisory.affected_configurations`, `.workarounds`, `.indicators_of_compromise`, `.serverless_statement` | ESA-only sections |
| Acknowledgements / credits | `…advisory.acknowledgements`, `.credits.value`, `.credits.type` | `user.name` is wrong — the credited party is an external researcher, not an actor in an event |
| Git provenance | `…advisory.git.owner`, `.repository`, `.ref`, `.path`, `.blob_sha`, `.commit_sha`, `.last_commit_date`, `.html_url` | |

One trap worth stating: **the git blob SHA must not go in `file.hash.sha1`.** A git blob hash is `sha1("blob <len>\0" + content)`, not the content's SHA-1.

The `Indicators of Compromise (IOC)` section is **detection guidance prose, not indicators** — it contains advice to review audit logs, not IOC values. It must not go in `threat.indicator.*`.

### 5.3 Related field enrichment

| ECS enrichment field | Source fields |
|---|---|
| `related.ip` | none |
| `related.user` | none |
| `related.hosts` | none |
| `related.hash` | none |

**Nothing belongs in `related.*`.** An advisory contains no IPs, hostnames, usernames, or artifact hashes. The three tempting candidates are all wrong: `discuss.elastic.co` is a documentation URL and not a host in the event, the git blob SHA is not a content hash of an artifact, and a credited researcher is not a user in the system. `ecs-mapping-analysis.md` §5.1 spells out each.

### 5.4 Geo enrichment candidates

**None.** There are no IP address fields in the data.

### 5.5 Entity field coverage

> N/A — no entity data streams identified. See §5.1 for why the entity framing was considered and rejected.

### 5.6 Mapping type decisions worth flagging

**The version-range array must be `nested`.** Under the default `object` mapping, ESA-2026-24's three ranges flatten to parallel arrays, and the query "is Kibana 8.19.20 affected?" matches the lower bound from one range against the upper bound of a *different* range — a false positive on a version that is genuinely fixed. Bounds should use Elasticsearch's `version` type, not `keyword`: `keyword` compares lexicographically, and `"8.19.13" < "8.2.0"` lexically, which is guaranteed wrong for Elastic's double-digit patch numbers. Denormalising `product`/`vendor` into each range object (rather than nesting inside a nested `affected[]`) keeps multi-product advisories correct with a single-level query.

**Document `_id`: fingerprint of the *normalized* ESA ID + git blob SHA.** Advisories are mutable — Elastic amends them, and ESA-2021-31 carries a nine-entry revision history. Every comparable reference stream in the monorepo uses natural-key-plus-change-detector (`qualys_vmdr/knowledge_base`, `tenable_io/plugin`, `ti_google_threat_intelligence/vulnerability`, `ti_flashpoint/vulnerability`, `rapid7_insightvm/vulnerability`). The blob SHA beats a timestamp: it is a content hash that changes if and only if bytes change, it arrives free on every Trees API poll, and it works even though whether the repo record carries an `updated_date` at all is `[UNVERIFIED]`. It also preserves the revision history as separate documents instead of collapsing it to whatever the last poll saw, with the corollary that any "current state" view needs a most-recent-per-advisory collapse. A deterministic `_id` additionally means an accidental multi-agent enrolment dedupes rather than duplicates.

Three caveats the audit added:

- **Normalize the ID before fingerprinting** (§4.5). Fingerprinting the raw four-digit filename form and adding normalization later would change every `_id` and silently duplicate the whole corpus.
- **A custom `_id` and a TSDS are mutually exclusive.** Nothing here proposes a TSDS and an advisory stream is a poor TSDS candidate anyway, but this choice forecloses that option permanently and should be made knowingly.
- **The mutability premise rests on a single sample.** `ESA-2021-31` is the only advisory in the 53-body sample with a revision log, and that log lives in the Discourse post, not in a verified repository file. Whether repository files are amended in place, and whether they carry any revision marker, is `[UNVERIFIED]` — which is precisely why the content-hash approach was chosen over a timestamp.

---

## 6. Configuration Plan

Full plan with per-variable justification, exclusions, and the precedent survey: `configuration-plan.md`.

### 6.1 Required configuration variables

| Variable | Type | Title | Description | Default | Show user | Secret |
|---|---|---|---|---|---|---|
| `api_url` | text | API URL | GitHub REST API base URL, no path. `https://api.github.com` for GitHub.com; `https://HOSTNAME/api/v3` for GHES; `https://api.SUBDOMAIN.ghe.com` for GHEC data residency. | `https://api.github.com` | false | — |
| `api_key` | password | GitHub Personal Access Token | Fine-grained token with resource owner set to the organization, access limited to the one repository, and `Contents: Read-only`. Required — the repository is private. | — | true | **true** |
| `owner` | text | Repository owner | Owner of the repository; the organization name if org-owned. | `elastic` | true | — |
| `repo` | text | Repository | The repository containing the advisory files. | `security-advisories` | true | — |
| `path` | text | Directory path | Directory inside the repository holding the advisories, relative to the root, no leading or trailing slash. Collected recursively. | `advisories` | true | — |
| `branch` | text | Branch | Branch to read from; a tag or commit SHA is also accepted. An incorrect value returns HTTP 404, indistinguishable from a permissions failure. | `main` | true | — |
| `interval` | text | Interval | Duration between GitHub API requests (h/m/s). Unchanged polls return HTTP 304 and consume no rate-limit budget. | `1h` | true | — |

**`api_key` is the only secret.**

`owner` and `repo` are two variables rather than one `owner/repo` string. This matches four existing `github` data streams (`code_scanning`, `dependabot`, `issues`, `secret_scanning`), matches the REST API's own path parameters, and — most importantly here — keeps the malformed-input surface small. That matters disproportionately when **every** input error produces the same undiagnosable 404.

### 6.2 Optional configuration variables

| Variable | Type | Title | Description | Default | Show user | Secret |
|---|---|---|---|---|---|---|
| `file_pattern` | text (multi) | File name patterns | Glob patterns matched against each file's path relative to the directory. Empty collects everything. Use to exclude `README.md`, templates, or schema files. | — (empty) | true | — |
| `http_client_timeout` | text | HTTP Client Timeout | Duration before the HTTP client connection times out. | `60s` | false | — |
| `proxy_url` | text | Proxy URL | `http[s]://<user>:<password>@<server>:<port>`, URL-encoded. | — | false | — |
| `ssl` | yaml | SSL Configuration | Needed only for GHES with a private CA, or a TLS-intercepting proxy. | — | false | — |
| `tags` | text (multi) | Tags | Tags to include in the published event. | `[forwarded, elastic-security-advisories]` | false | — |
| `processors` | yaml | Processors | Agent-side processors. | — | false | — |
| `enable_request_tracer` | bool | Enable request tracing | Logs requests and responses to the agent's local filesystem for debugging. Compromises security; debugging only. | `false` | false | — |

`file_pattern`'s default **should remain empty**, though the reasoning has changed. Pass 1 argued that guessing an extension was dangerous because the format was unknown — a default of `*.md` against a `.yaml` corpus would yield zero documents and no error. That premise is gone: the extension is known to be `.json`. The residual argument is narrower but still holds: filename casing is unverified, and whether non-advisory JSON (a schema, a template, a manifest) sits alongside the advisories is unknown. An empty default collects everything, which is noisy but visible; `*.json` is now a defensible alternative.

`enable_request_tracer` **is** a first-class CEL variable and should simply be included. Pass 1 flagged it as a "deliberate departure" from the standard variable set requiring special review; that framing inverts the burden of proof. It is declared by **297 of 361 CEL data streams across 102 packages**, and the `github` CEL stream's own description links the CEL input's tracer documentation. The operational argument for it here is strong on its own terms — every misconfiguration produces an identical information-free 404, and the tracer is the only in-product way to see the exact URL requested and the response received.

**Deliberately excluded:**

| Variable | Reason |
|---|---|
| `initial_interval` | There is no time window to look back over. The Trees API returns current state, not a time-ordered feed; the first poll captures the whole corpus by construction. |
| `batch_size` / `page_size` | Neither endpoint paginates, so a *page*-size knob would be inert. But see §7.4: with >1000 files, how many blobs are fetched per execution becomes a real design variable, and the exclusion should be revisited by whoever writes the CEL program rather than treated as settled. |
| OAuth2 block | Authentication is a static bearer token. The GitHub App path is technically impossible in CEL (§3.1). |
| `preserve_original_event` | Excluded because it is an `event.original`-removal toggle, which the research guardrails prohibit proposing. **Pass 1's stated reason was wrong** and should not be repeated: it claimed the variable is valid for filestream and syslog inputs only and "never CEL". In fact **327 of 361 CEL data streams declare it**, and it is functional in CEL — `github/data_stream/security_advisories/agent/stream/cel.yml.hbs:83-84` emits it into `tags`, which the ingest pipeline reads. It is the most common CEL variable after `tags`, `processors` and `interval`. |
| `preserve_duplicate_custom_fields` | Prohibited deprecated anti-pattern. Present in four `github` cloud-input streams (`:252`, `:443`, `:638`, `:782`) — **do not copy from there.** |

**One consequence of excluding `preserve_original_event` that should be deliberate rather than accidental**: the mapping populates `event.original` with the verbatim advisory bytes unconditionally, so with no operator toggle, `event.original` is always retained. For a corpus of a few thousand small JSON documents that is cheap and useful for reprocessing, but it should be a stated decision.

### 6.3 Deployment notes

**Polling interval: `1h`**, argued from the data rather than habit.

The usual cost-versus-freshness trade-off does not apply, because a 304 on an authorized conditional request consumes zero budget — `5m` and `24h` cost exactly the same, which is nothing. So the interval has to be argued on other grounds. The source changes roughly 12–15 times a year (52 distinct publication dates across 203 advisories; the last nine batches spaced 20–50 days apart, mean 30, median 24.5). `5m` buys a 55-minute latency improvement on a monthly event at 12× the poll volume, and now sits well inside the backfill window, risking overlapping work. `24h` — the `github` package's own default for its advisories stream — gives a 24-hour worst case on a security feed, doubling to 48 hours after one failed poll, and buys nothing. `1h` gives same-hour detection, never overlaps a backfill, and matches the `github` package's `audit` stream default and its stated 2m–1h valid range. Defensible range: `15m` to `6h`. **The larger corpus strengthens this recommendation rather than weakening it.**

**Network:** outbound HTTPS (443) to `api.github.com`, or the GHES host. Proxy supported via `proxy_url`.

**Rate limit:** a non-issue in steady state, and a manageable one-time cost on backfill. Steady state is literally zero units — 24 conditional polls a day, all 304s, independent of corpus size. The largest observed batch (48 advisories) costs 49 units, under 1% of one hour. Backfill, re-measured across the plausible corpus range:

| Corpus | API calls | Serial wall time | Share of a 5,000/hr budget |
|---|---|---|---|
| 500 files | 501 | ~1.8 min | 10% |
| 1,000 files | 1,001 | ~3.5 min | 20% |
| 3,000 files | 3,001 | ~10.5 min | 60% |
| ~5,000 files | ~5,001 | ~17 min | **100% — exceeds one hour's budget** |

So the backfill fits inside a single hour's budget up to roughly 5,000 files and only becomes a genuine constraint beyond that. Pass 1's figure of "201–501 requests, 4–10% of a single hour, 1.5–3.5 minutes" was correct for the corpus it assumed and is simply too small; the numbers above replace it. The backfill should be resumable across intervals rather than assumed to complete in one window.

The one real caveat: **the 5,000/hr limit is per user, not per token.** The `github` package's own `security_advisories` stream walks the entire global GitHub Advisory Database with `max_executions: 5000`, meaning one poll can consume the whole hourly budget by itself. If the same GitHub account backs both integrations, it can starve this one. The fix is a *different GitHub account*, not a different token.

**Volume:** still small. Roughly 1,000–3,000 documents on backfill, ~15 new per month, worst case 48 in a single poll. Measured against 57 real advisory bodies, the mean is **3.3 KB** and the median **1.4 KB** (min 545 B, max 53 KB), so even 3,000 documents is on the order of **10 MB** of raw text. Pass 1's "2–10 MB" range was right by luck: its per-document basis of 4–20 KB overstates the median advisory by 3–10×, which happened to offset its underestimate of the document count. No ILM tuning, shard planning, or capacity review is warranted.

**Agent placement — run this on exactly one agent.** The CEL cursor lives in each agent's local Filebeat registry, so running this on N agents produces N independent collectors, N× the documents, and N× the API cost against the same shared budget. Fleet cannot enforce a singleton integration. Recommend agentless (the `github` package already enables it) or a dedicated single-agent policy. The deterministic document `_id` (§5.6) is the safety net that makes an accidental multi-agent enrolment dedupe rather than duplicate.

---

## 7. Recommended Integration Architecture

### 7.1 Package name

`elastic_security_advisories`

### 7.2 Data streams

| Data stream name | Input type | Stream kind | Source | Description |
|---|---|---|---|---|
| `advisory` | `cel` | event | `GET /repos/{owner}/{repo}/git/trees/{branch}:{path}` + `/git/blobs/{sha}` | One document per Elastic Security Advisory file in the repository |
| `advisory_public` *(optional, see §7.3)* | `cel` | event | `discuss.elastic.co` category JSON + `cveawg.mitre.org` | Same corpus from public, credential-free endpoints |

### 7.3 Architecture rationale

**One data stream, because there is one entity.** The repository holds one document type. Splitting by product or by year would fragment a corpus that users want to query as a whole ("which advisories affect Kibana 8.19?"), and the Trees API enumerates the directory in a single call regardless.

**Whether to ship the public path as a second data stream is an open decision** (§8, question 5). The argument for: the private repo may be unreachable by whoever deploys this, and the public path needs no credential at all. The argument against: a second variable set, and a documented "do not enable both against the same index" caveat, for a corpus that largely overlaps. If the token cannot be obtained in reasonable time, build the public stream instead of waiting — the two produce documents that should map onto the same field set, since both are renderings of the same underlying advisory.

**Two things now bear on this decision that pass 1 did not know.** First, if the repository JSON turns out to be a CVE-record rendering, the public path stops being optional: fixed versions, workarounds, affected configurations and IOC guidance would have no repository source at all (§4.6). Second, the public path covers only the ~341 *published* advisories, so if the repository genuinely holds >1000 files, the two sources differ in coverage by roughly 3× and are not interchangeable — which also means the "do not enable both" caveat matters less than the "these are not equivalent" caveat.

### 7.4 Estimated complexity

- **Pipeline complexity:** **simple to moderate**, revised down from pass 1's "moderate to complex". The uncertainty was entirely in the file format, and it resolved in the favourable direction: a JSON source means decode-and-rename plus version-range normalization, not section parsing. The §4.6 Markdown risk register no longer applies to this path. The residual work is real but ordinary: ID normalization (§4.5), product-name normalization, and inclusive/exclusive version bounds. The one scenario that would push this back toward complex is the CVE-record case in §4.6, where fixed versions would have to come from a second source.
- **CEL complexity:** **moderate.** Two endpoints, no pagination, but a stateful `path → blob SHA` map in the cursor, ETag round-tripping, and a per-file fetch loop.
- **Field count estimate:** ~70–90 fields per document, of which ~12 are ECS and the rest sit under `elastic_security_advisories.advisory.*`.

**One scale constraint the CEL author must know about, and the capability that dissolves it.**

`max_executions` bounds how many times a CEL program may ask to be re-run via `want_more`. Its default is **1,000**, and `packages/github/data_stream/security_advisories` raises it to 5,000 at `cel.yml.hbs:24`. It is **not exposed as a Fleet variable**, so a new package must set it in its own template — nothing is inherited.

If the program fetches one advisory per execution, a >1000-file backfill **exceeds the default outright**. It would not fail loudly; it would exhaust the budget, log a warning, and resume at the next interval, converging slowly and noisily.

That one-blob-per-execution model is not forced, however. Verified live against mito v1.27.0: **a single CEL evaluation can issue many serial HTTP requests**, by mapping over a list of blob URLs and calling `do_request()` on each. A run performing one tree request plus ten blob requests in a single evaluation returned ten HTTP 200s with `x-ratelimit-used` advancing monotonically 129→139, confirming the requests are issued serially with no concurrency risk. Reproduction: `temp/api-review/batch.cel`.

The consequence is that blobs-per-execution is a free design variable, and the arithmetic stops being a constraint:

| Blobs per execution | Executions for a 3,000-file backfill | Wall time per evaluation |
|---|---|---|
| 1 | 3,001 | 0.2 s |
| 50 | 61 | 10.5 s |
| 100 | 31 | 21.0 s |

At 50–100 per execution a full backfill fits comfortably inside even the default 1,000 with no need to raise it. The opposite extreme should be avoided: fetching all 3,000 in one evaluation would block the input for over ten minutes. **How to structure this is the CEL author's decision** — recorded here as a verified capability and a sizing constraint, not as a prescription.

---

## 8. Open Questions and Gaps

| # | Question | Impact | Suggested resolution |
|---|---|---|---|
| 1 | **What are the JSON field names?** The format is now known to be JSON and the filename convention is `ESA-YYYY-NNNN.json`. What remains unknown is the schema: the key names, whether the record is an ESA-native superset or a rendering of CVE 5.x, whether it carries fixed versions, and whether it carries a publication status. | **BLOCKING** — determines the field mapping and whether a second data source is required (§4.6) | **The single highest-value action available.** Someone with read access pastes the contents of one file — ideally `ESA-2026-0081.json`, since its public twin `ESA-2026-81` is already captured for comparison. One file collapses the last blocking unknown. |
| 2 | **What accounts for the ~600 files beyond the ~386 publicly-known ESA IDs?** Unpublished advisories, year subdirectories, non-advisory files, or multiple files per advisory? | **High** — determines document counts, whether a status filter is needed, and question 11 | `gh api repos/elastic/security-advisories/git/trees/main:advisories?recursive=1` and a count by path shape. Answers this and question 3 together. |
| 3 | Do the **unpublished ESA IDs** (21 gaps in 2026, 5 in 2024) exist as files, perhaps marked withdrawn or embargoed? | Medium–High — affects counts and whether a `status` field is needed | Same as #2 |
| 4 | Is the repo the **source of truth** or a downstream published-artifact mirror? | High — determines freshness and whether drafts are present | Ask the Elastic Product Security team |
| 5 | Ship one data stream (GitHub) or two (GitHub + public Discourse)? | Medium, rising to High if #1 reveals a CVE-record schema, since fixed versions would then have no repository source | Decide once #1 is answered and the token situation is known |
| 6 | Can the deployer actually **obtain a token**? It needs org-owner approval with a once-daily notification digest. | High — gates deployment entirely | Start the approval request early; it is the long pole |
| 7 | Does the repo carry an `updated_date`, and how often are advisories amended post-publication? | Medium — affects change tracking; the blob-SHA `_id` is deliberately robust to this being unknown | Same as #1; Discourse's post-revisions API could quantify the public amendment rate |
| 8 | Are the 2026 volumes (116 advisories, a 48-in-one-day batch, ~5.7× the prior rate) the new normal or a backlog flush? | Low — affects nothing in the recommended design, since polling is free | Observe over time |
| 9 | Does `elastic/security-advisories` also publish **GitHub-native repository advisories** (`GET /repos/{owner}/{repo}/security-advisories`, permission `repository_advisories: read`)? | Medium — would be a fully structured alternative to parsing files | Check once repo access exists. The endpoint exists and returns 200 for `elastic/integrations` |
| 10 | GHES support is unverified for any specific version. The existing `github` package README says outright *"This integration is not compatible with GitHub Enterprise server."* | Low — `api_url` is cheap insurance, not a support commitment | Do not claim GHES support without testing |
| 11 | **Governance: should the integration ingest every file it finds?** If most of the >1000 files are unpublished, embargoed, or internal-only advisories, an unfiltered collector will index non-public vulnerability information about Elastic products, and any user of the resulting index inherits that exposure. | **High, and new** — this is a policy question, not a technical one, and it may constrain who the integration is for | Resolve with Elastic Product Security once #1 and #2 are answered. If the JSON carries a status field, filtering on it is the obvious control; if not, `file_pattern` is the only lever and it is a weak one. |
| 12 | Is `file_pattern` glob or RE2 regex? | Low — but a label/behaviour mismatch is another silent zero-document failure | Implementation choice for the CEL author; the description must state which |

---

## 9. Source Attribution

| Source | URL | Access method | Date |
|---|---|---|---|
| GitHub REST API documentation (Trees, Blobs, Contents, Commits, Compare, Search, rate limits, PATs, GitHub Apps, GHES quickstart) | <https://docs.github.com/en/rest> | Web fetch + live API verification | 2026-08-28 |
| GitHub API, live verification | `https://api.github.com` | Authenticated calls with the sandbox token; reproducible via `temp/verify-github-api.sh` and `temp/verify-github-setup.sh` | 2026-08-28 |
| Elastic Product Security | <https://www.elastic.co/product-security> | Web fetch | 2026-08-28 |
| Elastic Security Announcements (Discourse) | <https://discuss.elastic.co/c/announcements/security-announcements/31> | Category JSON, RSS, per-topic JSON, raw Markdown — all 315 topics harvested | 2026-08-28 |
| Elastic advisory generator prompt (the authoritative ESA template) | <https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder/agent-creation-prompt.md> | Web fetch; copy at `references/elastic-advisory-generator-prompt-TEMPLATE.md` | 2026-08-28 |
| Elastic Security Labs, advisory automation | <https://www.elastic.co/security-labs/blog/security-advisory-automation-rag-elastic-agent-builder> | Web fetch | 2026-08-28 |
| CVE Program record API | <https://cveawg.mitre.org/api/cve/> | All 340 Elastic-assigned records downloaded to `temp/cve5/` | 2026-08-28 |
| CVE Program CNA list | <https://raw.githubusercontent.com/CVEProject/cve-website/dev/src/assets/data/CNAsList.json> | Direct fetch | 2026-08-28 |
| NVD API 2.0 | <https://services.nvd.nist.gov/rest/json/cves/2.0?sourceIdentifier=security@elastic.co> | Direct fetch, 340 results | 2026-08-28 |
| OSV API | <https://api.osv.dev/v1/vulns/> | Direct fetch | 2026-08-28 |
| GitHub Advisory Database | <https://api.github.com/advisories> | Direct fetch | 2026-08-28 |
| OASIS CSAF 2.0 / 2.1 specifications | <https://docs.oasis-open.org/csaf/csaf/v2.0/cs03/csaf-v2.0-cs03.html> | Web fetch (to confirm Elastic publishes no CSAF) | 2026-08-28 |
| `elastic/integrations` monorepo | `/workspace/packages/` | Local checkout at `e7090bd7b4` | 2026-08-28 |
| ECS schema | `elastic/ecs` generated field CSVs, v9.3.0 / v9.4.0 / v9.5.0 / main | Downloaded; every ECS field claim verified against them | 2026-08-28 |
| `elastic/mito` (the CEL library) | <https://github.com/elastic/mito> | Shallow clone, inspected for available crypto primitives | 2026-08-28 |
| NVD API rate limits | <https://nvd.nist.gov/developers/start-here> | Web fetch | 2026-08-28 |
| `jmoon-elastic/esa-search` (community, non-official) | <https://github.com/jmoon-elastic/esa-search> | Clone; used only as a cross-check on product naming | 2026-08-28 |
| **Person with `elastic/security-advisories` read access** | — | Reported the filename `ESA-2026-0081.json` and that the directory may hold >1000 files. **The only direct observation of the repository's contents in this brief.** File contents were not supplied. | 2026-08-28 |
| Discourse search API (older ESA years) | `https://discuss.elastic.co/search.json?q=ESA-YYYY` | Live queries confirming ESA IDs exist for 2016, 2018, 2019, 2020, 2022 | 2026-08-28 |
| `elastic/mito` v1.27.0, built and executed | <https://github.com/elastic/mito> | CLI built from source; used to verify that one CEL evaluation can issue many serial HTTP requests | 2026-08-28 |
| OSV schema and registered database prefixes | <https://ossf.github.io/osv-schema/> | Web fetch; used to rule OSV out as the advisory schema | 2026-08-28 |
| ECS generated field CSVs, re-verified | `https://raw.githubusercontent.com/elastic/ecs/{v9.3.0,v9.4.0,v9.5.0,main}/generated/csv/fields.csv` | Independent re-verification of every ECS field claim on the review pass | 2026-08-28 |

---

## Companion artifacts

| Path | Contents |
|---|---|
| `research-brief.md` | This document |
| **`research-review.md`** | **Consolidated review of pass 1: what was verified, what was wrong, what changed, and what to trust. Read this to understand the provenance of any figure in this brief.** |
| `references/advisory-file-format.md` | Everything derivable about the JSON format: what the filename proves, the padded-vs-unpadded ID analysis, candidate schemas evaluated and ruled out, corpus size, and the precise list of what only repo access can answer |
| `references/review-ecs-and-config.md` | Audit of the ECS mapping and configuration plan: errors, overstated claims, guardrail violations, brief-vs-companion inconsistencies |
| `references/review-github-api.md` | Audit of the GitHub API research and `test-api.py`, with a live verification log and the scale re-analysis at 1,000–3,000 files |
| `references/review-landscape-and-precedent.md` | Audit of the publication landscape, precedent survey, deployment guide and sample data, with ~45 quantitative claims re-derived |
| `ecs-mapping-analysis.md` | Full ECS analysis: categorization with the 34-stream precedent survey, ECS field existence verification, the nine-part mapping table, mapping-type reasoning |
| `configuration-plan.md` | Variable plan with per-variable justification, exclusions, and the public-fallback config surface |
| `test-api.py` | Standalone Python script exercising the exact GitHub API flow proposed for the CEL program |
| `references/esa-publication-landscape.md` | How Elastic publishes advisories; the field inventory; machine-readable variants; the private-repo format inference with confidence levels |
| `references/github-api-collection-notes.md` | GitHub API mechanics, incremental strategies, rate limits, authentication, alternatives — with `[VERIFIED-DOC]` / `[VERIFIED-LIVE]` / `[UNVERIFIED]` labels throughout |
| `references/integrations-precedent.md` | Reusable patterns from `/workspace/packages`, with line-referenced excerpts and a priority-ordered reuse table |
| `references/deployment-and-setup.md` | Operator setup: token creation, org policy, approval flow, SAML SSO, the 404 diagnostic ladder, network, volume, backfill |
| `references/elastic-advisory-generator-prompt-TEMPLATE.md` | Verbatim copy of Elastic's own advisory template |
| `references/sample-events/` | Nine real advisories, machine-readable variants, and the hand-written expected ECS document |
| `temp/` | Raw artifacts: 315 forum topics, 57 advisory bodies, 340 CVE records, the NVD response, 177 CVE→ESA mappings, the live-verification scripts, and the review-pass scratch dirs (`format-hunt/`, `api-review/`, `landscape-review/`) |
