{{- generatedHeader }}
# ProjectDiscovery Cloud Integration for Elastic

## Overview
The ProjectDiscovery Cloud integration for Elastic collects vulnerability findings from the [ProjectDiscovery Cloud Platform (PDCP)](https://cloud.projectdiscovery.io). PDCP is a SaaS exposure-management product built around the open-source Nuclei scanner. It performs continuous external and internal vulnerability scanning, asset discovery, and credential leak monitoring across a multi-tenant platform.

This integration ingests the vulnerability findings produced by PDCP into Elasticsearch, normalizing them to ECS so they can be searched, correlated, and visualized alongside other security telemetry.

### Compatibility
This integration is compatible with the ProjectDiscovery Cloud Platform `v1` REST API at `https://api.projectdiscovery.io`.

### How it works
The integration polls the PDCP `POST /v1/scans/results/export` endpoint on a configurable interval using the [CEL input](https://www.elastic.co/docs/reference/integrations/cel) of Elastic Agent. It authenticates with an API key sent as the `X-API-Key` header and (optionally) selects a non-default team via `X-Team-Id`. The endpoint returns the entire result set matching the request filters in a single response — no pagination is required. One Elastic document is indexed per `VulnerabilityResults` row. When a row contains multiple detection events, ECS fields (target, evidence, classification, timestamps) are populated from the first detection while the full `event[]` array is preserved under `projectdiscovery_cloud.event` for drill-down.

## What data does this integration collect?
The ProjectDiscovery Cloud integration collects events of the following types:

* **Vulnerability findings** — one document per detection. Includes target, evidence, classification (CVE, CWE, CVSS, EPSS), template metadata, and asset enrichment (TLS, ASN, technologies, HTTP transcript).

### Supported use cases
* Centralize ProjectDiscovery Cloud vulnerability findings in Elasticsearch for correlation with other security signals.
* Drive vulnerability triage workflows in Kibana with ECS-normalized severity, CVE, and CVSS data.
* Enrich SIEM detections by pivoting from a host or domain to its known external/internal vulnerabilities.

## What do I need to use this integration?
* An active [ProjectDiscovery Cloud](https://cloud.projectdiscovery.io) account with at least one completed scan.
* A ProjectDiscovery Cloud API key. Generate one from **Settings → API Key** ([direct link](https://cloud.projectdiscovery.io/settings/api-key)).
* (Multi-team only) The team identifier from **Settings → Team** if the integration should target a non-default team.
* Outbound HTTPS connectivity from the Elastic Agent host to `api.projectdiscovery.io`.

## How do I deploy this integration?

### Agent-based deployment

Elastic Agent must be installed. For more details, check the Elastic Agent [installation instructions](docs-content://reference/fleet/install-elastic-agents.md). You can install only one Elastic Agent per host.

### Agentless deployment

Agentless deployments are only supported in Elastic Serverless and Elastic Cloud environments. Agentless deployments provide a means to ingest data while avoiding the orchestration, management, and maintenance needs associated with standard ingest infrastructure.

For more information, refer to [Agentless integrations](https://www.elastic.co/guide/en/serverless/current/security-agentless-integrations.html) and [Agentless integrations FAQ](https://www.elastic.co/guide/en/serverless/current/agentless-integration-troubleshooting.html).

### Onboard / configure
1. In Kibana, navigate to **Management → Integrations** and search for "ProjectDiscovery Cloud".
2. Click **Add ProjectDiscovery Cloud**.
3. Provide the **API Key** generated from PDCP **Settings → API Key**.
4. (Optional) Provide a **Team ID** if you want to scope ingestion to a specific PDCP team.
5. (Optional) Adjust the **Polling Interval**, **Initial Lookback**, and the various filter variables (severity, status, categories, hosts, etc.) to match your use case.
6. Save the integration policy and assign it to one or more agents.

### Validation
After enabling the integration and waiting one polling interval, open **Discover** in Kibana and run:

```
data_stream.dataset : "projectdiscovery_cloud.projectdiscovery_cloud"
```

Documents should appear with `event.module: projectdiscovery_cloud` and `event.kind: event`.

## Troubleshooting

For help with Elastic ingest tools, check [Common problems](https://www.elastic.co/docs/troubleshoot/ingest/fleet/common-problems).

* **`401 Unauthorized` from PDCP** — confirm the API key is correct and has not been rotated. Re-issue from Settings → API Key.
* **`403 Forbidden` from PDCP** — confirm the API key has access to the target team and that the team identifier (if configured) is valid.
* **No data flowing** — verify outbound HTTPS to `api.projectdiscovery.io` is reachable from the agent host, and that at least one scan has produced findings within the **Initial Lookback** window.

## Scaling

For more information on architectures that can be used for scaling this integration, check the [Ingest Architectures](https://www.elastic.co/docs/manage-data/ingest/ingest-reference-architectures) documentation.

The export endpoint returns the entire matching result set in a single HTTP response. For very large tenants, narrow the polling window with a smaller `time` value or apply additional filters (severity, status, categories) to limit response size.

## Reference

### projectdiscovery_cloud

The `projectdiscovery_cloud` data stream collects vulnerability findings from the PDCP `POST /v1/scans/results/export` endpoint. One Elastic document is indexed per exported `VulnerabilityResults` row. When a row contains multiple detection events, ECS fields are populated from the first detection while the full `event[]` array is preserved under `projectdiscovery_cloud.event` for drill-down.

{{ fields "projectdiscovery_cloud" }}

{{ ilm }}

{{ transform }}

### Inputs used
{{ inputDocs }}

### API usage
These APIs are used with this integration:

* `POST /v1/scans/results/export` — [Export filtered Scan results](https://docs.projectdiscovery.io/api-reference/export/export-filtered-scan-results)
