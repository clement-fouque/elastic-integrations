# Elastic Security Advisory (ESA) publication landscape and advisory document format

Research date: **2026-08-28**. All findings below come from public sources; every claim carries a
source URL. Anything I could not confirm against an official Elastic or CVE Program source is
tagged `[UNVERIFIED]`.

Scope note: this document covers how Elastic publishes security advisories publicly and what those
advisory documents contain. It deliberately says nothing about ingest pipelines, field mappings, or
manifest design — that is downstream work.

---

## 0. Executive summary

- ESA IDs are `ESA-<4-digit-year>-<sequence>`, sequence reset per calendar year, zero-padded to two
  digits for 1–99 and unpadded at 100+ (`ESA-2026-01` … `ESA-2026-99`, `ESA-2026-100`,
  `ESA-2026-137`). Sequence numbers are assigned internally and have gaps in the public record.
- The **only** official public publication channel is the Discourse forum category
  [Security Announcements](https://discuss.elastic.co/c/announcements/security-announcements/31).
  Elastic states this explicitly on its Product Security page.
- Discourse exposes that category as **JSON** and **RSS**, and each advisory post as JSON and raw
  Markdown. This is a fully usable machine-readable-ish surface (structured envelope, unstructured
  Markdown body).
- Elastic is a CVE Numbering Authority (`CNA-2017-0011`, shortName `elastic`). Every first-party
  ESA also lands in the **CVE Program as a CVE Record 5.x JSON**, which mirrors most advisory fields
  in a genuinely structured form and is freely retrievable from `cveawg.mitre.org`, NVD, and OSV.
- Elastic is **not** a CSAF provider. No `provider-metadata.json`, no `security.txt`, no CSAF files
  anywhere I could find. Confirmed independently.
- I found **zero** public references to the `elastic/security-advisories` repository. My inference
  about its file format is reasoned from the CVE `x_generator` field, the published advisory
  template, and Elastic's own description of its tooling — see §5, with confidence levels.

---

## 1. The ESA identifier scheme

### 1.1 Exact format

`ESA-YYYY-NN`

- `YYYY` — four-digit calendar year.
- `NN` — per-year sequence, **zero-padded to two digits** for values 1–99, then three digits
  naturally from 100 upward. There is no padding to three digits below 100: the public record
  contains `ESA-2026-99` immediately followed by `ESA-2026-100`.
- Uppercase `ESA` prefix in all published titles. In Discourse *slugs* it is lowercased and
  hyphen-mangled: `.../kibana-9-4-5-9-5-1-security-update-esa-2026-128/389539`.

Evidence: 203 advisory topics carrying an ESA ID in their title, harvested from the category JSON.
Of those, 178 use a two-digit sequence and 25 use three digits (all `>= 100`, all in 2026).

Elastic's own generator prompt states the field name and example format directly:

> **2. ESA Number** — The internal Elastic Security Advisory identifier (e.g., ESA-2025-01).

Source: <https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder/agent-creation-prompt.md>

Note the wording — Elastic calls it the **internal** identifier. It is minted inside Elastic's
process and then surfaced publicly.

### 1.2 Numbering is per-year and sparse

Counts of *publicly posted* advisories per ESA year, with the gaps in each year's sequence:

| ESA year | Public topics | Min seq | Max seq | Missing sequence numbers |
|---|---|---|---|---|
| 2021 | 1 | 31 | 31 | (older years pre-date the current title convention) |
| 2023 | 10 | 7 | 31 | 21 gaps |
| 2024 | 40 | 1 | 48 | 8 gaps: 28, 30, 33, 42, 43, 44, 45, 46 |
| 2025 | 36 | 1 | 39 | 3 gaps: 4, 11, 26 |
| 2026 | 116 | 1 | 137 | 21 gaps: 23, 31, 47, 48, 61, 62, 84, 85, 103, 107, 109, 114, 115, 117, 122, 125, 130, 131, 132, 134, 135 |

Two important structural facts fall out of this:

1. **Sequence numbers are reserved before publication and some are never published.** The gaps are
   not scrape errors — I paginated the entire category (315 topics across 11 pages) and the missing
   numbers simply do not exist as public topics. This mirrors how CVE IDs are reserved then
   sometimes rejected. An integration must not assume a dense sequence.
2. **Some ESA IDs share a single forum topic.** Several titles carry two IDs, e.g.
   `Kibana 8.7.1 Security Updates (ESA-2023-07, ESA-2023-08)` (topic 332330),
   `Kibana 8.15.1 Security Update (ESA-2024-27, ESA-2024-28)` (topic 366119),
   `Kibana 7.17.23/8.15.0 Security Updates (ESA-2024-32, ESA-2024-33)` (topic 373548). So the
   relationship between "forum post" and "advisory" is not strictly 1:1 historically, though
   every 2025–2026 post I examined carries exactly one ID.

Some gaps are also *later* backfills rather than permanent holes: `ESA-2024-20` was posted
2025-05-01 and `ESA-2024-21` on 2025-06-10. The ESA year reflects when the ID was assigned, not
when the post appeared. Any date logic must treat the ESA year and the post date as independent.

### 1.3 Publication cadence

Advisories are published in **batches tied to product release trains**, not continuously. Across
the 203 ESA-tagged topics there are only 52 distinct posting dates. Recent batch sizes:

| Post date | Advisories posted |
|---|---|
| 2026-08-13 | 48 |
| 2026-07-21 | 19 |
| 2026-07-01 | 11 |
| 2026-05-28 | 10 |
| 2026-04-08 | 6 |
| 2026-03-19 | 6 |
| 2026-02-26 | 7 |
| 2026-01-13 | 7 |
| 2025-12-18 | 11 |

Roughly monthly-to-six-weekly batches, with a very large tail event on 2026-08-13. Volume has grown
sharply: 40 published in ESA-year 2024, 36 in 2025, 116 already in 2026.

Elastic explains the timing itself: *"We draft the security advisory during the disclosure phase,
ahead of a planned product release that contains the fix."*
Source: <https://www.elastic.co/security-labs/blog/security-advisory-automation-rag-elastic-agent-builder>

---

## 2. Where Elastic publishes advisories publicly

### 2.1 Official channel — Discourse

`https://www.elastic.co/community/security` — which 301-redirects to
`https://www.elastic.co/product-security` (verified: `url_effective` resolves there) — is the
authoritative policy page. Verbatim:

> **Security Advisories**
>
> When a vulnerability is confirmed and resolved, we publish an **Elastic Security Advisory (ESA)**.
> This serves as the official announcement regarding security issues within Elastic products.
>
> Elastic is an authorized CVE Numbering Authority (CNA) where we assign CVE IDs to vulnerabilities
> and publish **Common Vulnerability Enumeration (CVE)** Records where our policy depends on where
> the vulnerability originates:
>
> - **Elastic Software:** For vulnerabilities identified within code produced by Elastic, we assign
>   a unique CVE ID and publish the CVE Record to the NVD database alongside the ESA to our own
>   portal at discuss.elastic.co.
> - **Third-Party Dependencies:** If a vulnerability exists in a third-party library or dependency
>   bundled with our software, we do not assign a new CVE ID. Instead, the ESA will reference the
>   existing upstream CVE ID defined by the third party.
>
> Each advisory includes:
>
> - An ESA identifier
> - The applicable CVE ID (either Elastic-assigned or Upstream)
> - A summary of the issue
> - Affected Versions
> - Remediation and mitigation details
> - Severity rating using Common Vulnerability Scoring System (CVSS)
>
> **How to stay informed:**
>
> - **View Advisories:** Elastic Security Announcements
> - Subscribe via Discuss: Click the bell icon and select 'Watching' on the page above
> - **Subscribe via RSS Feed:** Elastic Security Announcements RSS Feed

Source: <https://www.elastic.co/community/security> (HTTP 200, retrieved 2026-08-28)

That page's own hyperlinks resolve to:

- Category HTML: <https://discuss.elastic.co/c/announcements/security-announcements/31>
- Category RSS: <https://discuss.elastic.co/c/announcements/security-announcements.rss>

**There is no separate elastic.co advisories index page.** The old idea of a table on
`elastic.co/community/security` is gone; the page now just links out to Discourse. I found no
`elastic.co/security/advisories`, no docs-site advisory index, and no downloadable advisory list.

### 2.2 The Discourse surface in detail

| Endpoint | Returns | Notes |
|---|---|---|
| `https://discuss.elastic.co/c/announcements/security-announcements/31.json` | Topic list JSON | 30 topics/page; `?page=N`; `topic_list.more_topics_url` signals more. 315 total topics, 11 pages. |
| `https://discuss.elastic.co/c/announcements/security-announcements/31.rss` | RSS 2.0 | **25 items/page**, `?page=N` paginates. `<description>` contains the **full advisory body as HTML**. |
| `https://discuss.elastic.co/c/announcements/security-announcements.rss` | Same feed, slug-only form | The URL Elastic links from its own policy page. |
| `https://discuss.elastic.co/t/<id>.json` | Single topic + posts | Post objects carry `cooked` (HTML), `created_at`, `updated_at`, `version`, `username`, `topic_slug`. |
| `https://discuss.elastic.co/raw/<id>` | Raw Markdown of the topic | Prefixed with a `username \| timestamp \| #N` line per post. Cleanest source of the advisory text. |

Category ID `31` is stable and dates to 2015-06-06. Posting is staff-only:

> Security announcements for the Elastic stack. To report a security vulnerability, please follow
> the instructions on our Security Issues page. Posting to this category is restricted to staff only.

Source: category JSON, topic 2060 excerpt.

The RSS 25-item page cap is a real operational hazard given 48-advisory batches. An Elastic
Consulting Architect publicly described hitting exactly this while building the same kind of
collector:

> During testing, I found an important limitation: the RSS feed only exposes the most recent 25
> items by default (And Up until 08/13 it has been less than 25 per release). During a larger ESA
> release (43 Advisories), that meant relying on the base feed alone could miss advisories. I solved
> that by adding RSS pagination, allowing the collector to walk multiple pages on each polling cycle.

Source: <https://www.linkedin.com/posts/adam-tischler-9526317b_ecs-has-more-certified-elastic-engineers-activity-7496242341981089792-9kcy>
(Third-party account, not an Elastic publication — but the 25-item cap and `?page=N` behaviour are
independently confirmed above.)

### 2.3 CNA status

Confirmed against the CVE Program's own CNA list:

```json
{
  "shortName": "elastic",
  "cnaID": "CNA-2017-0011",
  "organizationName": "Elastic",
  "scope": "Elasticsearch, Kibana, Beats, Logstash, X-Pack, and Elastic Cloud Enterprise products only.",
  "contact": [{"email": [{"emailAddr": "security@elastic.co"}]}],
  "disclosurePolicy": [{"url": "https://www.elastic.co/community/security"}],
  "securityAdvisories": {"advisories": [{"url": "https://www.elastic.co/community/security"}]},
  "CNA": {"isRoot": false, "type": ["Vendor"], "TLR": {"shortName": "mitre"}},
  "country": "Netherlands"
}
```

Source: <https://raw.githubusercontent.com/CVEProject/cve-website/dev/src/assets/data/CNAsList.json>

Note the published scope text is stale relative to practice — Elastic now issues CVEs for Fleet
Server, APM Server, Elastic Agent, Elastic Defend, ECK, Elastic Package Registry, connectors, and
OTel distributions too (see §6).

**What CNA status implies for us:** every first-party Elastic vulnerability produces a CVE Record in
the CVE Program, which is a fully structured, freely downloadable JSON document that is effectively
a machine-readable twin of the ESA. This is the single most valuable consequence for integration
design. Elastic confirms the downstream fan-out:

> Each disclosure also gets published into the CVE Program, from which downstream national and
> regional databases ingest it automatically, including the US National Vulnerability
> Database (NIST), the EU's European Vulnerability Database (ENISA), and Japan's Japan
> Vulnerability Notes (JPCERT/CC).

Source: <https://www.elastic.co/security-labs/blog/security-advisory-automation-rag-elastic-agent-builder>

### 2.4 CSAF — confirmed absent

Independently verified on 2026-08-28, all from this host:

| URL | HTTP |
|---|---|
| `https://www.elastic.co/.well-known/csaf/provider-metadata.json` | **404** |
| `https://www.elastic.co/.well-known/csaf/index.txt` | **404** |
| `https://www.elastic.co/.well-known/csaf-aggregator/aggregator.json` | **404** |
| `https://www.elastic.co/.well-known/security.txt` | **404** |
| `https://www.elastic.co/security.txt` | **404** |
| `https://www.elastic.co/community/security/csaf` | **404** |
| `https://www.elastic.co/community/security` (control) | 200 |

Elastic does not appear in the OASIS CSAF trusted-provider ecosystem and publishes no CSAF 2.0
documents that I could locate. **Elastic is not a CSAF provider.** Confirmed.

---

## 3. Content structure of a published Elastic advisory

### 3.1 The authoritative template (published by Elastic)

This is the best find of the research track. Elastic's Security Labs published a blog post about
automating advisory drafting, and the accompanying prompt — which contains the **exact advisory
template** — is in a public Elastic repo:

<https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder/agent-creation-prompt.md>

A verbatim copy is saved at `references/elastic-advisory-generator-prompt-TEMPLATE.md`. The
`OUTPUT FORMAT` section reads, verbatim:

```
**Subject: [Product Name] [Release Fix Versions] Security Update ([ESA Number])**

**[CWE Title] in [Product Name] Leading to [Impact]**

Option 1 (first-party): [CWE Title] ([CWE-ID]) in [Product Name] can lead to [Impact] via [CAPEC Title] ([CAPEC-ID]).
  — If CAPEC is omitted per the Omit Rule, use: "... via [abstract description of attack vector]."

Option 2 (third-party dependency): Dependency on Vulnerable Third-Party Component (CWE-1395) exists in [Dependency] used by [Product Name] that could allow an attacker to [Impact]. Exploitation requires [Requirement] that triggers known vulnerabilities [CVE(s)].

**Affected Versions:**
*Fixes should be back-ported to all maintained versions unless there is a justified reason that the fix cannot be back-ported*

* 8.x: All versions from 8.0.0 up to and including [last affected 8.x version]
* 9.x:
  * All versions from 9.0.0 up to and including [last affected 9.x version]

**Affected Configurations:**
[... If all configurations are affected, state: "All configurations are affected."]

**Solutions and Mitigations:**

The issue is resolved in version [Release Fix Versions].

**For Users that Cannot Upgrade:**

Option 1 (no workarounds): There are no workarounds for this vulnerability.

Option 2 (workarounds exist):

**Self-Managed**
[Workaround instructions for self-managed deployments.]

**Cloud**
[Workaround instructions for Elastic Cloud Hosted, or note if the workaround is not available on this platform.]

**Indicators of Compromise (IOC)**

[Derive detection guidance ... If none can be identified, state: "No specific indicators of compromise have been identified for this vulnerability."]

[SERVERLESS BLOCK — include ONLY if the Serverless Mapping determines this product has a Serverless offering. Omit entirely otherwise.]

**Elastic Cloud Serverless**

Due to our continuous deployment and patching model, the vulnerability described in this security advisory was remediated in our Elastic Cloud Serverless offering before the public disclosure.

**Severity:** CVSSv3.1: [Severity Label] ( [Score] ) - [Vector String]
**CVE ID:** [CVE Number]
**Problem Type:** [CWE-ID] - [CWE Title]
**Impact:** [CAPEC-ID] - [CAPEC Title]  [omit this line if CAPEC was omitted per the Omit Rule]
```

The `Subject:` line becomes the Discourse **topic title**; the rest becomes the **post body**. This
is exactly what the real posts look like, which validates the template against production output.

The template also documents the **Serverless mapping rule**, which is a per-product enum worth
recording:

- Always include the Serverless block: **Elasticsearch, Kibana**
- Never include it: **Beats (Filebeat, Metricbeat, Packetbeat, Winlogbeat, Auditbeat, Heartbeat),
  Logstash, Elastic Agent, Fleet Server, APM Server, Enterprise Search**

And a product→language map used for CWE selection: Beats/Elastic Agent/Fleet Server/APM Server → Go;
Elasticsearch → Java; Logstash core → Java, plugins → Ruby (JRuby); Kibana → TypeScript/Node.js;
Enterprise Search → Ruby (JRuby).

### 3.2 Exact section headings observed in production

Measured across 53 real advisory bodies sampled across 2021–2026 (raw Markdown from
`discuss.elastic.co/raw/<id>`). Frequencies of the bold-label headings:

| Heading (exact text, minus the trailing colon) | Occurrences | Required? |
|---|---|---|
| `**CVE ID**` / `**CVE ID:**` | 47 | Effectively always |
| `**Severity:**` | 43 | Effectively always |
| `**Affected Versions:**` | 42 | Effectively always |
| `**Solutions and Mitigations:**` | 42 | Effectively always |
| `**Affected Configurations:**` | 18 | Optional |
| `**For Users that Cannot Upgrade:**` | 17 | Optional |
| `**Problem Type:**` | 13 | Modern advisories only |
| `**Impact:**` | 13 | Modern advisories only |
| `**Indicators of Compromise (IOC)**` | 4 | Optional, 2026+ |
| `**Elastic Cloud Serverless**` | 4 | Elasticsearch/Kibana only |
| `**Self-hosted**` / `**Cloud**` / `**Elastic Cloud**` | 5 / 4 / 2 | Sub-headings inside the workaround block |
| `**Description:**` | seen in RSS body of ESA-2026-128 | Rare label variant |
| `### Acknowledgements:` | 4 | Rare — only when an external reporter is credited |
| `## Update Log` / `## Change log` / `## Updates` | 1 / 2 / 3 | Only on long-lived "living" advisories |

Important formatting caveats an integration must survive:

- **Heading style is not stable.** Modern advisories use `**Bold Label:**`. 2023-era advisories and
  some 2026 ones use Markdown ATX headings — `# Title`, `## Solutions and Mitigations:`,
  `### Affected Versions:`. In the sample set there were 12 `Affected Versions:` and 13
  `Solutions and Mitigations:` rendered as ATX headings rather than bold labels.
- **The colon is inconsistent.** `**CVE ID**: CVE-...` and `**CVE ID:** CVE-...` both occur.
- **Duplicated headings happen.** ESA-2026-128 contains `**For Users that Cannot Upgrade:**` twice
  in a row (see the sample file).
- **The CVSS vector prefix is inconsistent.** Usually `CVSS:3.1/AV:N/...` but ESA-2026-02 has bare
  `AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` with no `CVSS:3.1/` prefix.
- **Severity label/score ordering varies.** `Medium (6.5)`, `High ( 7.7 )` (spaces inside parens),
  and `8.8(High)` (score first, no space) all appear.
- **Escaped hyphens.** Discourse raw Markdown emits `\-` for some separator hyphens, e.g.
  `**Severity:** CVSSv3.1: Medium (6.5) \- CVSS:3.1/AV:A/...`.
- **A non-standard `MPR` metric appears once.** ESA-2025-14's vector is
  `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/MPR:L` — a modified-privileges-required environmental
  metric spliced onto what is labelled a base vector.

### 3.3 Canonical field inventory

Pulling §3.1 and §3.2 together, a published Elastic advisory contains:

| Field | Where it appears | Always present? |
|---|---|---|
| ESA ID | Topic title, usually in trailing parentheses; sometimes also in the body's bold title line | Yes (2023+) |
| Product name(s) | Topic title, and in the body title sentence | Yes |
| Fix version list | Topic title, and under `Solutions and Mitigations` | Yes |
| Vulnerability title (`<CWE Title> in <Product> Leading to <Impact>`) | First bold/heading line of the body | 2026+ consistently |
| Description / summary | First paragraph after the title | Yes |
| CWE ID + title | Inline in the description, and on the `Problem Type:` line | 2025+ mostly |
| CAPEC ID + title | Inline in the description, and on the `Impact:` line | 2025+ mostly, omitted when no CAPEC fits |
| Affected versions | `Affected Versions:` bullet list | Yes |
| Affected configurations | `Affected Configurations:` | Optional |
| Solution / fixed versions | `Solutions and Mitigations:` | Yes |
| Workaround / mitigation | `For Users that Cannot Upgrade:` (+ `Self-Managed`/`Self-hosted`/`Cloud` sub-blocks) | Optional |
| Detection guidance | `Indicators of Compromise (IOC)` | Optional, 2026+ |
| Serverless remediation statement | `Elastic Cloud Serverless` | Elasticsearch/Kibana only |
| Severity label, CVSS base score, CVSS vector | `Severity:` line | Yes |
| CVE ID | `CVE ID:` line | Yes |
| Credit / acknowledgement | `Acknowledgements:` | Rare (4 of 53 sampled) |
| Publication date | Discourse `created_at` on the topic/post — **not in the body text** | Yes (envelope) |
| Revision history | `Update Log` / `Change log` sections — only on living advisories like ESA-2021-31 | Rare |
| Author | Discourse `username` (`ismisepaul`, `ikakavas`, `rodrigo_silva`, `kruskall`, `Levine`) | Yes (envelope) |

Two of these are **only** available from the Discourse envelope, never the body: **publication date**
and **last-updated timestamp** (`created_at` / `updated_at` / `version` on the post object).

### 3.4 A full worked example (ESA-2026-24, verbatim)

```
**Incorrect Authorization in Kibana Fleet Leading to Information Disclosure**

Incorrect Authorization (CWE-863) in Kibana can lead to information disclosure via Privilege Abuse
(CAPEC-122). A user with limited Fleet privileges can exploit an internal API endpoint to retrieve
sensitive configuration data, including private keys and authentication tokens, that should only be
accessible to users with higher-level settings privileges. [...]

**Affected Versions:**

* 8.x: All versions from 8.0.0 up to and including 8.19.13
* 9.x:
  * All versions from 9.0.0 up to and including 9.2.7
  * All versions from 9.3.0 up to and including 9.3.2

**Affected Configurations:**

Deployments with Fleet enabled where users have been granted the Fleet Agents privilege without the
Fleet Settings. [...]

**Solutions and Mitigations:**

The issue is resolved in versions 8.19.14, 9.2.8, and 9.3.3.

**For Users that Cannot Upgrade:**

* Review Fleet role assignments [...]
* Rotate any proxy credentials (private keys, authentication tokens) [...]

**Indicators of Compromise (IOC)**

Review Kibana audit logs for access to Fleet enrollment settings endpoints [...]

**Elastic Cloud Serverless**

Due to our continuous deployment and patching model, the vulnerability described in this security
advisory was remediated in our Elastic Cloud Serverless offering before the public disclosure.

**Severity:** CVSSv3.1: High ( 7.7 ) \- CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
**CVE ID:** CVE-2026-33461
**Problem Type:** CWE-863 \- Incorrect Authorization
**Impact:** CAPEC-122 \- Privilege Abuse
```

Topic title: `Kibana 8.19.14, 9.2.8, 9.3.3 Security Update (ESA-2026-24)`
Source: <https://discuss.elastic.co/t/kibana-8-19-14-9-2-8-9-3-3-security-update-esa-2026-24/385812>

### 3.5 Saved samples

All under `references/sample-events/`, each with a provenance comment header giving the source URL,
the Discourse topic title, `created_at`, and why the sample was chosen.

| File | ESA | Why it matters |
|---|---|---|
| `ESA-2026-01.md` | ESA-2026-01 | Metricbeat. The advisory Elastic itself cites as the first output of its AI drafting pipeline. Canonical modern template. |
| `ESA-2026-02.md` | ESA-2026-02 | Packetbeat. Rare `### Acknowledgements:` section; ATX headings; bare CVSS vector with no `CVSS:3.1/` prefix. |
| `ESA-2026-24.md` | ESA-2026-24 | Kibana Fleet. Fullest modern template — every optional section present including IOC and Serverless. |
| `ESA-2026-41.md` | ESA-2026-41 | Fleet Server. Third-party dependency variant (CWE-1395) referencing an upstream Go stdlib CVE. |
| `ESA-2026-128.md` | ESA-2026-128 | Kibana Fleet. `Description:` label variant plus a genuine duplicated heading — good malformed-input test case. |
| `ESA-2025-14.md` | ESA-2025-14 | Elasticsearch / Apache Tika. Upstream CVE; long multi-step numbered workaround with inline code and API links. |
| `ESA-2024-01.md` | ESA-2024-01 | Kibana. Leaner 2024 template: no CWE/CAPEC lines, no IOC, no Serverless. |
| `ESA-2023-16.md` | ESA-2023-16 | Multi-product (Beats + Elastic Agent + APM Server + Fleet Server). 2023 ATX-heading style. |
| `ESA-2021-31.md` | ESA-2021-31 | Log4Shell. 35 KB outlier: `Update Log` revision history, per-product and per-deployment-type subsections. The worst case for any parser. |

---

## 4. Machine-readable variants

### 4.1 Summary table

| Format | Available? | Endpoint | Notes |
|---|---|---|---|
| CSAF 2.0 | **No** | — | All well-known paths 404. Verified §2.4. |
| Discourse category JSON | **Yes** | `.../31.json?page=N` | Structured envelope (title, slug, id, `created_at`, counts). No advisory body. 30/page. |
| Discourse RSS | **Yes** | `.../31.rss?page=N` | Full advisory body as HTML in `<description>`. **25 items/page.** |
| Discourse topic JSON | **Yes** | `/t/<id>.json` | Post `cooked` HTML + `created_at`/`updated_at`/`version`. |
| Discourse raw Markdown | **Yes** | `/raw/<id>` | Cleanest body text. |
| CVE Record 5.x JSON | **Yes** | `https://cveawg.mitre.org/api/cve/<CVE-ID>` | **The genuinely structured twin of the ESA.** See §4.2. |
| NVD API 2.0 | **Yes** | `https://services.nvd.nist.gov/rest/json/cves/2.0?sourceIdentifier=security@elastic.co` | 340 Elastic-assigned CVEs total. |
| OSV | **Yes** | `https://api.osv.dev/v1/vulns/<CVE-ID>` | Mirror of cvelistV5, `database_specific.cna_assigner: "elastic"`. |
| GitHub Advisory DB (GHSA) | **Yes, but thin** | `https://api.github.com/advisories?cve_id=<CVE-ID>` | Mostly `"type": "unreviewed"` with empty `vulnerabilities[]`. See §4.5. |
| Official Elastic JSON download | **No** | — | Promised in 2020, never shipped. See §4.6. |

### 4.2 CVE Record 5.x — the richest structured source

Elastic-assigned CVEs are published in CVE Record Format 5.x, retrievable without auth:

```
https://cveawg.mitre.org/api/cve/CVE-2026-33461
```

Sample saved to `references/sample-events/ESA-2026-24.cve-record-5.1.json`. The CNA container maps
almost field-for-field onto the ESA:

| CVE Record path | ESA equivalent |
|---|---|
| `cveMetadata.cveId` | `CVE ID:` line |
| `cveMetadata.datePublished` / `dateUpdated` / `dateReserved` | Discourse `created_at` (approx.) |
| `containers.cna.title` | The bold advisory title line |
| `containers.cna.descriptions[].value` | The description paragraph (byte-identical in the cases I checked) |
| `containers.cna.descriptions[].supportingMedia[]` | Same text wrapped in `<p>…</p>` as `text/html` |
| `containers.cna.affected[].vendor` / `.product` | Product name |
| `containers.cna.affected[].versions[]` | `Affected Versions:` — as `{version, lessThan\|lessThanOrEqual, status, versionType}` |
| `containers.cna.affected[].defaultStatus` | (implicit; usually `"unaffected"`) |
| `containers.cna.metrics[].cvssV3_1` | `Severity:` line — full decomposed metrics plus `vectorString` and `baseScore` |
| `containers.cna.problemTypes[].descriptions[].cweId` + `description` | `Problem Type:` line |
| `containers.cna.impacts[].capecId` + `descriptions[].value` | `Impact:` line |
| `containers.cna.references[].url` | Back-link to the discuss.elastic.co advisory (this is how CVE↔ESA is joined) |
| `containers.cna.source.discovery` | `"Elastic"` / `"UNKNOWN"` / `"INTERNAL"` |
| `containers.cna.credits[]` | `Acknowledgements:` (present in only 5 of 340 records) |
| `containers.cna.x_generator.engine` | Elastic's tooling fingerprint — see §5 |
| `containers.adp[]` | CISA ADP Vulnrichment (SSVC), added downstream, not Elastic's |

There is **no ESA ID field** in the CVE record. The only link back is the reference URL, whose
Discourse slug embeds the ESA ID (`.../kibana-8-19-14-9-2-8-9-3-3-security-update-esa-2026-24/385812`).
I resolved 177 CVE→ESA pairs this way out of 340 records; the rest are older CVEs whose reference
slugs predate the ESA-in-slug convention.

Aggregate structure across all 340 Elastic-assigned CVE records (analysis script:
`temp/` shell history; raw records in `temp/cve5/`):

- CNA container keys: `providerMetadata` 340, `affected` 313, `descriptions` 313, `references` 313,
  `problemTypes` 311, `source` 204, `x_generator` 204, `metrics` 203, `title` 193, `impacts` 129,
  `x_legacyV4Record` 99, `datePublic` 92, `rejectedReasons` 27, `credits` 5.
- Version-object shapes: `{lessThanOrEqual, status, version, versionType}` ×346;
  `{status, version}` ×120; `{lessThan, status, version, versionType}` ×75;
  `{status, version, versionType}` ×17.
- `versionType`: `semver` ×432, absent ×120, `custom` ×4, plus one-off `1.x.x` and `8.x.x`.
- Metrics: `cvssV3_1` ×201, `cvssV4_0` ×2. **CVSS v3.1 is the norm; v4.0 is a rare exception.**
- 27 records are in `REJECTED` state with `rejectedReasons` — another reason not to assume a dense
  or fully-valid ID space.

### 4.3 NVD

`https://services.nvd.nist.gov/rest/json/cves/2.0?sourceIdentifier=security@elastic.co&resultsPerPage=2000`
returns `totalResults: 340`. Per-CVE-year distribution of Elastic-assigned CVEs:

| Year | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CVEs | 1 | 15 | 30 | 25 | 14 | 13 | 27 | 15 | 22 | 37 | 31 | 110 |

Reference-host distribution across those records: `discuss.elastic.co` 418, `www.elastic.co` 194,
`security.netapp.com` 51, `access.redhat.com` 17, `www.oracle.com` 12. Every modern Elastic CVE
points back at the Discourse advisory.

### 4.4 OSV

OSV mirrors the CVE Program, so Elastic advisories appear as `CVE-YYYY-NNNNN` OSV entries with:

```json
"database_specific": {
  "cna_assigner": "elastic",
  "cwe_ids": ["CWE-79"],
  "osv_generated_from": "https://github.com/CVEProject/cvelistV5/tree/main/cves/2025/25xxx/CVE-2025-25009.json"
}
```

OSV additionally resolves version ranges into git commit ranges and CPEs. Sample saved to
`references/sample-events/ESA-2025-20.osv.json`. There is **no `ESA-*` OSV ID namespace** — OSV does
not know about ESA IDs at all, only the CVE and the reference URL.

Querying by package (`POST https://api.osv.dev/v1/query` with
`{"package":{"name":"org.elasticsearch:elasticsearch","ecosystem":"Maven"}}`) returns 43 GHSA-prefixed
entries — those are GitHub Advisory Database records, a different view of the same CVEs.

### 4.5 GitHub Security Advisories

`https://api.github.com/advisories?cve_id=CVE-2026-33461` resolves to `GHSA-jf72-2wmj-p2f3`. Sample
saved to `references/sample-events/ESA-2026-24.github-advisory.json`. It is `"type": "unreviewed"`
with an empty `vulnerabilities[]` array — no ecosystem, no package, no version ranges — because
Elastic products largely are not distributed as npm/Maven packages that GitHub tracks. It does carry
`cvss_severities`, `cwes`, `epss`, and the discuss.elastic.co reference. Some Kibana CVEs do get
reviewed npm-ecosystem entries with proper version ranges (visible via Snyk and OSV Maven queries),
but coverage is inconsistent.

**Elastic does not publish repository-level GitHub Security Advisories.**
<https://github.com/elastic/elasticsearch/security/advisories> shows "There aren't any published
security advisories."

Rate-limiting note: unauthenticated `api.github.com` worked fine from this host during this
research; no throttling was encountered.

### 4.6 The promised-but-never-delivered JSON feed

In 2020, Josh Bressers of Elastic Product Security responded to a user asking for machine-readable
advisories:

> We are working on a project as we speak to tackle the challenges you lay out. It is going to take
> some time however. **The plan is to publish all of our advisories in ECS format** (this will also
> require some modifications to ECS), then allow the JSON to be downloaded as well as having a much
> nicer looking advisory page.
>
> — Josh Bressers, Elastic Product Security, 2020-04-17

Source: <https://discuss.elastic.co/t/security-announcements-rss-versions/228477>

Six years on, no such endpoint exists. This is relevant to §5: it tells us Elastic's Product Security
team has at least *considered* a structured, ECS-shaped representation of their advisory corpus.
`[UNVERIFIED]` whether anything from that project reached production internally.

### 4.7 Community-scraped dataset (not official)

`https://github.com/jmoon-elastic/esa-search` — a single-page ESA search tool by an Elastic employee,
public but explicitly marked "Private/internal use", containing `esas.json` with **244 records**
scraped from the Discourse category. Record shape:

```json
{
  "esa_id": "ESA-2026-137",
  "title": "Allocation of Resources Without Limits or Throttling in Kibana Leading to Denial of Service",
  "url": "https://discuss.elastic.co/t/kibana-8-19-20-9-4-5-security-update-esa-2026-137/389511",
  "affected_product": "Kibana",
  "fixed_version": "8.19.20, 9.4.5",
  "severity": "Medium (6.5)",
  "affected_ranges": [">=8.0.0 <=8.19.19", ">=9.0.0 <=9.4.4"]
}
```

Sample saved to `references/sample-events/community-esas-json-sample.json`; full clone in
`temp/esa-search/`. This is **not** an Elastic-official artifact and is not a proxy for the private
repo's format — it is one engineer's scrape of the same forum. It is useful mainly as evidence that
the forum text is parseable into exactly these fields, and as a cross-check for product names.

---

## 5. Clues about the private repo's file format

### 5.1 What I could and could not confirm

Re-confirmed the constraint (two attempts, as instructed):

- `curl https://github.com/elastic/security-advisories` → **404**
- `curl https://github.com/elastic/integrations` (control, same host) → **200**
- `gh api repos/elastic/security-advisories` → `{"message":"Not Found", "status":"404"}`

I also searched for any public reference to the repository:

- Web search for `"elastic/security-advisories"` — no hits describing the repo. Search engines
  surfaced only the Discourse category, `jmoon-elastic/esa-search`, and generic Elastic pages.
- Grep of the entire local `elastic/integrations` checkout — no references.
- The Elastic Security Labs advisory-automation blog and its public prompt repo — **no mention** of
  a git repository as the advisory store.

**Conclusion: there is no public documentation of the `elastic/security-advisories` repo's
structure.** Everything below is inference, labelled with confidence.

### 5.2 Evidence that a structured source of truth exists

**Evidence A — `x_generator` in the CVE records (strongest).** 122 of 340 Elastic CVE records carry:

```json
"x_generator": {"engine": "Elastic CVE Publisher 0.0.1"}   // 74 records
"x_generator": {"engine": "Elastic CVE Publisher 1.0.0"}   // 48 records
```

The remaining generator values are `Vulnogram 0.2.0` (49), `Vulnogram 0.1.0-dev` (29), and
`Vulnogram 0.5.0` (4) — Vulnogram being the off-the-shelf web form many CNAs use. The switch from
Vulnogram to a bespoke, semantically-versioned "Elastic CVE Publisher" is direct evidence that
Elastic built its own tool that **emits CVE Record 5.x JSON from some other source of truth**. A
program that generates CVE JSON needs structured input: product, vendor, version ranges with
`lessThanOrEqual`/`versionType`, CWE ID, CAPEC ID, CVSS vector, description, title, reference URL.
Every one of those is a field in the ESA.

Note the version numbering: `0.0.1` on the older records, `1.0.0` on the newer ones — a tool under
active development, consistent with a repo that holds both the tool and its data.

**Evidence B — the published template is field-oriented, not prose-oriented.** The template in §3.1
is a slot-filling structure with a fixed field order, conditional blocks driven by rules (the
Serverless block is included or omitted based on a product lookup table), and enum-like values. That
is a template rendered over a data record, not a hand-written document.

**Evidence C — batch publication.** 48 advisories posted on a single day (2026-08-13), 19 on
2026-07-21. Publishing 48 forum posts, 48 CVE records, and coordinating them with a release train by
hand is implausible. Batch behaviour implies a corpus that is processed and released together.

**Evidence D — the ID space is reserved-then-published with gaps.** ESA numbers are allocated before
publication and some never appear. That is the signature of a registry, not a folder of documents
someone writes as needed.

**Evidence E — Elastic's stated direction.** The 2020 statement about publishing advisories "in ECS
format ... allow the JSON to be downloaded" (§4.6), and the 2026 statement about wanting to wire
advisory generation into Elastic Workflows so that "InfoSec and Engineering collaborate on a single
document." A git repo with pull-request review is the obvious mechanism for that collaboration.

### 5.3 My best-supported inference

**Claim: the `advisories/` directory holds one structured file per advisory, keyed by ESA ID, in
either YAML or JSON — most likely Markdown-with-YAML-front-matter or plain YAML.**

Confidence breakdown:

| Sub-claim | Confidence | Basis |
|---|---|---|
| One file per advisory, named after the ESA ID | **High** | The ESA ID is the primary key throughout Elastic's process ("internal Elastic Security Advisory identifier"). A directory literally called `advisories/` keyed by anything else would be perverse. |
| The file contains structured, machine-parseable fields (not free prose) | **High** | Evidence A is close to conclusive: "Elastic CVE Publisher" must read structured input to emit valid CVE 5.x JSON. |
| The field set closely matches the CVE Record CNA container + the ESA template extras | **High** | The advisory template (§3.1) and the CVE CNA container (§4.2) are near-isomorphic. The repo record is very likely the union: CVE fields plus `esa_id`, plus the ESA-only sections (Affected Configurations, For Users that Cannot Upgrade, Indicators of Compromise, Elastic Cloud Serverless, Acknowledgements). |
| Format is YAML front matter + Markdown body, **or** plain YAML | **Medium** | The advisory body contains multi-paragraph Markdown with bullet lists, inline code, numbered steps, and hyperlinks (see `ESA-2025-14.md`). Markdown is the natural carrier for that, and YAML front matter the natural carrier for the scalar fields. Plain YAML with block scalars (`\|`) is equally workable and common in PSIRT tooling. |
| Format is CSAF JSON | **Low** | Elastic publishes no CSAF anywhere and is not in the CSAF provider ecosystem (§2.4). If they had CSAF internally, publishing a `provider-metadata.json` would be near-free. |
| Format is CVE Record 5.x JSON directly | **Low–Medium** | Tempting — the publisher emits it. But CVE 5.x has no slot for the ESA ID, Affected Configurations, workarounds, IOC guidance, or the Serverless statement, all of which the ESA carries. Those would have to live in `x_` extensions, which is awkward as a primary authoring format. More likely the repo format is the superset and CVE 5.x is a *rendering target*. |
| Directory is flat (`advisories/ESA-2026-24.md`) vs year-nested (`advisories/2026/...`) | **Low confidence either way** | The task prompt says the URL is `advisories/` with no year segment visible, which mildly favours flat, but a year-nested layout would also present as `advisories/` at the top level. With 137 advisories in 2026 alone, year-nesting would be the sane choice. `[UNVERIFIED]` |
| Filename casing (`ESA-2026-24.md` vs `esa-2026-24.yaml`) | **Cannot determine** | `[UNVERIFIED]` |

**What I would expect a file to contain**, as a reasoned reconstruction (this is inference, not
observed data — do not treat these as real field names):

```
esa_id, cve_id, title, product, description,
affected_versions (structured ranges), fixed_versions,
cwe_id, cwe_title, capec_id, capec_title,
cvss_version, cvss_score, cvss_severity, cvss_vector,
affected_configurations, workarounds, indicators_of_compromise,
serverless_statement (bool/text), acknowledgements,
discuss_url, published_date
```

**Practical consequence for the integration:** because the repo is inaccessible and its format
unverifiable, the defensible design is to treat the **public Discourse surface as the primary data
source** and the **CVE Record 5.x / NVD / OSV data as the structured enrichment source**, joined on
the CVE ID (and on the ESA ID extracted from the Discourse slug). That combination reproduces
essentially everything the private repo would give us, from sources that are stable, documented, and
authless. If the private repo later becomes reachable, its records should map cleanly onto the same
field set, since both are renderings of the same underlying advisory.

---

## 6. Elastic product / component taxonomy

### 6.1 Products appearing in advisories

From the `affected[].product` field across all 340 Elastic-assigned CVE records (authoritative,
since Elastic populates it):

| Product | CVE records |
|---|---|
| Kibana (incl. `kibana`, `Kibana X-Pack Security`) | 155 |
| Elasticsearch (incl. `elasticsearch`, `Elasticsearch X-Pack Security/Machine Learning`) | 69 |
| Logstash | 9 |
| Packetbeat | 7 |
| Elastic X-Pack Security / X-Pack Security | 9 |
| Fleet Server | 6 |
| Elastic Cloud Enterprise (incl. `(ECE)`) | 9 |
| APM Server | 5 |
| Elastic Agent (incl. `Elastic Agent and Elastic Defend`) | 5 |
| Elastic Defend | 3 |
| Elastic Enterprise Search / Enterprise Search / Enterprisesearch / Elastic App Search | 7 |
| Beats | 3 |
| Elastic Endpoint Security / Endpoint Security / Endpoint / + Elastic Endgame | 5 |
| Elastic Cloud on Kubernetes / Eck Operator | 4 |
| Metricbeat | 2 |
| Filebeat | 2 |
| APM agents (Java, Python, Ruby, .NET, Go) | 6 |
| Elastic Network Drive Connector | 1 |
| Elastic Sharepoint Online Python Connector | 1 |
| Elastic Package Registry | 1 |
| Elasticsearch-Hadoop | 1 |
| Elastic Code | 1 |
| Elastic X-Pack Alerting / Reporting | 2 |

Additional products seen in Discourse titles but not (yet) in the CVE product field:
**Elastic OTel Java**, **Synthetics Recorder**, **Winlogbeat**, **Auditbeat**, **Heartbeat**
(the last three appear in the template's Serverless mapping list).

`vendor` is `"Elastic"` in 313 of 313 records that have an `affected` block (3 legacy records use
`"n/a"`).

Important caveat: **product naming is not normalised.** `Kibana` and `kibana`,
`Elastic Cloud Enterprise` and `Elastic Cloud Enterprise (ECE)`, `Elastic Enterprise Search` and
`Enterprise Search` and `Enterprisesearch` all coexist. Anything consuming this needs a
normalisation table.

Sub-component naming appears in the *title* rather than the product field:
`Kibana Fleet`, `Kibana - Crowdstrike Connector`, `Packetbeat's MongoDB protocol parser`,
`Elasticsearch Wildcard Matching`, `Kibana Cases`.

### 6.2 How version ranges are expressed in advisory text

The dominant modern form is a nested bullet list keyed by major-version series. Shapes observed
across the sampled advisories (digits replaced by `N`), with frequency:

| Line shape | Count |
|---|---|
| `N.x: All versions from N.N.N up to and including N.N.N` | 21 |
| `All versions from N.N.N up to and including N.N.N` (nested under a bare `N.x:` parent) | 17 |
| `N.x:` (parent bullet with nested children) | 10 |
| `N.N.x:** All versions from N.N.N and up to and including N.N.N` | 5 |
| `N.x: All versions` (whole series affected, no bound) | 2 |
| `Version N.N.N` (single version) | 2 |
| `<Product> versions on or after N.N.N and before N.N.N` | 5 |
| `<Product> versions up to, but not including, N.N.N` | 3 |
| `<Product> versions before N.N.N` / `prior to and including N.N.N` | 3 |
| `<Product> version N.N.N through N.N.N` | 1 |

Canonical modern example (ESA-2026-24):

```
**Affected Versions:**

* 8.x: All versions from 8.0.0 up to and including 8.19.13
* 9.x:
  * All versions from 9.0.0 up to and including 9.2.7
  * All versions from 9.3.0 up to and including 9.3.2
```

Semantics worth noting:

- The boundary phrasing is **inclusive** in the modern form (`up to and including`) and **exclusive**
  in older prose (`before`, `up to, but not including`). Both appear; the two must not be conflated.
- A series may be listed with **no upper bound at all** — `7.x: All versions` — meaning the entire
  series is affected and unfixed (typically because the series is EOL).
- Ranges are **discontinuous per minor series**. `9.0.0–9.2.7` plus `9.3.0–9.3.2` is not one range;
  Elastic maintains parallel release branches and each gets its own bound.
- `Solutions and Mitigations` states fix versions as a **comma-separated list of point releases**
  across those parallel branches: `The issue is resolved in versions 8.19.14, 9.2.8, and 9.3.3.`
  Sometimes `version` singular, sometimes `versions`, sometimes with an Oxford comma, sometimes as a
  bullet list, sometimes phrased `Users should upgrade to version …` or `Users should upgrade to the
  versions below or later:`.
- Older advisories occasionally interleave the product name into each range line
  (`Elasticsearch versions on or after 8.0.0 and before 8.13.0`), which is how multi-product
  advisories disambiguate.

The **CVE Record** version data is far cleaner and should be preferred where available:

```json
"affected": [{
  "defaultStatus": "unaffected",
  "product": "Kibana",
  "vendor": "Elastic",
  "versions": [
    {"version": "9.3.0", "lessThanOrEqual": "9.3.2", "status": "affected", "versionType": "semver"},
    {"version": "9.0.0", "lessThanOrEqual": "9.2.7", "status": "affected", "versionType": "semver"},
    {"version": "8.0.0", "lessThanOrEqual": "8.19.13", "status": "affected", "versionType": "semver"}
  ]
}]
```

`versionType` is `semver` in 432 of 554 version objects. The CVE record does **not** carry the fixed
version — that only exists in the ESA prose and (derivably) in the topic title.

### 6.3 Deployment-type taxonomy

Advisories distinguish deployment types in workaround sections and the Serverless block. Observed
labels: `Self-Managed`, `Self-hosted`, `Self-hosted & Cloud`, `Cloud`, `Elastic Cloud`,
`Elastic Cloud Serverless`, `ECE`, `ECK`,
`Elastic Cloud customers with self-managed monitoring clusters`,
`Self-Managed without Elastic Stack Monitoring`.

The template formalises only `Self-Managed` / `Cloud` / `Elastic Cloud Serverless`; the rest is
historical drift.

### 6.4 CWE / CAPEC distributions

Top CWEs across 340 records: CWE-79 (26), CWE-532 (25), CWE-400 (23), CWE-770 (21), CWE-863 (18),
CWE-200 (17), CWE-862 (11), CWE-94 (9), CWE-269 (8), CWE-674 (8), CWE-639 (8), CWE-601 (8),
CWE-284 (7), CWE-918 (7), CWE-20 (6). Plus CWE-1395 for the third-party-dependency variant.

Top CAPECs: CAPEC-130 (37), CAPEC-1 (16), CAPEC-122 (13), CAPEC-153 (12), CAPEC-233 (6),
CAPEC-242 (6), CAPEC-664 (5), CAPEC-100 (5).

CVSS severity labels used in the `Severity:` line: `Low`, `Medium`, `High`, `Critical`.

---

## 7. Gaps, open questions, and areas for further investigation

1. **The private repo's actual format remains unverified.** Nothing public describes it. My §5
   inference rests on `x_generator`, the published template, and batch-publication behaviour — good
   circumstantial evidence, but circumstantial. Anyone with read access should spend two minutes
   confirming the directory layout and one file's contents; that would collapse the whole
   uncertainty. `[UNVERIFIED]`
2. **Whether the repo is the source of truth or a downstream mirror.** It could equally be a
   published-artifact archive that the CVE Publisher writes *to* rather than reads *from*. The
   distinction matters for freshness and for whether draft/embargoed advisories are present.
   `[UNVERIFIED]`
3. **Whether unpublished ESA IDs exist as files.** The public gaps (21 in 2026) might correspond to
   files marked as withdrawn/not-applicable, or to nothing at all. `[UNVERIFIED]`
4. **The `Elastic CVE Publisher` tool is not public.** No public repo, no blog post about it. Its
   input schema would answer most of §5 definitively. `[UNVERIFIED]`
5. **Discourse post edit history.** Advisories are amended (ESA-2021-31 has a full `Update Log`).
   The topic JSON exposes `version` and `updated_at` on each post, and Discourse has a post-revisions
   API, but I did not survey how often advisories are edited after publication. Worth checking if
   change tracking matters.
6. **Whether the 2026-08-13 batch of 48 is the new normal or a one-off backlog flush.** Volume
   tripled year-over-year. This affects any assumption about polling frequency and page depth.
7. **CVSS v4.0 adoption.** Only 2 of 340 records use it. If Elastic migrates, the `Severity:` line
   format will change.
8. **No official ESA↔CVE mapping table exists.** The join has to be done through the Discourse slug
   or the CVE reference URL. Both work, neither is contractual, and pre-2023 advisories do not carry
   the ESA ID in the slug at all.

---

## 8. Files written by this research track

### Curated (`references/`)

| Path | Contents |
|---|---|
| `references/esa-publication-landscape.md` | This document. |
| `references/elastic-advisory-generator-prompt-TEMPLATE.md` | Verbatim copy of Elastic's public advisory-generator prompt, containing the authoritative ESA output template. |
| `references/sample-events/ESA-2026-01.md` | Metricbeat advisory — canonical modern format. |
| `references/sample-events/ESA-2026-02.md` | Packetbeat — has `Acknowledgements:`, ATX headings, bare CVSS vector. |
| `references/sample-events/ESA-2026-24.md` | Kibana Fleet — every optional section present. |
| `references/sample-events/ESA-2026-41.md` | Fleet Server — third-party dependency (CWE-1395) variant. |
| `references/sample-events/ESA-2026-128.md` | Kibana Fleet — `Description:` variant, duplicated heading. |
| `references/sample-events/ESA-2025-14.md` | Elasticsearch/Tika — long procedural workaround. |
| `references/sample-events/ESA-2024-01.md` | Kibana — leaner 2024 format. |
| `references/sample-events/ESA-2023-16.md` | Multi-product — 2023 ATX-heading format. |
| `references/sample-events/ESA-2021-31.md` | Log4Shell — 35 KB living document with `Update Log`. |
| `references/sample-events/ESA-2026-24.cve-record-5.1.json` | CVE Record 5.x for CVE-2026-33461 (the structured twin of ESA-2026-24). |
| `references/sample-events/ESA-2026-24.github-advisory.json` | GitHub Advisory DB record for the same CVE. |
| `references/sample-events/ESA-2025-20.osv.json` | OSV record for CVE-2025-25009. |
| `references/sample-events/ESA-2026-128.discourse-topic.json` | Discourse per-topic JSON envelope. |
| `references/sample-events/ESA-2026-128.discourse-rss-item.xml` | RSS channel header + one full `<item>` with the advisory body as HTML. |
| `references/sample-events/discourse-category-topic-list.json` | Discourse category topic-list JSON shape. |
| `references/sample-events/community-esas-json-sample.json` | Community (non-official) scraped ESA dataset shape. |

### Raw artifacts (`temp/`)

| Path | Contents |
|---|---|
| `temp/cat31_all_topics.json` | All 315 topics from the Security Announcements category (11 pages). |
| `temp/cat31_page0.json`, `temp/cat31.rss` | First-page category JSON and the RSS feed. |
| `temp/raw/topic_*.md` | 54 raw-Markdown advisory bodies spanning 2021–2026. |
| `temp/sampled_meta.json` | ESA ID / topic ID / title / date index for the sampled advisories. |
| `temp/cve5/CVE-*.json` | All 340 Elastic-assigned CVE Records in 5.x format. |
| `temp/nvd_elastic_all.json` | Full NVD response for `sourceIdentifier=security@elastic.co`. |
| `temp/cve_to_esa.json` | 177 resolved CVE→ESA mappings derived from Discourse reference slugs. |
| `temp/cnalist.json` | CVE Program CNA list (contains the Elastic CNA entry). |
| `temp/osv_*.json`, `temp/gh_adv_*.json` | OSV and GitHub Advisory DB probe responses. |
| `temp/agent-creation-prompt.md` | Source copy of Elastic's advisory template prompt. |
| `temp/esa-search/` | Clone of `jmoon-elastic/esa-search` (community dataset). |
| `temp/thread_228477.md` | Discourse thread containing Elastic Product Security's 2020 statement about ECS-format advisories. |
| `temp/community_security.html` | Saved copy of the Elastic Product Security page. |
| `temp/topic_389539.json` | Discourse per-topic JSON. |
