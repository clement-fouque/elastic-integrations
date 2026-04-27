{{- generatedHeader }}
# HackerOne Integration for Elastic

## Overview

The HackerOne integration collects bug bounty and vulnerability disclosure reports from the [HackerOne Customer API](https://api.hackerone.com/customer-resources/) into Elasticsearch. It enables security teams to centralize HackerOne report data alongside other security telemetry, build operational dashboards (open vs. resolved reports, mean time to triage and resolution, severity distribution), correlate disclosed assets with internal asset inventories, and trigger alerts when new high or critical reports are filed.

### Compatibility

This integration is compatible with the HackerOne Customer API v1 (`https://api.hackerone.com/v1`). It targets Elastic customer programs that use HackerOne's Bug Bounty, Vulnerability Disclosure (VDP), or Pentest products and have access to the Customer API.

### How it works

The integration polls the `GET /v1/reports` endpoint of the HackerOne Customer API on a configurable schedule using the Elastic Agent CEL input. Each polling cycle uses HTTP Basic authentication, the JSON:API page-based pagination via the server-supplied `links.next` URL, and an incremental cursor (`filter[last_activity_at__gt]` plus `sort=reports.last_activity_at`) so subsequent intervals only collect reports updated since the previous run.

## What data does this integration collect?

The HackerOne integration collects the following data:

* **report** — Bug bounty and vulnerability disclosure reports including title, state (`new`, `triaged`, `needs-more-info`, `resolved`, `duplicate`, `informative`, `not-applicable`, `spam`), severity (CVSS v3 score and rating), submitter and assignee details, weakness/CWE classification, structured scope (asset identifier and type), bounty totals, SLA timers, and lifecycle timestamps.

### Supported use cases

* **SIEM and security operations**: bring HackerOne reports into the same store as alerts, audit logs, and detections.
* **Operational metrics**: track mean time to triage, mean time to resolution, open report backlog, and severity distribution.
* **Asset correlation**: join HackerOne reports against internal asset inventories using `structured_scope` identifiers.
* **Alerting**: trigger detections on newly filed `high` or `critical` reports, on SLA breaches, or on reports filed against critical scopes.

## What do I need to use this integration?

Before installing, you need:

* A HackerOne customer program with API access enabled.
* A HackerOne API token (identifier and secret). The identifier is used as the HTTP Basic username and the secret as the password. See [Authentication](https://api.hackerone.com/customer-resources/#authentication) in HackerOne's documentation.
* The handle of at least one program (for example `acme`) or one or more inbox IDs to scope collection. The Customer API requires that `GET /v1/reports` be filtered by `program` or `inbox_ids`.

## How do I deploy this integration?

### Agent-based deployment

Elastic Agent must be installed. For more details, check the Elastic Agent [installation instructions](docs-content://reference/fleet/install-elastic-agents.md). You can install only one Elastic Agent per host.

### Onboard / configure

1. In HackerOne, create an API token under **Settings → Program → API tokens**. Save the identifier and secret — the secret is shown only once.
2. In Kibana, install the HackerOne integration and configure the policy with the API token identifier, API token secret, and at least one program handle.
3. Optionally adjust the polling interval, the initial backfill window, and the page size (1–100, default 100).
4. Save the policy and verify that documents are flowing into the `logs-hackerone.report-*` data stream.

### Validation

Confirm the integration is working by querying the data stream in Discover:

```
data_stream.dataset: hackerone.report
```

A first poll backfills reports updated since the configured initial interval and subsequent polls collect only reports updated since the previous run.

## Troubleshooting

For help with Elastic ingest tools, check [Common problems](https://www.elastic.co/docs/troubleshoot/ingest/fleet/common-problems).

Common HackerOne-specific issues:

* **`401 Unauthorized`**: the API token identifier or secret is incorrect, or the token has been revoked. Regenerate the token in HackerOne and update the policy.
* **`403 Forbidden`**: the token lacks the required role for the configured program. Confirm the user that owns the token has access to the program.
* **`429 Too Many Requests`**: the program has exceeded the HackerOne rate limit (600 read requests per minute globally). Increase the polling interval or reduce the number of programs scoped per agent.
* **No reports collected**: confirm at least one program handle is configured and that the configured program has reports updated since the cursor.

## Scaling

For more information on architectures that can be used for scaling this integration, check the [Ingest Architectures](https://www.elastic.co/docs/manage-data/ingest/ingest-reference-architectures) documentation.

A single Elastic Agent can comfortably handle the per-token rate limit. For very large programs, consider distributing programs across multiple integration policies on different hosts to spread the API load.

## Reference

### report

The `report` data stream provides bug bounty and vulnerability disclosure reports from the HackerOne Customer API.

#### report fields

{{ fields "report" }}

{{ ilm }}

{{ transform }}

### Inputs used
{{ inputDocs }}

### API usage

This integration uses the HackerOne Customer API:

* [`GET /v1/reports`](https://api.hackerone.com/customer-resources/#reports-get-all-reports) — list reports, filtered and paginated.
