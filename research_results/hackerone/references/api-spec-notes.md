# HackerOne Customer API — Reports collection specification

Authoritative, **factual** notes for incremental polling against **`GET /v1/reports`** and testing via **`GET /v1/reports/{id}`**. Curated from official HackerOne API documentation (HTML) as of research date **2026-05-07**. No CEL or integration design guidance.

**Primary sources:**

- [Getting Started](https://api.hackerone.com/getting-started/) — base URL, auth, rate limits, errors, versioning, changelog
- [Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports) — `GET /v1/reports` (parameter table last revised **2026-04-14** on-page)
- [Get Report](https://api.hackerone.com/customer-resources/#reports-get-report) — `GET /v1/reports/{id}` (last revised **2026-04-14** on-page)
- [Report object](https://api.hackerone.com/customer-reference/#report) — attributes and relationships (last revised **2026-04-14** on-page)
- [JSON:API specification](https://jsonapi.org/format/) — general envelope, pagination, sparse fieldsets, `include` (HackerOne declares JSON API compliance on [Getting Started](https://api.hackerone.com/getting-started/))

**Local samples (from official doc examples, JSON-cleaned):**

- `research_results/hackerone/references/sample-events/list_reports_response.json` — list response (third list item in HTML is a documentation placeholder `"..."`; omitted for valid JSON; see §3)
- `research_results/hackerone/references/sample-events/single_report_response.json` — single-report `data` object tree (includes an **as-published** timestamp string that is not valid ISO 8601 hours: `2020-10-22T011:22:05.402Z` in author `created_at`; preserved verbatim from docs)

**Raw download (this research):** `research_results/hackerone/temp/api-docs-2026-05-07/getting-started.html`

---

## 1. Base URL and versioning

| Item | Fact (documented) |
|------|-------------------|
| **Production base URL** | `https://api.hackerone.com/` — shown as “API Endpoint” and in all customer samples ([Getting Started](https://api.hackerone.com/getting-started/)) |
| **Version in URL path** | **`v1`** — pattern `https://api.hackerone.com/{version}/{resource}` ([Versioning](https://api.hackerone.com/getting-started/#versioning)); **no default version** (“requested version must be specified”) |
| **Reports list path** | `GET https://api.hackerone.com/v1/reports` ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)); on-page heading also shows relative `GET /reports` under the versioned API |
| **Sandbox / non-prod API host** | Documentation describes a **sandbox program** you create on **`hackerone.com`** ([API sandbox](https://api.hackerone.com/getting-started/#api-sandbox), link to `https://hackerone.com/teams/new/sandbox`). There is **no separate sandbox API hostname** published on Getting Started; requests use the **same** `https://api.hackerone.com` host as production samples. **[INFERENCE:]`** Sandbox program data is served through the production API hostname; **`[UNVERIFIED]`** if any request-routing differs per program beyond normal authorization |

**Brief related endpoints (not deep-dived):**

- **`GET /v1/me/programs`** (doc: [Get your programs](https://api.hackerone.com/customer-resources#programs-get-your-programs)) — per [changelog Feb 20, 2017](https://api.hackerone.com/getting-started/#changelog); use to discover **program handles** for `filter[program][]`.
- **`GET /v1/incremental/activities`** — incremental **activity** stream under **Query Activities** ([customer-resources — Query Activities / `GET /incremental/activities`](https://api.hackerone.com/customer-resources/#activities-query-activities)); alternate source for “what changed,” not substitute for report list semantics.

---

## 2. Authentication

### Method

- **HTTP Basic Authentication** — API token **identifier** as username and token **secret** as password on **every request** ([Authentication](https://api.hackerone.com/getting-started/#authentication)).
- **Wire:** `Authorization: Basic <base64(username + ":" + token)>` (shown in Java / JavaScript samples across customer-resources pages; curl uses `-u "<YOUR_API_USERNAME>:<YOUR_API_TOKEN>"` on [Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).

### Clients should send

- **`Accept: application/json`** on read operations (all `GET` samples for reports use this header).

### Credential creation (high level)

- Customer Getting Started: tokens from **Program / organization context** for Professional, Community, or Enterprise; link to [Generate an API Token](https://docs.hackerone.com/organizations/api-tokens.html) ([Getting Started](https://api.hackerone.com/getting-started/)).
- **Detail / group permissions / admin UI** — out of scope here; see Help Center [API Tokens (organizations)](https://docs.hackerone.com/organizations/api-tokens.html).

### Token lifetime / rotation

- **OAuth2-style refresh or documented expiry** for organization API tokens: **not stated** on Getting Started. **[UNVERIFIED]** beyond Help Center org/hacker token articles.
- **Hacker** personal tokens: generating a new token **revokes** the previous ([API Token — hackers](https://docs.hackerone.com/hackers/api-token.html)) — analogous “rotation by replacement” behavior for that token type only.

### IP allowlisting vs invalid credentials

From [Authentication](https://api.hackerone.com/getting-started/#authentication):

- **IP whitelist** configured + **valid** credentials but disallowed IP → **`403 Forbidden`**
- **Invalid token** → **`401 Unauthorized`**

From [Error Responses — 403](https://api.hackerone.com/getting-started/#error-responses): token **cannot** perform the action — e.g. resource **another program or account**.

**Factual consolidation:** **`401`** aligns with identification failure / wrong username (**not email**, per 401 row). **`403`** is documented for **IP whitelist** **and** for **authorization / wrong program**. Distinction is **not** further narrowed in the error table body.

### OAuth2

- Customer **Getting Started** documents **only** HTTP Basic + API tokens for the REST API. **No `client_credentials`, `authorization_code`, or other OAuth2 flow** is documented there for Customer API access.
- **OAuth2 usable via Elastic `auth.oauth2`:** **Not supported by published Customer API auth docs** (treat as **manual token / Basic** from product perspective unless HackerOne publishes otherwise).
- Admin-console “generate token” is **not** an OAuth2 authorization flow ([Getting Started](https://api.hackerone.com/getting-started/#authentication)).

---

## 3. Reports — `GET /v1/reports` (Get All Reports)

### Path and method

- **Full URL:** `GET https://api.hackerone.com/v1/reports`
- **Doc slug:** [reports-get-all-reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)

### Required filter (documented)

> **IMPORTANT:** Either **`filter[program]`** or **`filter[inbox_ids]`** is **required** ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `filter[program][]` | Conditional | `array[string]` | Program **handles**; required if `filter[inbox_ids][]` **not** specified |
| `filter[inbox_ids][]` | Conditional | `array[integer]` | Inbox IDs; required if **`filter[program][]`** **not** specified |

### Optional filters (complete table per documentation)

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter[reporter][]` | `array[string]` | Hacker **usernames** |
| `filter[assignee][]` | `array[string]` | Assignee **usernames, emails or group names** |
| `filter[state][]` | `array[string]` | Current report state (enum below) |
| `filter[id][]` | `array[integer]` | Report IDs |
| `filter[weakness_id][]` | `array[integer]` | Weakness IDs |
| `filter[severity][]` | `array[string]` | Severity ratings (enum below) |
| `filter[asset_ids][]` | `array[integer]` | Asset IDs ([changelog Oct 1, 2025](https://api.hackerone.com/getting-started/#changelog)) |
| `filter[hacker_published]` | `boolean` | Published by hackers per truth value |
| `filter[hai_is_priority]` | `boolean` | Prioritization Agent; Enterprise / populated cases only |
| `filter[created_at__gt]` | `date-time` | Created **after** date |
| `filter[created_at__lt]` | `date-time` | Created **before** date |
| `filter[submitted_at__gt]` | `date-time` | Submitted **after** date |
| `filter[submitted_at__lt]` | `date-time` | Submitted **before** date |
| `filter[triaged_at__gt]` | `date-time` | Triaged **after** date |
| `filter[triaged_at__lt]` | `date-time` | Triaged **before** date |
| `filter[triaged_at__null]` | `boolean` | Triaged or not per value |
| `filter[closed_at__gt]` | `date-time` | Closed **after** date |
| `filter[closed_at__lt]` | `date-time` | Closed **before** date |
| `filter[closed_at__null]` | `boolean` | Closed or not per value |
| `filter[disclosed_at__gt]` | `date-time` | Disclosed **after** date |
| `filter[disclosed_at__lt]` | `date-time` | Disclosed **before** date |
| `filter[disclosed_at__null]` | `boolean` | “Filter by reports that are disclosed.” (boolean per doc wording) |
| `filter[reporter_agreed_on_going_public]` | `boolean` | Hacker disclosure request |
| `filter[bounty_awarded_at__gt]` | `date-time` | Bounty awarded **after** date |
| `filter[bounty_awarded_at__lt]` | `date-time` | Bounty awarded **before** date |
| `filter[bounty_awarded_at__null]` | `boolean` | “Filter by reports that have a bounty awarded.” |
| `filter[swag_awarded_at__gt]` | `date-time` | Swag awarded **after** date |
| `filter[swag_awarded_at__lt]` | `date-time` | Swag awarded **before** date |
| `filter[swag_awarded_at__null]` | `boolean` | Swag awarded or not per value |
| `filter[last_reporter_activity_at__gt]` / `__lt` | `date-time` | Reporter update after/before date |
| `filter[first_program_activity_at__gt]` / `__lt` | `date-time` | First program update after/before date |
| `filter[first_program_activity_at__null]` | `boolean` | Doc text: *“Filter by reports where the reporter received an update.”* |
| `filter[last_program_activity_at__gt]` / `__lt` | `date-time` | Program update after/before date |
| `filter[last_activity_at__gt]` / `__lt` | `date-time` | *“Filter by reports that received an update after/before the date specified.”* |
| `filter[last_public_activity_at__gt]` / `__lt` | `date-time` | Public update after date (`__gt`); **`__lt` row duplicates “after” in the published HTML** — treat as documentation error for the `__lt` description ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)) |
| `filter[keyword]` | `string` | Title and keywords |
| `filter[issue_tracker_reference_id]` | `string` | Issue tracker reference |
| `filter[issue_tracker_reference_id__null]` | `boolean` | Has reference or not per value |
| `filter[custom_fields][]` | `array[object]` | Custom field label/value — [custom-field-input](https://api.hackerone.com/customer-reference#custom-field-input) |

### Enumerated `filter[state][]`

`new`, `pending-program-review`, `triaged`, `needs-more-info`, `resolved`, `not-applicable`, `informative`, `duplicate`, `spam`, `retesting` ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports))

### Enumerated `filter[severity][]`

`none`, `low`, `medium`, `high`, `critical` — same page

### Pagination and sort

| Parameter | Type | Default / limits |
|-----------|------|------------------|
| `page[number]` | integer | Default **1** |
| `page[size]` | integer | Default **25**; allowed **1–100** (“currently limited”) |
| `sort` | string | See below |

### `sort` (detailed)

- **Multiple fields:** comma-separated; order of fields defines **primary / secondary** sort precedence ([Get All Reports — Detailed descriptions](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).
- **Descending:** prepend **`-`** to a field ([same section](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).
- **April 21, 2026 changelog:** “per-field direction control” for Reports, example `sort=reports.swag_awarded_at,-reports.bounty_awarded_at` ([changelog](https://api.hackerone.com/getting-started/#changelog)).
- **Allowed sort attributes (Reports):**  
  `reports.swag_awarded_at`, `reports.bounty_awarded_at`, `reports.last_reporter_activity_at`, `reports.first_program_activity_at`, `reports.last_program_activity_at`, `reports.triaged_at`, **`reports.created_at`**, `reports.closed_at`, `reports.last_public_activity_at`, **`reports.last_activity_at`**, `reports.disclosed_at`  
  — all use the **`reports.`** prefix per this table (**not** bare `created_at` for this endpoint).

**`[NOTE]`:** The **`Activities`** incremental endpoint documents a **different** `sort` + separate `order` parameter ([Query Activities](https://api.hackerone.com/customer-resources/#activities-query-activities)); do not assume Reports shares the Activities `order` parameter.

### Response envelope (documented example)

Successful list responses are JSON with at least:

- **`data`:** array of report resource objects ([example](https://api.hackerone.com/customer-resources/#reports-get-all-reports))
- **`links`:** pagination URLs; example keys: `self`, `next`, `last` ([same example](https://api.hackerone.com/customer-resources/#reports-get-all-reports))

```json
{
  "data": [ "..." ],
  "links": {
    "self": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=1",
    "next": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=2",
    "last": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=5"
  }
}
```

- **`meta`:** the **published Get All Reports example does not include `meta`**. Other endpoints show `meta` (e.g. `max_updated_at` on incremental activities). **`[UNVERIFIED]`** whether `/v1/reports` ever returns `meta` (e.g. `max_page`, `total_hits`) in live responses.

### Response headers (rate limits, etc.)

- **`X-RateLimit-Limit`**, **`X-RateLimit-Remaining`**, **`X-RateLimit-Reset`**, **`Retry-After`:** **not documented** on [Getting Started — Rate Limits](https://api.hackerone.com/getting-started/#rate-limits) in the reviewed HTML. **`[UNVERIFIED]`** in responses.

### Doc caveats on this page

- A blockquote above the JSON example reads *“ignores filter and returns all reports when feature disabled”* — **no further explanation** of which feature on the same page. **`[UNVERIFIED]`**

### Full sample

See `references/sample-events/list_reports_response.json` (two reports + `links`; official HTML inserts a third placeholder entry `"..."` which is not valid JSON).

---

## 4. Reports — `GET /v1/reports/{id}` (Get Report)

### Path and method

- **URL:** `GET https://api.hackerone.com/v1/reports/{id}`
- **Relative in docs:** `GET /reports/{id}` ([Get Report](https://api.hackerone.com/customer-resources/#reports-get-report))

### Parameters

| Name | In | Type | Required |
|------|-----|------|----------|
| `id` | path | integer | yes — report ID |

No query-parameter table on the Get Report page (only path `id`).

### Response shape vs list endpoint

- **Top-level JSON:API style:** `{ "data": { ... single report resource ... } }` ([example](https://api.hackerone.com/customer-resources/#reports-get-report))
- **More detail than typical list row:** the documented **Get Report** example embeds **full** `relationships` trees including **`activities`** (timeline), **`structured_scope`**, **`severity`**, **`assignee`**, **`attachments`**, **`summaries`**, **`custom_remediation_guidance`**, **`automated_remediation_guidance`**, **`inboxes`**, etc. The **Get All Reports** example shows **rich nested `data` inside relationships** but **does not** expand a non-empty `activities` array in the excerpt.
- **Reference:** [Report — relationships](https://api.hackerone.com/customer-reference/#report) lists all relationship keys and meanings.

### Full sample

`references/sample-events/single_report_response.json`

---

## 5. Pagination

### Mechanism

- **Page number + page size** via `page[number]` and `page[size]` ([Get All Reports parameters](https://api.hackerone.com/customer-resources/#reports-get-all-reports)) — aligns with common [JSON:API pagination](https://jsonapi.org/format/#fetching-pagination) patterns (HackerOne states JSON:API compliance on [Getting Started](https://api.hackerone.com/getting-started/)).

### Defaults and limits

- **`page[number]`:** default **1** (1-based) — explicit in parameter table
- **`page[size]`:** default **25**, max **100**, min **1**

### Next page and termination

- **Documented example** includes **`links.next`** and **`links.last`** with full query strings ([Get All Reports example](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).
- **Exact rule** when on the final page (omitted `next` vs `null` vs empty `data`): **not specified** in the Get All Reports prose. **`[UNVERIFIED]`** — conventional JSON:API clients often stop when **`links.next` is absent or null**; HackerOne does not state this.

### Stability under concurrent updates

- **Stable ordering guarantees** across pages when underlying rows change mid-scan: **not documented** for `/v1/reports`.
- **Duplicate sort keys:** no documented tie-breaker (e.g. `id`). **`[UNVERIFIED]`** ordering when many reports share the same `reports.last_activity_at` or `reports.created_at`.

---

## 6. Time-based filtering and incremental collection

### Datetime filters on reports

All `filter[...__gt]` / `filter[...__lt]` parameters in §3 use type **`date-time`** in the HTML table ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).

### Time format

- **Examples** use ISO-like UTC strings with **`Z`** (e.g. `2016-02-02T04:05:06.000Z`) ([responses](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).
- [Report object reference](https://api.hackerone.com/customer-reference/#report): attributes are **`string(date-time)`** formatted **according to ISO 8601**.
- **Strict inclusivity/exclusivity** of `__gt` / `__lt` boundaries (exclusive `>` vs inclusive `≥`): wording is **“after”** / **“before”**; **mathematical strictness not stated numerically**. **`[INFERENCE]`** typical SQL-style “greater than literal” for `__gt`; confirm empirically if edge-second behavior matters.

### Semantics of `last_activity_at` (critical)

[Changelog May 10, 2017](https://api.hackerone.com/getting-started/#changelog):

> “added **last_public_activity_at** in favor of **last_activity_at**. The new attribute … exposes the date of the **last public** activity. The **last_activity_at** attribute will now return the date of the **last activity, both public and internal**.”

So **`filter[last_activity_at__gt]`** / **`__lt`** align with **any** activity that updates that timestamp (public **or** internal), per this changelog + filter descriptions (“received an update”).

### Sort fields relevant to polling

- **Created-time ordered scans:** `sort=reports.created_at` (descending: `-reports.created_at`) — field is in the allowed list.
- **Last-activity ordered scans:** `sort=reports.last_activity_at` — field is in the allowed list.
- **`reports.updated_at`:** **not** in the documented Reports sort list. Do not assume it is a valid `sort` key. **[UNVERIFIED]** if server accepts unstated aliases.

### Factual “lossless” characterization (API contract only)

The API does **not** define integrator-level “lossless” behavior. Documented **facts** that bound what **can** be observed via **this endpoint alone**:

1. **New or newly-known reports by creation time** can be selected with **`filter[created_at__gt]`** / **`__lt`** and ordered by **`reports.created_at`** (and direction per `sort` rules).
2. **Reports that “received an update”** in the sense of **`last_activity_at`** can be selected with **`filter[last_activity_at__gt]`** / **`__lt`** and ordered by **`reports.last_activity_at`**, with **`last_activity_at`** including **internal and public** activity per [May 10, 2017 changelog](https://api.hackerone.com/getting-started/#changelog).
3. **Narrower activity semantics** (reporter-only, program-only, public-only) have **dedicated** filters and timestamps: e.g. `filter[last_public_activity_at__gt]`, `filter[last_reporter_activity_at__gt]`, `filter[last_program_activity_at__gt]` ([parameter table](https://api.hackerone.com/customer-resources/#reports-get-all-reports)).
4. **Activity-level feed** is a **different resource:** `GET /v1/incremental/activities` documents paginated **activity** objects and `updated_at_after` ([Query Activities](https://api.hackerone.com/customer-resources/#activities-query-activities)) — useful context; not a substitute for report list semantics.

**`[UNVERIFIED]`** whether every platform-side change a consumer cares about always mutates `last_activity_at` on the report row; the docs only define filter wording + the May 2017 attribute semantics above.

---

## 7. Rate limiting

From [Getting Started — Rate Limits](https://api.hackerone.com/getting-started/#rate-limits):

| Scope | Limit |
|-------|-------|
| **Read operations** | **600 requests per minute** |
| **Exception** | **Report pages:** **300 requests per minute** (parenthetical on same bullet) |
| **Write operations** | **25 requests per 20 seconds** |
| **Over limit** | HTTP **`429`**; copy references rate limits |

**Interpretation:** `GET /v1/reports` and `GET /v1/reports/{id}` are **report** reads; treat them as subject to the **300/min “report pages”** read cap as worded **[interpretation]** — **`[UNVERIFIED]`** if HackerOne uses a narrower definition of “report pages.”

**Other limits (changelog):** e.g. **10/min** for [Get payment transactions](https://api.hackerone.com/customer-resources/#programs-get-payment-transactions) ([changelog Apr 15, 2026](https://api.hackerone.com/getting-started/#changelog)) — unrelated to reports but shows per-endpoint limits exist.

### Headers and 429 body

- **Rate limit / retry headers:** **not documented** on Getting Started. **`[UNVERIFIED]`**
- **429 response JSON example:** **not** provided on the rate-limit section. **`[UNVERIFIED]`** body shape beyond general **`errors`** schema (§8).

---

## 8. Error responses

### HTTP statuses (Customer Getting Started)

From [Error Responses](https://api.hackerone.com/getting-started/#error-responses):

| Code | Meaning |
|------|---------|
| **400** | Bad Request — does not conform; see endpoint docs |
| **401** | Unauthorized — missing/wrong identification; username **not** an email |
| **403** | Forbidden — token cannot perform action / wrong program or account |
| **404** | Not Found |
| **406** | Not Acceptable — **documented text says** responses when client requests **`application/javascript`** (conflicts with `Accept: application/json` in samples — **likely documentation typo for `application/json`**) |
| **422** | Unprocessable Entity |
| **429** | Too Many Requests |
| **500** | Internal Server Error |
| **503** | Service Unavailable |

**401 vs 403 (documented angles):**

- **401:** identification / username problems ([401 row](https://api.hackerone.com/getting-started/#error-responses)) + invalid token called out under [Authentication](https://api.hackerone.com/getting-started/#authentication).
- **403:** IP whitelist with **valid** creds ([Authentication](https://api.hackerone.com/getting-started/#authentication)); also **authorization / wrong program** ([403 row](https://api.hackerone.com/getting-started/#error-responses)).

### Body format

- Customer reference defines top-level **`errors`** array of error objects with at least **`status`** (integer) and optional **`title`**, **`detail`**, **`source.parameter`** — [errors](https://api.hackerone.com/customer-reference/#errors), [error](https://api.hackerone.com/customer-reference/#error).

Example schema (from customer-reference):

```json
{
  "errors": [
    {
      "status": 0,
      "title": "string",
      "detail": "string",
      "source": {
        "parameter": "string"
      }
    }
  ]
}
```

---

## 9. Field selection (`fields[…]`) / sparse fieldsets / `include`

### Published parameters for Reports endpoints

The **Get All Reports** and **Get Report** pages list **only** the parameters in §§3–4 ([customer-resources anchors](https://api.hackerone.com/customer-resources/#reports-get-all-reports)). **No `include`** or **`fields[...]`** query parameters appear in those tables.

### JSON:API generic support

- HackerOne states the API is **JSON:API compliant** ([Getting Started](https://api.hackerone.com/getting-started/)); JSON:API defines [`include`](https://jsonapi.org/format/#fetching-includes) and [sparse fieldsets](https://jsonapi.org/format/#fetching-sparse-fieldsets).
- **Whether `include` / `fields` work on `/v1/reports`:** **not documented** on the Reports endpoint pages. **`[UNVERIFIED]`** behavior if clients send them.

### Practical observation from official examples

- **Get All Reports** and **Get Report** examples **embed related objects inside `relationships.*.data`** (often with nested `attributes`) rather than using a top-level **`included`** array ([list example](https://api.hackerone.com/customer-resources/#reports-get-all-reports), [single example](https://api.hackerone.com/customer-resources/#reports-get-report)). That is **factual for documentation samples**; live responses may vary **`[UNVERIFIED]`**.

### Relationship keys on `report` (for interpretation / future `include` trials)

From [Report object — relationships](https://api.hackerone.com/customer-reference/#report):  
`program`, `assignee`, `attachments`, `swag`, `weakness`, `structured_scope`, `campaign`, `severity`, `reporter`, `triggered_pre_submission_trigger`, `activities`, `bounties`, `summaries`, `custom_field_values`, `automated_remediation_guidance`, `custom_remediation_guidance`, `inboxes`, `collaborators`, …

---

## 10. Response parsing notes (factual)

- Responses are **JSON** with **`data`** members using objects that include **`id`**, **`type`**, **`attributes`**, and **`relationships`** in the official examples ([Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports), [Get Report](https://api.hackerone.com/customer-resources/#reports-get-report)).
- **List:** `data` is an **array** of report resources; **single:** `data` is one **object**.
- **Relationships** in the published examples often contain **nested resource payloads** under `data` (not only JSON:API “linkage” objects with `id` + `type`). Consumers should treat the wire format as **HackerOne’s JSON:API profile** as shown in docs, not assume strict minimal linkage-only responses.
- When a top-level **`included`** array appears: JSON:API uses it for **compound documents** ([JSON:API compound documents](https://jsonapi.org/format/#document-compound-documents)). **Reports doc examples reviewed here do not show `included` for these two endpoints.**

---

## Revision history (source document)

Get All Reports / Get Report on-page **Last revised: 2026-04-14**; parameter **sort** semantics updated in **changelog 2026-04-21** ([Getting Started changelog](https://api.hackerone.com/getting-started/#changelog)).

---

## Gaps explicitly left `[UNVERIFIED]`

See sections above for `meta` on report list, pagination termination details, rate-limit headers, 429 bodies, undocumented `include`/`fields`, `links.next` on last page, concurrent pagination stability, strict boundary semantics for `__gt`/`__lt`, “report pages” exact membership, OAuth beyond published Basic auth, SAML constraints on tokens, meaning of “ignores filter when feature disabled” blockquote.
