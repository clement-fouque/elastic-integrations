# HackerOne Customer API — Report object field inventory

**Sources:** Primary schema from [Customer Reference](https://api.hackerone.com/customer-reference/) (objects `#report`, nested types, `#activity-*`). Request/response motifs from [Customer Resources — Reports](https://api.hackerone.com/customer-resources/) (`GET /reports/{id}`, `GET /reports`).  
**Fetched snapshot (workspace):** `research_results/hackerone/temp/customer-reference/customer-reference-fetched.md`  
**Activity catalog:** Every activity discriminator is documented under [`activity-types-catalog.md`](./activity-types-catalog.md).

## Out of scope (per research brief)

Not inventoried here as standalone program APIs: standalone `asset`/`program`/`organization`/analytics/automation top-level endpoints. Nested objects referenced **from `report`** (e.g. `program`, `weakness`, `structured_scope`, `campaign`) **are included**.

---

## Enumeration reference (explicit in customer-reference)

### `report-main-states` ([link](https://api.hackerone.com/customer-reference#report-main-states))

| Value |
|---|
| `draft` |
| `open` |
| `closed` |

### `report-states` ([link](https://api.hackerone.com/customer-reference#report-states))

| Value |
|---|
| `new` |
| `pending-program-review` |
| `triaged` |
| `needs-more-info` |
| `resolved` |
| `not-applicable` |
| `informative` |
| `duplicate` |
| `spam` |
| `retesting` |

### Severity rating (`severity-ratings`) ([link](https://api.hackerone.com/customer-reference#severity-ratings))

| Value |
|---|
| `none` |
| `low` |
| `medium` |
| `high` |
| `critical` |

### Weakness resource `type`

The JSON:API discriminator for weaknesses is documented as **`weakness`** ([link](https://api.hackerone.com/customer-reference#weakness)). `attributes.external_id` references **CWE or CAPEC** per the `#weakness` description.

### `structured-scope.attributes.asset_type`

The **`#structured-scope`** section defines `asset_type` as **`string`** and does **not** publish an enumerated-values table ([link](https://api.hackerone.com/customer-reference#structured-scope)). Example payloads use tokens such as `URL`/`url`. For related asset-type tokens that HackerOne documents with explicit enumeration when describing **organization/program `asset` records**, see [`#asset` Enumerated Values](https://api.hackerone.com/customer-reference#asset) (`domain`, `url`, `cidr`, `hardware`, `sourceCode`, `iosAppStore`, `iosTestflight`, `iosIpa`, `androidPlayStore`, `androidApk`, `windowsMicrosoftStore`, `executable`, `other`, `smartContract`, `api`, `aiModel`, `awsCloudConfig`, `azureCloudConfig`). **[Interpretation]** overlap with structured scope is plausible but **`#structured-scope` does not re-list that enum verbatim** ([UNVERIFIED] exact parity with program scope identifiers).

---

## Logistics & schema notes

| Topic | Detail |
|---|---|
| **`comments` relationship** | No separate report `relationships.comments` appears in `#report`; discussion content uses `activities[]` (`activity-comment` type) ([`#report`](https://api.hackerone.com/customer-reference#report), [`#activity-comment`](https://api.hackerone.com/customer-reference#activity-comment)). |
| **`submitted_at` on responses** | `GET /reports` documents filters `filter[submitted_at__gt]` / `__lt` ([reports list](https://api.hackerone.com/customer-resources/#reports-get-all-reports)); **`#report` attributes omit `submitted_at`**. |
| **`has_bug_bounty_program`** | Not listed on `#report` attributes — not inventoried here. |
| **`bounty` assigner relationship** | [`#bounty`](https://api.hackerone.com/customer-reference#bounty) documents **attributes only** (no `bounty_assigner`/`awarded_at`/`updated_at` table rows). **`activity-bounty-awarded`** carries program actor plus `bounty_amount`/`bonus_amount` ([activity catalog](./activity-types-catalog.md)). |
| **`swag` monetary fields** | [`#swag`](https://api.hackerone.com/customer-reference#swag): `sent`, `created_at`, `user`, `address` — **no** `amount` / `currency`. |
| **`automations` on report** | `triggered_pre_submission_trigger` → [`trigger`](https://api.hackerone.com/customer-reference#trigger) only per `#report`. |
| **`calculation_method` + CVSS 4.0** | `#severity` Enumerated Values list `manual`, `cvss_3_0_hackerone`, `cvss_3_1`; prose documents `cvss_4_0_metric_set` ([`#severity`](https://api.hackerone.com/customer-reference#severity)). |
| **`#inbox` JSON mismatch** | Example JSON uses `message`; attributes table specifies `type`/`name`. **Prefer the table.** |
| **`custom-field-attribute.helper_text`** | Present in **`#custom-field-value`** example payloads; omitted from summarized attribute table excerpt — **[UNVERIFIED]** as always returned. |

---

## Report (`type: report`)

Base: [`#report`](https://api.hackerone.com/customer-reference#report), last revised **2026-04-14**.

### Resource identity

| Field path | Type | Description | Example value | Always present? | Notes |
|---|---|---|---|---|---|
| `data.id` | string | Report identifier | `"1337"` | yes | String form in documented samples |
| `data.type` | string | JSON:API discriminator | `report` | yes | Literal `report` |

### Attributes (`data.attributes`)

| Field path | Type | Description | Example value | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.title` | string | Title | `"XSS in login form"` | yes | |
| `attributes.vulnerability_information` | string¦null | Raw vuln narrative | `"..."` | optional | Markdown unparsed ([`#report`](https://api.hackerone.com/customer-reference#report)) |
| `attributes.main_state` | `report-main-states` | Lifecycle bucket vs `state` | `"open"` | yes | `#report-main-states` |
| `attributes.state` | `report-states` | Operational state | `"new"` | yes | `#report-states` |
| `attributes.created_at` | string(date-time) | Created | `'2016-02-02T04:05:06.000Z'` | yes | ISO 8601 |
| `attributes.triaged_at` | datetime¦null | Triage milestone | `'2016-02-03T10:00:00.000Z'` / `null` | optional | Resets post-reopen (`#report`) |
| `attributes.closed_at` | datetime¦null | Closed | `'2016-02-10T16:00:00.000Z'` / `null` | optional | Resets post-reopen |
| `attributes.last_reporter_activity_at` | datetime¦null | Reporter-originating activity timestamp | `'2019-08-20T14:26:20.531Z'` | optional | Seen in samples ([customer-resources](https://api.hackerone.com/customer-resources/#reports-get-report)) |
| `attributes.first_program_activity_at` | datetime¦null | First program activity timestamp | `'2019-08-20T14:26:20.531Z'` | optional | |
| `attributes.last_program_activity_at` | datetime¦null | Last program-side activity timestamp | `'2019-08-20T15:25:56.627Z'` | optional | |
| `attributes.last_activity_at` | datetime¦null | Aggregate latest activity timestamp | `'2019-08-20T15:25:56.627Z'` | optional | |
| `attributes.last_public_activity_at` | datetime¦null | Latest public-visible activity timestamp | `'2019-08-20T15:25:56.627Z'` | optional | |
| `attributes.bounty_awarded_at` | datetime¦null | Latest bounty issuance timestamp | `null` until awarded | optional | |
| `attributes.swag_awarded_at` | datetime¦null | Latest swag timestamp | nullable | optional | |
| `attributes.disclosed_at` | datetime¦null | Disclosure clock | nullable | optional | |
| `attributes.reporter_agreed_on_going_public_at` | datetime¦null | Disclosure consent marker | nullable | optional | |
| `attributes.issue_tracker_reference_id` | string | Tracker key | `'T7413'` | optional | |
| `attributes.issue_tracker_reference_url` | string | Tracker hyperlink | `'https://example.com/reference'` | optional | |
| `attributes.cve_ids[]` | string | Assigned CVE identifiers | `[]`, `["CVE-2016-0001"]` | optional | |
| `attributes.source` | string¦null | Provenance/channel label | `'jira'` / `null` | optional | Free-form (`#report`) |
| `attributes.timer_bounty_awarded_miss_at` | datetime¦null | Bounty SLA deadline | nullable | optional | Weekends excluded |
| `attributes.timer_bounty_awarded_elapsed_time` | integer¦null | Elapsed SLA seconds toward bountyAward | nullable | optional | |
| `attributes.timer_first_program_response_miss_at` | datetime¦null | First response SLA breach projection | nullable | optional | Public comment SLA |
| `attributes.timer_first_program_response_elapsed_time` | integer¦null | Seconds toward first-response SLA | nullable | optional | |
| `attributes.timer_report_resolved_miss_at` | datetime¦null | Resolution SLA deadline projection | nullable | optional | Null when reporter blocks |
| `attributes.timer_report_resolved_elapsed_time` | integer¦null | Elapsed resolve SLA seconds | nullable | optional | |
| `attributes.timer_report_triage_miss_at` | datetime¦null | Triage SLA deadline projection | nullable | optional | Null when inactive |
| `attributes.timer_report_triage_elapsed_time` | integer¦null | Elapsed triage SLA seconds | nullable | optional | |
| `attributes.original_report_id` | string¦null | Cloned-from report id | nullable | optional | |
| `attributes.hai_is_priority` | boolean¦null | Prioritization agent flag | nullable | optional | Enterprise feature (`#report`) |
| `attributes.hai_is_priority_reason` | string¦null | Agent rationale snippet | textual / `null` | optional | Complements Hai flag |

**Count — documented leaf attribute keys:** **31**.

### Relationships (`data.relationships`)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `relationships.program.data` | program | Owning bounty/disclosure entity | inlined `program` stub | logically required\* | `\*`Described `#report`; may be omitted only on malformed responses ([UNVERIFIED]) |
| `relationships.assignee.data` | `user` XOR `group` | Routed owner | `user`/`group` object | optional | Discriminators `user`/`group` |
| `relationships.reporter.data` | `user` | Reporter persona | user inline | optional | Adds signal/reputation subset |
| `relationships.collaborators.data[]` | collaborator | Participation weights | collaborators array | optional | [`#collaborator`](https://api.hackerone.com/customer-reference#collaborator) |
| `relationships.attachments.data[]` | attachment[] | Reporter attachments | `[]` | optional | `#attachment` |
| `relationships.swag.data[]` | swag[] | Swag rows | `[...]` | optional | `#swag` |
| `relationships.weakness.data` | weakness | CWE/CAPEC selection | CWE row | optional | `#weakness` |
| `relationships.structured_scope.data` | structured-scope | Structured asset row | structured scope stub | optional | `#structured-scope` |
| `relationships.severity.data` | severity | CVSS-aligned severity blob | `#severity` | optional | `#severity` |
| `relationships.campaign.data` | campaign¦null | Campaign association | `'null'` or campaign | nullable | `#campaign`, April 2026 reference bump |
| `relationships.triggered_pre_submission_trigger.data` | trigger | Pre-submit notice | `#trigger` | optional | Older reports may omit |
| `relationships.activities.data[]` | activity (subtypes) | Timeline | Mixed activities | optional | `./activity-types-catalog.md` (`63`) |
| `relationships.bounties.data[]` | bounty[] | Award history | bounty rows | optional | `#bounty` |
| `relationships.summaries.data[]` | report-summary[] | Summaries (`researcher`/`team`/`triage`) | summarization rows | optional | `#report-summary` |
| `relationships.custom_field_values.data[]` | custom-field-value[] | Enterprise custom fields | KV rows | optional | `#custom-field-value` |
| `relationships.automated_remediation_guidance.data` | automated-remediation-guidance | Automated guidance url | CWE article link | optional | `#automated-remediation-guidance` |
| `relationships.custom_remediation_guidance.data` | custom-remediation-guidance | Human remediation text | remediation row | optional | `#custom-remediation-guidance` |
| `relationships.inboxes.data[]` | inbox[] | Org inbox memberships | `#inbox` rows | optional | Oct 2023 changelog context per reference |

---

## `user`

Source: `#user`, last revised **2025-10-16** ([link](https://api.hackerone.com/customer-reference#user)).

| Field path | Type | Description | Example value | Always present? | Notes |
|---|---|---|---|---|---|
| `id` | string | Account id | `"1337"` | yes | |
| `type` | string | discriminator | `"user"` | yes | |
| `attributes.username` | string | Canonical handle | `'api-example'` | yes | |
| `attributes.name` | string | Display name | `'API Example'` | yes | Empty allowed |
| `attributes.disabled` | boolean | Locked account flag | `false` | yes | |
| `attributes.profile_picture.62x62` | string | thumbnail url | CDN path | yes | Quartet required |
| `attributes.profile_picture.82x82` | string | thumbnail url | CDN path | yes | |
| `attributes.profile_picture.110x110` | string | thumbnail url | CDN path | yes | |
| `attributes.profile_picture.260x260` | string | thumbnail url | CDN path | yes | |
| `attributes.created_at` | datetime | Account created | ISO | yes | |
| `attributes.bio` | string¦null | Biography | text / `null` | optional | |
| `attributes.website` | string¦null | Personal site | url / `null` | optional | |
| `attributes.location` | string¦null | Location text | text / `null` | optional | |
| `attributes.reputation` | number¦null | Reputation points | `7` / `null` | optional | Documented as reporter-only on report |
| `attributes.signal` | number¦null | Signal score | `7` / `null` | optional | reporter-only on report |
| `attributes.impact` | number¦null | Impact score | `30` / `null` | optional | reporter-only on report |
| `attributes.hackerone_triager` | boolean¦null | Triager flag | `false` | optional | |
| `attributes.user_type` | string¦null | Account class | `'hacker'` (example) | optional | **No enum table** in reference |

---

## `group`

[`#group`](https://api.hackerone.com/customer-reference#group)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.name` | string | Group label | `'Admin'` | yes | |
| `attributes.permissions[]` | string | RBAC rows | `'report_management'` | yes | `reward_management`,`program_management`,`user_management` |
| `attributes.created_at` | datetime | Created | ISO | yes | |

---

## `program` / `program_small` (inlined on report)

[`#program_small`](https://api.hackerone.com/customer-reference#program_small)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `id` | string | Program id | `'1337'` | yes | |
| `type` | string | Always `program` | `'program'` | yes | |
| `attributes.handle` | string | Program slug | `'security'` | yes | |
| `attributes.created_at` | datetime | Created | ISO | yes | |
| `attributes.updated_at` | datetime | Updated | ISO | yes | |
| `relationships.groups.data[]` | group[] | *(optional expansion)* | groups | optional | Generally absent on report fetch |
| `relationships.members.data[]` | member[] | *(optional expansion)* | members | optional | Includes nested `user` |
| `relationships.policy_attachments.data[]` | attachment[] | Policy files | attachments | optional | |
| `relationships.custom_field_attributes.data[]` | custom-field-attribute[] | Field schema | definitions | optional | |
| `relationships.transactions.data[]` | transaction[] | Billing rows | ledger | optional | Primarily program endpoint |

### `member` (when expanded)

[`#member`](https://api.hackerone.com/customer-reference#member)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.permissions[]` | string | Member capabilities | permission tokens | yes | |
| `attributes.groups[]` | object | Optional membership groups | nested `group` | optional | |
| `attributes.created_at` | datetime | Joined | ISO | yes | |
| `relationships.user.data` | user | Person | user row | yes | |

---

## `severity`

[`#severity`](https://api.hackerone.com/customer-reference#severity)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.rating` | severity-ratings | Bucket | `'high'` | yes | |
| `attributes.author_type` | string | `User` or `Team` | `'User'` | yes | Enumerated |
| `attributes.user_id` | integer | Authoring user id | `1337` | yes | |
| `attributes.score` | number¦null | CVSS composite | `8.7` | optional | Null for manual |
| `attributes.attack_vector` | string¦null | CVSS vector axis | `'adjacent'` | optional | enumerations in doc |
| `attributes.attack_complexity` | string | CVSS AC | `'low'` | optional | |
| `attributes.privileges_required` | string | CVSS PR | `'low'` | optional | |
| `attributes.user_interaction` | string | CVSS UI | `'required'` | optional | |
| `attributes.scope` | string¦null | CVSS scope | `'changed'` | optional | |
| `attributes.confidentiality` | string | C impact | `'low'` | optional | |
| `attributes.integrity` | string | I impact | `'high'` | optional | |
| `attributes.availability` | string | A impact | `'high'` | optional | |
| `attributes.calculation_method` | string | Calculator provenance | `'cvss_3_1'` | optional | Table omits `cvss_4_0` literal |
| `attributes.cvss_vector_string` | string¦null | Vector string | `'CVSS:3.1/...'` | optional | |
| `attributes.message` | string | Rationale | text | optional | |
| `attributes.cvss_4_0_metric_set` | object | CVSS 4 metrics | nested fields | optional | Subfields enumerated in doc |
| `attributes.created_at` | datetime | Created | ISO | yes | |

---

## `weakness`

[`#weakness`](https://api.hackerone.com/customer-reference#weakness)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.name` | string | Title | `'Cross-Site Request Forgery (CSRF)'` | yes | |
| `attributes.description` | string | Narrative | long text | yes | |
| `attributes.external_id` | string | CWE/CAPEC slug | `'cwe-352'` | yes | |
| `attributes.created_at` | datetime | Created | ISO | yes | |

---

## `structured-scope`

[`#structured-scope`](https://api.hackerone.com/customer-reference#structured-scope)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.asset_identifier` | string | Identifier | `'api.example.com'` | yes | |
| `attributes.asset_type` | string | Category | `'URL'` | yes | **No enum table** on this section |
| `attributes.eligible_for_bounty` | boolean | Bounty eligible | `true` | yes | |
| `attributes.eligible_for_submission` | boolean | Accepts submissions | `true` | yes | |
| `attributes.instruction` | string¦null | Scope notes | text / `null` | optional | |
| `attributes.confidentiality_requirement` | string | CVSS env | `'high'` | optional | `none|low|medium|high` |
| `attributes.integrity_requirement` | string | CVSS env | `'high'` | optional | |
| `attributes.availability_requirement` | string | CVSS env | `'high'` | optional | |
| `attributes.max_severity` | string | Cap | `'critical'` | yes | `none|low|medium|high|critical` |
| `attributes.created_at` | datetime | Created | ISO | yes | |
| `attributes.updated_at` | datetime | Updated | ISO | yes | |
| `attributes.reference` | string¦null | Customer tag | `'H001001'` | optional | |

---

## `bounty`

[`#bounty`](https://api.hackerone.com/customer-reference#bounty)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.amount` | string¦null | USD principal | `'500.00'` | optional | |
| `attributes.bonus_amount` | string¦null | USD bonus | `'50.00'` | optional | |
| `attributes.awarded_amount` | string¦null | Paid-out currency amount | `'415.96'` | optional | |
| `attributes.awarded_bonus_amount` | string¦null | Paid bonus in awarded currency | `'41.60'` | optional | |
| `attributes.awarded_currency` | string¦null | ISO currency | `'EUR'` | optional | |
| `attributes.created_at` | datetime | Row created | ISO | yes | |

---

## `swag`

[`#swag`](https://api.hackerone.com/customer-reference#swag)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.sent` | boolean | Fulfillment flag | `false` | yes | |
| `attributes.created_at` | datetime | Award timestamp | ISO | yes | |
| `relationships.user.data` | user | Recipient | user row | yes | |
| `relationships.address.data` | address | Shipping address | address row | yes | |

### `address`

[`#address`](https://api.hackerone.com/customer-reference#address)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.name` | string | Recipient | `'Jane Doe'` | yes | |
| `attributes.street` | string | Street | `'535 Mission Street'` | yes | |
| `attributes.city` | string | City | `'San Francisco'` | yes | |
| `attributes.postal_code` | string | Postal | `'94105'` | yes | |
| `attributes.state` | string | Region | `'CA'` | yes | |
| `attributes.country` | string | Country | `'United States of America'` | yes | |
| `attributes.tshirt_size` | string¦null | Apparel size enum | `'W_Large'` | optional | Enumerated `M_*`/`W_*` sizes |
| `attributes.phone_number` | string¦null | Phone | `'+1-510-000-0000'` | optional | |
| `attributes.created_at` | datetime | Created | ISO | yes | |

---

## `attachment`

[`#attachment`](https://api.hackerone.com/customer-reference#attachment)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.file_name` | string | Filename | `'root.rb'` | yes | |
| `attributes.content_type` | string | MIME | `'text/x-ruby'` | yes | |
| `attributes.file_size` | integer | Bytes | `2871` | yes | |
| `attributes.expiring_url` | string | Hour-long download URL | path w/ SAS | yes | |
| `attributes.created_at` | datetime | Uploaded | ISO | yes | |

---

## `custom-field-value` + `custom-field-attribute`

[`#custom-field-value`](https://api.hackerone.com/customer-reference#custom-field-value), [`#custom-field-attribute`](https://api.hackerone.com/customer-reference#custom-field-attribute)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `custom-field-value.attributes.value` | string¦null | Stored answer | `'Infrastructure'` | yes | |
| `custom-field-value.attributes.created_at` | datetime | Created | ISO | yes | |
| `custom-field-value.attributes.updated_at` | datetime | Updated | ISO | yes | |
| `custom-field-value.relationships.custom_field_attribute.data` | custom-field-attribute | Schema | definition row | yes | |
| `custom-field-attribute.attributes.label` | string | Label | `'Product Squad'` | yes | |
| `custom-field-attribute.attributes.field_type` | string | Widget type | `'List'` | optional | |
| `custom-field-attribute.attributes.internal` | boolean | Internal-only | `false` | optional | |
| `custom-field-attribute.attributes.required` | boolean | Required flag | `false` | optional | |
| `custom-field-attribute.attributes.regex` | string¦null | Validation | pattern / `null` | optional | |
| `custom-field-attribute.attributes.error_message` | string¦null | Regex failure text | text / `null` | optional | |
| `custom-field-attribute.attributes.checkbox_text` | string¦null | Checkbox copy | text / `null` | optional | |
| `custom-field-attribute.attributes.configuration` | string¦null | Option pack | CSV string | optional | |
| `custom-field-attribute.attributes.created_at` | datetime | Created | ISO | yes | |
| `custom-field-attribute.attributes.updated_at` | datetime | Updated | ISO | yes | |
| `custom-field-attribute.attributes.archived_at` | datetime¦null | Archived | ISO / `null` | optional | |

---

## `automated-remediation-guidance`

[`#automated-remediation-guidance`](https://api.hackerone.com/customer-reference#automated-remediation-guidance)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.reference` | string | Guidance URL | `'https://cwe.mitre.org/...'` | yes | |
| `attributes.created_at` | datetime | Created | ISO | yes | |

---

## `custom-remediation-guidance`

[`#custom-remediation-guidance`](https://api.hackerone.com/customer-reference#custom-remediation-guidance)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.message` | string | Guidance body | long text | yes | |
| `attributes.created_at` | datetime | Created | ISO | yes | |
| `relationships.author.data` | user | Author/editor | user row | yes | |

---

## `inbox`

[`#inbox`](https://api.hackerone.com/customer-reference#inbox)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.type` | string | Inbox class | `'default'` | yes | values `custom`,`default`,`summary` |
| `attributes.name` | string | Label | `'HackerOne'` | yes | |

---

## `campaign`, `campaign_objective`, bounty table stub

[`#campaign`](https://api.hackerone.com/customer-reference#campaign), [`#campaign_objective`](https://api.hackerone.com/customer-reference#campaign_objective)

### `campaign.attributes`

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `campaign_type` | string | Genre | `'multiplier'` | yes | |
| `researchers_information` | string¦null | Hacker-visible notes | textual | optional | |
| `critical`,`high`,`medium`,`low` | number¦null | Multipliers | `2`, `1.5`, ... | optional | |
| `bounty_pool_limit` | integer¦null | Spending cap | `null` | optional | |
| `start_date`,`end_date` | datetime¦null | Window | ISO | optional | |
| `status` | string | Lifecycle | `'scheduled'` | yes | enumerated `scheduled|active|inactive` |
| `target_audience` | boolean¦null | Targeted hackers | `false` | optional | |
| `extended_at` | datetime¦null | Extension marker | ISO / `null` | optional | |
| `total_reports` | integer¦null | Count | `0` | optional | |
| `valid_reports` | integer¦null | Valid subset count | `0` | optional | |
| `total_critical_reports` | integer¦null | Critical bucket | `0` | optional | |
| `total_high_reports` | integer¦null | High bucket | `0` | optional | |
| `bounty_spent` | number¦null | Spent bounty | `0` | optional | |

### `campaign.relationships`

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `campaign_objective.data` | campaign-objective | Campaign narrative | nested row | optional | |
| `structured_scopes.data[]` | structured-scope[] | Scope focus | scopes | optional | |
| `bounty_table_row.data` | bounty-table-row | Reference payout ladder | ints per severity | nullable | enumerated `type` `bounty-table-row` |

### `campaign_objective.attributes`

[`#campaign_objective`](https://api.hackerone.com/customer-reference#campaign_objective)

| Field path | Description | Notes |
|---|---|---|
| `name`,`description`,`category`,`key` | Naming metadata | category nullable |
| `target_audience_description` | Audience copy | nullable |
| `asset_types[]` | Applicable structured asset labels | `[string]` free-form |

### `bounty-table-row.attributes`

| Fields | Meaning |
|---|---|
| `low`,`medium`,`high`,`critical` integers¦null | Baseline payouts |

---

## `collaborator`

[`#collaborator`](https://api.hackerone.com/customer-reference#collaborator)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `weight` | number | Collaboration weight | `1` | yes | |
| `user` | user | Collaborator persona | inlined `user` | yes | Mirrors sample |

---

## `trigger`

[`#trigger`](https://api.hackerone.com/customer-reference#trigger)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.title` | string¦null | Friendly automation name | `'Example Trigger'` | optional | |

---

## `report-summary`

[`#report-summary`](https://api.hackerone.com/customer-reference#report-summary)

| Field path | Type | Description | Example | Always present? | Notes |
|---|---|---|---|---|---|
| `attributes.content` | string | Summary prose | textual | yes | Markdown unparsed |
| `attributes.category` | enum | Originating cohort | `'team'` | yes | `researcher`,`team`,`triage` enumerated |
| `attributes.created_at` | datetime | Authored | ISO | yes | |
| `attributes.updated_at` | datetime | Edited | ISO | yes | |
| `relationships.attachments.data[]` | attachment[] | Appendix files | attachments | optional | sample shows `[]` |
| `relationships.user.data` | user | Author | user row | yes | |

---

## Activity inheritance + catalog

Activities inherit `#activity` base fields then specialize per discriminator. **63** discriminators enumerated in [`activity-types-catalog.md`](./activity-types-catalog.md).

---

## High-value security analytics mappings

| Analytic angle | Canonical JSON paths |
|---|---|
| Severity / CVSS stance | `data.relationships.severity.data.attributes.{rating,score,cvss_vector_string,cvss_4_0_metric_set}` |
| SLA posture | `data.attributes.timer_*` + timeline `activities[]` timestamps |
| Exploit taxonomy | `data.relationships.weakness.data.attributes.external_id` |
| Attack surface | `data.relationships.structured_scope.data.attributes.{asset_type,asset_identifier,max_severity}` |
| Economic impact | `data.relationships.bounties[].attributes.{amount,awarded_amount,awarded_currency}` + optional `campaign` multipliers |

---

## Sample fixtures *(JSON:API-ish)*

| File | Notes |
|---|---|
| [`sample-events/report_new.json`](./sample-events/report_new.json) | `main_state` **constructed** (required per schema but omitted in some examples) |
| [`sample-events/report_triaged.json`](./sample-events/report_triaged.json) | merges severity/weakness + `activity-bug-triaged` doc JSON |
| [`sample-events/report_resolved_with_bounty.json`](./sample-events/report_resolved_with_bounty.json) | combines bounty/swag timelines, collaborator + group shapes, abbreviated campaign |

All include `meta.fixture_notes` tagging constructed versus documentation-extracted payloads.
