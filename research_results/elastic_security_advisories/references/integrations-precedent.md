# Precedent in `elastic/integrations` for a GitHub file-collection CEL integration

Survey of the `elastic/integrations` monorepo (local checkout at `/workspace`, packages under
`/workspace/packages/<name>/`) for reusable patterns.

All file paths below are relative to `/workspace`. Line numbers were current at the time of
research (repo HEAD `e7090bd7b4b90774406bcd9e098b3eaf704ef727`).

---

## 0. Headline findings

1. **No package in the monorepo reads files from a git repository.** This integration has no
   direct structural precedent. The closest analogue is `ti_recordedfuture`, which fetches a
   single whole-file dump over HTTP and uses an ETag to skip unchanged downloads.
2. **The `github` package has exactly one `cel` data stream — `security_advisories` — and it
   targets the *global* GitHub Advisory Database, not repository files.** This is the answer to
   "why not just use the github package?" (§5).
3. Every reusable ingredient does exist somewhere, just not assembled together:
   Link-header pagination (§2), an ETag-skip cursor (§3), a persisted worklist for
   list-then-fetch-each traversal (§4), and `x-ratelimit-*` handling via the CEL `rate_limit()`
   function (§6).
4. **`httpjson` still dominates the `github` package** — 5 of its 6 data streams use it. Only
   `security_advisories`, the newest, uses `cel`. Since `httpjson` is deprecated and must not be
   recommended, the `security_advisories` stream is the only `github`-package template worth
   copying idioms from.

Search evidence for finding #1:

```
$ rg -l "raw.githubusercontent|git/trees|/contents/|api.github.com" packages
# → only packages/github/** (its own API URLs and test fixtures), plus unrelated
#   matches in santa, crowdstrike, arista_ngfw, nginx_ingress_controller,
#   security_detection_engine, o365, m365_defender, akamai, ti_opencti, osquery_manager.
#   None reads repository file contents.

$ rg -l "git clone|git_url|\.git\b" packages --glob "*.hbs" --glob "*manifest.yml"
packages/fim/manifest.yml      # file integrity monitoring, unrelated
```

---

## 1. The `github` package at a glance

`packages/github/manifest.yml` — name `github`, version `2.26.0`, owner
`elastic/security-service-integrations`, categories `[security, productivity_security]`.

### 1.1 Data streams and their inputs

| Data stream | Input(s) | Notes |
| --- | --- | --- |
| `audit` | `abs`, `aws-s3`, `azure-eventhub`, `gcs`, `httpjson` | 5 alternative transports for the same data |
| `code_scanning` | `httpjson` | deprecated input |
| `dependabot` | `httpjson` | deprecated input |
| `issues` | `httpjson` | deprecated input |
| `secret_scanning` | `httpjson` | deprecated input |
| **`security_advisories`** | **`cel`** | **the only CEL stream; the one to learn from** |

### 1.2 Policy-template input declarations

`packages/github/manifest.yml:86-125` declares the `cel` input at policy-template level and
attaches `proxy_url` and `ssl` vars there rather than per-stream:

```86:103:packages/github/manifest.yml
      - type: cel
        title: Collect GitHub Security Advisories data via API
        description: Collect GitHub Security Advisories data via API.
        vars:
          - name: proxy_url
            type: text
            title: Proxy URL
            multi: false
            required: false
            show_user: false
            description: URL to proxy connections in the form of http[s]://<user>:<password>@<server name/ip>:<port>. Please ensure your username and password are in URL encoded format.
          - name: ssl
            type: yaml
            title: SSL Configuration
            description: SSL configuration options. See [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-ssl.html#ssl-common-config) for details.
            multi: false
            required: false
            show_user: false
```

Agentless deployment is enabled for this package
(`packages/github/manifest.yml:53-61`, `organization: security`, `division: engineering`,
`team: security-service-integrations`).

---

## 2. Base URL configuration (github.com vs GHES) — reusable

Every `github` data stream exposes the API host as a variable rather than hardcoding it. Two
distinct conventions are in use, and the difference matters:

**Host-only variable** (`audit`, `issues`, `code_scanning`, `dependabot`, `secret_scanning`) —
the CEL/httpjson template appends the path:

```56:63:packages/github/data_stream/audit/manifest.yml
      - name: api_url
        type: text
        title: API URL.
        description: The API URL without the path.
        multi: false
        required: true
        show_user: false
        default: https://api.github.com
```

Identical block at `packages/github/data_stream/issues/manifest.yml:75-82`.

**Full-URL variable** (`security_advisories`) — the whole endpoint including path is the var:

```9:16:packages/github/data_stream/security_advisories/manifest.yml
      - name: api_url
        type: text
        title: API URL
        description: URL for GitHub Security Advisories database REST API
        multi: false
        required: true
        show_user: false
        default: https://api.github.com/advisories
```

For a repo-file integration the **host-only** convention is the better precedent: the CEL
program needs to build several different paths (tree, blob) from the same base, and a GHES user
only has to change `https://api.github.com` → `https://ghes.example.com/api/v3`.

Both use `show_user: false`, keeping the field out of the default Fleet UI while remaining
overridable — appropriate for a value that only GHES users change.

The `audit` stream additionally exposes an `enterprise` variable
(`packages/github/data_stream/audit/manifest.yml:25-28`): "The GitHub enterprise name/ID.
Either `Organization Name` or `Enterprise Name` must be set."

The package README is explicit that GHES support is not universal —
`packages/github/_dev/build/docs/README.md:53`: *"This integration is not compatible with
GitHub Enterprise server."*

---

## 3. Authentication variables — reusable

```17:24:packages/github/data_stream/security_advisories/manifest.yml
      - name: api_key
        type: password
        title: API key
        description: The GitHub Personal Access Token (PAT) is used to authenticate with the GitHub REST API. You may leave this field blank for public repositories, as authentication is not required for them.
        multi: false
        required: false
        show_user: true
        secret: true
```

The three attributes that matter: `type: password`, `secret: true`, and `show_user: true`.

The template pairs this with conditional redaction so the token never reaches the request
tracer or debug logs — `packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs:9-21`:

```9:21:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
{{#if api_key}}
  api_key: {{api_key}}
{{/if}}
  advisory_type: {{advisory_type}}
  batch_size: {{batch_size}}
{{#if api_key}}
redact:
  fields:
    - api_key
{{else}}
redact:
  fields: ~
{{/if}}
```

And the optional-header idiom that omits `Authorization` entirely when no key is configured —
note the `?"Authorization"` optional-field syntax and `optional.ofNonZeroValue`:

```36:40:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
    "Header": {
        "Accept": ["application/vnd.github+json"],
        "X-GitHub-Api-Version": ["2022-11-28"],
        ?"Authorization": has(state.api_key) && state.api_key != "" ? optional.ofNonZeroValue(["Bearer " + state.api_key]) : optional.ofNonZeroValue([]),
    },
```

**Directly reusable**: the `Accept: application/vnd.github+json` +
`X-GitHub-Api-Version: 2022-11-28` + `Authorization: Bearer <token>` header triple is exactly
what the Trees and Blobs APIs need. For a private repo the credential becomes mandatory, so the
conditional wrapper can be dropped and `api_key` marked `required: true`.

---

## 4. `Link: rel="next"` pagination — the exact CEL idiom

This is the most directly transferable code in the repo. Three files implement it;
`github` is the reference:

- `packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs`
- `packages/servicenow/data_stream/event/agent/stream/cel.yml.hbs`
- `packages/auth0/data_stream/logs/agent/stream/cel.yml.hbs`

The pattern is a named `regexp` block at config level, then three uses of it in the program.

**1. Declare the pattern once** (config-level `regexp:` map, compiled once at input start):

```22:24:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
regexp:
  github_link_next: '<([^>]+)>; rel="next"'
max_executions: 5000
```

**2. Prefer the cursor's saved next URL over building a fresh first-page URL:**

```26:34:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
  request(
    "GET",
    state.?cursor.next_url.orValue(state.url.trim_right("/") + "?" + {
        "per_page": [string(state.batch_size)],
        "type": [state.advisory_type],
        "sort": ["published"],
        "order": ["desc"]
      }.format_query()
    )
  ).with({
```

Note `state.url.trim_right("/")` (defensive trailing-slash handling) and `.format_query()`
(correct URL encoding of a `map<string, list<string>>`).

**3. Extract the next URL into the cursor, and set `want_more` from the same condition:**

```63:79:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
        "cursor": {
           ?"next_url": (
            (has(resp.?Header.Link) && size(resp.Header.Link) != 0 && resp.Header.Link[0].re_match("github_link_next")) ?
              resp.Header.Link[0].re_find_submatch("github_link_next")[?1]
            :
              optional.none()
          ),
        },
        "events": body.map(
          e,
          {
            "message": e.encode_json(),
          }
        ),
        "url": state.url,
        "want_more": has(resp.?Header.Link) && size(resp.Header.Link) != 0 && resp.Header.Link[0].re_match("github_link_next"),
      }
```

Key details worth carrying over:

- `resp.?Header.Link` — optional traversal; the header is absent on the last page.
- `resp.Header.Link[0]` — Go canonicalises the header name to `Link` and values are a
  **list of strings**, hence the `[0]`.
- `re_find_submatch(...)[?1]` — optional index into the submatch list, yielding
  `optional<string>`, which pairs with `?"next_url"` so the key simply disappears when there is
  no next page. This is cleaner than storing a sentinel.
- `"url": state.url` is re-emitted explicitly. Per the CEL input docs, `state.url` must be
  present in the returned value to survive to the next evaluation.
- `max_executions: 5000` raises the default 1,000-execution `want_more` budget.

**Relevance here.** The Trees API is *not* paginated, so this idiom is not needed for the
recommended enumeration strategy. It *is* needed if the design ever falls back to the Contents
API or the Commits API, both of which paginate via `Link` — verified live, e.g.
`GET /commits?path=…&since=…&per_page=3` returns
`link: <…&page=2>; rel="next", <…&page=6>; rel="last"`.

---

## 5. The existing `security_advisories` data stream — and why it does not fit

**This is the section a reviewer will read first.**

### 5.1 What it actually collects

Endpoint: `https://api.github.com/advisories`
(`packages/github/data_stream/security_advisories/manifest.yml:16`) — the **global GitHub
Advisory Database**, GitHub's public, curated catalogue of vulnerabilities in open-source
packages across ecosystems (npm, PyPI, Go, Maven, …). It is the same dataset browsable at
<https://github.com/advisories>.

Query parameters used
(`packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs:28-34`):
`per_page`, `type`, `sort=published`, `order=desc`.

The `advisory_type` variable is a three-way select — `reviewed`, `unreviewed`, `malware`
(`manifest.yml:25-37`) — which are the global database's curation tiers. Default interval `24h`
(`manifest.yml:38-45`).

Authentication is **optional** (`manifest.yml:22`: *"You may leave this field blank for public
repositories, as authentication is not required for them"*), because the global database is public.

### 5.2 The five reasons it cannot be reused

| | Existing `security_advisories` | What we need |
| --- | --- | --- |
| **Data source** | Global GitHub Advisory Database (`/advisories`) — GitHub's public catalogue of OSS package vulnerabilities | Files in the `advisories/` directory of one private repo |
| **Scope** | Every ecosystem, every vendor, tens of thousands of records | Elastic's own product advisories, a few hundred documents |
| **Format** | GitHub-defined JSON schema, fixed and stable | Whatever file format that repo uses — Markdown, YAML, JSON; unknown |
| **Auth** | Optional; public data | **Mandatory**; private repo, `Contents: Read-only` required |
| **Pagination/incrementality** | `Link: rel="next"` cursor over a server-sorted feed | No pagination; incrementality must come from blob SHA or ETag diffing |

There is no parameter, media type, or filter on `GET /advisories` that makes it return
repository file contents. It is a different endpoint returning a different entity.

Note also that a *third* thing exists and should not be confused with either:
`GET /repos/{owner}/{repo}/security-advisories` returns **GitHub-native repository security
advisories** — draft/published advisory objects managed through the repo's Security tab, backed
by GitHub's own data model (fine-grained permission `repository_advisories: read`). Verified live
that this endpoint returns 200 for `elastic/integrations`. This is *still* not "files in the
`advisories/` directory". If `elastic/security-advisories` happens to publish GitHub-native
advisories mirroring its files, that endpoint would be a structured alternative worth evaluating —
but that is unknown without repo access.

### 5.3 What IS worth copying from it

Despite the data mismatch, this data stream is the best in-repo template for GitHub API
mechanics in CEL: the header triple (§3), the redaction pattern (§3), the `Link` pagination
idiom (§4), the request-tracer block (§7), and the error-event shape (§8).

### 5.4 Field-mapping precedent

`packages/github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml`
maps the GitHub advisory JSON onto both a `github.security_advisory.*` custom namespace and
ECS `vulnerability.*`. The ECS targets it populates:

| ECS field | Source |
| --- | --- |
| `vulnerability.id` | `cve_id` (line 62-66) |
| `vulnerability.description` | `description` (141-145) |
| `vulnerability.severity` | `severity` (241-245) |
| `vulnerability.score.base` | `cvss.score`, converted to float (86-90) |
| `vulnerability.reference` | advisory `html_url` (187-191) |
| `vulnerability.classification` | constant `CVSS` (280-283) |
| `vulnerability.enumeration` | constant `CVE` (284-287) |

It also sets `event.kind: enrichment`, `event.category: [vulnerability]`, `event.type: [info]`
(lines 12-25) — the right event triplet for advisory documents, which describe a condition
rather than an occurrence.

Other `vulnerability.*` mapping precedent, if a richer model is needed:

- `packages/snyk/data_stream/issues/elasticsearch/ingest_pipeline/default.yml` — populates
  `vulnerability.severity` (73), `vulnerability.enumeration` (82, 106), `vulnerability.id` (94),
  `vulnerability.reference` (118).
- `packages/ti_flashpoint/data_stream/vulnerability/fields/ecs.yml` — the
  `constant_keyword` convention for provenance:
  `observer.vendor`, `observer.product`, and `vulnerability.scanner.vendor`.
- Further `vulnerability.*` users: `packages/aws/data_stream/inspector/`,
  `packages/google_scc/data_stream/finding/`, `packages/qualys_was/data_stream/vulnerability/`,
  `packages/claroty_xdome/data_stream/vulnerability/`, `packages/sentinel_one/data_stream/application_risk/`,
  `packages/crowdstrike/data_stream/vulnerability/`, `packages/hackerone/data_stream/report/`.

---

## 6. ETag-based skip using the cursor — `ti_recordedfuture` ★ closest precedent

**`packages/ti_recordedfuture/data_stream/threat/agent/stream/cel.yml.hbs:48-68`** is the only
place in the monorepo that uses HTTP conditional-request semantics to avoid re-downloading
unchanged data. It is the closest structural analogue to what this integration needs.

The approach: a cheap **`HEAD` request** first, compare the returned `Etag` against the value
saved in `state.cursor.etag`, and only issue the `GET` when they differ.

```48:68:packages/ti_recordedfuture/data_stream/threat/agent/stream/cel.yml.hbs
  }.as(req,
    request("HEAD", req.url).with(req.headers).do_request().as(headResp,
      (headResp.StatusCode == 200 && headResp.Header.?Etag[?0].orValue("") == state.?cursor.etag.orValue("NONE")) ?
        // no new data - the etag matches what we've seen
        state.with({
          "events": [],
          "want_more": false,
        })
      :
        // new data available (or etag check failed)
        request("GET", req.url).with(req.headers).do_request().as(resp, (resp.StatusCode == 200) ?
          // successful response
          state.with({
            "events": try({ "data": resp.Body.mime("application/gzip") }, "error").as(unzipped,
              (has(unzipped.error) ? resp.Body : unzipped.data).mime("text/csv; header=present").as(parsed,
                parsed.map(e, { "message": e.encode_json() })
              )
            ),
            "cursor": state.?cursor.orValue({}).with({ "etag": resp.Header.?Etag[0].orValue("NONE") }),
            "want_more": false,
         })
```

Idioms to carry over:

- `headResp.Header.?Etag[?0].orValue("")` — safe optional chain through an absent header and an
  empty value list.
- `state.?cursor.etag.orValue("NONE")` — a sentinel default so the first run always fetches.
- `state.?cursor.orValue({}).with({...})` — merge into the existing cursor rather than replacing
  it, preserving sibling keys.
- Returning `{"events": [], "want_more": false}` on the no-change path.

**Adaptation needed.** `ti_recordedfuture` spends a `HEAD` request to test the ETag. Against
GitHub that is unnecessary and strictly worse: sending `If-None-Match` on the real `GET` yields
a **304 that costs zero rate-limit budget** (verified — see
`github-api-collection-notes.md` §3.1), so the conditional `GET` is both cheaper and one
round-trip shorter than `HEAD`-then-`GET`. Two verified caveats: the ETag must be echoed back
**with its surrounding double quotes**, and the zero-cost property requires the request to carry
a valid `Authorization` header.

**Gap.** No package currently sends `If-None-Match` or `If-Modified-Since`:

```
$ rg -n "If-None-Match|If-Modified-Since" packages --glob "*.hbs"
# (no matches)
```

So this integration would be establishing that pattern.

---

## 7. Persisted worklist / "list then fetch each" — `abnormal_security`

Enumerating files and then fetching each one's content across multiple CEL executions is the
list-then-detail shape. The most complete implementation is
**`packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs`**.

The control structure (lines 28-40): if a worklist already exists in state, skip the list call
and keep draining it; otherwise fetch a fresh page.

```28:40:packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
  (
    has(state.?worklist.threats) && size(state.worklist.threats) > 0 ?
      state
    :
      (
        state.?want_more.orValue(false) ?
          state
        :
          state.with({
            "start_time": state.?cursor.last_timestamp.orValue((now - duration(state.initial_interval)).format(time_layout.RFC3339)),
            "end_time": now.format(time_layout.RFC3339),
          })
      ).as(state, state.with(
```

Then the detail fetch indexes the worklist by a persisted `next` pointer (line 79):

```78:83:packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
        request("GET",
          state.url.trim_right("/") + "/v1/threats/" + string(state.worklist.threats[state.next].threatId) + "?" + {
            "pageSize": [string(state.page_size)],
            "pageNumber": [string(state.child_next_page)]
          }.format_query()
        ).with({
```

and advances or clears it (lines 137-149):

```137:149:packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
            "worklist": int(state.next) + 1 < size(state.worklist.threats) || has(body.nextPageNumber) ? state.worklist : {},
            "child_next_page": has(body.nextPageNumber) ? body.nextPageNumber : 1,
            "next": (
              has(body.nextPageNumber) ?
                state.next
              :
                int(state.next) + 1 < size(state.worklist.threats) ?
                  int(state.next) + 1
                :
                  0
            ),
```

It also handles a mid-traversal deletion — an item present in the list but 404 on detail fetch —
by emitting a sentinel event and skipping, rather than erroring the whole run
(lines 151-168 plus the `drop_event` processor at lines 219-223):

```151:157:packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
        : resp.StatusCode == 404 ?
          // Threat deleted before detail fetch: skip.
          {
            "events": [{"retry": true}],
            "cursor": {
              "last_timestamp": state.end_time
            },
```

```219:223:packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
processors:
- drop_event:
    when:
      equals:
        retry: true
```

This 404-skip pattern is directly relevant: a file can be deleted between the tree enumeration
and the blob fetch. (Though with the Blobs API this is less likely than with the Contents API,
because a blob SHA remains fetchable until garbage collection even after the path is removed.)

Other worklist implementations, if a second opinion is useful:
`packages/crowdstrike/data_stream/identity_protection_assessment/`,
`packages/cyera/data_stream/datastore/`, `packages/sentinel_one/data_stream/unified_alert/`,
`packages/qualys_was/data_stream/vulnerability/`, `packages/vectra_rux/data_stream/audit/`,
and the `checkpoint_harmony_endpoint` family (7 data streams sharing one template).

**Caution.** `abnormal_security` is *not* a clean template to copy wholesale: it repeats a large
state-update block four times across its success/404/error branches, which is exactly the kind
of duplication that makes CEL programs hard to review. Take the control-flow shape, not the layout.

---

## 8. Rate-limit handling — `qualys_vmdr` and `mimecast`

**`packages/qualys_vmdr/data_stream/user_activity/agent/stream/cel.yml.hbs:95-124`** uses the
CEL `rate_limit()` function to translate response headers into the input's own throttling.
This is highly relevant because **`rate_limit()`'s magic suffixes are exactly GitHub's header
convention** — `-Limit`, `-Remaining`, `-Reset` with an `x-ratelimit` prefix:

```95:119:packages/qualys_vmdr/data_stream/user_activity/agent/stream/cel.yml.hbs
      resp.Header.transformMapEntry(k, v,
        // Canonicalise header keys to match rate_limit conventions.
        // -Limit, -Remaining and -Reset are magic suffixes in rate_limit.
        {
          k.has_suffix("-Limit") ?
            (k.trim_suffix("-Limit").to_lower() + "-Limit")
          : k.has_suffix("-Remaining") ?
            (k.trim_suffix("-Remaining").to_lower() + "-Remaining")
          :
            k.to_lower(): v,
        }
      ).as(headers,
        // Calculate rate limits.
        rate_limit(
          headers.with(
            {
              "x-ratelimit-Reset": [string(headers[?"x-ratelimit-towait-sec"][0].orValue("3600"))],
            }
          ),
          "x-ratelimit",
          false,
          true,
          duration(string(headers[?"x-ratelimit-window-sec"][0].orValue("3600")) + "s"),
          0
        )
      ).as(rate_headers, rate_headers.with({
```

Qualys needs the elaborate header-rewriting because its headers are non-standard
(`x-ratelimit-towait-sec`, `x-ratelimit-window-sec`). **GitHub needs none of it** — it emits
`x-ratelimit-limit`, `x-ratelimit-remaining`, and `x-ratelimit-reset` (reset as UTC epoch
seconds) natively, which is precisely what `rate_limit(headers, "x-ratelimit", …)` expects.
So the useful takeaway is the *existence and call signature* of `rate_limit()`, not the
transformation code around it.

`packages/mimecast/data_stream/threat_intel_malware_grid/agent/stream/cel.yml.hbs:147-158`
shows the complementary defensive pattern — treat a bare 429 as a back-off signal, emit no
error event, and crucially **do not advance the cursor**:

```147:154:packages/mimecast/data_stream/threat_intel_malware_grid/agent/stream/cel.yml.hbs
        : resp.StatusCode == 429 ?
          // For reasons, Mimecast does not set X-RateLimit-* headers
          // until the rate limit has been exceeded, so treat 429 codes
          // as a sentinel to back off. We don't want to log errors and
          // we do not want to update the cursor, so return an empty
          // events array.
          {
            "events": [],
```

Directly applicable: GitHub returns **403 *or* 429** for both primary and secondary limits, so
both codes need this treatment, not just 429.

Only four packages handle rate-limit headers at all:
```
$ rg -ln "X-RateLimit|x-ratelimit|Retry-After" packages --glob "cel.yml.hbs"
packages/mimecast/data_stream/threat_intel_malware_customer/agent/stream/cel.yml.hbs
packages/mimecast/data_stream/threat_intel_malware_grid/agent/stream/cel.yml.hbs
packages/qualys_gav/data_stream/asset/agent/stream/cel.yml.hbs
packages/qualys_vmdr/data_stream/user_activity/agent/stream/cel.yml.hbs
```

---

## 9. The `enable_request_tracer` pattern — reusable verbatim

Config block
(`packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs:3-6`):

```3:6:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
resource.tracer:
  enabled: {{enable_request_tracer}}
  filename: "../../logs/cel/http-request-trace-*.ndjson"
  maxbackups: 5
```

Paired variable
(`packages/github/data_stream/security_advisories/manifest.yml:80-88`):

```80:88:packages/github/data_stream/security_advisories/manifest.yml
      - name: enable_request_tracer
        type: bool
        title: Enable request tracing
        default: false
        multi: false
        required: false
        show_user: false
        description: >
          The request tracer logs requests and responses to the agent's local file-system for debugging configurations. Enabling this request tracing compromises security and should only be used for debugging. See [documentation](https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-input-cel.html#_resource_tracer_filename) for details.
```

Conventions: `default: false`, `show_user: false`, the security warning in the description,
`maxbackups: 5`, the `../../logs/cel/` relative path, and the `*` glob in the filename that the
input expands per-input. This block is copied near-verbatim across the whole monorepo and should
be reproduced as-is.

Note the interaction with `redact` (§3): the tracer writes full request/response bodies to disk,
so the `redact.fields` list is what keeps the token out of those files. The two features must be
configured together.

---

## 10. Error-event shape — reusable verbatim

```41:56:packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs
  }).do_request().as(resp, (resp.StatusCode != 200) ?
    {
      "events": {
        "error": {
          "code": string(resp.StatusCode),
          "id": string(resp.Status),
          "message": "GET " + state.url.trim_right("/") + ": " + (
            (size(resp.Body) != 0) ?
              string(resp.Body)
            :
              string(resp.Status) + " (" + string(resp.StatusCode) + ")"
          ),
        },
      },
      "want_more": false,
    }
```

The matching pipeline side terminates cleanly on a data-collection error rather than producing a
malformed document —
`packages/github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml:8-11`:

```8:11:packages/github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml
  - terminate:
      tag: data_collection_error_4bdbb3d0
      if: ctx.error?.message != null && ctx.message == null && ctx.event?.original == null
      description: error message set and no data to process.
```

For a private repo one extra branch is worth adding beyond this template: GitHub answers
**404, not 403**, when the credential lacks access (verified live). A bare 404 on the tree
endpoint most likely means a bad or under-scoped token, not a missing directory, and the error
message should say so — otherwise every misconfiguration looks like an empty repository.

---

## 11. Testing precedent

`packages/github/data_stream/security_advisories/_dev/deploy/docker/files/config.yml` is a
mock-server config for `elastic-package`'s HTTP mock. It demonstrates matching on path, method,
`query_params`, and `request_headers`, and — importantly for the pagination idiom — **synthesising
a `Link` header that points back at the mock itself**:

```14:19:packages/github/data_stream/security_advisories/_dev/deploy/docker/files/config.yml
      - status_code: 200
        headers:
          Content-Type:
            - application/json
          Link:
            - '<http://{{ .request.host }}/advisories?after=abcd>; rel="next"'
```

The `{{ .request.host }}` template variable and the `minify_json` helper for inline fixture
bodies are the two reusable tricks here. A second rule matching `query_params: {after: abcd}`
serves page 2, so the full pagination loop is exercised in system tests.

System-test configs live alongside at
`packages/github/data_stream/security_advisories/_dev/test/system/` — three of them
(`test-non-authentication-config.yml`, `test-reviewed-config.yml`, `test-unreviewed-config.yml`),
covering the authenticated and unauthenticated paths separately.

Pipeline tests: `_dev/test/pipeline/test-vulnerability.log` (NDJSON input) plus
`test-vulnerability.log-expected.json`.

For this integration the mock would need to serve a tree response, blob responses, and — to test
the incremental path properly — a **304 on a second request carrying `If-None-Match`**. Whether
the `elastic-package` mock server supports conditional-request matching on
`request_headers: {if-none-match: …}` is untested here; the config format does support arbitrary
`request_headers` matching, so it is plausible. **[UNVERIFIED]**

---

## 12. Summary — what to reuse, by priority

| Priority | Pattern | Source |
| --- | --- | --- |
| 1 | GitHub header triple + optional `Authorization` + `redact` | `github/…/security_advisories/agent/stream/cel.yml.hbs:9-21,36-40` |
| 2 | ETag stored in `state.cursor`, skip when unchanged (adapt `HEAD` → conditional `GET`) | `ti_recordedfuture/…/threat/agent/stream/cel.yml.hbs:48-68` |
| 3 | Persisted worklist + `next` pointer for list-then-fetch-each | `abnormal_security/…/threat/agent/stream/cel.yml.hbs:28-40,78-83,137-149` |
| 4 | `enable_request_tracer` block + variable | `github/…/security_advisories/{agent/stream/cel.yml.hbs:3-6, manifest.yml:80-88}` |
| 5 | Error-event shape + `terminate` processor | `github/…/security_advisories/{cel.yml.hbs:41-56, ingest_pipeline/default.yml:8-11}` |
| 6 | Host-only `api_url` variable for GHES portability | `github/data_stream/audit/manifest.yml:56-63` |
| 7 | 404-on-detail-fetch skip via sentinel event + `drop_event` | `abnormal_security/…/threat/agent/stream/cel.yml.hbs:151-157,219-223` |
| 8 | `rate_limit()` on `x-ratelimit-*`; 403/429 back-off without advancing cursor | `qualys_vmdr/…/user_activity/…:95-124`; `mimecast/…/threat_intel_malware_grid/…:147-158` |
| 9 | `Link: rel="next"` regexp + cursor idiom (only if a paginated endpoint is used) | `github/…/security_advisories/agent/stream/cel.yml.hbs:22-24,26-34,63-79` |
| 10 | ECS `vulnerability.*` mapping targets and `event.kind: enrichment` | `github/…/security_advisories/elasticsearch/ingest_pipeline/default.yml:12-25,62-66,86-90,141-145,187-191,241-245,280-287` |
| 11 | Mock-server config with synthesised headers | `github/…/security_advisories/_dev/deploy/docker/files/config.yml:14-19` |

**What has no precedent and must be designed fresh:** reading files from a git repository;
sending `If-None-Match` (no package does this today); diffing a persisted `path → blob SHA` map;
and decoding base64 file content in a CEL/ingest context. On the last point, mito's
`base64_decode` uses Go's `base64.StdEncoding.DecodeString`
(`../temp/mito/lib/crypto.go:443-454`), which tolerates the newline-wrapped base64 that GitHub's
Contents and Blobs APIs return — verified by compiling and running the decode. So no
newline-stripping step is required.
