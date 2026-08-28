# Configuration plan — `elastic_security_advisories`

Configuration variable plan for the custom (never-to-be-published) Elastic Agent integration that
ingests Elastic Security Advisory files from `advisories/` in the private GitHub repository
`elastic/security-advisories`.

**Collection method:** `cel` input against the GitHub REST API — Git Trees API to enumerate the
directory, Git Blobs API to fetch each file, sub-tree ETag plus a persisted `path → blob SHA` map
for change detection (Strategy A in
[`references/github-api-collection-notes.md`](./references/github-api-collection-notes.md) §2).

**Scope of this document.** Tables and prose only. No manifest YAML, no ingest-pipeline
processors, no CEL program. Operator-facing GitHub setup and deployment notes are in
[`references/deployment-and-setup.md`](./references/deployment-and-setup.md).

**Authority.** The variable set below is derived from the CEL standard-variable table in
`data-collection-methods.md`, adapted to this data source. Every variable outside that table is
called out explicitly with its justification (§4) or its reason for exclusion (§5).

---

## 1. Variables defined by the existing `github` package

Reported exactly as they appear in the manifests, for reuse of naming conventions and to identify
which conventions must *not* be carried over.

### 1.1 `packages/github/data_stream/security_advisories/manifest.yml`

The package's only `cel` data stream, and therefore the closest naming precedent. One stream,
`template_path: cel.yml.hbs`.

| Variable | Type | Title | Default | Required | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `api_url` | text | API URL | `https://api.github.com/advisories` | true | **false** | — |
| `api_key` | password | API key | — | **false** | true | **true** |
| `advisory_type` | select | Advisory type | — (options: `reviewed`, `unreviewed`, `malware`) | true | true | — |
| `interval` | text | Interval | `24h` | true | true | — |
| `batch_size` | integer | Batch Size | `100` | true | false | — |
| `tags` | text (multi) | Tags | `[forwarded, github-security-advisories]` | true | false | — |
| `preserve_original_event` | bool | Preserve original event | `false` | true | true | — |
| `processors` | yaml | Processors | — | false | false | — |
| `enable_request_tracer` | bool | Enable request tracing | `false` | false | false | — |

Notes on this stream:

- `api_key` is `required: false` because the global GitHub Advisory Database is public — its
  description says *"You may leave this field blank for public repositories."* **That inverts for
  us:** the repository is private, so the credential is mandatory.
- `api_url` here is a **full-URL** variable (host + path). The `audit` stream uses the **host-only**
  convention instead. Host-only is the right precedent for us (§4.1).
- ⚠️ **`preserve_original_event` is present here and must not be copied.** Per
  `data-collection-methods.md`, that variable is valid for file and syslog inputs only, **never for
  CEL**. Its presence in this CEL stream is a legacy artifact.

### 1.2 `packages/github/data_stream/audit/manifest.yml`

Five alternative transports for the same data. Only the first is relevant as naming precedent.

**Stream 1 — `httpjson`** (`enabled: false`; `httpjson` is deprecated and must not be used for new
work, but its *variable names* are the package's established vocabulary):

| Variable | Type | Title | Default | Required | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `access_token` | password | Personal Access Token | — | true | true | **true** |
| `organization` | text | Organization Name | — | false | true | — |
| `enterprise` | text | Enterprise Name | — | false | true | — |
| `http_client_timeout` | text | HTTP Client Timeout | `60s` | false | true | — |
| `interval` | text | Interval | `1h` | true | true | — |
| `initial_interval` | text | Initial Interval | `730h` (30 days) | true | true | — |
| `api_url` | text | API URL. | `https://api.github.com` | true | **false** | — |
| `ssl` | yaml | SSL Configuration | — | false | false | — |
| `proxy_url` | **text** | Proxy URL | — | false | false | — |
| `tags` | text (multi) | Tags | `[forwarded, github-audit]` | true | **true** | — |
| `preserve_original_event` | bool | Preserve original event | `false` | true | true | — |
| `processors` | yaml | Processors | — | false | false | — |

Note `interval` is documented as *"The value must be between 2m and 1h"* — the package's own
guidance that 1h is the sensible upper bound for an API poll. Note also `proxy_url` is `text`, not
`url`, throughout the package.

**Streams 2–5 — `azure-eventhub`, `aws-s3`, `azure-blob-storage`, `gcs`.** Transport-specific
credential and object-store variables that have no bearing on a CEL data stream (`eventhub`,
`connection_string`, `storage_account*`, `access_key_id`, `bucket_arn`, `bucket_list_prefix`,
`queue_url`, `file_selectors`, `containers`, `buckets`, `poll`, `poll_interval`,
`number_of_workers`, `timestamp_epoch`, `expand_event_list_from_field`, and so on).

⚠️ **All four of these streams define `preserve_duplicate_custom_fields`**
(`bool`, `required: true`, `show_user: false`, `default: false`) — at
`audit/manifest.yml:252`, `:443`, `:638`, and `:782`. This is a **prohibited** deprecated pipeline
anti-pattern. It must not be carried over. Its presence in the most obvious precedent package is
precisely why it is called out here.

### 1.3 `packages/github/manifest.yml` (package level)

`name: github`, `version: 2.26.0`, `format_version: 3.4.0`,
`categories: [security, productivity_security]`,
`owner: elastic/security-service-integrations`.

One policy template (`github`) with `deployment_modes: default` **and** `agentless` (release beta,
`organization: security`, `division: engineering`, `team: security-service-integrations`) —
relevant to the single-agent question in `deployment-and-setup.md` §2.3.

Variables declared at **policy-template input level** rather than per-stream:

| Input | Variable | Type | Title | Default | Required | Show user |
| --- | --- | --- | --- | --- | --- | --- |
| `httpjson` | `enable_request_tracer` | bool | Enable request tracing | — | false | false |
| `cel` | `proxy_url` | text | Proxy URL | — | false | false |
| `cel` | `ssl` | yaml | SSL Configuration | commented-out `certificate_authorities` example | false | false |

The `cel` input declares **no** other package-level variables. So in the `github` package,
`proxy_url` and `ssl` live at the policy-template level for CEL, and everything else lives on the
data stream. That split is worth mirroring, though it is a manifest-authoring decision rather than
a configuration-plan one.

### 1.4 Conventions worth reusing verbatim

| Convention | Source |
| --- | --- |
| `owner` / `repo` as **separate** text variables, titled "Repository owner" and "Repository" | `code_scanning`, `dependabot`, `issues`, `secret_scanning` manifests |
| `api_url`, host-only, `default: https://api.github.com`, `show_user: false` | `audit/manifest.yml:56-63` |
| Credential as `type: password` + `secret: true` + `show_user: true` | `security_advisories/manifest.yml:17-24` |
| `interval` as `type: text`, `show_user: true`, description naming the h/m/s units | both |
| `tags` as `type: text`, `multi: true`, `required: true`, defaulting to `[forwarded, <name>]` | both |
| `processors` as `type: yaml`, `required: false`, `show_user: false` | both |
| `enable_request_tracer` block, `default: false`, `show_user: false`, with the security warning in the description | `security_advisories/manifest.yml:80-88` |
| `http_client_timeout` as `type: text`, `default: 60s` | `audit/manifest.yml:32-39` |

---

## 2. Required configuration variables

| Variable | Type | Title | Description | Default | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `api_url` | text | API URL | The GitHub REST API base URL, without a path. Use `https://api.github.com` for GitHub.com. For GitHub Enterprise Server use `https://HOSTNAME/api/v3`. For GitHub Enterprise Cloud with data residency use `https://api.SUBDOMAIN.ghe.com`. | `https://api.github.com` | **false** | — |
| `api_key` | password | GitHub Personal Access Token | The GitHub Personal Access Token used to authenticate with the GitHub REST API. A fine-grained token is strongly recommended: set the resource owner to the organization that owns the repository, grant access to only that repository, and grant `Contents: Read-only`. Required — the repository is private. See the integration documentation for the full setup and approval procedure. | — | true | **true** |
| `owner` | text | Repository owner | The owner of the GitHub repository. If the repository belongs to an organization, this is the name of the organization. | `elastic` | true | — |
| `repo` | text | Repository | The GitHub repository that contains the advisory files. | `security-advisories` | true | — |
| `path` | text | Directory path | Path to the directory inside the repository that holds the advisory files, relative to the repository root, with no leading or trailing slash. Every file beneath this directory is collected recursively. | `advisories` | true | — |
| `branch` | text | Branch | The branch to read advisories from. A tag name or a commit SHA is also accepted. This must match a ref that exists in the repository — an incorrect value returns HTTP 404, which is indistinguishable from a permissions failure. | `main` | true | — |
| `interval` | text | Interval | Duration between requests to the GitHub API. Supported units for this parameter are h/m/s. Unchanged polls are answered with HTTP 304 and consume no GitHub API rate-limit budget. | `1h` | true | — |

**Secret variables: `api_key` only.**

Type notes, where the recommendation departs from the standard table:

- **`api_url`** corresponds to the standard table's `url` row (type `url`, show user yes). The
  recommendation is `type: text` and `show_user: false`, matching all six existing `github` data
  streams. `text` is right because the value is a *base* with no path and Fleet's `url` validation
  offers nothing useful here; `show_user: false` is right because only GHES and data-residency
  users ever change it, and surfacing it invites people to paste a full endpoint URL into it.
- **`api_key`** corresponds to the standard table's `api_key` / `token` row. Name and type match the
  existing CEL stream exactly. Title changed from the precedent's "API key" to "GitHub Personal
  Access Token" because that is literally what the operator pastes, and mislabeling it as an
  "API key" sends people looking for a non-existent GitHub API-key feature. `required` flips from
  the precedent's `false` to **`true`**.
- **`interval`** matches the standard table exactly (`text`, required, show user).

---

## 3. Optional configuration variables

| Variable | Type | Title | Description | Default | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `file_pattern` | text (multi) | File name patterns | Glob patterns matched against each file's path relative to the configured directory. Only matching files are collected. Leave empty to collect every file in the directory. Use this to exclude non-advisory content such as `README.md`, templates, or schema files. | — (empty: collect everything) | true | — |
| `http_client_timeout` | text | HTTP Client Timeout | Duration before declaring that the HTTP client connection has timed out. Valid time units are ns, us, ms, s, m, h. | `60s` | false | — |
| `proxy_url` | text | Proxy URL | URL to proxy connections in the form of `http[s]://<user>:<password>@<server name/ip>:<port>`. Please ensure your username and password are in URL encoded format. | — | false | — |
| `ssl` | yaml | SSL Configuration | SSL configuration options. Required only for GitHub Enterprise Server instances using a private certificate authority, or when a TLS-intercepting proxy is in the path. See the Filebeat SSL documentation for details. | — | false | — |
| `tags` | text (multi) | Tags | Tags to include in the published event. | `[forwarded, elastic-security-advisories]` | false | — |
| `processors` | yaml | Processors | Processors are used to reduce the number of fields in the exported event or to enhance the event with metadata. This executes in the agent before the logs are parsed. | — | false | — |

**No optional variable is secret.**

Type notes:

- **`proxy_url`** — the standard table specifies type `url`. The recommendation is `type: text`,
  matching every instance in the `github` package and the overwhelming majority of the monorepo.
  Rationale: proxy URLs routinely carry embedded credentials (`http://user:pass@host:3128`), and
  `text` avoids any URL-format validation surprises on that form. Either choice is defensible;
  consistency with precedent wins.
- **`tags`** — the standard table marks this `show user: yes`. The recommendation is
  `show_user: false`, matching the `github` package's CEL stream (its `httpjson` stream uses
  `true`). For a single-purpose internal integration the default tag set is not something operators
  need to see in the primary form. Note the package-spec idiom used by both precedents:
  `required: true` **with** a default, which means "always emitted, never has to be typed" rather
  than "the user must supply it". Either `required` value works.
- **`ssl`** and **`processors`** match the standard table exactly.
- **`http_client_timeout`** maps to the CEL input's `resource.timeout`; the standard table calls
  the row `http_client_timeout`, which is also the name used by 290 data streams in the monorepo,
  including `github/audit`.

---

## 4. Product-specific variables — justification

Each variable below is outside the generic CEL standard set, or is a standard row that needs a
data-source-specific decision. Each is tied to a documented requirement of *this* data source, not
to a pipeline behaviour toggle.

### 4.1 `api_url` — the GitHub API base URL

**Requirement.** GitHub's REST API is not served from a single host. Verified from GitHub's own
documentation:

| Deployment | Base URL |
| --- | --- |
| GitHub.com / GitHub Enterprise Cloud | `https://api.github.com` |
| **GitHub Enterprise Server** | **`http(s)://HOSTNAME/api/v3`** |
| GHEC with data residency | `https://api.SUBDOMAIN.ghe.com` |

The GHES form is documented at
<https://docs.github.com/en/enterprise-server@3.14/rest/quickstart>, which shows
`curl --url "http(s)://HOSTNAME/api/v3/repos/REPO-OWNER/REPO-NAME/issues"` and
`new Octokit({ baseUrl: "http(s)://HOSTNAME/api/v3" })`. Hard-coding `https://api.github.com` would
make GHES support impossible without a package rebuild.

**Host-only, not full-URL.** The `github` package uses both conventions. Host-only is required
here, because the CEL program builds **two different paths** from the same base:

```
{api_url}/repos/{owner}/{repo}/git/trees/{branch}:{path}?recursive=1
{api_url}/repos/{owner}/{repo}/git/blobs/{sha}
```

A full-URL variable cannot express that. A GHES operator changes exactly one field.

**Caveat.** Making the variable configurable is cheap insurance, not a support commitment. The
existing `github` package README states outright *"This integration is not compatible with GitHub
Enterprise server."* GHES fine-grained-PAT availability and rate-limit configuration vary by
release. Do not claim GHES support without testing. `[UNVERIFIED]` for any specific GHES version.

### 4.2 `owner` + `repo` as two variables, not one `owner/repo` string

**Recommendation: two separate variables.** Assessment:

| | Two variables (`owner`, `repo`) | One variable (`repository` = `owner/repo`) |
| --- | --- | --- |
| Matches the REST API shape | Yes — GitHub documents `owner` and `repo` as **separate path parameters** of `GET /repos/{owner}/{repo}/git/trees/{tree_sha}` | No — must be split by the client |
| Precedent in the monorepo | **Four `github` data streams** (`code_scanning`, `dependabot`, `issues`, `secret_scanning`) use separate `owner` / `repo` text vars, titled "Repository owner" and "Repository", and compose them as `{{api_url}}/repos/{{owner}}/{{repo}}/…` | No precedent found |
| Malformed-input surface | Small — two plain identifiers | Large — must tolerate `https://github.com/elastic/security-advisories`, a `.git` suffix, a trailing slash, a leading `@`, and a missing `/` |
| Failure mode of bad input | 404, but the operator sees two separately-labelled fields to check | 404, and the operator must reason about string splitting |
| Fleet validation | Two independently required fields | One field, all-or-nothing |
| Operator familiarity | Identical field names and titles to the `github` package they may already run | Novel |

The malformed-input point is not hypothetical. Because **every** failure on this data source is a
404 (see `deployment-and-setup.md` §1.8), anything that widens the space of silent input errors is
disproportionately costly. Two fields is the lower-entropy choice.

**Defaults.** Unlike the generic `github` package, this integration exists to read exactly one
repository, so both fields get defaults: `owner: elastic`, `repo: security-advisories`. That makes
the happy path zero-typing while keeping the integration usable against a fork or a mirror.

**`repo` must be `required: true`** here, whereas the `github` package marks it `required: false`.
In the `github` package an empty `repo` switches the template to an org-wide endpoint
(`/orgs/{owner}/code-scanning/alerts`). The Git Trees API has no org-wide form, so an empty `repo`
would simply produce a malformed URL.

### 4.3 `path` — the directory to scan

**Requirement.** The `{ref}:{path}` tree-ish form is the mechanism that scopes enumeration to one
subdirectory in a single request (`github-api-collection-notes.md` §1.3). The `path` component is
not optional in that construction — something has to be supplied.

**Why it must be user-configurable rather than a template constant.** The repository is
inaccessible and **its directory layout is unverified**. `esa-publication-landscape.md` §5.3 rates
"flat `advisories/ESA-2026-24.md`" versus "year-nested `advisories/2026/…`" as *"low confidence
either way"*, and observes that with 116 advisories in 2026 alone, year-nesting would be the sane
engineering choice. Recursive enumeration handles year-nesting transparently, so a flat-vs-nested
surprise is fine — but a *renamed* or *relocated* directory is not, and neither is a repository
whose advisories live under, say, `data/advisories/`. A configurable path turns "rebuild and
redeploy the package" into "edit one field in Fleet".

It also gives the operator a way to narrow the scope deliberately — pointing at `advisories/2026`
to limit an initial rollout, for example.

**Format.** No leading or trailing slash. This must be stated in the description, because the
tree-ish syntax is `{branch}:{path}` and a leading slash produces a 404.

### 4.4 `branch` — the git ref

**Requirement.** The Trees API's `tree_sha` path parameter is documented as *"The SHA1 value or ref
(branch or tag) name of the tree"*. When addressing a tree by ref there is **no server-side
default** — a ref must be named. (This differs from the Contents API, whose optional `ref` query
parameter defaults to the repository's default branch.)

**Why a default of `main` is not enough on its own.** `main` is the modern GitHub default but not
universal; `master` and publication-specific branches both occur. The failure mode of guessing
wrong is — again — a bare 404 identical to a permissions failure. The mitigation is twofold: expose
the variable, and tell the operator in the setup guide to read `default_branch` from
`GET /repos/{owner}/{repo}` during the diagnostic probe, which returns it
([verified live](./references/deployment-and-setup.md#18-verifying-the-404-not-403-failure-mode-and-how-to-self-diagnose-it)).

**Naming.** `branch` over `ref`: `ref` matches the Contents API query-parameter name and is
technically more accurate (tags and SHAs are accepted), but `branch` is what an operator is
actually looking for in a Fleet form. The description carries the nuance. There is no precedent in
the monorepo for either name — a repo-scan search for `branch`, `ref`, `git_ref`, `directory`, and
similar variable names across all `manifest.yml` files returns nothing relevant.

### 4.5 `file_pattern` — filename filter

**Recommendation: include it, optional, with an empty default.**

**Justification.** The Trees API returns **every** blob beneath the directory. The repository's
actual contents are unverified, and a directory called `advisories/` in a working repository very
plausibly also contains a `README.md`, a `CODEOWNERS`, a `.gitkeep`, a JSON schema, a template
file, or an image directory. Every one of those would be fetched (one wasted request each) and
indexed as a bogus advisory document. There is no other lever an operator has to fix that without a
package rebuild.

This is a **collection-scope filter**, directly analogous to `bucket_list_prefix` and
`file_selectors` — both of which appear in the standard-variable tables for the object-store
inputs — rather than a pipeline behaviour toggle.

**Why the default should stay empty. (Reasoning rebuilt 2026-08-28 — the original premise is dead.)**
This previously argued that guessing an extension was dangerous *because the format was unknown*: a
default of `*.md` against a `.yaml` corpus would produce zero documents and no error. The format is
now known — the files are JSON (`ESA-2026-0081.json`) — so `*.json` is a defensible default and that
argument no longer applies.

The residual case for an empty default is narrower but still real: filename **casing** is unverified,
and whether non-advisory JSON (a schema, a template, a manifest, a README) sits alongside the
advisories is unknown. Given that the >1000 reported files exceed the ~386 publicly-known ESA IDs by
roughly 600, the directory plausibly contains more than just advisories. An empty default collects
everything, which is noisy but **visible**, and the operator can narrow it having seen what is
actually there — whereas a wrong pattern fails silently. That asymmetry is the whole argument.

**Caveat.** Whether the filter is implemented as glob matching or RE2 regex is an implementation
choice for the CEL-program author; the description must state which. Glob is recommended as the
more approachable of the two for a user-facing field.

### 4.6 `interval` — recommended value and justification

**Recommendation: `1h`.**

This is argued from the observed publication cadence, not from habit. The default `5m` used across
many integrations is wrong here, and so is the `24h` used by the `github` package's own
`security_advisories` stream.

**Step 1 — how often does the data actually change?**

From `esa-publication-landscape.md` §1.3: across 203 ESA-tagged topics there are only **52 distinct
publication dates**. Advisories are published in batches tied to product release trains, not
continuously. The nine most recent batches:

| Date | Advisories | Days since previous batch |
| --- | --- | --- |
| 2025-12-18 | 11 | — |
| 2026-01-13 | 7 | 26 |
| 2026-02-26 | 7 | 44 |
| 2026-03-19 | 6 | 21 |
| 2026-04-08 | 6 | 20 |
| 2026-05-28 | 10 | 50 |
| 2026-07-01 | 11 | 34 |
| 2026-07-21 | 19 | 20 |
| 2026-08-13 | **48** | 23 |

Mean gap **≈ 30 days**, median **≈ 24.5 days** (sorted gaps: 20, 20, 21, 23, 26, 34, 44, 50).
Elastic explains the timing itself: *"We draft the
security advisory during the disclosure phase, ahead of a planned product release that contains the
fix."* So the source data changes roughly **12–15 times a year**.

(The repository is the *authoring* store, so it will also churn during drafting, before
publication. That raises the change frequency somewhat but not its order of magnitude, and it makes
low-latency polling *less* valuable, not more — early churn is draft noise.)

**Step 2 — what does polling frequency cost?** Essentially nothing. With the sub-tree ETag
strategy, an unchanged poll returns HTTP 304, and a 304 on an authorized request **consumes zero
rate-limit budget** (verified live, `github-api-collection-notes.md` §3.1). So the usual
cost-versus-freshness trade-off that sets polling intervals **does not apply**. `5m` and `24h` cost
the same: zero.

**Step 3 — so the interval must be argued on other grounds.**

| Interval | Polls/year | Change events observed/year | Poll "hit rate" | Worst-case detection latency |
| --- | --- | --- | --- | --- |
| `5m` | 105,120 | ~12 | 0.011 % | 5 min |
| `15m` | 35,040 | ~12 | 0.034 % | 15 min |
| **`1h`** | **8,760** | **~12** | **0.14 %** | **1 hour** |
| `6h` | 1,460 | ~12 | 0.82 % | 6 hours |
| `24h` | 365 | ~12 | 3.3 % | 24 hours |

**Why not `5m`:** it buys a 55-minute latency improvement on an event that occurs about once a
month, at 12× the poll volume, and it has three concrete downsides. (a) An initial backfill of
**1,000–3,000 files takes 3.5–10.5 minutes** of serial requests — *revised upward 2026-08-28 from
"200–500 files, 1.5–3.5 minutes"*, which now puts the backfill **well past** a 5-minute interval
rather than uncomfortably close to it, so a slow network or a mid-backfill restart would produce
overlapping or repeatedly-abandoned work. This strengthens the recommendation. (b) It multiplies the
damage of an accidental multi-agent deployment (`deployment-and-setup.md` §2.3) by 12×. (c) It
produces 288 "no change" poll cycles per day per agent in the logs, which trains operators to
ignore the log. None of that is catastrophic; it is simply unpaid-for.

**Why not `24h`** (the `github` package's default for its own advisories stream): a 24-hour
worst-case detection latency on a feed whose entire purpose is alerting on Elastic product
vulnerabilities is poor, and a single failed poll silently doubles it to 48 hours. Since the poll is
free, there is nothing to buy with that latency.

**Why `1h`:**

- Same-hour detection is meaningful for a security advisory feed; sub-hour is not, because ESAs are
  published in coordination with an already-shipped fix after coordinated disclosure. The
  operationally relevant granularity is "same business hour", not "same minute".
- A single missed poll costs 2 hours, not 2 days.
- It comfortably exceeds the worst-case backfill duration, so polls never overlap.
- It matches the `github` package's `audit` stream default of `1h`, and that stream's description
  states the valid range is *"between 2m and 1h"* — i.e. the package's own view of the sensible
  ceiling for an API poll.
- Rate-limit consumption remains **zero** in steady state.

**Defensible range:** `15m` to `6h`. Do not go below `5m`. `24h` is acceptable only if the operator
explicitly wants a once-daily digest and accepts the latency.

---

## 5. Variables deliberately excluded

Every standard-table row not adopted above, and every legacy pattern visible in the precedent
packages, with the reason.

### 5.1 Standard CEL rows that do not apply to this data source

| Standard variable | Excluded because |
| --- | --- |
| `initial_interval` | **There is no time window to look back over.** The Trees API returns the *current state* of a directory, not a time-ordered event feed. The first poll captures the entire corpus by construction; there is nothing an "initial lookback" could mean. Including it would imply a history-replay capability that does not exist. (Contrast `github/audit`, which sets `initial_interval: 730h` because the audit-log endpoint genuinely is a time-windowed feed.) |
| `batch_size` / `page_size` | **Neither endpoint paginates.** The Trees API returns the whole sub-tree in one response with an explicit `truncated` flag and no `Link` header; the Blobs API returns exactly one blob. Verified live in `github-api-collection-notes.md` §1.3–1.4. A page-size knob would be inert. (A "blobs fetched per CEL execution" tuning constant is a plausible template-level value, but it is an implementation detail, not a documented vendor-side requirement, so it does not belong in the manifest.) |
| OAuth2 block — `client_id`, `client_secret`, `token_url`, `authorization_url`, `scopes` | The GitHub API here is authenticated with a static bearer token. The one OAuth-adjacent alternative, a GitHub App installation token, is **technically impossible in CEL** — it requires signing an RS256 JWT and mito's crypto library exposes only HMAC, no RSA and no JWT builder (`github-api-collection-notes.md` §4.3). An OAuth app requires an interactive browser flow with no non-interactive path. |

### 5.2 Prohibited — must not appear under any circumstances

| Variable / pattern | Status |
| --- | --- |
| `preserve_duplicate_custom_fields` | **PROHIBITED.** A deprecated pipeline anti-pattern. Present in four `github/audit` streams (`:252`, `:443`, `:638`, `:782`) — do not copy it from there. |
| Any `event.ingested` toggle | **PROHIBITED.** |
| Any trailing `event.original` removal flag | **PROHIBITED.** |
| `preserve_original_event` | **Excluded because it is an `event.original`-removal toggle**, which the research guardrails prohibit proposing as a configuration variable. **Corrected 2026-08-28:** this row previously claimed the variable is "not valid for CEL" and "a legitimate variable *only* for file (filestream) and syslog (tcp/udp) inputs", and dismissed its appearance at `github/data_stream/security_advisories/manifest.yml:64-71` as a legacy artifact. That was **wrong** — it is declared by **327 of 361 CEL data streams across 113 packages**, and it is functional in CEL: `github/data_stream/security_advisories/agent/stream/cel.yml.hbs:83-84` emits it into `tags`, which the ingest pipeline reads at `default.yml:320` and `:340`. It is the most common CEL variable after `tags`, `processors` and `interval`. The exclusion still stands, but only on the guardrail ground stated above. **One consequence to make deliberate:** with no toggle, `event.original` is retained unconditionally. For a few thousand small JSON documents that is cheap and useful for reprocessing, but it should be a stated decision rather than a side effect of this exclusion. |

### 5.3 Outside the standard table — one convention variable, flagged

`enable_request_tracer` is **not** in the CEL standard-variable table, but it appears in **370**
data streams across the monorepo, including the `github` CEL stream, and is copied near-verbatim
everywhere.

| Variable | Type | Title | Description | Default | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `enable_request_tracer` | bool | Enable request tracing | The request tracer logs requests and responses to the agent's local file-system for debugging configurations. Enabling this request tracing compromises security and should only be used for debugging. | `false` | false | — |

**Recommendation: include it**, and the argument is unusually strong for this specific integration.
Every misconfiguration of this data source produces an identical, information-free HTTP 404
(`deployment-and-setup.md` §1.8). The request tracer is the only in-product way for an operator to
see the exact URL that was requested and the exact response received, which converts an
undiagnosable "no data" into a five-second diagnosis.

**One condition on including it, and a correction. (Revised 2026-08-28.)** This previously called the
variable "a deliberate departure from the authoritative standard table" needing special review. That
framing was wrong and inverted the burden of proof: `enable_request_tracer` is declared by **297 of
361 CEL data streams across 102 packages** (370 data streams overall), and the `github` CEL stream's
own description links the *CEL input's* tracer documentation. It is a first-class CEL variable and
should simply be included on the operational argument above.

The real condition is the security one: the tracer writes full request and response bodies to disk,
so it needs to be accompanied by redaction covering `api_key` (`integrations-precedent.md` §9). How
that is wired is the CEL author's call, not a configuration-plan decision. Agentless deployments cannot easily retrieve the trace files, so
the variable is of limited use there.

---

## 6. Summary

**Required (7):** `api_url`, `api_key`, `owner`, `repo`, `path`, `branch`, `interval`
**Optional (6):** `file_pattern`, `http_client_timeout`, `proxy_url`, `ssl`, `tags`, `processors`
**Convention, flagged (1):** `enable_request_tracer`

**Secret (`secret: true`): `api_key`, and nothing else.**

Residual risk: `proxy_url` may embed credentials but is not marked secret anywhere in the monorepo,
including the `github` package. If the deployment uses an authenticating proxy, those credentials
sit in the Fleet policy in the clear. Prefer source-IP-authenticated egress. Note this in the
integration README rather than deviating from the convention.

---

## 7. Credential-free fallback: the public data source

The private repository may be unreachable by whoever deploys this — the token requires organization
approval, SAML SSO authorization, and repository read access that a given deployer may simply not
have (`deployment-and-setup.md` §1). The public fallback reproduces essentially the same corpus with
**no credential at all**. The detailed data analysis is in `esa-publication-landscape.md` §2, §4 and
§5.3; this section covers only the configuration surface and the trade-offs.

### 7.1 Data sources

| Source | Endpoint | Auth | Provides |
| --- | --- | --- | --- |
| Discourse category JSON | `https://discuss.elastic.co/c/announcements/security-announcements/31.json?page=N` | none | Topic envelope: title, slug, id, `created_at`. 30 topics/page; `topic_list.more_topics_url` signals more. |
| Discourse topic JSON | `https://discuss.elastic.co/t/<id>.json` | none | Post `cooked` HTML, `created_at`, `updated_at`, `version`. |
| Discourse raw Markdown | `https://discuss.elastic.co/raw/<id>` | none | Cleanest advisory body text. |
| CVE Record 5.x | `https://cveawg.mitre.org/api/cve/<CVE-ID>` | none | The structured twin: title, description, structured version ranges, CVSS vector, CWE, CAPEC. |
| NVD API 2.0 | `https://services.nvd.nist.gov/rest/json/cves/2.0` | optional key | 340 Elastic-assigned CVEs; CPE data. |
| OSV | `https://api.osv.dev/v1/vulns/<CVE-ID>` | none | Resolved version ranges, git commit ranges, CPEs. |

The ESA↔CVE join is via the Discourse slug embedded in the CVE record's reference URL — the CVE
record itself has no ESA ID field (`esa-publication-landscape.md` §4.2).

### 7.2 Configuration surface

**Required**

| Variable | Type | Title | Description | Default | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `url` | url | Discourse URL | Base URL of the Discourse instance publishing Elastic Security Announcements. | `https://discuss.elastic.co` | false | — |
| `category_id` | integer | Category ID | The Discourse category ID for Security Announcements. Stable since 2015-06-06; posting is restricted to Elastic staff. | `31` | false | — |
| `interval` | text | Interval | Duration between requests. Supported units are h/m/s. | `1h` | true | — |

**Optional**

| Variable | Type | Title | Description | Default | Show user | Secret |
| --- | --- | --- | --- | --- | --- | --- |
| `enrich_from_cve` | bool | Enrich from CVE Record 5.x | Fetch the CVE Program record for each advisory's CVE ID to obtain structured version ranges, CVSS metrics, CWE and CAPEC identifiers. Requires outbound access to `cveawg.mitre.org`. | `true` | true | — |
| `cve_api_url` | url | CVE Record API URL | Base URL of the CVE Program's record API. | `https://cveawg.mitre.org/api/cve` | false | — |
| `enrich_from_osv` | bool | Enrich from OSV | Fetch OSV records for resolved version ranges and CPEs. Requires outbound access to `api.osv.dev`. | `false` | true | — |
| `osv_api_url` | url | OSV API URL | Base URL of the OSV vulnerability API. | `https://api.osv.dev/v1/vulns` | false | — |
| `nvd_api_url` | url | NVD API URL | Base URL of the NVD CVE API 2.0. | `https://services.nvd.nist.gov/rest/json/cves/2.0` | false | — |
| `nvd_api_key` | password | NVD API Key | Optional NVD API key. Without one, NVD permits 5 requests per rolling 30-second window; with one, 50. Request a key at `https://nvd.nist.gov/developers/request-an-api-key`. | — | true | **true** |
| `max_pages` | integer | Maximum pages per poll | Safety bound on how many Discourse category pages to walk in a single poll. Set to 0 for unbounded. | `20` | false | — |
| `http_client_timeout`, `proxy_url`, `ssl`, `tags`, `processors` | — | — | As in §3. | — | — | — |

**Secret: `nvd_api_key` only** — and it is genuinely optional. **The primary path needs no
credential whatsoever**, which is the entire point of this fallback.

`nvd_api_key` is justified by a documented vendor-side rate limit, not by convenience:
*"The public rate limit (without an API key) is 5 requests in a rolling 30 second window; the rate
limit with an API key is 50 requests in a rolling 30 second window"*
(<https://nvd.nist.gov/developers/start-here>). At 5 req/30 s, enriching 340 CVEs on a backfill
takes ~34 minutes of forced sleeping; with a key, ~3.5 minutes. NVD additionally advises
*"automated requests should include a range where `lastModStartDate` equals the time of the last
CVE or CPE received"* and that this be done *"no more than once every two hours"* — which is a hard
constraint on any NVD-derived interval, and a reason to prefer CVE Record 5.x over NVD as the
enrichment source.

`max_pages` is a judgement call flagged as such: it is not in the standard table, and is not
strictly necessary because the documented termination condition (`more_topics_url` absent) is
reliable. It is proposed as an unbounded-walk safety bound only. Discourse's page size is fixed
server-side (30 for JSON, 25 for RSS), so a `page_size` variable would be inert and is excluded.

### 7.3 Trade-offs versus the private repository

**In favour of the fallback**

- **Zero credentials on the primary path.** No fine-grained PAT, no organization approval, no daily
  approval-digest wait, no SAML SSO authorization, no leaver risk when the token owner departs, no
  366-day rotation treadmill, no 50-token-per-user ceiling. This removes essentially every item in
  `deployment-and-setup.md` §1.
- **No 404 ambiguity.** These are public endpoints; an error is an error. The single worst property
  of the GitHub path — that every misconfiguration is an indistinguishable 404 — simply does not
  exist here.
- **Deployable by anyone**, including someone with no Elastic GitHub access at all.
- **Genuinely structured enrichment.** CVE Record 5.x gives decomposed CVSS metrics, `lessThan` /
  `lessThanOrEqual` version ranges with `versionType`, CWE and CAPEC IDs — arguably *better*
  structured than whatever the repository holds, and it maps near field-for-field onto the ESA
  (`esa-publication-landscape.md` §4.2).

**Against**

- **No conditional-request support on the primary source.** [VERIFIED-LIVE] `discuss.elastic.co`
  returns `cache-control: no-cache, no-store` and **no `ETag` and no `Last-Modified`** on both the
  category JSON and the RSS feed. The entire zero-cost-polling property of the GitHub design
  evaporates: every poll transfers the full page payload. (`cveawg.mitre.org` does return a weak
  ETag; `api.osv.dev` returns none.) Change detection must fall back to comparing topic
  `updated_at` / `version` against a persisted cursor.
- **Pagination hazard on batch days.** The RSS feed serves **25 items per page** and the JSON 30,
  while the largest observed batch was **48 advisories in one day**. A collector that reads only the
  first page will silently miss advisories on exactly the days that matter most. Page walking is
  mandatory, not optional — an Elastic Consulting Architect publicly described hitting precisely
  this (`esa-publication-landscape.md` §2.2).
- **HTML/Markdown parsing instead of a structured file.** The advisory body arrives as rendered
  HTML (`cooked`) or forum Markdown (`/raw/<id>`) and must be section-parsed. Elastic's advisory
  template is stable and slot-structured (`esa-publication-landscape.md` §3.1–3.2), so this is
  tractable — but it is scraping, and a forum-theme change can break it.
- **No ESA ID field anywhere.** It must be extracted from the Discourse topic slug by regex. CVE
  records do not carry it; OSV does not know ESA IDs exist. Only **177 of 340** CVE→ESA pairs could
  be resolved this way, because older slugs predate the ESA-in-slug convention.
- **Discourse is not a contractual API.** It has no versioning commitment to Elastic's consumers and
  no deprecation policy. GitHub's REST API has both (`X-GitHub-Api-Version`, currently `2026-03-10`
  with `2022-11-28` still supported [VERIFIED-LIVE]).
- **Two to four egress hosts instead of one** (`discuss.elastic.co`, plus `cveawg.mitre.org`,
  `api.osv.dev`, `services.nvd.nist.gov`), each needing its own allow-list entry, its own timeout
  and retry behaviour, and its own failure mode. NVD in particular is slow and periodically
  unavailable.
- **Published advisories only.** The repository would presumably also hold drafts and reserved-but-
  unpublished ESA IDs; the forum by definition holds only what has shipped. For most use cases that
  is a feature, not a defect.

**Verdict.** The public fallback is a legitimate primary design, not a degraded one — this is
`esa-publication-landscape.md` §5.3's own conclusion: *"the defensible design is to treat the public
Discourse surface as the primary data source and the CVE Record 5.x / NVD / OSV data as the
structured enrichment source."* The GitHub path wins on data fidelity (the authoring source of
truth, with reserved IDs and pre-publication state), on protocol quality (documented, versioned,
ETag-backed, zero-cost polling), and on parse robustness. The public path wins decisively on
deployability. If the private repository is not reachable within the project's timeframe, build the
public collector; the two produce documents that should map onto the same field set, since both are
renderings of the same underlying advisory.

---

## 8. Gaps and open questions

1. **The repository's actual contents are unverified.** File format, naming convention, directory
   nesting, and file count are all unknown (`esa-publication-landscape.md` §5, and
   `github-api-collection-notes.md` gap 4). This is why `path`, `branch`, and `file_pattern` are
   variables rather than constants — they are the levers that let an operator recover from a wrong
   assumption without a package rebuild.
2. **`file_pattern` semantics — glob or RE2 regex?** Left to the CEL-program author. The
   description must say which; a mismatch between the label and the behaviour is another silent
   zero-document failure.
3. **Whether `api_url` should live on the data stream or on the policy-template input.** The
   `github` package puts `proxy_url` and `ssl` at the policy-template level for its CEL input and
   everything else on the stream. With a single data stream the distinction is cosmetic; it becomes
   real if a second stream (e.g. the public Discourse fallback) is added to the same package.
4. **Whether to ship both collection paths as two data streams in one package.** §7 argues the
   public path is independently viable. Two streams in one package would let an operator run the
   GitHub path where credentials exist and the public path elsewhere — at the cost of a second
   variable set and a documented "do not enable both against the same index" caveat. Not decided
   here.
5. ~~**`enable_request_tracer` inclusion** is a deliberate departure from the authoritative standard
   variable table (§5.3).~~ **Resolved 2026-08-28:** not a departure. 297 of 361 CEL streams declare
   it. Include it; no special review needed. See §5.3.
6. **The `interval` recommendation assumes the repository's change rate tracks the publication
   cadence.** If the repository sees heavy pre-publication drafting churn, the observed change rate
   will be higher than the 12–15/year publication rate — which argues for the *same* `1h` interval
   or longer, never shorter, since draft churn is not information worth low-latency delivery. If
   the repository turns out to receive only a single squashed commit per release train, `6h` would
   be equally defensible.
