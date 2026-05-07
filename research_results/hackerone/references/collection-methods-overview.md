# HackerOne report data — collection methods (Track A reference)

Official sources cited inline. Scope: customer-facing **bug bounty reports** (`reports`) and alternatives for getting that data into a SIEM/logging pipeline.

---

## 1. REST Customer API (`https://api.hackerone.com/v1/`)

- **Overview:** HTTPS JSON API conforming to [JSON:API](https://jsonapi.org/). Version is mandatory in the path (`/v1/...`). See [Getting Started](https://api.hackerone.com/getting-started/).
- **Reports listing:** `GET https://api.hackerone.com/v1/reports` — [Get All Reports](https://api.hackerone.com/customer-resources#reports-get-all-reports).  
  - **Required filter:** either `filter[program][]` (program handles) **or** `filter[inbox_ids][]` must be supplied; otherwise the call is invalid for normal use.
  - **Pagination:** `page[number]`, `page[size]` with size between 1 and 100 (default 25 per [customer-resources](https://api.hackerone.com/customer-resources#reports-get-all-reports)).
  - **Rich filters/sort:** numerous time bounds, state, severity, assignee, custom fields, etc. (same doc section).
- **Single report:** `GET /v1/reports/{id}` (see [customer-resources / reports](https://api.hackerone.com/customer-resources#reports)).
- **Related activity stream (optional complement):** [Query activities](https://api.hackerone.com/customer-resources#activities-query-activities) — useful for fine-grained change history; not a substitute for full report snapshots if the goal is “current report state as document.”
- **Authentication:** HTTP Basic — API token **identifier** as username, token **value** as password ([Getting Started — Authentication](https://api.hackerone.com/getting-started/#authentication)).
- **Rate limits ([Getting Started — Rate Limits](https://api.hackerone.com/getting-started/#rate-limits)):**  
  - Read operations: **600 requests/minute** (exception: **report pages 300 requests/minute**).  
  - Write operations: **25 requests / 20 seconds**.  
  - Separate limit noted in changelog for billing transactions: **10/min** ([changelog in Getting Started](https://api.hackerone.com/getting-started/)).
- **IP allowlisting interaction:** If an IP whitelist is configured for the account and the request originates from a non-allowed IP, the server responds with **403 Forbidden** even with valid credentials ([Getting Started — Authentication](https://api.hackerone.com/getting-started/#authentication)).

---

## 2. Webhooks (program-level, outbound HTTPS POST)

### Availability and administration

- Webhooks subscribe to **report and program** events; each delivery is an **HTTP POST** to a configured URL ([API — Webhooks](https://api.hackerone.com/webhooks)).
- Created at **program** level and bound to the **permissions of the user who creates the webhook** ([API — Webhooks](https://api.hackerone.com/webhooks), [Help Center — Webhooks](https://docs.hackerone.com/organizations/webhooks.html)).
- **UI path:** Engagements → program kebab → **Settings** → **Automation** → **Webhooks** ([Help Center — Webhooks](https://docs.hackerone.com/organizations/webhooks.html)).
- **Edition note:** Help Center states the feature is **not available on all product/platform editions**; details in [Product and Platform Entitlement Overview](https://docs.hackerone.com/en/articles/12975245-hackerone-product-and-platform-entitlement-overview) (article notes login may be required) ([Webhooks help](https://docs.hackerone.com/organizations/webhooks.html)).

### Supported webhook event types (official table)

From [API — Webhooks — Events](https://api.hackerone.com/webhooks/#events):

| Event |
| --- |
| `report_agreed_on_going_public` |
| `report_bounty_awarded` |
| `report_bounty_suggested` |
| `report_closed_as_duplicate` |
| `report_closed_as_informative` |
| `report_closed_as_spam` |
| `report_closed_as_not_applicable` |
| `report_comment_created` |
| `report_comments_closed` |
| `report_created` |
| `report_custom_field_value_updated` |
| `report_needs_more_info` |
| `report_new` |
| `report_prioritised` |
| `report_reopened` |
| `report_resolved` |
| `report_retest_approved` |
| `report_retest_rejected` |
| `report_retest_user_completed` |
| `report_retest_user_expired` |
| `report_retest_user_left` |
| `report_retesting` |
| `report_triaged` |
| `report_group_assigned` |
| `report_manually_disclosed` |
| `report_not_eligible_for_bounty` |
| `report_became_public` |
| `report_undisclosed` |
| `report_swag_awarded` |
| `report_user_assigned` |
| `program_hacker_joined` |
| `program_hacker_left` |

### Payload shape and headers

- JSON body with `data` containing activity/report objects (example in [API — Example delivery](https://api.hackerone.com/webhooks/#example-delivery)).
- Delivery headers ([API — Delivery headers](https://api.hackerone.com/webhooks/#delivery-headers)):

| Header | Purpose |
| --- | --- |
| `X-H1-Event` | Event name that triggered delivery |
| `X-H1-Delivery` | GUID for the delivery |
| `X-H1-Signature` | HMAC SHA256 hex digest of the body (see below) |

### Signature / HMAC verification

- Recommended: configure a **shared secret** in the webhook; `X-H1-Signature` is `sha256=<hexdigest>` where the HMAC key is the secret ([API — Validating payloads](https://api.hackerone.com/webhooks/#validating-payloads-from-hackerone)).
- If **no secret** is configured, the HMAC uses an **empty string** as the key ([same section](https://api.hackerone.com/webhooks/#validating-payloads-from-hackerone)).
- Validation should use a **constant-time** comparison ([examples](https://api.hackerone.com/webhooks/#validating-payloads-from-hackerone)).

### Operational notes (delivery guarantees)

- Help Center mentions **Recent deliveries** UI and **Test request** for debugging ([Webhooks — Managing](https://docs.hackerone.com/organizations/webhooks.html)).
- **Retries, backoff, SLA, ordering:** [UNVERIFIED] — not documented in the reviewed Webhooks API page or Help Center webhook article; assume **at-most-once** style delivery unless HackerOne publishes explicit guarantees elsewhere.

---

## 3. First-party integrations (push to external systems)

These are alternatives for workflow or logging but are **vendor-specific connectors**, not a general-purpose Elastic Agent ingest path.

- **Splunk:** HEC push from **Automation → Integrations**; documentation states integration is **only available to Enterprise programs** ([Splunk Integration](https://docs.hackerone.com/organizations/splunk-integration.html)). Event categories include report submissions, state changes, assignments, comments, disclosures, rewards (same article).
- **Sumo Logic, AWS Security Hub, Microsoft Teams, PagerDuty, ServiceNow collections, Jira, GitHub/GitLab, etc.:** Listed under [Supported Integrations](https://docs.hackerone.com/organizations/supported-integrations.html). Edition availability varies ([entitlement overview](https://docs.hackerone.com/en/articles/12975245-hackerone-product-and-platform-entitlement-overview) cited there).
- **Slack:** [New Slack Integration](https://docs.hackerone.com/en/articles/12598847-new-slack-integration) (linked from supported integrations catalog).
- **Automations:** Organization-level automation and event→activity mapping is documented under [Automation Security & Event Mapping](https://docs.hackerone.com/en/articles/9653488-automation-security-event-mapping); relevant for understanding which platform activities fan out to automations/webhooks—not a separate export channel by itself.

---

## 4. Why REST polling is the primary fit for Elastic Agent (conceptual)

- Provides **authenticated, stable JSON** contracts for `/v1/reports` and `/v1/reports/{id}` ([customer-resources](https://api.hackerone.com/customer-resources#reports-get-all-reports)).
- Enables **historical backfill** and reconciliation (webhooks are event-driven only and omit quiet periods).
- No requirement for customers to expose a **public ingestion URL** on their side (webhooks/Splunk HEC inverted model).
- A polling integration naturally respects published **rate limits** via interval and page size ([rate limits](https://api.hackerone.com/getting-started/#rate-limits)).

Using the **CEL input** in Elastic Agent to perform periodic HTTPS GETs with Basic auth is consistent with how other API integrations are built in this repo; implementation details are out of scope for this research note.

---

## 5. Attachments and binary content

- Report and comment flows have **upload** endpoints (e.g. `POST /reports/attachments`, `POST /reports/{report_id}/attachments`) per [customer-resources](https://api.hackerone.com/customer-resources/#reports-upload-attachments) (see changelog/history in [Getting Started](https://api.hackerone.com/getting-started/)).
- Payloads may include `expiring_url` on attachment objects (example in [Splunk integration sample event](https://docs.hackerone.com/organizations/splunk-integration.html)).
- **Permanent deletion of attachments:** Changelog entry documents `DELETE` capability for attachments on a report ([July 25, 2024 changelog](https://api.hackerone.com/getting-started/)) — relevant for long-term SIEM retention vs. live platform.

---

## 6. Sandbox and testing

- **API sandbox program:** [Getting Started — API sandbox](https://api.hackerone.com/getting-started/#api-sandbox) links to `https://hackerone.com/teams/new/sandbox`; states users can pick an edition and get access to almost all platform features for testing.

---

## Document history

- Track A research snapshot: 2026-05-07. Primary URLs: [api.hackerone.com/getting-started](https://api.hackerone.com/getting-started/), [api.hackerone.com/webhooks](https://api.hackerone.com/webhooks), [api.hackerone.com/customer-resources](https://api.hackerone.com/customer-resources), [docs.hackerone.com](https://docs.hackerone.com/).
