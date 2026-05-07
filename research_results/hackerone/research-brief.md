# Research Brief: HackerOne (Bug Bounty Reports)

> **Generated:** 2026-05-07
> **Researcher:** AI-assisted research via /research-integration skill
> **Status:** READY FOR REVIEW
> **Confidence:** HIGH (API contract, fields, sample payloads all sourced from official HackerOne customer documentation; competitive SIEM coverage validated against vendor catalogs at fetch time)

---

## 1. Product Overview

### 1.1 What is it?

HackerOne is a vulnerability disclosure and bug bounty platform that acts as a marketplace between organizations running disclosure / bug bounty programs and independent security researchers ("hackers") who submit vulnerability reports. Customer organizations receive prioritized vulnerability reports, triage them through a stateful workflow (`new` → `triaged` → `resolved` / `duplicate` / `not-applicable` / etc.), pay bounties, and ultimately disclose where appropriate. HackerOne is widely used by enterprise software vendors, financial services, US government agencies, and consumer technology companies.

### 1.2 Vendor

- **Vendor name:** HackerOne, Inc.
- **Product name:** HackerOne (Customer / Organization-facing API)
- **Product category:** Vulnerability Disclosure & Bug Bounty Platform (security workflow / vulnerability management)
- **Vendor documentation portal:** https://api.hackerone.com/ (API reference) and https://docs.hackerone.com/ (Help Center)

### 1.3 Data generated

The integration's scope is **bug bounty reports** — the customer-facing report record that represents a single hacker-submitted vulnerability disclosure. A report carries:

- **Lifecycle state and timestamps** — creation, triage, closure, disclosure, last activity (public + internal), bounty / swag award, and per-stage SLA timers.
- **Vulnerability metadata** — title, free-form vulnerability description (markdown), severity rating + CVSS metrics, CWE/CAPEC weakness, optional CVE IDs.
- **Actors** — reporter (hacker) identity, assignee (user or group), collaborators, program / organization context, and (optionally) a campaign multiplier configuration.
- **In-scope asset under attack** — `structured_scope` with asset identifier, asset type, and bounty/severity policy fields.
- **Economic impact** — bounty + swag award rows with USD principal, awarded currency, and bonus amounts.
- **Activity timeline** — 63 distinct activity types ([`references/activity-types-catalog.md`](references/activity-types-catalog.md)) covering comments, state transitions, attachments, retest lifecycle, etc.
- **Customer organization metadata** — issue-tracker reference IDs/URLs, custom field values, inbox routing, remediation guidance.

Out of scope for this research: standalone Programs API, Activities incremental stream, payment transactions, asset/program inventory, SIEM webhooks. Webhooks are noted as an alternative collection method but not deeply inventoried (see `references/collection-methods-overview.md`).

### 1.4 Existing Elastic coverage

**No existing Elastic integration package** for HackerOne was found in this repository (`packages/` search for `hackerone` returned zero results). This research is the foundation for a **new integration package**.

### 1.5 Competitive SIEM coverage

The competitive SIEM landscape for HackerOne is **thin** — there is no Splunkbase TA or QRadar SIEM DSM directly listed for HackerOne, and Sumo Logic does not publish a dedicated app. The only first-party SIEM-adjacent integrations HackerOne maintains are vendor-side push connectors (Splunk HEC, Sumo HTTP Source) and an IBM QRadar **SOAR** (not SIEM) workflow. None of the three competitors offers an API-pull integration with ECS-style normalization, which is where Elastic's recommended `cel`-based approach is differentiated.

| Vendor | Integration name | Supported data sources | Collection method | Link |
|--------|-----------------|----------------------|-------------------|------|
| IBM QRadar | No SIEM listing found (only **IBM Security QRadar SOAR** workflow) | Report submissions escalated to SOAR cases — not a log-source feed | Vendor-side UI escalation workflow into SOAR (not SIEM ingest) | https://docs.hackerone.com/organizations/ibm-security-soar.html |
| Splunk | "Splunk Integration" (HackerOne-published, **not** on Splunkbase) | Report submissions, state changes, assignments, comments, disclosures, rewards (Enterprise programs only) | Vendor push to Splunk HTTP Event Collector (HEC) over HTTPS, JSON payload | https://docs.hackerone.com/organizations/splunk-integration.html |
| Sumo Logic | "Sumo Logic Integration" (HackerOne-published, generic HTTP Source on Sumo side) | All HackerOne webhook events (configurable: "send everything" or per-event) | Webhook HTTPS POST to Sumo HTTP Source (`X-H1-Event`, `X-H1-Delivery`, `X-H1-Signature`) | https://docs.hackerone.com/organizations/sumo-logic-integration.html |

See [`references/competitive-siem-coverage.md`](references/competitive-siem-coverage.md) for full per-vendor analysis including support tier, version dates, gaps, and comparison notes.

## 2. Data Collection Method

### 2.1 Recommended method

- **Input type:** `cel` (REST API polling)
- **Rationale:** The HackerOne Customer API exposes a stable, JSON:API-compliant `GET /v1/reports` endpoint with HTTP Basic auth, page-number pagination (default 25, max 100), rich time-range filters, and a configurable `sort` parameter. This is the only collection method that:
  - Allows **historical backfill** and reconciliation (webhooks are at-most-once, fire-and-forget).
  - Doesn't require the customer to expose an inbound webhook URL on their side.
  - Returns the **complete current report state** including activity timeline, severity, weakness, scope, and bounty rows in one call (`GET /v1/reports/{id}`).
  - Aligns with how every other competing SIEM that supports HackerOne ingests (push-based, but with narrower coverage). Elastic's pull approach is differentiating.

### 2.2 Alternative methods

| Method | Input type | Pros | Cons |
|--------|-----------|------|------|
| REST API pull (`GET /v1/reports`) | `cel` | Complete state, backfill, pagination, no inbound listener | Pull cadence (latency = polling interval); subject to 300 req/min on report pages |
| Webhooks (program-level HTTPS POST) | `http_endpoint` | Real-time delivery; broader event taxonomy (63 webhook event types per [Webhooks API](https://api.hackerone.com/webhooks/)) | At-most-once, no retries documented; requires public webhook URL; per-program configuration; not all editions supported |
| Activities incremental stream (`GET /v1/incremental/activities`) | `cel` | Activity-grain change stream | Activities-only (not full report rows); duplicate work to reconstitute report state; not a substitute for `/v1/reports` |
| Vendor push to HEC / HTTP Source | n/a (out of scope for Elastic) | None for Elastic | Vendor-specific to Splunk/Sumo |

The integration should standardize on **REST API pull** for the v1 `report` data stream. Webhooks could be considered as a secondary input in a future iteration but are not required for v1.

### 2.3 Vendor-side setup required

The customer organization must, before the integration can poll:

1. **Confirm API access entitlement.** API tokens are available to **Professional**, **Community**, and **Enterprise** programs ([Getting Started](https://api.hackerone.com/getting-started/)). A free **Sandbox** program (`https://hackerone.com/teams/new/sandbox`) is suitable for testing.
2. **Create an API token** as an Organization Administrator, in **Organization Settings → API Tokens**:
   - Click **Create API Token**, give it a meaningful name.
   - Assign it to a group with at least **`report_management`** permission (read-only access to reports is sufficient; write permissions are not needed).
   - Copy the token **identifier** (used as the HTTP Basic username) and **value** (used as the password). The value is shown **only once** at creation.
3. **Identify the program handle(s)** to poll. The handle is the slug used in `https://hackerone.com/<handle>` (e.g. `security` → `https://hackerone.com/security`). Visible in the HackerOne UI under Engagements.
4. **(Optional) IP allowlisting.** If the organization has enabled IP allowlisting on API tokens, the Elastic Agent's egress IP(s) must be added to the allowlist; otherwise `GET /v1/reports` returns **`403 Forbidden`** even with valid credentials ([Authentication](https://api.hackerone.com/getting-started/#authentication)).

## 3. Data Source Details

### 3.1 Connection and authentication

- **Base URL:** `https://api.hackerone.com/`
- **API version:** `v1` — explicit in path (`https://api.hackerone.com/v1/{resource}`). HackerOne does not provide a default; the version segment is mandatory ([Versioning](https://api.hackerone.com/getting-started/#versioning)).
- **Authentication:** see below.
- **Rate limits:**
  - Read operations: **600 requests/minute** overall.
  - **Report pages: 300 requests/minute** (parenthetical exception in [Rate Limits](https://api.hackerone.com/getting-started/#rate-limits) — `GET /v1/reports` and `GET /v1/reports/{id}` should be assumed in this stricter cap, **`[INTERPRETATION]`** based on the wording).
  - Write operations: 25 requests / 20 seconds (not relevant for this read-only integration).
  - Per-endpoint exceptions exist (e.g. payment transactions: 10/min) but do not affect reports.
  - **Rate-limit response headers (`X-RateLimit-*`, `Retry-After`) are not documented** in the reviewed HTML — `[UNVERIFIED]` whether they appear in live responses.
- **Documentation:** [Getting Started](https://api.hackerone.com/getting-started/).

**Authentication detail (API key / static Basic-auth token):**

- **Method:** HTTP Basic — token **identifier** as username, token **value** as password.
- **Header format:** `Authorization: Basic base64("<token_identifier>:<token_value>")`.
- **Recommended client headers:** `Accept: application/json` (used in all official curl/Java/JavaScript samples).
- **Credential creation steps:** Organization Administrator → **Organization Settings → API Tokens** → **Create API Token**, assign to group with `report_management` permission. Reference: [HackerOne — Generate an API Token](https://docs.hackerone.com/organizations/api-tokens.html).
- **Required scopes/permissions:** `report_management` (group permission). Read-only access to reports is sufficient.
- **Token lifetime:** **Not documented** — there is no published expiry or refresh mechanism for organization tokens (`[UNVERIFIED]`). Operators rotate by creating a new token, updating the integration, and revoking the old one. (Hacker personal tokens auto-revoke on regeneration, but those are a different token class and not used here.)

**OAuth2 status:** HackerOne's published Customer API documentation (Getting Started → Authentication) describes **only** HTTP Basic with API tokens. **No `client_credentials`, `authorization_code`, refresh_token flow, or OpenAPI `securitySchemes` definition for OAuth2 was found** in the customer documentation. The integration should use Basic auth as the primary method. If HackerOne later publishes an OAuth2 flow, the CEL input's `auth.oauth2` block can be added.

### 3.2 Endpoints / data paths

The integration polls **`GET /v1/reports`** for incremental collection. `GET /v1/reports/{id}` is included for connectivity testing and not used in the steady-state poll loop.

| Endpoint / Path | Method | Purpose | Event types |
|----------------|--------|---------|-------------|
| `/v1/reports` | GET | List reports for one or more programs / inboxes, with time-range and state filters | All `report` records in scope |
| `/v1/reports/{id}` | GET | Fetch one report with full relationship tree (activities, severity, weakness, etc.) | Single `report` record (used for testing only) |

**Request shape — `GET /v1/reports`:**

- **Required filter (one of):**
  - `filter[program][]` — array of program handles (strings), OR
  - `filter[inbox_ids][]` — array of inbox IDs (integers).
- **Other filters:** rich set covering `state`, `severity`, `assignee`, `reporter`, time bounds (`created_at__gt`/`__lt`, `last_activity_at__gt`/`__lt`, `triaged_at__gt`/`__lt`, plus equivalents for `submitted_at`, `closed_at`, `disclosed_at`, `bounty_awarded_at`, `swag_awarded_at`, `last_reporter_activity_at`, `first_program_activity_at`, `last_program_activity_at`, `last_public_activity_at`), `keyword`, `issue_tracker_reference_id`, `custom_fields[]`, etc. Full table in [`references/api-spec-notes.md` §3](references/api-spec-notes.md).
- **Pagination:** `page[number]` (default 1), `page[size]` (default 25, max 100, min 1).
- **Sort:** comma-separated; prefix `-` for descending. Allowed sort attributes for reports: `reports.created_at`, `reports.last_activity_at`, `reports.last_public_activity_at`, `reports.last_reporter_activity_at`, `reports.first_program_activity_at`, `reports.last_program_activity_at`, `reports.triaged_at`, `reports.closed_at`, `reports.disclosed_at`, `reports.bounty_awarded_at`, `reports.swag_awarded_at`. Note the `reports.` prefix is **required** for this endpoint (do not assume bare `created_at` works as a sort key).

**Enumerations (used in filters):**

- `filter[state][]`: `new`, `pending-program-review`, `triaged`, `needs-more-info`, `resolved`, `not-applicable`, `informative`, `duplicate`, `spam`, `retesting`.
- `filter[severity][]`: `none`, `low`, `medium`, `high`, `critical`.

**Response envelope (documented example):**

```json
{
  "data": [ /* array of report resource objects */ ],
  "links": {
    "self": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=1",
    "next": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=2",
    "last": "https://api.hackerone.com/v1/reports?filter%5Bprogram%5D%5B%5D=security&page%5Bnumber%5D=5"
  }
}
```

The published Get All Reports example does **not** include a top-level `meta` block; `[UNVERIFIED]` whether live responses include `meta.max_page`, `meta.total_hits`, etc.

**Error responses:**

| Code | Meaning |
|------|---------|
| 400 | Bad request — does not conform to endpoint contract |
| 401 | Unauthorized — missing/invalid token (note: the token *identifier* is used as the username, **not** an email) |
| 403 | Forbidden — IP allowlist with valid creds, OR token cannot access the requested program |
| 404 | Not found |
| 406 | Not Acceptable — doc text says triggered by `application/javascript` requests; **likely doc typo for `application/json`** |
| 422 | Unprocessable entity |
| 429 | Too Many Requests (rate limit) |
| 500 / 503 | Server / unavailable |

Body uses a JSON:API `errors` array: `[{ status, title, detail, source: { parameter } }]` ([customer-reference / errors](https://api.hackerone.com/customer-reference/#errors)).

### 3.3 Pagination (API only)

- **Mechanism:** **page-number** pagination — JSON:API `page[number]` + `page[size]` parameters. No cursor / offset / link-header / keyset variant is exposed for `/v1/reports`.
- **Page size parameter:** `page[size]` (default 25, max 100, min 1).
- **Page number parameter:** `page[number]` (1-based, default 1).
- **Next page indicator:** `links.next` in the response body (full URL with query parameters preserved). Pagination metadata in `meta` is not documented for this endpoint.
- **Termination condition:** **Not explicitly documented** in the API reference. Conventional JSON:API behavior is that `links.next` is **absent or null** on the final page; `[UNVERIFIED]` whether HackerOne returns `null` vs omitting the key vs returning a link to a page that yields an empty `data` array. A robust client must check **both** `links.next` presence and the size of `data` (`< page_size` ⇒ last page).
- **Stability under concurrent updates:** **Not documented**. There is no published tie-breaker (e.g. `id`) for sort keys with duplicate values; `[UNVERIFIED]` whether mid-scan inserts/updates can cause skipped or duplicated rows.
- **Documentation:** [Get All Reports](https://api.hackerone.com/customer-resources/#reports-get-all-reports), [JSON:API pagination](https://jsonapi.org/format/#fetching-pagination).

### 3.4 Time-based filtering (API only)

- **Recommended cursor field:** `filter[last_activity_at__gt]` paired with `sort=reports.last_activity_at` (ascending). This captures both new reports and updates to existing ones — `last_activity_at` is documented to update on **any** activity (public or internal) per the [May 10, 2017 changelog](https://api.hackerone.com/getting-started/#changelog).
  - Use `filter[last_activity_at__lt]` only if you need to bound the upper end (e.g., re-running a fixed historical window).
- **Alternative cursor field:** `filter[created_at__gt]` + `sort=reports.created_at` if the integration only cares about **new** reports and not state updates. Less complete.
- **Time format:** ISO 8601 with millisecond precision and `Z` UTC suffix, e.g. `2016-02-02T04:05:06.000Z` (consistent across all datetime attributes per [`#report`](https://api.hackerone.com/customer-reference/#report) "string(date-time) formatted according to ISO 8601").
- **Timezone:** UTC. All documented examples use `Z` suffix.
- **Sort order:** Ascending sort by `reports.last_activity_at` is recommended for cursor-based polling so the highest watermark seen on the current poll becomes the lower bound of the next poll. The default sort order is **not documented** by the endpoint; `sort` is described as configurable. The April 21, 2026 changelog added per-field direction control (e.g. `sort=reports.swag_awarded_at,-reports.bounty_awarded_at`).
- **Boundary semantics:** filter docs say "after"/"before" but do not specify strict (`>`) vs inclusive (`>=`); `[INFERENCE]` typical SQL-style strict greater-than for `__gt`.
- **Incremental collection state to persist between polls:** the **maximum `last_activity_at`** observed across all collected report rows. Use that value (optionally minus a small overlap buffer to cover race conditions) as the next poll's `filter[last_activity_at__gt]`. The CEL builder agent will choose how to encode this in `state.cursor` per its own patterns.

### 3.5 Reference documentation

| Title | URL | Relevance |
|-------|-----|-----------|
| Customer API — Getting Started | https://api.hackerone.com/getting-started/ | Base URL, auth, rate limits, errors, versioning, changelog |
| Customer API — Get All Reports | https://api.hackerone.com/customer-resources/#reports-get-all-reports | `GET /v1/reports` parameter table, sample response, sort enums |
| Customer API — Get Report | https://api.hackerone.com/customer-resources/#reports-get-report | `GET /v1/reports/{id}` (single report with full relationships) |
| Customer Reference — Report object | https://api.hackerone.com/customer-reference/#report | Report attributes + relationships schema |
| Customer Reference — All resource types | https://api.hackerone.com/customer-reference/ | Schemas for `user`, `program`, `weakness`, `severity`, `bounty`, `activity-*` (63 types), etc. |
| Customer API — Webhooks | https://api.hackerone.com/webhooks/ | Alternative collection method (out of scope for v1 integration) |
| HackerOne Help Center — API Tokens | https://docs.hackerone.com/organizations/api-tokens.html | Token creation steps, rotation behavior |
| HackerOne — Splunk Integration (vendor doc) | https://docs.hackerone.com/organizations/splunk-integration.html | Competitive reference + HEC payload sample |
| HackerOne — Sumo Logic Integration (vendor doc) | https://docs.hackerone.com/organizations/sumo-logic-integration.html | Competitive reference + webhook subscription model |
| JSON:API specification | https://jsonapi.org/format/ | General envelope, pagination, sparse fieldsets, includes |

## 4. Data Format and Structure

### 4.1 Format overview

- **Wire format:** JSON, JSON:API-flavored (`{ "data": ..., "links": { ... } }` envelope; `data` items have `id`/`type`/`attributes`/`relationships`).
- **Encoding:** UTF-8.
- **Compression:** None at the application layer (HTTP `Content-Encoding: gzip` may be applied at the transport layer; not part of the response contract).
- **Envelope structure:**
  - **List:** `data` is an **array** of report resources; sibling `links` carries pagination URLs.
  - **Single:** `data` is a single object with the full relationship tree expanded inline (no top-level `included` array in published examples).
- **JSON:API peculiarities:** HackerOne's documented examples expand related resources **inline under `relationships.<rel>.data`** (with nested `attributes`) rather than using the strict JSON:API "linkage object + top-level `included`" pattern. Treat the wire format as **HackerOne's JSON:API profile as shown in docs**, not strict spec compliance. Live responses may diverge; `[UNVERIFIED]`.

### 4.2 Event types

For the `report` data stream, **one report = one event**. Each event represents the current state of a HackerOne report at the time of polling. Updates to an existing report appear as new documents (or replace existing documents — that retention strategy is the integration builder's choice).

The "type" dimension within the data stream is the **report state** (`hackerone.report.state`). All states are emitted by the same data stream; they're discriminated downstream via `event.action` + `event.outcome`.

| State | Description | Relative volume | Priority |
|-----------|-------------|-----------------|----------|
| `new` | Newly submitted, not yet triaged | Medium-high | High (active triage queue) |
| `pending-program-review` | Awaiting program-side review | Medium | Medium |
| `triaged` | Confirmed valid, in remediation | Medium-high | High (work in flight) |
| `needs-more-info` | Triage on hold, waiting for reporter | Low-medium | Medium |
| `resolved` | Vulnerability remediated | High (cumulative) | High (closed-loop reporting) |
| `not-applicable` | Out of scope / not a vulnerability | Medium | Low (housekeeping) |
| `informative` | Useful but not actionable | Low-medium | Low |
| `duplicate` | Same as a previous report | Medium | Low |
| `spam` | Off-topic / abuse | Low | Low |
| `retesting` | Resolved report under retest | Low | Medium |

**Activity sub-events:** Each report carries an `activities` relationship with up to 63 distinct activity types (full catalog in [`references/activity-types-catalog.md`](references/activity-types-catalog.md)). For the v1 `report` data stream the activity timeline is **stored as a flattened sub-array on the report document**, not exploded into separate documents. A future `activity` data stream could expand this if needed.

### 4.3 Field inventory

The HackerOne **`report` object** has **31 documented attributes** plus **18 relationships** (each with its own nested attribute set). Full inventory is in [`references/field-schema-analysis.md`](references/field-schema-analysis.md). Highlights below.

#### Common fields (always present on every report)

| Field path | Type | Description | Example value | Always present? |
|-----------|------|-------------|---------------|-----------------|
| `data.id` | string | Report identifier (numeric, returned as string) | `"1337"` | yes |
| `data.type` | string | JSON:API discriminator | `"report"` | yes |
| `data.attributes.title` | string | Short human-readable summary | `"XSS in login form"` | yes |
| `data.attributes.state` | enum (`report-states`) | Operational state | `"triaged"` | yes |
| `data.attributes.main_state` | enum (`report-main-states`) | Lifecycle bucket: `draft`/`open`/`closed` | `"open"` | yes |
| `data.attributes.created_at` | ISO 8601 datetime | When the report was created | `"2016-02-02T04:05:06.000Z"` | yes |
| `data.relationships.program.data.attributes.handle` | string | Program slug (organization identifier) | `"security"` | yes |

#### Optional / nullable attributes (present when applicable)

| Field path | Type | Description |
|-----------|------|-------------|
| `data.attributes.vulnerability_information` | string | Markdown narrative from the hacker |
| `data.attributes.triaged_at` | datetime\|null | Triage milestone (resets on reopen) |
| `data.attributes.closed_at` | datetime\|null | Closed (resets on reopen) |
| `data.attributes.last_activity_at` | datetime\|null | Aggregate latest activity (public + internal) |
| `data.attributes.last_public_activity_at` | datetime\|null | Latest public-visible activity |
| `data.attributes.last_reporter_activity_at` | datetime\|null | Latest reporter-side activity |
| `data.attributes.last_program_activity_at` | datetime\|null | Latest program-side activity |
| `data.attributes.first_program_activity_at` | datetime\|null | First program-side activity |
| `data.attributes.bounty_awarded_at` | datetime\|null | Most recent bounty award |
| `data.attributes.swag_awarded_at` | datetime\|null | Most recent swag award |
| `data.attributes.disclosed_at` | datetime\|null | Public disclosure (if disclosed) |
| `data.attributes.reporter_agreed_on_going_public_at` | datetime\|null | Disclosure consent marker |
| `data.attributes.issue_tracker_reference_id` | string | External tracker key (e.g. `T7413`) |
| `data.attributes.issue_tracker_reference_url` | string | External tracker URL |
| `data.attributes.cve_ids[]` | string[] | Assigned CVE identifiers |
| `data.attributes.source` | string\|null | Provenance/channel label |
| `data.attributes.original_report_id` | string\|null | Cloned-from report id |
| `data.attributes.hai_is_priority` | boolean\|null | Hai prioritization flag (Enterprise) |
| `data.attributes.hai_is_priority_reason` | string\|null | Hai prioritization rationale |
| `data.attributes.timer_bounty_awarded_miss_at` | datetime\|null | Bounty SLA deadline projection |
| `data.attributes.timer_bounty_awarded_elapsed_time` | int\|null | Elapsed seconds toward bounty SLA |
| `data.attributes.timer_first_program_response_miss_at` | datetime\|null | First-response SLA projection |
| `data.attributes.timer_first_program_response_elapsed_time` | int\|null | Elapsed seconds toward first-response SLA |
| `data.attributes.timer_report_resolved_miss_at` | datetime\|null | Resolution SLA projection |
| `data.attributes.timer_report_resolved_elapsed_time` | int\|null | Elapsed seconds toward resolution SLA |
| `data.attributes.timer_report_triage_miss_at` | datetime\|null | Triage SLA projection |
| `data.attributes.timer_report_triage_elapsed_time` | int\|null | Elapsed seconds toward triage SLA |

#### Key relationship sub-trees

Each relationship returns a nested resource (or array) with its own attribute set. Full schemas in [`references/field-schema-analysis.md`](references/field-schema-analysis.md).

| Relationship | Cardinality | Purpose | Notable fields |
|--------------|-------------|---------|---------------|
| `relationships.program.data` | 1 | Owning program / organization | `attributes.handle`, `id`, `created_at` |
| `relationships.reporter.data` | 1 | The hacker who submitted | `attributes.username`, `name`, `disabled`, optional `reputation`/`signal`/`impact` |
| `relationships.assignee.data` | 0..1 | Routed owner (user OR group) | `type` discriminates `user`/`group`; permissions on group |
| `relationships.collaborators.data[]` | 0..N | Co-reporters with weights | nested `user` + `weight` |
| `relationships.weakness.data` | 0..1 | CWE/CAPEC selection | `attributes.name`, `external_id` (e.g. `cwe-352`) |
| `relationships.structured_scope.data` | 0..1 | In-scope asset under attack | `asset_identifier`, `asset_type`, `eligible_for_bounty`, `max_severity`, CVSS env requirements |
| `relationships.severity.data` | 0..1 | Severity + CVSS metrics | `rating`, `score`, `cvss_vector_string`, `calculation_method` (`manual`/`cvss_3_0_hackerone`/`cvss_3_1`/`cvss_4_0_metric_set`), all CVSS axis fields |
| `relationships.bounties.data[]` | 0..N | Bounty award rows | `amount`, `bonus_amount`, `awarded_amount`, `awarded_currency`, `awarded_bonus_amount` |
| `relationships.swag.data[]` | 0..N | Swag award rows | `sent`, plus nested `user` and `address` |
| `relationships.attachments.data[]` | 0..N | Reporter-uploaded files | `file_name`, `content_type`, `file_size`, `expiring_url` (1-hour signed URL) |
| `relationships.activities.data[]` | 0..N | Timeline (63 types) | base `activity` fields + per-type extras (see catalog) |
| `relationships.summaries.data[]` | 0..N | Researcher / team / triage summaries | `content`, `category`, author user |
| `relationships.custom_field_values.data[]` | 0..N | Customer-defined fields | label + value |
| `relationships.inboxes.data[]` | 0..N | Org inbox memberships | `name`, `type` (`default`/`custom`/`summary`) |
| `relationships.campaign.data` | 0..1 | Bounty multiplier campaign | `campaign_type`, multipliers per severity, dates |
| `relationships.automated_remediation_guidance.data` | 0..1 | CWE article URL | `reference` |
| `relationships.custom_remediation_guidance.data` | 0..1 | Free-text guidance | `message`, author user |
| `relationships.triggered_pre_submission_trigger.data` | 0..1 | Pre-submission warning | `title` |

### 4.4 Sample data

See [`references/sample-events/`](references/sample-events/) for representative payloads:

- `list_reports_response.json` — `GET /v1/reports` list response with two reports (one `new`, one `triaged`) + `links.{self,next,last}`. Sourced verbatim from official documentation; the third placeholder entry `"..."` from the HTML doc was omitted to keep the file valid JSON.
- `single_report_response.json` — `GET /v1/reports/{id}` response with the full relationship tree.
- `report_new.json` — synthesized `new`-state report (`main_state` constructed; otherwise documentation fields).
- `report_triaged.json` — `triaged`-state with severity + weakness + `activity-bug-triaged`.
- `report_resolved_with_bounty.json` — `resolved`-state with bounty + swag + collaborator + abbreviated campaign.

See [`references/field-schema-analysis.md`](references/field-schema-analysis.md) for the complete vendor-side field inventory and [`references/activity-types-catalog.md`](references/activity-types-catalog.md) for the 63 activity discriminators.

#### Inline sample (most representative — single triaged report list row)

```json
{
  "id": "1338",
  "type": "report",
  "attributes": {
    "title": "CSRF in admin panel",
    "state": "triaged",
    "created_at": "2016-02-02T04:05:06.000Z",
    "submitted_at": "2016-02-04T04:05:06.000Z",
    "vulnerability_information": "...",
    "triaged_at": "2016-02-03T03:01:36.000Z",
    "closed_at": null,
    "last_reporter_activity_at": null,
    "first_program_activity_at": null,
    "last_program_activity_at": null,
    "bounty_awarded_at": null,
    "swag_awarded_at": null,
    "disclosed_at": null,
    "issue_tracker_reference_id": "T554",
    "issue_tracker_reference_url": "https://phabricator.tld/T554",
    "cve_ids": []
  },
  "relationships": {
    "reporter": {
      "data": {
        "id": "1337",
        "type": "user",
        "attributes": {
          "username": "api-example",
          "name": "API Example",
          "disabled": false,
          "created_at": "2016-02-02T04:05:06.000Z",
          "profile_picture": {
            "62x62": "/assets/avatars/default.png",
            "82x82": "/assets/avatars/default.png",
            "110x110": "/assets/avatars/default.png",
            "260x260": "/assets/avatars/default.png"
          }
        }
      }
    },
    "program": {
      "data": {
        "id": "1337",
        "type": "program",
        "attributes": {
          "handle": "security",
          "created_at": "2016-02-02T04:05:06.000Z",
          "updated_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "weakness": {
      "data": {
        "id": "1337",
        "type": "weakness",
        "attributes": {
          "name": "Cross-Site Request Forgery (CSRF)",
          "description": "...",
          "external_id": "cwe-352",
          "created_at": "2016-02-02T04:05:06.000Z"
        }
      }
    },
    "bounties": { "data": [] }
  }
}
```

### 4.5 Timestamp handling

- **Primary timestamp field (for `@timestamp`):** `data.attributes.last_activity_at`, with a fallback to `data.attributes.created_at` when null. This aligns the document timestamp with the field used for incremental polling, so each polled document's `@timestamp` is the same value the cursor will advance past.
- **Format:** ISO 8601 with millisecond precision and `Z` UTC suffix (e.g. `2016-02-02T04:05:06.000Z`).
- **Timezone:** UTC (always — `Z` suffix is consistent across all documented samples and is required by the [`#report` reference](https://api.hackerone.com/customer-reference/#report) "string(date-time) formatted according to ISO 8601").
- **Additional timestamps:** `created_at` (event start), `triaged_at`, `closed_at`, `disclosed_at`, `bounty_awarded_at`, `swag_awarded_at`, plus per-stage timer fields. All ISO 8601 UTC.
- **Documentation glitch:** the official Get Report sample contains an invalid string `2020-10-22T011:22:05.402Z` (three-digit hour) for one author's `created_at`. This is preserved verbatim in [`single_report_response.json`](references/sample-events/single_report_response.json); pipelines should be tolerant of malformed timestamps in nested actor fields.

### 4.6 Special parsing considerations

- **Relationships expanded inline.** HackerOne's documented examples nest `attributes` under `relationships.<rel>.data` rather than emitting a top-level `included` array. The pipeline must walk `relationships.*.data[.attributes]` directly and not rely on JSON:API `included` resolution.
- **`assignee.type` discriminator.** The assignee can be either `user` or `group`. The pipeline must branch on `data.relationships.assignee.data.type` to extract the right fields (`username` for users, `name` for groups).
- **`activities` is heterogeneous.** 63 distinct activity types share a base schema (`id`/`type`/`report_id`/`message`/`internal`/`created_at`/`updated_at`) but each adds type-specific fields. The recommended v1 strategy is to store the full `activities` array as a single `flattened` field on the report document and not attempt to map every per-type field. A future `activity` data stream could explode them into separate documents.
- **`weakness.external_id` mixed namespaces.** Values are CWE-style (`cwe-352`) **or** CAPEC-style (`capec-19`). The pipeline should split prefix → namespace and remainder → numeric ID.
- **`bounties[]` numeric strings.** `amount`, `awarded_amount`, etc. are returned as **strings**. Convert to numeric in the pipeline.
- **`expiring_url` on attachments.** Attachment URLs are signed and expire after ~1 hour. Do not retain `expiring_url` long-term; preserve only `file_name`, `content_type`, `file_size`.
- **Doc inconsistency on `#inbox`.** Example JSON uses `message`, attribute table uses `name`/`type`. Prefer the attribute table per the field-schema analysis.
- **`page_size` vs result count.** The list endpoint `data` array MAY have fewer rows than `page_size` even before the last page (documentation does not guarantee otherwise). Pagination termination must check both `links.next` AND `data.length`.

## 5. ECS Mapping Analysis

Full mapping in [`ecs-mapping-analysis.md`](ecs-mapping-analysis.md). Summary below.

### 5.1 Categorization per event type

The HackerOne report is a vulnerability disclosure record — neither an authentication, network, malware, nor process event. Closest ECS category is **`vulnerability`**. All states use the same `event.kind`/`event.category`/`event.type`; differentiation is via `event.action` and `event.outcome`.

| Report state | event.kind | event.category | event.type | event.outcome |
|-----------|------------|----------------|------------|---------------|
| `new` | `event` | `[vulnerability]` | `[info]` | `unknown` |
| `pending-program-review` | `event` | `[vulnerability]` | `[info]` | `unknown` |
| `triaged` | `event` | `[vulnerability]` | `[info]` | `unknown` |
| `needs-more-info` | `event` | `[vulnerability]` | `[info]` | `unknown` |
| `resolved` | `event` | `[vulnerability]` | `[info]` | `success` |
| `not-applicable` | `event` | `[vulnerability]` | `[info]` | `failure` |
| `informative` | `event` | `[vulnerability]` | `[info]` | `unknown` |
| `duplicate` | `event` | `[vulnerability]` | `[info]` | `failure` |
| `spam` | `event` | `[vulnerability]` | `[info]` | `failure` |
| `retesting` | `event` | `[vulnerability]` | `[info]` | `unknown` |

`event.action` = `report-<state>` (kebab-cased). Constant `event.module = hackerone`, `event.dataset = hackerone.report`. `event.outcome` here is **outcome of the disclosure decision**, not technical success/failure.

### 5.2 Field mappings

Selected mappings (full table in [`ecs-mapping-analysis.md`](ecs-mapping-analysis.md)).

| Source field | ECS field | Notes |
|-------------|-----------|-------|
| `data.id` | `event.id` | Stringified integer report id |
| `data.id` | `vulnerability.report_id` | Same value, semantic role |
| `https://hackerone.com/reports/{id}` (constructed) | `event.url`, `vulnerability.reference` | URL prefix configurable for sandbox programs |
| `data.attributes.title` | `message` | Short summary |
| `data.attributes.last_activity_at` (fallback `created_at`) | `@timestamp` | Aligned with cursor field |
| `data.attributes.created_at` | `event.created`, `event.start` | |
| `data.attributes.last_activity_at` | `event.end` | |
| `data.attributes.state` | `hackerone.report.state` | Drives `event.action` and `event.outcome` |
| `data.attributes.vulnerability_information` | `vulnerability.description` | Markdown narrative |
| `data.attributes.cve_ids[0]` | `vulnerability.id` | First CVE if any (full array on `hackerone.report.cve_ids`) |
| `data.relationships.severity.data.attributes.rating` | `vulnerability.severity` | `none`/`low`/`medium`/`high`/`critical` |
| `data.relationships.severity.data.attributes.score` | `vulnerability.score.base` | CVSS base score |
| `data.relationships.severity.data.attributes.calculation_method` | `vulnerability.score.version` | Map `cvss_3_0_hackerone`→`3.0`, `cvss_3_1`→`3.1`, `cvss_4_0_metric_set`→`4.0`, `manual`→unset |
| `data.relationships.weakness.data.attributes.name` | `vulnerability.classification` | E.g. `Cross-Site Request Forgery (CSRF)` |
| `data.relationships.weakness.data.attributes.external_id` | `vulnerability.enumeration` | `CWE` if `cwe-` prefix, `CAPEC` if `capec-` |
| `data.relationships.reporter.data.attributes.username` | `user.name` | Primary actor (the hacker) |
| `data.relationships.reporter.data.attributes.name` | `user.full_name` | May be empty |
| `data.relationships.reporter.data.id` | `user.id` | |
| `data.relationships.program.data.attributes.handle` | `organization.name` | Program slug = canonical org id in HackerOne |
| `data.relationships.program.data.id` | `organization.id` | |
| `data.relationships.structured_scope.data.attributes.asset_identifier` (when `asset_type=url`) | `url.original` | Conditional |
| (constant) `HackerOne` | `observer.vendor`, `observer.product`, `vulnerability.scanner.vendor` | |
| (everything else) | `hackerone.report.*` | ~70 leaf custom fields + 1 flattened activities subtree |

### 5.3 Related field enrichment

| ECS enrichment field | Source fields |
|---------------------|--------------|
| `related.user[]` | `reporter.username`, `assignee.username` (when `assignee.type=user`), `collaborators[].user.username`, `summaries[].user.username`, `custom_remediation_guidance.author.username` |
| `related.hosts[]` | `structured_scope.asset_identifier` when `asset_type ∈ {domain, url}` (extract hostname from URL form) |
| `related.ip[]` | none — HackerOne reports do not carry IP addresses |
| `related.hash[]` | none |

### 5.4 Geo enrichment candidates

**None.** HackerOne reports do not carry IP addresses for the asset under attack, the reporter, or the customer organization. No `*.geo.*` enrichment is appropriate.

## 6. Configuration Plan

Full plan in [`configuration-plan.md`](configuration-plan.md). Summary below.

### 6.1 Required configuration variables

| Variable | Type | Title | Description | Default | Show user |
|----------|------|-------|-------------|---------|-----------|
| `url` | url | API URL | HackerOne API base URL. The integration appends `/v1/reports`. | `https://api.hackerone.com` | yes |
| `api_token_identifier` | text | API token identifier | Identifier portion of the HackerOne API token. Used as the username in HTTP Basic auth. | none | yes |
| `api_token_value` | password | API token value | Secret value of the HackerOne API token. Used as the password in HTTP Basic auth. | none | yes |
| `program_handles` | text (list) | Program handles | One or more HackerOne program handles to collect reports for (e.g. `security`). At least one program handle OR one inbox ID is required by the API. | none | yes |
| `interval` | text | Polling interval | How often to query for new and updated reports. Honor HackerOne's 300 req/min rate limit on report pages. | `5m` | yes |

### 6.2 Optional configuration variables

| Variable | Type | Title | Description | Default | Show user |
|----------|------|-------|-------------|---------|-----------|
| `inbox_ids` | text (list) | Inbox IDs | Alternative scope filter: HackerOne organization inbox IDs. Either `program_handles` or `inbox_ids` must be supplied; both may be combined. | none | yes |
| `initial_interval` | text | Initial lookback | How far back to look on the very first poll. Maps to `filter[last_activity_at__gt] = now - initial_interval`. | `24h` | yes |
| `page_size` | integer | Page size | Reports per page request. API caps at 100. | `100` | yes |
| `state_filter` | text (list) | State filter | Optional list of report states to include. Empty = all. | none | yes |
| `severity_filter` | text (list) | Severity filter | Optional list of severity ratings to include. Empty = all. | none | yes |
| `report_url_prefix` | text | Report URL prefix | Prefix used to construct the public report URL written to `event.url`. | `https://hackerone.com/reports` | no |
| `http_client_timeout` | text | HTTP client timeout | Per-request timeout. | `60s` | no |
| `proxy_url` | url | HTTP proxy URL | HTTP/HTTPS proxy if Elastic Agent must route through one. | none | no |
| `ssl` | yaml | SSL configuration | TLS overrides. HackerOne API uses publicly-trusted certs. | none | no |
| `tags` | text (list) | Tags | User-defined tags appended to events. | `[forwarded, hackerone-report]` | yes |
| `processors` | yaml | Processors | Additional processors. | none | no |
| `preserve_original_event` | bool | Preserve original event | Keep raw JSON:API response on `event.original`. | `false` | yes |
| `preserve_duplicate_custom_fields` | bool | Preserve duplicate custom fields | Keep custom field values under their original case-sensitive labels. | `false` | no |

### 6.3 Deployment notes

- **Network requirements:** Outbound HTTPS (TCP/443) to `api.hackerone.com`. No inbound listening required.
- **Egress IP:** If the HackerOne organization has IP allowlisting enabled on API tokens, the Elastic Agent's egress IP(s) must be in the allowlist or the API returns `403 Forbidden`.
- **Rate limit budget:** 300 reads/min on report pages. With `page_size=100` and `interval=5m`, a single program polled once per 5 minutes uses ≤ 1 request/poll for steady state and ≤ 5–10 requests/poll for backfill — well under the limit. Multiple programs share the same identity-based limit.
- **Token rotation:** HackerOne does not document a token expiry. Operators rotate by creating a new token, updating the integration config, and revoking the old one.
- **Sandbox testing:** A free HackerOne sandbox program (`https://hackerone.com/teams/new/sandbox`) runs on the same `api.hackerone.com` host as production. Use it for end-to-end validation.

## 7. Recommended Integration Architecture

### 7.1 Package name

`hackerone` (lowercase, single word — matches the user request and HackerOne's canonical product name).

### 7.2 Data streams

| Data stream name | Input type | Source | Description |
|-----------------|------------|--------|-------------|
| `report` | `cel` | `GET https://api.hackerone.com/v1/reports` | One document per HackerOne bug bounty report; updates flow as new documents (or replacements depending on retention strategy). |

### 7.3 Architecture rationale

**Single data stream (`report`)** — the `GET /v1/reports` endpoint is the **system of record for the report entity**: it returns the report's full current state plus relationship trees (severity, weakness, scope, bounties, activities up to 63 types, summaries, custom fields, inboxes, campaign). All state transitions are reflected in `state` + `last_activity_at`. Splitting into multiple streams (e.g. one per state, or one per relationship) would force the integration to make multiple API calls per report and lose the natural document-per-report shape.

**Activities not exploded.** The 63 activity types share only a small common schema; per-type fields are heterogeneous. Storing them as a `flattened` sub-array on the parent report keeps mapping simple and avoids a 60+ pipeline branching tree. A future `activity` data stream could be added if dashboards need per-activity-type aggregations — research already enumerates the catalog in [`references/activity-types-catalog.md`](references/activity-types-catalog.md).

**Webhooks not in v1.** Adding a webhook receiver (`http_endpoint` input) would offer near-real-time delivery for the catalog of 31 `report_*` and 2 `program_*` webhook events, but introduces operational burden (public URL, HMAC validation, edition-gated availability) and duplicates state already covered by the API pull. Defer to a v2 enhancement.

### 7.4 Estimated complexity

- **Pipeline complexity:** **Moderate.** Flat root attributes are simple, but 18 relationship sub-trees, ECS `vulnerability.*` mapping, the `weakness.external_id` namespace split, the `assignee.type` user-vs-group branch, the `bounties[]` numeric-string conversion, the `cvss_calculation_method` → `vulnerability.score.version` normalization, and `related.*` aggregation all add work. The activities flattening keeps complexity bounded.
- **CEL complexity:** **Moderate.** Single endpoint, simple Basic auth (no OAuth), straightforward page-number pagination, but cursor state (`last_activity_at`) must be persisted between polls and combined with first-poll `initial_interval` lookback. Multi-program support adds a fan-out (one CEL request loop per program handle).
- **Field count estimate:** ~25 ECS fields populated + ~70 custom `hackerone.report.*` leaf fields + 1 flattened `hackerone.report.activities` subtree. ≈ **95 mapped fields per document** plus the flattened sub-tree.

## 8. Open Questions and Gaps

| # | Question | Impact | Suggested resolution |
|---|----------|--------|---------------------|
| 1 | Pagination termination signal — is `links.next` omitted, returned as `null`, or always present (with empty `data` on overflow)? | Medium — affects loop termination correctness | Validate empirically with `test-api.py` against a real program; the current CEL design handles both `links.next == null` and `data.length < page_size` already |
| 2 | Are `X-RateLimit-*` / `Retry-After` headers actually returned on 200 / 429? | Low (the integration paces itself via `interval` regardless) | Capture from `test-api.py` traces; if present, the CEL builder agent can choose whether to use them |
| 3 | Does HackerOne consider `GET /v1/reports/{id}` part of the "report pages 300 req/min" cap, or is it under the 600 req/min general read limit? | Low | API docs are ambiguous; pace the test endpoint conservatively (≤ 300 req/min) |
| 4 | Stable ordering across pages when many reports share the same `last_activity_at` value | Medium — could cause duplicates / skips at page boundaries | Mitigate by overlapping the cursor by a small buffer (e.g. last cursor minus 1s) and relying on document `_id`-based deduplication in Elasticsearch (CEL builder decision) |
| 5 | Is there a documented OAuth2 flow for organization API access that's not on Getting Started? | Medium — would change auth design if found | Requires HackerOne support / engineering inquiry; absence in public docs is the working assumption |
| 6 | What is the meaning of the on-page blockquote *"ignores filter and returns all reports when feature disabled"* on the Get All Reports page? | Low — informational | Ask HackerOne support if behavior matters for a specific customer |
| 7 | Are the report URLs `https://hackerone.com/reports/{id}` correct for sandbox programs and private programs, or do they use a different prefix? | Low — handled by the configurable `report_url_prefix` | The default works for production public programs; configurable variable allows override |
| 8 | Field-mapping decision: store `hackerone.report.activities` as `flattened` vs `nested` with subset of common fields | Low — affects query patterns, not correctness | Recommended `flattened` for v1; revisit if dashboards need per-activity-type aggregations |

## 9. Source Attribution

| Source | URL | Access method | Date |
|--------|-----|---------------|------|
| HackerOne — Getting Started (auth, rate limits, errors, versioning, changelog) | https://api.hackerone.com/getting-started/ | Web fetch (raw HTML in `temp/api-docs-2026-05-07/getting-started.html`) | 2026-05-07 |
| HackerOne — Customer Resources (Get All Reports, Get Report) | https://api.hackerone.com/customer-resources/ | Web fetch (raw HTML in `temp/customer-reference/customer-resources-fetched.md`) | 2026-05-07 |
| HackerOne — Customer Reference (Report object, all nested resources, 63 activity types) | https://api.hackerone.com/customer-reference/ | Web fetch + structured extraction (raw markdown in `temp/customer-reference/customer-reference-fetched.md`) | 2026-05-07 |
| HackerOne — Webhooks (alternative collection method survey) | https://api.hackerone.com/webhooks/ | Web fetch | 2026-05-07 |
| HackerOne Help Center — API Tokens | https://docs.hackerone.com/organizations/api-tokens.html | Web fetch | 2026-05-07 |
| HackerOne Help Center — Splunk Integration (competitive ref) | https://docs.hackerone.com/organizations/splunk-integration.html | Web fetch | 2026-05-07 |
| HackerOne Help Center — Sumo Logic Integration (competitive ref) | https://docs.hackerone.com/organizations/sumo-logic-integration.html | Web fetch | 2026-05-07 |
| HackerOne Help Center — IBM Security QRadar SOAR (competitive ref) | https://docs.hackerone.com/organizations/ibm-security-soar.html | Web fetch | 2026-05-07 |
| Splunkbase app search | https://splunkbase.splunk.com/apps/#/search/query/hackerone | Web fetch (0 results at retrieval) | 2026-05-07 |
| IBM QRadar SIEM integrations | https://www.ibm.com/products/qradar-siem/integrations | Web fetch (no HackerOne match) | 2026-05-07 |
| Sumo Logic integrations index | https://www.sumologic.com/help/docs/integrations/ | Web fetch (no HackerOne match) | 2026-05-07 |
| HackerOne Swagger Codegen repo | (cloned to `temp/hackerone-swagger-codegen/`) | Git clone via deep-research subagent | 2026-05-07 |
| JSON:API specification | https://jsonapi.org/format/ | Reference (own knowledge + spec) | n/a |
| ECS field reference | https://www.elastic.co/docs/reference/ecs/ecs-field-reference | Reference (own knowledge + skill) | n/a |
