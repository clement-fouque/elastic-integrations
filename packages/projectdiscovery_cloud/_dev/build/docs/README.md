{{- generatedHeader }}
# ProjectDiscovery Cloud Integration for Elastic

## Overview

The ProjectDiscovery Cloud integration brings vulnerability scan results from the [ProjectDiscovery Cloud Platform](https://cloud.projectdiscovery.io) (PDCP) into Elastic Security. Use it to correlate Nuclei template matches against your external, internal, and cloud assets with the rest of your security telemetry.

The integration polls PDCP on a schedule you choose and fetches the full vulnerability scan snapshot for the configured time window. Each poll produces an authoritative snapshot — the same finding observed across multiple polls is stored as a separate document per poll, which gives you a per-day view of the vulnerability state for trend analysis.

### Compatibility

This integration works with the [ProjectDiscovery Cloud Platform API](https://docs.projectdiscovery.io/api-reference/introduction) (`v1`). You need a PDCP account and an API key with access to the team workspace whose findings you want to collect.

### How it works

On each scheduled run, the integration:

1. Connects to the PDCP API using your API key and team identifier.
2. Issues a single bulk export request (`POST /v1/scans/results/export?async=false&type=json`) filtered by the configured time window, severity, and vulnerability status.
3. Sends each returned finding to Elasticsearch for search, dashboards, and alerting.

The integration does not maintain a cursor between polls — each request returns the full filtered snapshot for the configured time window. This is by design: the snapshot model makes daily state easy to reason about and avoids the operational complexity of cursor management.

## What data does this integration collect?

Each vulnerability finding includes details such as:

* **Detection metadata** — the Nuclei template that matched, the scanned host or URL, the matcher that fired, and any extracted evidence.
* **Severity and lifecycle** — the finding's severity (`info`, `low`, `medium`, `high`, `critical`), workflow status (`open`, `fixed`, `false_positive`, `duplicate`, `fix_in_progress`, `accepted_risk`, `triaged`), and regression flag.
* **Vulnerability metadata** — CVE identifier (when the template name is a CVE), description, remediation guidance, and reference URLs.
* **Optional HTTP evidence** — the full HTTP request and response transcripts that triggered the detection, when **Include HTTP Evidence** is enabled.

### Supported use cases

* Monitor PDCP scan output from a single place in Elastic Security alongside your other vulnerability scanners.
* Build dashboards that track open vulnerabilities, regressions, and remediation velocity.
* Trigger alerts for newly detected high or critical findings.

## What do I need to use this integration?

Before you install the integration, gather the following from PDCP:

1. **A PDCP account** with access to the team workspace whose vulnerability scan results you want to collect.
2. **An API key.** In the PDCP dashboard, go to **Settings → API Key** to create one. Save the key — it is shown only once. Programmatic key management is available via `POST /v1/user/apikey`.
3. **The Team ID** for the workspace you want to query. In the PDCP dashboard, go to **Settings → Team** (or visit `https://cloud.projectdiscovery.io/settings/team`). A single API key can belong to multiple teams; the Team ID selects the workspace context for each request.
4. **(Optional) A dedicated service-account user.** API keys inherit the creating user's team role. For an integration deployment, create a user with the minimum permission required to read scan results and create the key from that account.

## How do I deploy this integration?

### Agent-based deployment

Elastic Agent must be installed. For more details, check the Elastic Agent [installation instructions](docs-content://reference/fleet/install-elastic-agents.md). You can install only one Elastic Agent per host.

### Onboard / configure

1. In Kibana, go to **Integrations** and search for **ProjectDiscovery Cloud**.
2. Click **Add ProjectDiscovery Cloud**.
3. Fill in the required settings:
   * **API URL** — PDCP API base URL (default: `https://api.projectdiscovery.io`).
   * **API Key** — the API key from **Settings → API Key**.
   * **Team ID** — the Team ID from **Settings → Team**.
   * **Interval** — how often to poll the API (default: `24h`, aligned with the daily-snapshot model).
4. Optionally narrow what is collected with the **Time Range**, **Severity Filter**, and **Status Filter** options.
5. Enable **Include HTTP Evidence** if you need the raw HTTP request/response transcripts. Disabled by default to reduce index size.
6. Save the integration policy and assign it to an Elastic Agent policy.

To collect findings from multiple PDCP teams, add one integration instance per team, each with its own Team ID.

### Validation

After the integration is running, open **Discover** in Kibana and search for `event.dataset: "projectdiscovery_cloud.vulnerability_scan"`. Findings appear within one polling interval after they are present in the configured time window.

## Troubleshooting

For help with Elastic ingest tools, check [Common problems](https://www.elastic.co/docs/troubleshoot/ingest/fleet/common-problems).

* 401 Unauthorized: The API key is wrong or has been revoked. Create a new key under **Settings → API Key** and update the integration policy.
* 403 Forbidden: The key is valid but the user does not have access to the requested team workspace. Verify the configured **Team ID** matches a team the API key's owner belongs to.
* 429 Too Many Requests: The PDCP API rate limit has been hit. Increase the polling interval or narrow the filter set (severity, vulnerability status). The integration applies a static outbound rate limit (10 requests per second); it does not parse `X-Ratelimit-*` response headers for adaptive backoff.
* No documents indexed: Confirm that scans exist and have produced findings in the configured team workspace and that the configured time window covers their last update time.

## Scaling

For guidance on scaling data ingestion, see [Ingest Architectures](https://www.elastic.co/docs/manage-data/ingest/ingest-reference-architectures).

The export endpoint returns the full filtered snapshot in a single request. Large snapshots (months or years of history) may take longer to fetch — narrow the **Time Range** or **Severity Filter** to reduce response size.

## Reference

### vulnerability_scan

The `vulnerability_scan` data stream collects vulnerability findings from PDCP. Each finding is stored as one document per poll. The same long-lived finding seen across multiple polls produces multiple documents — query the latest by `projectdiscovery_cloud.vulnerability.id` and use a top-hits aggregation on `@timestamp` to get the most recent state.

#### vulnerability_scan fields

{{ fields "vulnerability_scan" }}

{{ event "vulnerability_scan" }}

{{ ilm }}

{{ transform }}

### Inputs used

{{ inputDocs }}

### API usage

This integration uses the following ProjectDiscovery Cloud API endpoint:

* [Export filtered scan results](https://docs.projectdiscovery.io/api-reference/export/export-filtered-scan-results) — `POST /v1/scans/results/export?async=false&type=json`. A single bulk request per poll returns the full filtered snapshot.
