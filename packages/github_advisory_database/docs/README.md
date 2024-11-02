# github_advisory_database Integration

## Overview

Explain what the integration is, define the third-party product that is providing data, establish its relationship to the larger ecosystem of Elastic products, and help the reader understand how it can be used to solve a tangible problem.
Check the [overview guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-overview) for more information.

## Datastreams

Provide a high-level overview of the kind of data that is collected by the integration. 
Check the [datastreams guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-datastreams) for more information.

## Requirements

The requirements section helps readers to confirm that the integration will work with their systems.
Check the [requirements guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-requirements) for more information.

## Setup

Point the reader to the [Observability Getting started guide](https://www.elastic.co/guide/en/observability/master/observability-get-started.html) for generic, step-by-step instructions. Include any additional setup instructions beyond what’s included in the guide, which may include instructions to update the configuration of a third-party service.
Check the [setup guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-setup) for more information.

## Troubleshooting (optional)

Provide information about special cases and exceptions that aren’t necessary for getting started or won’t be applicable to all users. Check the [troubleshooting guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-troubleshooting) for more information.

## Reference

Provide detailed information about the log or metric types we support within the integration. Check the [reference guidelines](https://www.elastic.co/guide/en/integrations-developer/current/documentation-guidelines.html#idg-docs-guidelines-reference) for more information.

## Logs

### vulnerability

Insert a description of the datastream here.

**Exported fields**

| Field | Description | Type |
|---|---|---|
| @timestamp | Event timestamp. | date |
| data_stream.dataset | Data stream dataset name. | constant_keyword |
| data_stream.namespace | Data stream namespace. | constant_keyword |
| data_stream.type | Data stream type. | constant_keyword |
| event.dataset | Event dataset | constant_keyword |
| event.module | Event module | constant_keyword |
| github_advisory_database.vulnerability.credits.type |  | keyword |
| github_advisory_database.vulnerability.credits.user.avatar_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.events_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.followers_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.following_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.gists_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.gravatar_id |  | keyword |
| github_advisory_database.vulnerability.credits.user.html_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.id |  | long |
| github_advisory_database.vulnerability.credits.user.login |  | keyword |
| github_advisory_database.vulnerability.credits.user.node_id |  | keyword |
| github_advisory_database.vulnerability.credits.user.organizations_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.received_events_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.repos_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.site_admin |  | boolean |
| github_advisory_database.vulnerability.credits.user.starred_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.subscriptions_url |  | keyword |
| github_advisory_database.vulnerability.credits.user.type |  | keyword |
| github_advisory_database.vulnerability.credits.user.url |  | keyword |
| github_advisory_database.vulnerability.credits.user.user_view_type |  | keyword |
| github_advisory_database.vulnerability.cve_id |  | keyword |
| github_advisory_database.vulnerability.cvss.score |  | long |
| github_advisory_database.vulnerability.cvss.vector_string |  | keyword |
| github_advisory_database.vulnerability.cvss_severities.cvss_v3.score |  | long |
| github_advisory_database.vulnerability.cvss_severities.cvss_v3.vector_string |  | keyword |
| github_advisory_database.vulnerability.cvss_severities.cvss_v4.score |  | long |
| github_advisory_database.vulnerability.cvss_severities.cvss_v4.vector_string |  | keyword |
| github_advisory_database.vulnerability.cwes.cwe_id |  | keyword |
| github_advisory_database.vulnerability.cwes.name |  | keyword |
| github_advisory_database.vulnerability.description |  | keyword |
| github_advisory_database.vulnerability.epss.percentage |  | long |
| github_advisory_database.vulnerability.epss.percentile |  | long |
| github_advisory_database.vulnerability.ghsa_id |  | keyword |
| github_advisory_database.vulnerability.github_reviewed_at |  | keyword |
| github_advisory_database.vulnerability.html_url |  | keyword |
| github_advisory_database.vulnerability.identifiers.type |  | keyword |
| github_advisory_database.vulnerability.identifiers.value |  | keyword |
| github_advisory_database.vulnerability.nvd_published_at |  | keyword |
| github_advisory_database.vulnerability.published_at |  | keyword |
| github_advisory_database.vulnerability.references |  | keyword |
| github_advisory_database.vulnerability.repository_advisory_url |  | keyword |
| github_advisory_database.vulnerability.severity |  | keyword |
| github_advisory_database.vulnerability.source_code_location |  | keyword |
| github_advisory_database.vulnerability.summary |  | keyword |
| github_advisory_database.vulnerability.type |  | keyword |
| github_advisory_database.vulnerability.updated_at |  | keyword |
| github_advisory_database.vulnerability.url |  | keyword |
| github_advisory_database.vulnerability.vulnerabilities.first_patched_version |  | keyword |
| github_advisory_database.vulnerability.vulnerabilities.package.ecosystem |  | keyword |
| github_advisory_database.vulnerability.vulnerabilities.package.name |  | keyword |
| github_advisory_database.vulnerability.vulnerabilities.vulnerable_version_range |  | keyword |
| github_advisory_database.vulnerability.withdrawn_at |  | date |


