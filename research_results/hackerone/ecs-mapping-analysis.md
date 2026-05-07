# HackerOne `report` — ECS mapping analysis

This document maps fields from the HackerOne `GET /v1/reports` JSON:API response to ECS fields, identifies fields that should live under the integration's custom `hackerone.*` namespace, and proposes `event.*` categorization.

The single data stream covered here is `report` (one document per HackerOne report). A "report" event carries the current state of a HackerOne bug bounty report at the time of polling; updates produce new documents (or replace old ones depending on retention strategy — out of scope for research).

References:
- [`references/api-spec-notes.md`](./references/api-spec-notes.md) — request/response contract
- [`references/field-schema-analysis.md`](./references/field-schema-analysis.md) — full vendor-side field inventory (31 attributes + 18 relationships)
- ECS field reference: <https://www.elastic.co/docs/reference/ecs/ecs-field-reference>

---

## 1. Categorization (event.*)

The HackerOne `report` is a record of a vulnerability disclosure submitted by a hacker to a customer program. It is not an authentication, network, malware, or process event. The closest ECS category is **`vulnerability`**.

| Report state | event.kind | event.category | event.type | event.outcome | event.action |
|--------------|-----------|----------------|-----------|---------------|--------------|
| `new` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-new` |
| `pending-program-review` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-pending-program-review` |
| `triaged` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-triaged` |
| `needs-more-info` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-needs-more-info` |
| `resolved` | `event` | `[vulnerability]` | `[info]` | `success` | `report-resolved` |
| `not-applicable` | `event` | `[vulnerability]` | `[info]` | `failure` | `report-not-applicable` |
| `informative` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-informative` |
| `duplicate` | `event` | `[vulnerability]` | `[info]` | `failure` | `report-duplicate` |
| `spam` | `event` | `[vulnerability]` | `[info]` | `failure` | `report-spam` |
| `retesting` | `event` | `[vulnerability]` | `[info]` | `unknown` | `report-retesting` |

Notes:
- `event.outcome` semantics here mean "outcome of the disclosure decision," not technical success/failure.
- `event.action` uses kebab-case derived from the state.
- `event.dataset` is the constant `hackerone.report`; `event.module` is the constant `hackerone`.

## 2. Timestamp mapping

| Source field | ECS field | Notes |
|--------------|-----------|-------|
| `data.attributes.last_activity_at` (fallback `created_at`) | `@timestamp` | Aligns with the documented incremental polling cursor (`filter[last_activity_at__gt]`). When `last_activity_at` is null, fall back to `created_at`. |
| `data.attributes.created_at` | `event.created` | When the report was first created on HackerOne. |
| `data.attributes.last_activity_at` | (alias) `event.end` | Optional. The most recent activity boundary. |
| `data.attributes.created_at` | (alias) `event.start` | Optional. Beginning of the report's lifecycle. |

Source format is ISO 8601 with millisecond precision and `Z` suffix (e.g., `2016-02-02T04:05:06.000Z`) per the docs.

## 3. Field mappings to ECS

### Report identity and URL

| Source field | ECS field | Notes |
|--------------|-----------|-------|
| `data.id` | `event.id` | Stringified integer report id. |
| `data.id` | `vulnerability.report_id` | Same value, semantic role. |
| (constructed) `https://hackerone.com/reports/{id}` | `event.url` | Pipeline constructs from `data.id`. |
| (constructed) `https://hackerone.com/reports/{id}` | `vulnerability.reference` | Same URL, vulnerability semantic. |
| `data.attributes.title` | `message` | Short human-readable summary. |

### Vulnerability fields

| Source field | ECS field | Notes |
|--------------|-----------|-------|
| `data.relationships.severity.data.attributes.rating` | `vulnerability.severity` | Values: `none`, `low`, `medium`, `high`, `critical`. ECS expects free-text but these match common SIEM conventions. |
| `data.relationships.severity.data.attributes.score` | `vulnerability.score.base` | CVSS base score (numeric). |
| `data.relationships.severity.data.attributes.calculation_method` | `vulnerability.score.version` | Map `cvss_3_0_hackerone` → `3.0`, `cvss_3_1` → `3.1`, `cvss_4_0` → `4.0`, `manual` → leave unset. |
| `data.relationships.weakness.data.attributes.name` | `vulnerability.classification` | E.g. `Cross-Site Request Forgery (CSRF)`. |
| `data.relationships.weakness.data.attributes.external_id` | `vulnerability.enumeration` | When prefixed `cwe-` set value to `CWE` (and store the raw id under `hackerone.report.weakness.external_id`). When prefixed `capec-` set value to `CAPEC`. |
| `data.attributes.cve_ids[0]` | `vulnerability.id` | The first assigned CVE (if any). When no CVE is assigned, leave `vulnerability.id` unset (HackerOne report id is already in `vulnerability.report_id`). |
| `data.attributes.vulnerability_information` | `vulnerability.description` | Markdown narrative from the hacker. |
| `data.attributes.cve_ids[]` | `hackerone.report.cve_ids` | Full array preserved on the vendor namespace. |
| (constant) `HackerOne` | `vulnerability.scanner.vendor` | Constant. |

### Reporter, assignee, and program (actors)

| Source field | ECS field | Notes |
|--------------|-----------|-------|
| `data.relationships.reporter.data.attributes.username` | `user.name` | Primary actor: the reporter. |
| `data.relationships.reporter.data.id` | `user.id` | |
| `data.relationships.reporter.data.attributes.name` | `user.full_name` | May be empty. |
| `data.relationships.reporter.data.attributes.username` (alias) | `related.user[]` | Always added. |
| `data.relationships.assignee.data.attributes.username` (when type=user) | `hackerone.report.assignee.username` | Vendor namespace; assignee is sometimes a group. |
| `data.relationships.assignee.data.attributes.name` (when type=group) | `hackerone.report.assignee.group_name` | Group label. |
| `data.relationships.assignee.data.type` | `hackerone.report.assignee.type` | `user` or `group`. |
| `data.relationships.collaborators.data[].user.attributes.username` | `related.user[]` | Appended. |
| `data.relationships.program.data.attributes.handle` | `organization.name` | The program handle is the canonical organization-level identifier in HackerOne. |
| `data.relationships.program.data.id` | `organization.id` | |

### State, lifecycle, and SLA timers (vendor namespace)

The HackerOne report carries 31 documented attributes, most of them lifecycle timestamps. Map the analytic-most-relevant ones to ECS where possible; preserve the rest under `hackerone.report.*`.

| Source field | Target field | Notes |
|--------------|--------------|-------|
| `data.attributes.state` | `hackerone.report.state` | Also drives `event.action` and `event.outcome`. |
| `data.attributes.main_state` | `hackerone.report.main_state` | `draft`/`open`/`closed`. |
| `data.attributes.title` | `hackerone.report.title` | Also mapped to `message`. |
| `data.attributes.vulnerability_information` | `hackerone.report.vulnerability_information` | Also mapped to `vulnerability.description`. |
| `data.attributes.source` | `hackerone.report.source` | Free-form provenance label. |
| `data.attributes.triaged_at` | `hackerone.report.triaged_at` | Date. |
| `data.attributes.closed_at` | `hackerone.report.closed_at` | Date. |
| `data.attributes.last_reporter_activity_at` | `hackerone.report.last_reporter_activity_at` | Date. |
| `data.attributes.first_program_activity_at` | `hackerone.report.first_program_activity_at` | Date. |
| `data.attributes.last_program_activity_at` | `hackerone.report.last_program_activity_at` | Date. |
| `data.attributes.last_public_activity_at` | `hackerone.report.last_public_activity_at` | Date. |
| `data.attributes.bounty_awarded_at` | `hackerone.report.bounty_awarded_at` | Date. |
| `data.attributes.swag_awarded_at` | `hackerone.report.swag_awarded_at` | Date. |
| `data.attributes.disclosed_at` | `hackerone.report.disclosed_at` | Date. |
| `data.attributes.reporter_agreed_on_going_public_at` | `hackerone.report.reporter_agreed_on_going_public_at` | Date. |
| `data.attributes.issue_tracker_reference_id` | `hackerone.report.issue_tracker_reference_id` | Keyword. |
| `data.attributes.issue_tracker_reference_url` | `hackerone.report.issue_tracker_reference_url` | Keyword (URL). |
| `data.attributes.original_report_id` | `hackerone.report.original_report_id` | Keyword (cloned-from). |
| `data.attributes.hai_is_priority` | `hackerone.report.hai.is_priority` | Boolean. |
| `data.attributes.hai_is_priority_reason` | `hackerone.report.hai.is_priority_reason` | Keyword. |
| `data.attributes.timer_*_miss_at` (×4) | `hackerone.report.timer.<name>.miss_at` | Date. |
| `data.attributes.timer_*_elapsed_time` (×4) | `hackerone.report.timer.<name>.elapsed_time_seconds` | Long. Source is documented as integer seconds. |

### Severity (vendor namespace, additional fields)

Whatever doesn't fit cleanly into ECS `vulnerability.score.*` lives under `hackerone.report.severity.*`:

| Source field | Target field |
|--------------|--------------|
| `severity.attributes.cvss_vector_string` | `hackerone.report.severity.cvss_vector_string` |
| `severity.attributes.author_type` | `hackerone.report.severity.author_type` |
| `severity.attributes.user_id` | `hackerone.report.severity.user_id` |
| `severity.attributes.attack_vector` | `hackerone.report.severity.attack_vector` |
| `severity.attributes.attack_complexity` | `hackerone.report.severity.attack_complexity` |
| `severity.attributes.privileges_required` | `hackerone.report.severity.privileges_required` |
| `severity.attributes.user_interaction` | `hackerone.report.severity.user_interaction` |
| `severity.attributes.scope` | `hackerone.report.severity.scope` |
| `severity.attributes.confidentiality` | `hackerone.report.severity.confidentiality` |
| `severity.attributes.integrity` | `hackerone.report.severity.integrity` |
| `severity.attributes.availability` | `hackerone.report.severity.availability` |
| `severity.attributes.calculation_method` | `hackerone.report.severity.calculation_method` |
| `severity.attributes.cvss_4_0_metric_set` | `hackerone.report.severity.cvss_4_0` (group of keyword fields) |

### Structured scope (asset under attack)

The structured scope identifies the in-scope asset the report targets. HackerOne `asset_type` values are vendor-specific (`url`, `domain`, `cidr`, `iosAppStore`, etc.) and don't map cleanly to a single ECS field.

| Source field | Target field | Notes |
|--------------|--------------|-------|
| `structured_scope.attributes.asset_identifier` | `hackerone.report.scope.asset_identifier` | Keep on vendor namespace. |
| `structured_scope.attributes.asset_type` | `hackerone.report.scope.asset_type` | Vendor-specific enum. |
| `structured_scope.attributes.asset_identifier` | `url.original` | Only when `asset_type` is `url`. |
| `structured_scope.attributes.max_severity` | `hackerone.report.scope.max_severity` | |
| `structured_scope.attributes.eligible_for_bounty` | `hackerone.report.scope.eligible_for_bounty` | Boolean. |
| `structured_scope.attributes.eligible_for_submission` | `hackerone.report.scope.eligible_for_submission` | Boolean. |
| `structured_scope.attributes.confidentiality_requirement` | `hackerone.report.scope.confidentiality_requirement` | |
| `structured_scope.attributes.integrity_requirement` | `hackerone.report.scope.integrity_requirement` | |
| `structured_scope.attributes.availability_requirement` | `hackerone.report.scope.availability_requirement` | |
| `structured_scope.attributes.reference` | `hackerone.report.scope.reference` | Customer's tag. |

### Bounty and swag (economic impact)

Reports can have multiple bounties (initial + bonus + program-side adjustments) attached. Preserve the array under the vendor namespace.

| Source field | Target field | Notes |
|--------------|--------------|-------|
| `bounties.data[].attributes.amount` | `hackerone.report.bounties[].amount` | Numeric (USD principal) — convert from string. |
| `bounties.data[].attributes.bonus_amount` | `hackerone.report.bounties[].bonus_amount` | Numeric — convert from string. |
| `bounties.data[].attributes.awarded_amount` | `hackerone.report.bounties[].awarded_amount` | Numeric in awarded currency. |
| `bounties.data[].attributes.awarded_bonus_amount` | `hackerone.report.bounties[].awarded_bonus_amount` | Numeric. |
| `bounties.data[].attributes.awarded_currency` | `hackerone.report.bounties[].awarded_currency` | ISO 4217 code. |
| `bounties.data[].attributes.created_at` | `hackerone.report.bounties[].created_at` | Date. |
| (computed) sum of `amount` + `bonus_amount` over bounties | `hackerone.report.bounty.total_amount` | Convenience aggregation in USD. |
| `swag.data[].attributes.sent` | `hackerone.report.swag[].sent` | Boolean. |
| `swag.data[].attributes.created_at` | `hackerone.report.swag[].created_at` | Date. |

### Activities (timeline)

The `activities` relationship carries the report's timeline (60+ activity types). For the `report` data stream, we preserve the activities array under the vendor namespace as flattened metadata; we do NOT explode each activity into a separate document. (A future `activity` data stream could do that.)

| Source field | Target field |
|--------------|--------------|
| `activities.data[].type` | `hackerone.report.activities[].type` |
| `activities.data[].id` | `hackerone.report.activities[].id` |
| `activities.data[].attributes.created_at` | `hackerone.report.activities[].created_at` |
| `activities.data[].attributes.updated_at` | `hackerone.report.activities[].updated_at` |
| `activities.data[].attributes.internal` | `hackerone.report.activities[].internal` |
| `activities.data[].attributes.message` | `hackerone.report.activities[].message` |
| (per-type extra fields, varying) | `hackerone.report.activities[].<type-specific>` (stored as `flattened`) |

A pragmatic approach: store the full activities array as a single `flattened` field (`hackerone.report.activities`) to avoid mapping explosion across 60+ activity types with heterogeneous fields. Document this in the field file.

### Other vendor-namespace fields

- `data.relationships.attachments.data[]` → `hackerone.report.attachments[]` (file_name, content_type, file_size; do NOT preserve `expiring_url` long-term — it expires after 1 hour).
- `data.relationships.summaries.data[]` → `hackerone.report.summaries[]` (researcher/team/triage notes).
- `data.relationships.custom_field_values.data[]` → `hackerone.report.custom_fields[]` (label + value pairs).
- `data.relationships.inboxes.data[]` → `hackerone.report.inboxes[]` (inbox name + type).
- `data.relationships.campaign.data` → `hackerone.report.campaign` (when present; bounty multiplier campaign metadata).
- `data.relationships.automated_remediation_guidance.data` → `hackerone.report.remediation.automated.reference` (URL).
- `data.relationships.custom_remediation_guidance.data` → `hackerone.report.remediation.custom.message` (free text).

## 4. Related field enrichment

| ECS enrichment field | Source fields |
|---------------------|--------------|
| `related.user[]` | `reporter.username`, `assignee.username` (when assignee.type=user), `collaborators[].user.username`, `summaries[].user.username`, `custom_remediation_guidance.author.username` |
| `related.hosts[]` | `structured_scope.asset_identifier` when `asset_type` ∈ `{domain, url}` (extract hostname from URL form) |
| `related.ip[]` | none (HackerOne reports don't carry IPs directly) |
| `related.hash[]` | none |

## 5. Geo enrichment candidates

None. HackerOne reports do not carry IP addresses for the asset under attack, the reporter, or the customer organization. No `*.geo.*` enrichment is appropriate.

## 6. Constants

| ECS field | Constant value |
|-----------|---------------|
| `observer.vendor` | `HackerOne` |
| `observer.product` | `HackerOne` |
| `event.module` | `hackerone` |
| `event.dataset` | `hackerone.report` |
| `vulnerability.scanner.vendor` | `HackerOne` |

## 7. Field count summary

| Layer | Approximate field count |
|-------|------------------------|
| ECS fields populated | ~25 (event.*, vulnerability.*, user.*, organization.*, observer.*, related.*, message, @timestamp, url.*) |
| Custom `hackerone.report.*` keyword/date/numeric leaf fields | ~70 |
| `hackerone.report.activities` (flattened) | 1 (subtree, no per-key mapping) |
| Total per document | ~95 mapped + 1 flattened subtree |

## 8. Open mapping questions

1. **Activities flattening vs. structured nesting.** Storing the activities array as `flattened` keeps mapping cost flat across 60+ activity types but loses the ability to query specific activity attributes via `keyword` aggregations. An alternative is `nested` with a strict subset of common fields (`type`, `created_at`, `internal`, `message`). Recommend `flattened` for v1; revisit if dashboards need per-activity-type aggregations.
2. **`event.url` construction.** HackerOne does not return the report URL in the API response; the standard URL is `https://hackerone.com/reports/{id}`. This is a stable convention for production but unusable for sandbox programs. Consider making the URL prefix configurable via `report_url_prefix` (default `https://hackerone.com/reports`).
3. **Severity score version mapping.** `calculation_method` includes `manual` (no CVSS version) and `cvss_3_0_hackerone` (HackerOne-specific scoring profile, not standard CVSS 3.0). The mapping in section 3 is best-effort; some operators may want the raw `calculation_method` value preserved as `vulnerability.score.version` instead of normalized.
4. **Bounty currency.** HackerOne returns separate `amount`/`awarded_amount` (string-typed numeric values) and `awarded_currency` (ISO 4217). Operators in non-USD programs may want `bounty.total_amount` computed in their preferred currency rather than USD. Out of scope for the integration's default mapping.
