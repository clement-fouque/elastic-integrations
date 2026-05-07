# HackerOne integration — configuration plan

This document captures the configuration variables that the integration's `report` data stream needs to expose to the user, mapped to the standard CEL input variables and the few HackerOne-specific options identified during research.

References:
- [`references/api-spec-notes.md`](./references/api-spec-notes.md) — API contract (auth, filters, pagination, sort)
- [`references/collection-methods-overview.md`](./references/collection-methods-overview.md) — collection method rationale
- `data-collection-methods.md` (skill reference) — standard CEL variables

---

## 1. Recommended input type

**`cel`** — HackerOne exposes a JSON:API REST endpoint (`GET /v1/reports`) with HTTP Basic auth, page-number pagination, time-range filters, and configurable sort. CEL is the standard CEL/REST input in Elastic Agent integrations.

## 2. Required configuration variables

| Variable | Type | Title | Description | Default | Show user |
|----------|------|-------|-------------|---------|-----------|
| `url` | url | API URL | HackerOne API base URL. The integration appends `/v1/reports` (and `/v1/reports/{id}` for tests). | `https://api.hackerone.com` | yes |
| `api_token_identifier` | text | API token identifier | The identifier portion of the HackerOne API token. Generated under Organization Settings → API Tokens. Used as the username in HTTP Basic auth. | none | yes |
| `api_token_value` | password | API token value | The secret value of the HackerOne API token. Used as the password in HTTP Basic auth. Visible only once at creation in the HackerOne UI. | none | yes |
| `program_handles` | text (list) | Program handles | One or more HackerOne program handles to collect reports for (e.g. `security`, `acme-bug-bounty`). At least one program handle OR one inbox ID is required by the API. | none | yes |
| `interval` | text | Polling interval | How often to query the API for new and updated reports. Honor HackerOne's 300 req/min rate limit on report pages. | `5m` | yes |

## 3. Optional configuration variables

| Variable | Type | Title | Description | Default | Show user |
|----------|------|-------|-------------|---------|-----------|
| `inbox_ids` | text (list) | Inbox IDs | Alternative scope filter: HackerOne organization inbox IDs. Either `program_handles` or `inbox_ids` must be supplied; both can be combined. | none | yes |
| `initial_interval` | text | Initial lookback | How far back to look on the very first poll. Maps to `filter[last_activity_at__gt] = now - initial_interval`. | `24h` | yes |
| `page_size` | integer | Page size | Number of reports per page request. The API caps at 100. | `100` | yes |
| `state_filter` | text (list) | State filter | Optional list of report states to include. Allowed values: `new`, `pending-program-review`, `triaged`, `needs-more-info`, `resolved`, `not-applicable`, `informative`, `duplicate`, `spam`, `retesting`. Empty = all states. | none (all) | yes |
| `severity_filter` | text (list) | Severity filter | Optional list of severity ratings to include. Allowed: `none`, `low`, `medium`, `high`, `critical`. Empty = all severities. | none (all) | yes |
| `report_url_prefix` | text | Report URL prefix | Prefix used to construct the public report URL written to `event.url`. | `https://hackerone.com/reports` | no |
| `http_client_timeout` | text | HTTP client timeout | Timeout for individual HTTP requests. | `60s` | no |
| `proxy_url` | url | HTTP proxy URL | HTTP/HTTPS proxy if Elastic Agent must route through one to reach `api.hackerone.com`. | none | no |
| `ssl` | yaml | SSL configuration | TLS configuration overrides (CA bundle, verification mode). HackerOne API uses publicly-trusted certificates. | none | no |
| `tags` | text (list) | Tags | User-defined tags appended to every event. | `[forwarded, hackerone-report]` | yes |
| `processors` | yaml | Processors | Additional Elastic Agent processors. | none | no |
| `preserve_original_event` | bool | Preserve original event | Keep the raw JSON:API response on `event.original`. | `false` | yes |
| `preserve_duplicate_custom_fields` | bool | Preserve duplicate custom fields | If true, also keep custom field values under their original case-sensitive labels. | `false` | no |

## 4. Variable-to-API-parameter mapping

| Config variable | Used in API request | Notes |
|----------------|---------------------|-------|
| `url` | `${url}/v1/reports` | Base URL |
| `api_token_identifier` + `api_token_value` | `Authorization: Basic <b64(id:value)>` | HTTP Basic auth on every request |
| `program_handles` | `filter[program][]=<handle>` | Repeated array param, one per handle |
| `inbox_ids` | `filter[inbox_ids][]=<id>` | Repeated array param, one per id |
| `interval` | (CEL state — not sent to API) | Drives polling cadence |
| `initial_interval` | `filter[last_activity_at__gt]=<now-initial_interval>` (first poll only) | After the first poll, the cursor takes over |
| `page_size` | `page[size]=<n>` | API max 100 |
| `state_filter` | `filter[state][]=<state>` | Repeated array param |
| `severity_filter` | `filter[severity][]=<severity>` | Repeated array param |
| Cursor (CEL state, not user-configurable) | `filter[last_activity_at__gt]=<cursor_value>`, `sort=reports.last_activity_at` | The CEL program persists `last_activity_at` of the most recently seen report between polls |

## 5. Vendor-side prerequisites

To make the integration work, the user must complete these steps on the HackerOne side. The integration UI should link to them.

1. **Confirm API access entitlement.** API token use requires a Professional, Community, or Enterprise edition program; Sandbox programs work for testing. Contact HackerOne sales if no eligible edition exists.
2. **Create an API token.**
   - Sign in as an Organization Administrator.
   - Navigate to **Organization Settings → API Tokens**.
   - Click **Create API Token** and give it a meaningful name.
   - Assign the token to a group with at least the `report_management` permission (read-only access to reports is sufficient).
   - Copy the token **identifier** and **value** — the value is shown only once at creation.
3. **Identify program handles.** Programs are scoped by their slug ("handle"), e.g. `security` for the `https://hackerone.com/security` program. Handles are visible in the HackerOne UI under Engagements.
4. **(Optional) IP allowlisting.** If the organization has enabled IP allowlisting, add the egress IP(s) of the Elastic Agent host to the allowlist; otherwise the API will return `403 Forbidden` even with valid credentials.

## 6. Deployment notes

- **Network requirements:** Outbound HTTPS (TCP/443) to `api.hackerone.com`. No inbound listening required.
- **Egress IP:** If the HackerOne organization has IP allowlisting enabled, the Elastic Agent's egress IP must be in the allowlist.
- **Rate limit budget:** 300 reads/min on report pages. With `page_size=100` and the recommended polling interval of `5m`, a single program polled once per 5 minutes uses ≤ 1 request/poll for steady state and ≤ 5–10 requests/poll for backfill — well under the limit. Multiple programs in the same agent share the same identity-based limit and should not exceed it for typical workloads.
- **Token rotation:** HackerOne does not document a token expiry. Operators rotate by creating a new token, updating the integration config, and revoking the old one. Hacker personal tokens are different — generating a new one revokes the previous; this integration uses organization tokens, not hacker tokens.
- **Sandbox testing:** A free HackerOne sandbox program (`https://hackerone.com/teams/new/sandbox`) runs on the same `api.hackerone.com` host as production. Use it to validate the integration end-to-end before pointing at the production program.

## 7. Configuration questions deferred to the integration builder

These are implementation-level decisions, not research output. They are listed here only so the integration builder doesn't lose track of them:

- Should `program_handles` and `inbox_ids` both be presented in the UI or should one be hidden as "advanced"? (Suggest: both visible because most customers know one but not the other.)
- Should the integration emit a fatal error vs a warning if neither `program_handles` nor `inbox_ids` is set? (The API will reject the call regardless.)
- Should the integration offer a separate "backfill" data stream or rely on `initial_interval` only? (Out of scope for research.)
