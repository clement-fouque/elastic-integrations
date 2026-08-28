# ECS mapping analysis — `elastic_security_advisories`

Research date: **2026-08-28**. Research output only: this document describes **the data and its
target field mapping**. It contains no pipeline processors, no `fields/*.yml` content, and no
recommendations about pipeline configuration or error handling. Field *types* are stated because
the mapping target is part of the data description; how those types get authored is downstream work.

Inputs this analysis builds on:

- `references/esa-publication-landscape.md` — advisory field inventory (§3), CVE Record 5.x
  mapping (§4.2), product taxonomy and version-range semantics (§6), reconstructed repo field
  set (§5.3).
- `references/github-api-collection-notes.md` — collection is Git Trees + Git Blobs against a
  private repo, so every document also carries git provenance.
- `references/sample-events/` — nine real advisory bodies plus CVE Record 5.x, OSV, GitHub
  Advisory and Discourse envelope samples.

ECS verification basis (all ECS claims below were checked against the generated schema, not
against memory):

```
https://raw.githubusercontent.com/elastic/ecs/v9.3.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/v9.3.0/generated/ecs/ecs_flat.yml
https://raw.githubusercontent.com/elastic/ecs/v9.4.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/v9.5.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/main/generated/csv/fields.csv
https://www.elastic.co/docs/reference/ecs/ecs-vulnerability   (live reference page)
```

Local copies: `temp/ecs/fields-9.3.0.csv`, `temp/ecs/fields-v9.4.0.csv`, `temp/ecs/fields-v9.5.0.csv`,
`temp/ecs/fields-main.csv`, `temp/ecs/ecs-9.3.0.yml`.

Assumed naming throughout: package `elastic_security_advisories`, one data stream `advisory`,
so the custom namespace is `elastic_security_advisories.advisory.*` and
`event.dataset` is `elastic_security_advisories.advisory`.

---

## 0. Recommendation up front

| Decision | Recommendation |
|---|---|
| `event.kind` | `enrichment` |
| `event.category` | `["vulnerability"]` |
| `event.type` | `["info"]` |
| `event.outcome` | **not set** |
| `event.dataset` | `elastic_security_advisories.advisory` |
| `event.module` | `elastic_security_advisories` |
| Stream classification | **Event stream** (reference/enrichment corpus), **not** an entity stream. Do not use `event.kind: asset`, do not use `entity.*`. |
| Document `_id` | Fingerprint of `esa_id` + git blob SHA — content-addressed revision key |
| Version-range mapping | `nested` array of objects, with `type: version` on the bound fields |
| ECS `vulnerability.*` fields usable | **10** of the 13 members at v9.3.0 (14 at v9.5.0). See §2.1. |
| Biggest ECS gaps | ESA ID, advisory title, fixed versions, version ranges, CWE/CAPEC, workarounds, IOC guidance, Serverless statement, credits, git provenance |

---

## 1. Event categorization

### 1.1 What an ESA document actually is

One document is one **vulnerability disclosure**, authored by Elastic Product Security, describing
a defect in an Elastic product. It is not an observation of anything on a host. There is no asset,
no scanner, no detection, no actor, no outcome. It is reference material whose purpose is to be
joined against *other* data — a Kibana version inventory, a scan result, a CVE seen in a SIEM alert.

Three further properties matter for categorization:

1. **Stable natural key — but with two string renderings.** The ESA ID is the primary key of Elastic's
   own process (`esa-publication-landscape.md` §1.1: Elastic calls it "the internal Elastic Security
   Advisory identifier").

   > **Added 2026-08-28 (review pass 2), and it affects every join and the document `_id`.** The
   > repository renders the ID with the sequence **zero-padded to four digits** (`ESA-2026-0081.json`,
   > a real reported filename), while every public rendering pads to a **minimum of two** and widens
   > naturally (`ESA-2026-24`, `ESA-2026-81`, `ESA-2026-137`). `ESA-2026-0081` is the public
   > `ESA-2026-81`. **The two string forms do not match**, so the natural key must be the pair
   > *(year, integer sequence)*.
   >
   > Concretely: `…advisory.esa_year` and `…advisory.esa_sequence` (both `integer`), proposed in §3.1
   > as a convenience, are in fact the **canonical join key** and should be treated as such rather than
   > as optional extras — deriving an integer sequence normalizes `0081` to `81` for free. Populate
   > `…advisory.esa_id` and `vulnerability.report_id` with the **normalized public form**, since that is
   > what joins to the Discourse slug, the CVE record's reference URL, and every other corpus; keep the
   > raw filename in `file.name`. Fingerprint the `_id` (§1.6) over the **normalized** ID: doing it over
   > the raw four-digit form and adding normalization later would change every `_id` and silently
   > duplicate the entire index.
2. **Mutable.** Advisories are amended in place. `ESA-2021-31` carries a nine-entry `## Update Log`
   spanning 2021-12-16 to 2022-01-13 (`references/sample-events/ESA-2021-31.md`). The CVE twin has
   `cveMetadata.dateUpdated` distinct from `datePublished` — for CVE-2026-33461 the record was
   updated a day after publication.
3. **The corpus is re-read whole.** Collection Strategy A enumerates the entire `advisories/`
   sub-tree every poll and fetches only blobs whose SHA changed. There is no advancing event cursor.

### 1.2 The four candidate framings, compared

Against `ecs-field-mappings/references/categorization-cheatsheet.md`:

| Candidate | Cheatsheet definition | Verdict for an ESA |
|---|---|---|
| `event.kind: event` + `category: [vulnerability]` | "General event/log… most common value for integration logs." | **Weak fit.** An advisory is not an event that happened at a point in time on a monitored system. Widely used in the repo for vulnerability data, but mostly by streams that genuinely emit one record per vulnerability-per-asset. Defensible as a lowest-common-denominator, not correct. |
| `event.kind: enrichment` | "Enrichment/context feeds — IOC/context datasets that enrich other events." | **Best fit.** This is precisely a context dataset whose value is joining to other events on CVE ID or product/version. Elastic's own precedent for *the same shape of data* uses this (§1.3). |
| `event.kind: asset` | "Entity/inventory snapshot records — one document per entity per collection cycle… the document *describes the entity itself*." | **Wrong.** An advisory is not an entity in the entity-store sense. The `entity.type` allowed values are `bucket, database, container, function, queue, host, user, application, service, session, cloud, orchestrator` — an advisory is none of them. See §1.4. |
| `event.kind: state` | "Periodic categorical state of an observation — a finding or posture result *about* a resource at a point in time (e.g. CDR misconfiguration/vulnerability findings)." | **Wrong for this data.** `state` is the CDR finding framing: a resource was evaluated and here is its posture. `cdr-field-requirements.md` mandates `state` for vulnerability findings and pairs it with `resource.id`, `resource.name`, `host.name`, `package.version` — every one of which requires an evaluated asset. An ESA has no asset. Also relevant: CDR applicability is explicitly scoped to "cloud security integrations — those covering CSPM, CWPP, or vulnerability management use cases." A vendor's own disclosure corpus is not vulnerability management of your estate. |

`event.category: ["vulnerability"]` is unambiguous. The ECS definition is "Relating to vulnerability
scan results. Use this category to analyze vulnerabilities detected by Tenable, Qualys, internal
scanners, and other vulnerability management sources," and ECS declares
`expected_event_types: ["info"]` for it — so `event.type: ["info"]` is the only ECS-sanctioned
pairing. Both verified in `temp/ecs/ecs-9.3.0.yml`.

`event.outcome` is left unset. The cheatsheet: "Do not set `event.outcome` for purely informational
or metric/state events where outcome does not apply." A disclosure document has no
success/failure dimension.

`event.action` is likewise left unset — there is no source-specific verb.

### 1.3 Precedent survey in `elastic/integrations`

Surveyed data streams whose ingest pipeline mentions `vulnerability`. The tables below enumerate
roughly 30 of them, chosen to cover both sides of the axis that matters: does the document describe a
**vulnerability itself** (a catalog/reference record) or a **vulnerability found on an asset** (a
finding)?

> **Corrected 2026-08-28 (review pass 2).** This section previously claimed to have "surveyed **every**
> data stream whose ingest pipeline mentions `vulnerability` (34 streams across 23 packages)". Both
> parts were wrong. The real population is **75 streams across 58 packages** (78/58 case-insensitively;
> 65/51 restricted to `default.yml`; 44/38 restricted to streams that actually set
> `event.category: vulnerability`). No reading of the criterion yields 34/23. This is a substantial and
> useful sample, but it is **not exhaustive**, and it should not be cited as though it were.
>
> **The "splits cleanly" framing is also overstated, in one direction.** Of the asset-finding streams,
> *zero* use `enrichment` — that half holds firmly. But of the ~10 catalog/reference streams, only
> **4** use `enrichment` (`github/security_advisories`, `first_epss/vulnerability`, and two
> `ti_google_threat_intelligence` streams); the other 6 use `state` (`ti_flashpoint`,
> `tenable_io/plugin`), `event` (`tenable_sc/plugin`, `rapid7_insightvm/vulnerability`,
> `crowdstrike/vulnerability`) or `alert` (`qualys_vmdr/knowledge_base`). "Catalog streams lean
> `enrichment`" is therefore false as an aggregate claim; the majority of them do not.
>
> **The recommendation is unaffected**, because it never actually depended on the aggregate. It rests
> on `github/security_advisories` being an exact structural twin that sets the triple at
> `default.yml:12-25` (verified line-exact), plus ECS's own `expected_event_types: ["info"]` on
> `event.category: vulnerability`. Read §1.4's closest-analogue argument as the load-bearing one and
> this survey as supporting context.

**Reference / catalog streams — one document per vulnerability definition:**

| Package / stream | `event.kind` | `event.category` | `event.type` | Pipeline path |
|---|---|---|---|---|
| **`github` / `security_advisories`** | **`enrichment`** | `[vulnerability]` | `[info]` | `packages/github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml:12-25` |
| `first_epss` / `vulnerability` | `enrichment` | `vulnerability` | `info` | `packages/first_epss/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `ti_google_threat_intelligence` / `vulnerability` | `enrichment` | `vulnerability` | `info` | `packages/ti_google_threat_intelligence/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `ti_google_threat_intelligence` / `vulnerability_weaponization` | `enrichment` | `vulnerability` | `info` | same package, `vulnerability_weaponization` stream |
| `ti_flashpoint` / `vulnerability` | `state` | `vulnerability` | `info` | `packages/ti_flashpoint/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `tenable_io` / `plugin` | `state` | — | `[info]` | `packages/tenable_io/data_stream/plugin/elasticsearch/ingest_pipeline/default.yml` |
| `tenable_sc` / `plugin` | `event` | — | `[info]` | `packages/tenable_sc/data_stream/plugin/elasticsearch/ingest_pipeline/default.yml` |
| `qualys_vmdr` / `knowledge_base` | `alert` | `[vulnerability]` | `[info]` | `packages/qualys_vmdr/data_stream/knowledge_base/elasticsearch/ingest_pipeline/default.yml` |
| `rapid7_insightvm` / `vulnerability` | `event` | `[vulnerability]` | `[info]` | `packages/rapid7_insightvm/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `crowdstrike` / `vulnerability` | `event` | `vulnerability` | `info` | `packages/crowdstrike/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |

**Asset-finding streams — one document per vulnerability-on-asset:**

| Package / stream | `event.kind` | `event.category` | `event.type` | Pipeline path |
|---|---|---|---|---|
| `wiz` / `vulnerability` | `alert` | `[vulnerability]` | `[info]` | `packages/wiz/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `tenable_io` / `vulnerability` | `state` | `[vulnerability]` | `[info]` | `packages/tenable_io/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `carbon_black_cloud` / `asset_vulnerability_summary` | `state` | (unset) | — | `packages/carbon_black_cloud/data_stream/asset_vulnerability_summary/elasticsearch/ingest_pipeline/default.yml` |
| `qualys_vmdr` / `asset_host_detection` | `alert` | `[vulnerability]` | `[info]` | `packages/qualys_vmdr/data_stream/asset_host_detection/elasticsearch/ingest_pipeline/default.yml` |
| `rapid7_insightvm` / `asset_vulnerability` | `event` | `vulnerability` | `info` | `packages/rapid7_insightvm/data_stream/asset_vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `aws` / `inspector` | `event` | `vulnerability` | `info` | `packages/aws/data_stream/inspector/elasticsearch/ingest_pipeline/default.yml` |
| `aws` / `securityhub_findings` | `state` | `[vulnerability]`… | `info` | `packages/aws/data_stream/securityhub_findings/elasticsearch/ingest_pipeline/default.yml` |
| `sysdig` / `vulnerability` | `event` | `vulnerability` | `info` | `packages/sysdig/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `prisma_cloud` / `vulnerability` | `event` | `vulnerability` | `info` | `packages/prisma_cloud/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `microsoft_defender_endpoint` / `vulnerability`, `m365_defender` / `vulnerability` | `event` | `vulnerability` | `info` | respective `default.yml` |
| `claroty_xdome` / `vulnerability` | `state` | `vulnerability` | `info` | `packages/claroty_xdome/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `armis`, `bitsight`, `xm_cyber`, `eset_protect` / `*vulnerability*` | `event` | `vulnerability` | `info` | respective `default.yml` |
| `snyk` / `issues` | `[alert]` | — | `[info]` | `packages/snyk/data_stream/issues/elasticsearch/ingest_pipeline/default.yml` |
| `nozomi_networks` / `node_cve` | `alert` | `vulnerability` | `info` | `packages/nozomi_networks/data_stream/node_cve/elasticsearch/ingest_pipeline/default.yml` |

Also checked, as the task requested: `github` / `dependabot` and `github` / `code_scanning` both
set `event.kind: alert` with `event.type` of `creation`/`deletion` conditional on
`fixed_at`/`dismissed_at`. That is correct for *them* — a Dependabot alert is a finding on a
specific repository with an open/closed lifecycle — and correct evidence that it is **not** the
model for a disclosure document.

**The repo is genuinely inconsistent** (`event`, `state`, `alert`, `enrichment` all appear for
overlapping data shapes), so the honest reading of the precedent is not "the repo says X" but
"the repo splits, and the *closest analogue* is unambiguous."

### 1.4 The decisive precedent

`packages/github/data_stream/security_advisories` ingests **GitHub Security Advisory documents** —
a corpus of vendor-published vulnerability disclosures, keyed by a stable advisory ID (`ghsa_id`),
carrying CVE ID, CVSS score and vector, CWE list, description, summary, affected version ranges,
credits, references, and `published_at`/`updated_at`/`withdrawn_at` dates. That is a field-for-field
structural twin of an ESA. It sets:

```
packages/github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml
  L12-15   event.kind      = enrichment
  L16-20   event.category  = [vulnerability]
  L21-25   event.type      = [info]
```

and its `sample_event.json` confirms the shape post-ingest. `first_epss` (a pure CVE-keyed
reference feed) and both `ti_google_threat_intelligence` vulnerability streams reach the same
conclusion independently.

**Recommendation: `event.kind: enrichment`, `event.category: ["vulnerability"]`,
`event.type: ["info"]`, `event.outcome` unset.**

### 1.5 Event stream or entity stream?

Applying `entity-mappings/references/entity-datastream-classification.md`, which requires signals
1 **and** 2 to both hold:

| Signal | Strength | Holds for ESA? |
|---|---|---|
| **1. No event timestamp** — only subject properties | Necessary | **Partially.** `published_date` is genuinely a property of the advisory. But it is also a real, meaningful point in time at which the disclosure entered the world, and it is what a user wants on the time axis. Call this ambiguous rather than satisfied. |
| **2. Idempotent re-read** — full snapshot each cycle, no time filter, no advancing cursor | **Strongest** | **Holds.** Strategy A re-enumerates the whole `advisories/` tree; there is no `since` parameter and no cursor that advances through an event log. |
| **3. Stable primary key** | Supporting | **Holds.** `ESA-YYYY-NN`. |
| **4. Vendor vocabulary** | Supporting | **Fails.** The vocabulary is *advisories*, *disclosures*, *security announcements* — the classification guide lists *alerts, findings* as event-style vocabulary and *users, devices, assets, inventory, identities* as entity-style. Advisories match neither list, but they are far closer to *findings* than to *inventory*. |

Signal 2 holds; signal 1 is at best ambiguous. **Classification: event stream, not entity stream.**

The stronger argument is semantic rather than mechanical. `entity.type` in ECS v9.3.0 has an
allowed-value list of `bucket, database, container, function, queue, host, user, application,
service, session, cloud, orchestrator` (verified in `temp/ecs/fields-9.3.0.csv` and the
classification guide). An advisory is not any of those. The entity store models *subjects that act
or are acted upon* — users, hosts, services. A disclosure document is a description of a defect,
not a subject. Forcing `event.kind: asset` and `entity.id` onto it would put ESA records into
entity-store views alongside users and hosts, which is actively wrong.

`event.kind: enrichment` already carries the "this is a reference corpus, not a timeline" meaning
that the entity framing was reaching for, without the entity-store side effects. It is also what
lets the corpus behave sensibly in the Security UI's enrichment paths.

Note the deliberate consequence: `event.kind: enrichment` means the ECS pin stays at the repo
default `git@v9.3.0`. The conditional `git@v9.5.0` pin exists only for entity streams.

### 1.6 Mutability and the document `_id`

Advisories are mutable, so the interesting question is whether ingest should be **append-only**
(every revision is a new document) or **upsert/latest-state** (one document per ESA ID, overwritten).

The repo precedent for reference-style vulnerability streams is uniform and it is neither pure
append nor pure upsert — it is **content-addressed revision keying**: fingerprint the natural key
*together with* a change-detecting field into `_id`.

| Stream | Fingerprint inputs → `_id` | Path |
|---|---|---|
| `qualys_vmdr` / `knowledge_base` | `json.QID`, `json.LAST_SERVICE_MODIFICATION_DATETIME`, `json.CVE_LIST` | `.../knowledge_base/elasticsearch/ingest_pipeline/default.yml` |
| `tenable_io` / `plugin` | `json.id`, `json.attributes.plugin_modification_date` | `.../plugin/elasticsearch/ingest_pipeline/default.yml` |
| `ti_google_threat_intelligence` / `vulnerability` | `gti.vulnerability.attributes.cve_id`, `…last_modification_date` | `.../vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `ti_flashpoint` / `vulnerability` | `json.id`, `json.timelines.last_modified_at` | `.../vulnerability/elasticsearch/ingest_pipeline/default.yml` |
| `rapid7_insightvm` / `vulnerability` | `json.id`, `json.modified`, `json.added`, `json.description`, `json.cves`, `json.published` | `.../vulnerability/elasticsearch/ingest_pipeline/default.yml` |

This gives idempotent re-reads (unchanged record → same `_id` → no-op overwrite) while preserving
each amendment as a separate document, so `ESA-2021-31`'s revision history remains queryable
instead of being flattened to whatever the last poll saw.

**Recommendation: `_id` = fingerprint of (ESA ID, git blob SHA).**

The git blob SHA is strictly better than a timestamp for this source, and this is the one place
where the collection method genuinely improves on the alternatives:

- A blob SHA is a **content hash**. It changes if and only if the bytes change. A `last_modified`
  timestamp can be missing, can be identical across a real edit, or can change on a no-op touch.
- `github-api-collection-notes.md` §1.4 already establishes that the Trees API hands you the blob
  SHA for free on every poll, so no extra request is needed and no parsing is required to obtain it.
- It is robust to advisories that carry no in-document `updated_date` at all — and since the repo
  format is unverified, whether such a field exists is `[UNVERIFIED]`.

Including the ESA ID (rather than fingerprinting the blob SHA alone) keeps the key human-traceable
and survives the pathological case of two advisory files with byte-identical content.

Note the corollary for downstream consumers: because each amendment produces a new document,
"the current state of ESA-2026-24" is *the most recent document for that `esa_id`*, not "the
document." Whether that collapse belongs in a transform, in a Kibana query, or nowhere is an
implementation question outside this document's scope, but it should be flagged to the builder.

**Rejected alternative:** `_id` = fingerprint of the ESA ID alone (pure upsert to latest state).
This is simpler and gives one document per advisory, but it silently destroys revision history —
exactly the information `ESA-2021-31` exists to convey — and it is not what any comparable stream
in the repo does.

---

## 2. Which ECS fields genuinely exist

### 2.1 `vulnerability.*` — the exact member list

Verified against ECS v9.3.0, v9.4.0, v9.5.0 and `main`, and cross-checked against the live
reference page <https://www.elastic.co/docs/reference/ecs/ecs-vulnerability>.

| ECS field | Type | Exists at v9.3.0? | Usable for an ESA? |
|---|---|---|---|
| `vulnerability.category` | `keyword` (array) | Yes | Technically yes — but ECS frames it as a platform/architecture bucket ("Debian", "SUSE", "Database", "Firewall"), sourced from the Qualys category taxonomy. Nothing in an ESA maps cleanly. **Leave unset.** |
| `vulnerability.classification` | `keyword` | Yes | **Yes** — constant `CVSS`. Same as `github/security_advisories` L280-283. |
| `vulnerability.description` | `keyword` + `.text` multi-field (`match_only_text`) | Yes | **Yes** — the advisory description paragraph. |
| `vulnerability.description.text` | `match_only_text` | Yes | Inherited multi-field, not separately set. |
| `vulnerability.enumeration` | `keyword` | Yes | **Yes** — constant `CVE`. |
| `vulnerability.id` | `keyword` | Yes | **Yes** — the CVE ID. |
| `vulnerability.reference` | `keyword` | Yes | **Yes** — the `discuss.elastic.co` advisory URL. |
| `vulnerability.report_id` | `keyword` | Yes | **Yes, with a caveat.** ECS describes it as "the report or scan identification number" (example `20191018.0001`). The ESA ID is Elastic Product Security's report identifier for this disclosure, so the fit is reasonable. Precedent for a non-scan use: `hackerone/data_stream/report/elasticsearch/ingest_pipeline/default.yml:82` copies the HackerOne report ID into it. Recommend mapping the ESA ID here **in addition to** the canonical custom field, not instead of it. |
| `vulnerability.scanner.vendor` | `keyword` | Yes | **Yes, semantically loose.** Elastic is not a scanner; it is the CNA and publisher. Precedent both ways: `ti_google_threat_intelligence/data_stream/vulnerability/…/default.yml:58` sets it to `Google` for a non-scanner feed, while `github/security_advisories` omits it entirely. Recommend setting it to `Elastic` for cross-integration query symmetry, and also setting `observer.vendor`/`observer.product`. |
| `vulnerability.score.base` | **`float`** | Yes | **Yes** — the CVSS base score. |
| `vulnerability.score.environmental` | `float` | Yes | **No.** Elastic publishes base metrics only (203 of 340 CVE records carry `metrics`, all `cvssV3_1` or `cvssV4_0` base). See §4.3 for the one anomalous `MPR` case. |
| `vulnerability.score.temporal` | `float` | Yes | **No.** Never published. |
| `vulnerability.score.version` | `keyword` | Yes | **Yes** — `"3.1"` (or `"4.0"` in the 2 known records that use CVSS v4). |
| `vulnerability.severity` | `keyword` | Yes | **Yes** — `Low` / `Medium` / `High` / `Critical`. Casing discussed in §4.4. |
| `vulnerability.status` | `keyword`, **beta** | **No — v9.5.0+ only** | **Not applicable at any pin.** ECS defines it as "the lifecycle state of a vulnerability finding **on an asset**," allowed values `open, fixed, reopened, unknown`. There is no asset. Do not set it, and do not bump the ECS pin to reach it. |

**Ten of the thirteen members are usable** (thirteen distinct fields at v9.3.0, fourteen at v9.5.0;
the fourteenth CSV row is the `vulnerability.description.text` multi-field, not a separate member).
*Corrected 2026-08-28: this document previously said "nine of the fourteen" here while its own table
above marks ten usable, and gave three different member counts in three places. The disputed field is
`vulnerability.scanner.vendor`, which §2.5 and §3.1 go on to recommend populating, so it is counted.*
There is no `vulnerability.title`, no
`vulnerability.published_date`, no `vulnerability.cwe`, no `vulnerability.capec`, no
`vulnerability.vector`, no `vulnerability.solution`, no `vulnerability.workaround` — despite all
of those being names people reach for. `vulnerability.published_date` in particular appears in
`cdr-field-requirements.md` and in several packages, but it is a **custom** field defined in
package `fields.yml`, not ECS. Verified absent from v9.3.0 through `main`.

### 2.2 `vulnerability.*` has no fixed-version and no version-range field — stated explicitly

This is the single largest gap and it is worth being blunt about.

The complete ECS `vulnerability` fieldset is the thirteen members above (fourteen at v9.5.0). **None of them expresses:**

- the version in which the vulnerability was **fixed** (`8.19.14, 9.2.8, 9.3.3` for ESA-2026-24);
- an affected **version range** of any kind — no lower bound, no upper bound, no inclusivity flag,
  no version-type discriminator;
- the fact that ranges are **discontinuous per release branch** (`>=9.0.0 <=9.2.7` *and*
  `>=9.3.0 <=9.3.2` are two separate ranges, not one).

ECS `package.*` does not fill the gap either. Its thirteen members are `architecture`,
`build_version`, `checksum`, `description`, `install_scope`, `installed`, `license`, `name`, `path`,
`reference`, `size`, `type`, `version` — all describing **one installed package instance**, not a
range. `package.version` means "the version present on this asset." Setting it from an advisory's
lower bound would be a lie.

`package.fixed_version` is **not ECS**. It is a widely-copied CDR convention, defined as a custom
field in **12** packages (`aws`, `aws_securityhub`, `cloud_security_posture`, `google_scc`,
`m365_defender`, `microsoft_defender_cloud`, `microsoft_defender_endpoint`, `prisma_cloud`,
`qualys_vmdr`, `rapid7_insightvm`, `sysdig`, `tenable_io`), 11 of them in a file literally named
`fields/package.yml`. The exception is `wiz`, which defines it in
`wiz/data_stream/vulnerability/fields/fields.yml:180-184` instead. Example definition, `packages/sysdig/data_stream/vulnerability/fields/package.yml`:

```yaml
- name: package
  type: group
  fields:
    - name: fixed_version
      type: keyword
      description: In which version of the package the vulnerability was fixed.
```

**Required custom fields to close the gap** (all under `elastic_security_advisories.advisory.*`):

| Custom field | Type | Holds |
|---|---|---|
| `…advisory.fixed_versions` | `keyword[]` | `["8.19.14", "9.2.8", "9.3.3"]` |
| `…advisory.affected_versions` | `nested` | Array of range objects — see §4.2 |
| `…advisory.affected_versions.vendor` | `keyword` | `Elastic` |
| `…advisory.affected_versions.product` | `keyword` | `Kibana` |
| `…advisory.affected_versions.version` | `version` | Lower bound / exact version |
| `…advisory.affected_versions.less_than` | `version` | Exclusive upper bound |
| `…advisory.affected_versions.less_than_or_equal` | `version` | Inclusive upper bound |
| `…advisory.affected_versions.status` | `keyword` | `affected` / `unaffected` |
| `…advisory.affected_versions.version_type` | `keyword` | `semver` / `custom` / absent |
| `…advisory.affected_versions.range` | `keyword` | Rendered `>=8.0.0 <=8.19.13`, for display and for exact-string matching |
| `…advisory.default_status` | `keyword` | CVE `affected[].defaultStatus`, usually `unaffected` |

An additional note the builder will need: the **CVE record does not carry the fixed version**
(`esa-publication-landscape.md` §6.2). Fixed versions exist only in the ESA prose
(`Solutions and Mitigations`) and, derivably, in the Discourse topic title. So if the repo file is
CVE-shaped, fixed versions must come from the advisory body.

### 2.3 `package.*` for the affected product

Recommended use, narrowly:

| ECS field | Use | Rationale |
|---|---|---|
| `package.name` | **Yes** — the affected product name (`Kibana`). Array-valued for multi-product advisories such as `ESA-2023-16` (Beats + Elastic Agent + APM Server + Fleet Server). | This is the field every vulnerability-finding stream in the repo populates with the affected package name (`crowdstrike`, `sysdig`, `m365_defender`, `aws/inspector`, `rapid7_insightvm`, `wiz`, `microsoft_defender_endpoint`). Setting it makes ESA records joinable to scan findings on the same key. |
| `package.version` | **No.** | Means "the installed version." An advisory has ranges, not an installed version. |
| `package.type`, `package.reference`, `package.description` | **No.** | Nothing in the advisory maps. |

Caveat from `esa-publication-landscape.md` §6.1: product naming is **not normalised** upstream —
`Kibana`/`kibana`, `Elastic Cloud Enterprise`/`Elastic Cloud Enterprise (ECE)`,
`Elastic Enterprise Search`/`Enterprise Search`/`Enterprisesearch` all coexist. Whatever lands in
`package.name` needs a normalisation table if it is to be joinable. Sub-components
(`Kibana Fleet`, `Packetbeat's MongoDB protocol parser`) appear only in the **title**, never in the
product field, so they need their own custom field (`…advisory.component`).

### 2.4 `file.*` and `url.*` for git provenance

**`url.*` should hold the public advisory URL, not the GitHub file URL.** There is only one root
`url.*` object, and the `discuss.elastic.co` link is the semantically primary URL: it is what
`vulnerability.reference` points at, it is the CVE record's only reference, and it is the join key
that resolves CVE→ESA. This mirrors `github/security_advisories`, which runs `uri_parts` over the
advisory's `html_url` into `url.*` (`default.yml:192-206`). The GitHub blob URL is provenance and
belongs in the custom namespace.

**`file.*` is a genuine fit for the repo-file metadata**, with one important exclusion:

| Source | Target | Verdict |
|---|---|---|
| Trees API `path` (`advisories/2026/ESA-2026-0024.json`) | `file.path` (`keyword` + `.text`) | **Yes** |
| Derived directory (`advisories/2026`) | `file.directory` (`keyword`) | **Yes** |
| Derived basename (`ESA-2026-0024.json`) | `file.name` (`keyword`) | **Yes** — note the repository uses the **four-digit** ESA form; see §1.2 |
| Derived extension (`json`) | `file.extension` (`keyword`) | **Yes** |
| Trees API `size` | `file.size` (`long`) | **Yes** |
| Trees API blob `sha` | ~~`file.hash.sha1`~~ | **No — do not do this.** A git blob SHA is `sha1("blob <len>\0" + content)`, not the SHA-1 of the file content. Putting it in `file.hash.sha1` would make it collide, in a `related.hash`-style pivot, with genuine content hashes that will never match. Use `…advisory.git.blob_sha`. |
| Commit SHA, repo owner, repo name, branch/ref, last commit date, GitHub HTML URL | — | **No ECS home.** All custom. |

Repo owner and name have no ECS field. `organization.name` is about the organization the *event
relates to*, not a source-code host account, and `service.name` is about the service that emitted
the data. The `github` package itself sets **neither** — it keeps all repository metadata under
`github.*`. Follow that: `…advisory.git.owner`, `…advisory.git.repository`, `…advisory.git.ref`.

### 2.5 Other ECS fields worth setting

| Field | Value | Note |
|---|---|---|
| `@timestamp` | Advisory publication date | See §3.7 |
| `ecs.version` | `9.3.0` | Matches repo-default ECS pin |
| `event.id` | ESA ID | ECS `event.id` is "unique ID to describe the event" — the ESA ID is exactly that |
| `event.reference` | `discuss.elastic.co` advisory URL | ECS: "reference URL linking to additional information about this event" — precise fit |
| `event.url` | Same URL | ECS: "URL linking to an external system to continue investigation" |
| `event.original` | Verbatim advisory file bytes | ECS `keyword`. The ECS home for the unparsed source document. |
| `observer.vendor` | `Elastic` | Precedent: `ti_google_threat_intelligence` sets `observer.vendor`/`observer.product` alongside `vulnerability.scanner.vendor` |
| `observer.product` | `Elastic Security Advisories` | " |
| `message` | Rendered advisory body | ECS `match_only_text`. Legitimate but overlaps `…advisory.body`; pick one, do not populate both |
| `tags` | `["forwarded", "elastic-security-advisories"]` | Convention only — see §3 |

---

## 3. Complete field mapping table

Legend for the **Source** column:

- **ESA** — the advisory record's own field. **Corrected 2026-08-28:** the repository files are JSON,
  so this is a JSON key lookup, not Markdown section parsing. The specific key names are
  `[UNVERIFIED]`; the `RECON` markers below stand. Markdown section parsing applies only if the
  public Discourse path is built (`esa-publication-landscape.md` §3).
- **CVE5** — present in the CVE Record 5.x structured twin (§4.2), fully observable.
- **RECON** — from the reconstructed repo field set (§5.3). `[UNVERIFIED]` field name.
- **GIT** — from the Git Trees / Blobs collection envelope.

`ESA+CVE5` means the value exists in both and the CVE record is the cleaner form.

### 3.1 Identity

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| `esa_id` (`ESA-2026-24`) | ESA, RECON | `elastic_security_advisories.advisory.esa_id` | `keyword` | **Canonical natural key.** No ECS field for a vendor advisory ID. |
| " | " | `vulnerability.report_id` | `keyword` | ECS. Secondary. §2.1. |
| " | " | `event.id` | `keyword` | ECS. |
| ESA year component | derived | `…advisory.esa_year` | `integer` | Convenience; year and post date are independent (§1.2 of the landscape doc) |
| ESA sequence component | derived | `…advisory.esa_sequence` | `integer` | Sparse; gaps are real |
| `cve_id` (`CVE-2026-33461`) | ESA, CVE5 `cveMetadata.cveId` | `vulnerability.id` | `keyword` | ECS |
| " | " | `…advisory.cve_id` | `keyword` | Retain source form |
| (constant) | — | `vulnerability.enumeration` | `keyword` | ECS, `CVE` |
| (constant) | — | `vulnerability.classification` | `keyword` | ECS, `CVSS` |
| Advisory title (`Incorrect Authorization in Kibana Fleet Leading to Information Disclosure`) | ESA first line, CVE5 `containers.cna.title` | `…advisory.title` | `keyword` + `match_only_text` multi-field | **No ECS field.** `vulnerability.title` does not exist. Confirmed absent v9.3.0→main. |
| Discourse topic title / `Subject:` line | ESA | `…advisory.subject` | `keyword` | Carries product + fix versions + ESA ID |
| Sub-component (`Kibana Fleet`) | ESA title | `…advisory.component` | `keyword` | Only ever in the title, never the CVE product field |
| Description paragraph | ESA, CVE5 `descriptions[].value` | `vulnerability.description` | `keyword` + `.text` (`match_only_text`) | ECS. Byte-identical between the two sources in every case checked. |
| Full advisory body (Markdown) | ESA, GIT blob | `…advisory.body` | `match_only_text` | See §4.1 |
| Verbatim source file | GIT blob | `event.original` | `keyword` | ECS |

### 3.2 CVSS

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| CVSS version (`3.1`) | ESA `Severity:` line, CVE5 `metrics[].cvssV3_1.version` | `vulnerability.score.version` | `keyword` | ECS. **Not numeric** — it is `"3.1"`, a keyword. |
| " | " | `…advisory.cvss.version` | `keyword` | |
| Base score (`7.7`) | ESA, CVE5 `.baseScore` | `vulnerability.score.base` | **`float`** | ECS-fixed. See §4.3. |
| " | " | `…advisory.cvss.base_score` | `float` | |
| Severity label (`High`) | ESA, CVE5 `.baseSeverity` (`HIGH`) | `vulnerability.severity` | `keyword` | ECS. Casing: §4.4. |
| " | " | `…advisory.cvss.base_severity` | `keyword` | |
| Vector string | ESA, CVE5 `.vectorString` | `…advisory.cvss.vector_string` | `keyword` | **No ECS field for a CVSS vector.** Verified absent. |
| `attackVector` (`NETWORK`) | CVE5 | `…advisory.cvss.attack_vector` | `keyword` | Precedent for decomposed metrics as `keyword` in a vendor namespace: `packages/hackerone/data_stream/report/fields/fields.yml:477-489` (`attack_complexity`, `attack_vector`, `availability`, `confidentiality`, plus a separate `cvss_4_point_0_metrics` group) and `packages/google_scc/data_stream/finding/fields/fields.yml:786-806` (`availability_impact`, `base_score`, `confidentiality_impact`, `integrity_impact`, `privileges_required`, `scope`, `user_interaction`) |
| `attackComplexity` (`LOW`) | CVE5 | `…advisory.cvss.attack_complexity` | `keyword` | |
| `privilegesRequired` (`LOW`) | CVE5 | `…advisory.cvss.privileges_required` | `keyword` | |
| `userInteraction` (`NONE`) | CVE5 | `…advisory.cvss.user_interaction` | `keyword` | |
| `scope` (`CHANGED`) | CVE5 | `…advisory.cvss.scope` | `keyword` | |
| `confidentialityImpact` (`HIGH`) | CVE5 | `…advisory.cvss.confidentiality_impact` | `keyword` | |
| `integrityImpact` (`NONE`) | CVE5 | `…advisory.cvss.integrity_impact` | `keyword` | |
| `availabilityImpact` (`NONE`) | CVE5 | `…advisory.cvss.availability_impact` | `keyword` | |

The decomposed metrics are only reliably available from the CVE record; they are derivable from the
vector string but the vector string itself is inconsistently formatted in the ESA prose
(`esa-publication-landscape.md` §3.2: `ESA-2026-02` has a bare `AV:A/AC:L/…` with no `CVSS:3.1/`
prefix; `ESA-2025-14` splices a `/MPR:L` environmental metric onto a base vector).

### 3.3 CWE and CAPEC

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| CWE ID (`CWE-863`) | ESA `Problem Type:`, CVE5 `problemTypes[].descriptions[].cweId` | `…advisory.cwe.id` | `keyword` | **No ECS field.** ECS has no CWE fieldset anywhere; `vulnerability.category`/`.classification` are not it. |
| CWE title (`Incorrect Authorization`) | ESA, CVE5 `.description` | `…advisory.cwe.title` | `keyword` | |
| CAPEC ID (`CAPEC-122`) | ESA `Impact:`, CVE5 `impacts[].capecId` | `…advisory.capec.id` | `keyword` | **No ECS field.** `threat.technique.*` is ATT&CK, not CAPEC — do not misuse it. |
| CAPEC title (`Privilege Abuse`) | ESA, CVE5 `impacts[].descriptions[].value` | `…advisory.capec.title` | `keyword` | |

Both are single-valued in every modern advisory but the CVE schema allows arrays
(`problemTypes[]`, `impacts[]`), so both should tolerate multi-value.

### 3.4 Affected product and versions

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| Vendor (`Elastic`) | CVE5 `affected[].vendor` | `…advisory.vendor` | `keyword` | 313 of 313 records with an `affected` block say `Elastic` |
| Product (`Kibana`) | ESA title, CVE5 `affected[].product` | `package.name` | `keyword` (array) | ECS. §2.3. |
| " | " | `…advisory.products` | `keyword` (array) | Raw, un-normalised source form |
| `defaultStatus` (`unaffected`) | CVE5 `affected[].defaultStatus` | `…advisory.default_status` | `keyword` | |
| Version-range array | ESA `Affected Versions:` bullets, CVE5 `affected[].versions[]` | `…advisory.affected_versions` | **`nested`** | §4.2 |
| ↳ `version` (`9.3.0`) | CVE5 | `…affected_versions.version` | `version` | Lower bound, or exact version when no bound present |
| ↳ `lessThan` | CVE5 | `…affected_versions.less_than` | `version` | Exclusive upper bound (75 of 554 version objects) |
| ↳ `lessThanOrEqual` | CVE5 | `…affected_versions.less_than_or_equal` | `version` | Inclusive upper bound (346 of 554) |
| ↳ `status` | CVE5 | `…affected_versions.status` | `keyword` | `affected` / `unaffected` |
| ↳ `versionType` | CVE5 | `…affected_versions.version_type` | `keyword` | `semver` ×432, absent ×120, `custom` ×4, one-offs `1.x.x`, `8.x.x` |
| ↳ product/vendor | CVE5 | `…affected_versions.product` / `.vendor` | `keyword` | Denormalised into each range so multi-product advisories stay queryable — §4.2 |
| ↳ rendered range | derived | `…affected_versions.range` | `keyword` | `>=8.0.0 <=8.19.13`. Matches the community dataset's `affected_ranges` shape. |
| Fixed versions (`8.19.14, 9.2.8, 9.3.3`) | ESA `Solutions and Mitigations:` **only** | `…advisory.fixed_versions` | `keyword[]` | **No ECS field. Absent from the CVE record entirely.** §2.2. Consider `version` type if range queries on the fix are wanted; `keyword` is the safer default because the source is a free-text sentence. |
| Solution sentence | ESA | `…advisory.solution` | `match_only_text` | Preserves the exact prose, which varies (`version` vs `versions`, Oxford comma, bullet list, `Users should upgrade to…`) |

### 3.5 Remediation, configurations, IOC, Serverless

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| `Affected Configurations:` | ESA (18 of 53 sampled) | `…advisory.affected_configurations` | `match_only_text` | Prose. Sometimes literally `All configurations are affected.` |
| `For Users that Cannot Upgrade:` | ESA (17 of 53) | `…advisory.workarounds` | `match_only_text` | Multi-paragraph Markdown, bullets, numbered steps, inline code, links (`ESA-2025-14`). Can appear **twice** (`ESA-2026-128`). |
| " (presence) | derived | `…advisory.has_workarounds` | `boolean` | `false` when the text is "There are no workarounds…" |
| Workaround deployment sub-blocks (`Self-Managed`, `Self-hosted`, `Cloud`, `Elastic Cloud`, `ECE`, `ECK`) | ESA | `…advisory.workaround_deployment_types` | `keyword[]` | Un-normalised historical drift; §6.3 of the landscape doc lists nine observed labels |
| `Indicators of Compromise (IOC)` | ESA (4 of 53, 2026+) | `…advisory.indicators_of_compromise` | `match_only_text` | **Detection *guidance* prose, not indicators.** Do not put it in `threat.indicator.*` — there are no IOC values, only advice to review audit logs. |
| " (presence) | derived | `…advisory.has_indicators_of_compromise` | `boolean` | |
| `Elastic Cloud Serverless` statement | ESA (Elasticsearch/Kibana only) | `…advisory.serverless_statement` | `match_only_text` | Near-boilerplate text |
| " (presence) | derived | `…advisory.serverless_affected` | `boolean` | Per-product rule documented in the template (§3.1 of the landscape doc) |
| Third-party-dependency variant (CWE-1395) | ESA / derived | `…advisory.is_third_party_dependency` | `boolean` | Distinguishes template Option 1 vs Option 2; `ESA-2026-41` is the example |
| Upstream CVE IDs referenced in a dependency advisory | ESA | `…advisory.upstream_cve_ids` | `keyword[]` | Distinct from `vulnerability.id` when Elastic did not assign |
| `Update Log` / `Change log` / `Updates` | ESA (rare; `ESA-2021-31`) | `…advisory.update_log` | `match_only_text` | Living-document revision history. Nine entries in `ESA-2021-31`. |

### 3.6 Acknowledgements

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| `Acknowledgements:` prose | ESA (4 of 53) | `…advisory.acknowledgements` | `match_only_text` | e.g. "We would like to thank AISLE Research for responsibly disclosing…" (`ESA-2026-02`) |
| Credited party names | CVE5 `credits[]` (only 5 of 340 records) | `…advisory.credits.value` | `keyword` | **No ECS field.** `user.name` is wrong — the credited party is an external researcher or organization, not an actor in an event. |
| Credit type | CVE5 `credits[].type` | `…advisory.credits.type` | `keyword` | `finder`, `reporter`, etc. |
| Discovery source | CVE5 `source.discovery` | `…advisory.discovery` | `keyword` | Enum: `Elastic` / `UNKNOWN` / `INTERNAL` |

### 3.7 Dates

`@timestamp` is the **advisory publication date**. That is the value a user wants on the time axis:
"which advisories dropped in the 2026-08-13 batch?" is the natural question. It is also what the
comparable streams do (`github/security_advisories` uses the advisory's publication time).

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| Publication date | RECON `published_date`, Discourse `created_at`, CVE5 `cveMetadata.datePublished` | `@timestamp` | `date` | Three sources; they differ by minutes. For ESA-2026-24: Discourse `2026-04-08T16:18:41.426Z`, CVE `2026-04-08T16:41:27.335Z`. **The advisory record's own published date is authoritative**; fall back to the CVE date. |
| " | " | `…advisory.published_date` | `date` | Retain explicitly — `@timestamp` alone loses the distinction once a fallback is used |
| Advisory last-updated | RECON, Discourse `updated_at` | `…advisory.updated_date` | `date` | **No ECS field.** `event.created` is "when first created", not "when last updated" — do not misuse it. |
| CVE `dateReserved` | CVE5 | `…advisory.reserved_date` | `date` | `2026-03-20T10:53:23.099Z` — ~19 days before publication |
| CVE `datePublished` | CVE5 | `…advisory.cve_published_date` | `date` | Kept separate from the ESA publication date |
| CVE `dateUpdated` | CVE5 | `…advisory.cve_updated_date` | `date` | Changes when CISA ADP enriches, independent of Elastic |
| Git last commit date | GIT | `…advisory.git.last_commit_date` | `date` | Collection-side provenance, not advisory semantics |

The ESA **year** in the ID and the publication **date** are independent: `ESA-2024-20` was posted
2025-05-01. Nothing should derive one from the other.

### 3.8 References

| Source field | Source | ECS / custom target | Type | Notes |
|---|---|---|---|---|
| `discuss.elastic.co` advisory URL | RECON `discuss_url`, CVE5 `references[].url` | `vulnerability.reference` | `keyword` | ECS |
| " | " | `event.reference` | `keyword` | ECS |
| " | " | `event.url` | `keyword` | ECS |
| " | " | `url.original`, `url.full` | `wildcard` (+ `.text`) | ECS. `url.full`/`url.original` are `wildcard` in ECS, not `keyword`. |
| " parsed | derived | `url.scheme`, `url.domain`, `url.path` | `keyword`, `keyword`, `wildcard` | ECS |
| Discourse topic ID (`385812`) | derived from the URL | `…advisory.discuss_topic_id` | `long` | The only durable Discourse handle |
| Full reference list (upstream CVE links, vendor advisories, release notes) | CVE5 `references[]` | `…advisory.references` | `keyword[]` | Multi-valued. `url.*` holds only the primary. |

### 3.9 Git provenance

Every field here is custom. See §2.4 for why the blob SHA must not go in `file.hash.sha1` and why
`url.*` is reserved for the advisory URL.

| Source field | Source | ECS / custom target | Type |
|---|---|---|---|
| Repo owner (`elastic`) | GIT / config | `…advisory.git.owner` | `keyword` |
| Repo name (`security-advisories`) | GIT / config | `…advisory.git.repository` | `keyword` |
| Branch / ref (`main`) | GIT / config | `…advisory.git.ref` | `keyword` |
| File path | GIT Trees `path` | `file.path` (+ `.text`) | `keyword` |
| " | " | `…advisory.git.path` | `keyword` |
| Directory | derived | `file.directory` | `keyword` |
| File name | derived | `file.name` | `keyword` |
| Extension | derived | `file.extension` | `keyword` |
| File size | GIT Trees `size` | `file.size` | `long` |
| " | " | `…advisory.git.size` | `long` |
| Blob SHA | GIT Trees `sha` | `…advisory.git.blob_sha` | `keyword` |
| Commit SHA | GIT Commits | `…advisory.git.commit_sha` | `keyword` |
| Last commit date | GIT Commits | `…advisory.git.last_commit_date` | `date` |
| GitHub HTML URL for the file | derived | `…advisory.git.html_url` | `keyword` |
| Generator fingerprint (`Elastic CVE Publisher 0.0.1`) | CVE5 `x_generator.engine` | `…advisory.generator` | `keyword` |

Duplicating path and size into both `file.*` and `…advisory.git.*` is a judgement call: `file.*`
gives cross-integration query symmetry, and the `git` sub-group keeps the provenance block coherent
and self-describing. If only one is wanted, keep `file.*` for path/name/extension/size and the
`git` sub-group for everything with no ECS home.

---

## 4. Mapping types

### 4.1 Long Markdown prose blocks

Affected: `…advisory.body`, `.workarounds`, `.indicators_of_compromise`,
`.affected_configurations`, `.serverless_statement`, `.solution`, `.acknowledgements`,
`.update_log`.

**Recommendation: `match_only_text`.**

Reasoning:

- These are **read in a document flyout and full-text searched**. Nobody aggregates on the exact
  byte-string of a workaround paragraph, so the `keyword` capability is dead weight.
- They routinely exceed `keyword`'s conventional `ignore_above: 1024`. `ESA-2025-14`'s workaround
  is a multi-step numbered procedure with inline code and API links; `ESA-2021-31`'s body is 35 KB.
  A `keyword` over `ignore_above` is silently not indexed — searchable neither by term nor by
  phrase — which is a quiet correctness failure.
- `match_only_text` is the ECS default for the same class of content (`message` is
  `match_only_text`; every ECS `.text` multi-field is `match_only_text`). It drops norms and term
  frequencies and reconstructs positions from `_source`, which is the right trade for prose that is
  searched but never relevance-ranked against a corpus.
- Plain `text` would be the choice only if BM25 scoring quality across advisories mattered. It does
  not, even at the corrected corpus size of 1,000-3,000 documents (times revisions, given the
  fingerprint `_id`) — relevance ranking across a few thousand advisories is not the use case.
- The repo agrees: `match_only_text` appears in 108 package `fields/*.yml` files, and
  `github/security_advisories` maps `github.security_advisory.description` to `match_only_text`
  (`packages/github/data_stream/security_advisories/fields/fields.yml`).

**Two exceptions:**

1. `vulnerability.description` is an ECS field and its shape is not negotiable: `keyword` primary
   with a `vulnerability.description.text` (`match_only_text`) multi-field. Descriptions are short
   enough (ESA-2026-24's is ~530 characters) that the keyword side is usable.
2. `…advisory.title` should be `keyword` **with** a `match_only_text` multi-field. Titles are short,
   bounded, and genuinely worth aggregating on ("how many `Incorrect Authorization` advisories?"),
   while also worth searching as text.

`…advisory.subject`, `.component`, and `.discovery` are short and bounded: plain `keyword`.

### 4.2 The version-range array — `nested`, not `object`, not `flattened`

**Recommendation: `nested`.** This is not a preference; `object` gives wrong answers.

The query that matters is *"is version X of product P affected by this advisory?"* Answering it
requires correlating three values **within the same range object**: `product`, the lower bound
(`version`), and the upper bound (`less_than_or_equal` / `less_than`).

ESA-2026-24 has three ranges:

```
{version: 8.0.0, lessThanOrEqual: 8.19.13}
{version: 9.0.0, lessThanOrEqual: 9.2.7}
{version: 9.3.0, lessThanOrEqual: 9.3.2}
```

Under the default `object` mapping, Elasticsearch flattens the array into parallel scalar lists:

```
affected_versions.version              = [8.0.0, 9.0.0, 9.3.0]
affected_versions.less_than_or_equal   = [8.19.13, 9.2.7, 9.3.2]
```

Now ask "is Kibana **8.19.20** affected?" — a real question, because 8.19.20 exists and is *not*
affected (the fix shipped in 8.19.14). The query is `version <= 8.19.20 AND less_than_or_equal >=
8.19.20`. Clause 1 matches on `8.0.0`. Clause 2 matches on `9.2.7` and `9.3.2`. Both clauses are
satisfied by the document, so the document matches — **a false positive**, produced by pairing a
bound from one range with a bound from a different range. This is the textbook `nested` failure
mode, and it is aggravated here because Elastic maintains parallel release branches so
discontinuous ranges are the norm, not the exception (`esa-publication-landscape.md` §6.2).

`nested` forces both clauses to be satisfied by the *same* sub-document, which produces the
correct answer.

Rejected alternatives:

- **`object`** — wrong answers, as above.
- **`flattened`** — worse. `flattened` collapses every leaf to a `keyword` in one field, offers no
  numeric or version-aware comparison, no per-object isolation, and no range query at all. It is
  for unbounded unknown keys; these keys are a known, fixed set of seven.
- **A single rendered `keyword` string** (`">=8.0.0 <=8.19.13"`) — this is what
  `github/security_advisories` does (`vulnerable_version_range`, `type: keyword`) and what the
  community `esas.json` dataset does (`affected_ranges`). It is fine for **display** and for exact
  string matching, and worth keeping as `…affected_versions.range` alongside the structured fields,
  but it cannot answer "is X affected?" without client-side parsing.

**Nested-within-nested is not needed.** The CVE structure is
`affected[] → {vendor, product, versions[]}` — two levels. Rather than nesting `versions` inside a
nested `affected`, **denormalise `product` and `vendor` into each range object** and keep one
flat `nested` array. This handles multi-product advisories such as `ESA-2023-16` (Beats + Elastic
Agent + APM Server + Fleet Server) correctly, keeps the query a single `nested` clause, and avoids
the query complexity and indexing cost of two nesting levels.

**Precedent for `nested` on affected-package arrays:**
`packages/aws_securityhub/data_stream/finding/fields/fields.yml:3631-3636` declares both
`affected_code` and `affected_packages` as `type: nested`.

**Type of the bound fields: `version`, not `keyword`.** `keyword` range queries compare
lexicographically, and semver breaks under that: `"8.19.13" < "8.2.0"` lexically but `8.19.13 >
8.2.0` semantically. Since Elastic's version numbers routinely run into double-digit patch and
minor components (`8.19.13`, `9.3.2`, `8.19.20`), this is not theoretical — it is guaranteed to
produce wrong answers. Elasticsearch's `version` field type exists for exactly this and sorts
semver-aware. Non-semver values (`versionType: custom`, and the one-off `1.x.x` / `8.x.x`) are
accepted rather than rejected; they simply sort after valid versions. `version` is in the mapping
matrix and is already used in the repo:
`packages/tenable_sc/data_stream/plugin/fields/fields.yml:190-191`,
`packages/checkpoint_harmony_endpoint/data_stream/*/fields/fields.yml`.

`keyword` is the safe fallback if `version` proves problematic, at the cost of correct range
comparison.

**Open shape to flag:** the ESA prose has forms the CVE structure cannot express —
`7.x: All versions` (whole series affected, no upper bound, typically EOL) and single-version
statements (`Version N.N.N`). The unbounded case needs a deliberate representation (omit the upper
bound and rely on `status`, rather than inventing a sentinel).

### 4.3 CVSS score — `float`, and the choice is not yours

ECS defines `vulnerability.score.base` as **`float`** (verified in v9.3.0 through `main`). Declaring
it `external: ecs` inherits `float`. Overriding to `double` would diverge from ECS for no benefit.

On the merits `float` is also correct: CVSS base scores are one-decimal values in [0.0, 10.0].
IEEE-754 single precision gives ~7 significant decimal digits, roughly six orders of magnitude more
than needed. The familiar `7.7 → 7.699999809265137` artefact is a display concern, not a precision
one, and it applies equally to every ECS score field across every integration.

The custom mirror `…advisory.cvss.base_score` should also be `float`, for consistency and so the
two never disagree on a round-trip. Repo precedent: `github/security_advisories` converts its CVSS
scores with `type: float` (`default.yml:71-76`, `95-100`, `114-119`) and declares them `float`.

`vulnerability.score.temporal` and `.environmental` exist in ECS but should be left unset — Elastic
publishes base metrics only. The one apparent exception, `ESA-2025-14`'s
`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/MPR:L`, splices a *modified* privileges-required
metric onto a string labelled as the base vector. It is a data defect, not an environmental score;
mapping it to `.environmental` would be inventing a value that was never computed.

### 4.4 `vulnerability.severity` casing

ECS attaches **no `allowed_values`** to `vulnerability.severity` (verified in
`temp/ecs/ecs-9.3.0.yml`), so there is no schema-level constraint. The documented example is
`Critical` — Title Case.

The repo is genuinely split:

- **lowercased**: `packages/github/data_stream/dependabot/…/default.yml:318`,
  `packages/xm_cyber/data_stream/vulnerability/…/default.yml:451`,
  `packages/jupiter_one/data_stream/asset/…/pipeline_risks_and_alerts.yml:429`. And
  `github/security_advisories` copies GitHub's raw value through unchanged, which is lowercase —
  its own `sample_event.json` shows `"severity": "unknown"`.
- **Title Case**: `packages/tenable_io/data_stream/vulnerability/…/default.yml:525` sets `None`.
- **`cdr-field-requirements.md`** mandates `Low`, `Medium`, `High`, `Critical`, `None`.

**Recommendation: Title Case** — `Low` / `Medium` / `High` / `Critical`.

Three reasons: it matches the ECS documented example; it matches the only cross-cutting written
guidance that exists (the CDR field requirements); and, conveniently, **it is already exactly what
the ESA prose emits** (`esa-publication-landscape.md` §6.4 confirms `Low`, `Medium`, `High`,
`Critical` are the only labels used), so it is a pass-through with no case transformation and no
risk of mangling an unexpected value. Note the CVE record's `baseSeverity` is upper-case (`HIGH`),
so if the CVE record is the source rather than the prose, a normalisation is needed.

`None` is in the CDR enum but has never appeared in an ESA. Do not synthesise it.

### 4.5 Every proposed field, with its type

**ECS fields** (types inherited from ECS, listed for completeness):

| Field | Type |
|---|---|
| `@timestamp` | `date` |
| `ecs.version` | `keyword` |
| `event.kind`, `.category`, `.type`, `.id`, `.reference`, `.url`, `.original` | `keyword` (`.category`/`.type` arrays) |
| `event.dataset`, `event.module` | `constant_keyword` (single value per stream/package) |
| `data_stream.type`, `.dataset`, `.namespace` | `constant_keyword` |
| `tags` | `keyword[]` |
| `message` | `match_only_text` |
| `observer.vendor`, `observer.product` | `keyword` — `constant_keyword` is the better choice (one value per package) |
| `vulnerability.id`, `.report_id`, `.enumeration`, `.classification`, `.severity`, `.reference` | `keyword` |
| `vulnerability.scanner.vendor` | `keyword` — `constant_keyword` is the better choice |
| `vulnerability.description` | `keyword` + `.text` (`match_only_text`) |
| `vulnerability.score.base` | `float` |
| `vulnerability.score.version` | `keyword` |
| `package.name` | `keyword` |
| `file.path` | `keyword` + `.text` (`match_only_text`) |
| `file.directory`, `file.name`, `file.extension` | `keyword` |
| `file.size` | `long` |
| `url.original`, `url.full`, `url.path` | `wildcard` (`.original`/`.full` carry `.text` multi-fields) |
| `url.scheme`, `url.domain` | `keyword` |

**Custom fields** under `elastic_security_advisories.advisory.*`:

| Field | Type |
|---|---|
| `esa_id`, `cve_id`, `subject`, `component`, `vendor`, `default_status`, `discovery`, `generator`, `discuss_url` | `keyword` |
| `esa_year`, `esa_sequence` | `integer` |
| `discuss_topic_id` | `long` |
| `title` | `keyword` + `match_only_text` multi-field |
| `products`, `fixed_versions`, `references`, `upstream_cve_ids`, `workaround_deployment_types` | `keyword[]` |
| `body`, `solution`, `affected_configurations`, `workarounds`, `indicators_of_compromise`, `serverless_statement`, `acknowledgements`, `update_log` | `match_only_text` |
| `has_workarounds`, `has_indicators_of_compromise`, `serverless_affected`, `is_third_party_dependency` | `boolean` |
| `published_date`, `updated_date`, `reserved_date`, `cve_published_date`, `cve_updated_date` | `date` |
| `cvss.version`, `.base_severity`, `.vector_string`, `.attack_vector`, `.attack_complexity`, `.privileges_required`, `.user_interaction`, `.scope`, `.confidentiality_impact`, `.integrity_impact`, `.availability_impact` | `keyword` |
| `cvss.base_score` | `float` |
| `cwe.id`, `cwe.title`, `capec.id`, `capec.title` | `keyword` |
| `credits.value`, `credits.type` | `keyword` |
| `affected_versions` | **`nested`** |
| ↳ `.vendor`, `.product`, `.status`, `.version_type`, `.range` | `keyword` |
| ↳ `.version`, `.less_than`, `.less_than_or_equal` | `version` |
| `git.owner`, `.repository`, `.ref`, `.path`, `.blob_sha`, `.commit_sha`, `.html_url` | `keyword` |
| `git.size` | `long` |
| `git.last_commit_date` | `date` |

No field needs `flattened`. No field needs `wildcard` beyond what ECS already assigns to `url.*`.
No field is a metric, so no `metric_type`, `unit`, or `dimension` applies anywhere.

---

## 5. `related.*` and `tags`

### 5.1 `related.*` — honest answer: nothing belongs here

ECS `related` has exactly four members (verified, v9.3.0 through `main`):

| Field | Type | Content in an ESA |
|---|---|---|
| `related.ip` | `ip[]` | **None.** No advisory in the sample set contains an IP address. |
| `related.hosts` | `keyword[]` | **None.** No hostnames. |
| `related.user` | `keyword[]` | **None.** No usernames. |
| `related.hash` | `keyword[]` | **None.** No file or artifact hashes. |

**Recommendation: leave all four unset.** Populating them would be inventing data.

The three tempting-but-wrong candidates, spelled out so nobody re-litigates them:

1. **`related.hosts` ← `discuss.elastic.co`.** No. `related.hosts` is for hostnames of *hosts
   involved in the event*. A URL's domain is already correctly represented by `url.domain`. Putting
   it in `related.hosts` would pollute host-pivot searches with a documentation domain that appears
   on every single advisory.
2. **`related.hash` ← the git blob SHA.** No. `related.hash` exists so an analyst can pivot from a
   malware hash in one event to the same hash in another. A git object hash of an advisory file is
   not that kind of hash and will never legitimately match anything else in the cluster.
3. **`related.user` ← the credited researcher.** No. Acknowledgements name external researchers and
   organizations ("AISLE Research"), not user accounts in the estate. It would never match a
   `user.name` from any other data source, and it would add noise to identity pivots.

`cdr-field-requirements.md` does state "CDR integrations MUST populate `related.*`" — but that
requirement is scoped to CDR findings that have a resource, actor IPs, and IAM users. This is not a
CDR stream (§1.2), and there is nothing to populate. Non-population here is the correct outcome,
not a gap.

The genuinely useful cross-data-source pivots for this corpus are `vulnerability.id` (CVE) and
`package.name` (product) — both already mapped. That is what makes an ESA record joinable, and it
is the whole point of `event.kind: enrichment`.

### 5.2 `tags`

`tags` (`keyword[]`, ECS base fieldset) carries stream provenance markers, not advisory content.
The observed convention in the closest analogue
(`packages/github/data_stream/security_advisories/sample_event.json`) is
`["forwarded", "github-security-advisories"]`, i.e. the generic `forwarded` marker plus a
package/stream identifier. The analogous value here is
`["forwarded", "elastic-security-advisories"]`.

These come from the input configuration, not from the advisory data, so there is nothing to derive
and nothing to parse.

**Do not use `tags` for advisory attributes.** The tempting candidates —
"has-workarounds", "serverless-affected", "third-party-dependency", the severity label — all have
proper typed homes already (`…advisory.has_workarounds` as `boolean`,
`…advisory.serverless_affected` as `boolean`, `…advisory.is_third_party_dependency` as `boolean`,
`vulnerability.severity` as `keyword`). Duplicating them into `tags` gives an untyped, unaggregatable
second representation that will drift.

`labels.*` is the one ECS object exempt from the vendor-prefix rule and is available for ad-hoc
key-value markers, but nothing in an ESA needs it — every field here is known in advance and
deserves a real type.

---

## 6. Sample mapped document

Written to:

```
research_results/elastic_security_advisories/references/sample-events/ESA-2026-24.mapped-ecs.json
```

It is the fully-mapped ECS document for **ESA-2026-24 / CVE-2026-33461**, built from
`references/sample-events/ESA-2026-24.md` (the verbatim advisory body) and
`references/sample-events/ESA-2026-24.cve-record-5.1.json` (the CVE Record 5.x twin). ESA-2026-24
was chosen because it is the fullest modern template — every optional section is present, including
Affected Configurations, For Users that Cannot Upgrade, Indicators of Compromise, and the Elastic
Cloud Serverless block — and because its CVE record supplies all eight decomposed CVSS metrics.

The file carries two comment blocks that are part of its value:

- `_comment_provenance` — source URLs, ECS verification basis, and an explicit `[UNVERIFIED]`
  marker on the entire `git.*` block, whose values are format-valid synthetic placeholders because
  `elastic/security-advisories` returns HTTP 404 from this environment.
- `_comment_deliberately_absent` — the fields that are **not** in the document and why, so a
  downstream builder does not read their absence as an oversight: all four `related.*` members,
  `host.*`/`user.*`/`source.*`/`cloud.*`, `package.version`,
  `vulnerability.score.temporal`/`.environmental`, `vulnerability.status`,
  `vulnerability.category`, `event.outcome`, `event.action`.

---

## 7. Gaps, open questions, and things the builder must decide

1. **The repo file format is unverified.** `elastic/security-advisories` is private and 404s from
   here. Every "source field" in §3 marked `RECON` comes from the reasoned reconstruction in
   `esa-publication-landscape.md` §5.3, not from an observed schema. The mapping *targets* are firm
   — they are driven by what the advisory *contains*, which is fully observable from the public
   corpus — but the source-side field names are `[UNVERIFIED]` and will need a pass once someone
   with repo access can look. `[UNVERIFIED]`
2. **Whether the repo record carries the ESA-only sections at all.** If the repo file turns out to
   be CVE Record 5.x JSON rather than a superset, then fixed versions, affected configurations,
   workarounds, IOC guidance, the Serverless statement, and the ESA ID itself are all absent from it
   and must come from the Discourse body. That would change the collection design, not this mapping.
   `[UNVERIFIED]`
3. **Multi-ESA advisories.** Several historical topics carry two ESA IDs in one post
   (`ESA-2023-07, ESA-2023-08`; `ESA-2024-27, ESA-2024-28`; `ESA-2024-32, ESA-2024-33`). If the repo
   mirrors that, the "one document = one advisory" assumption breaks and `esa_id` becomes
   multi-valued — which in turn breaks the `_id` fingerprint. Every 2025–2026 post examined carries
   exactly one ID, so this may be historical only. `[UNVERIFIED]`
4. **Unbounded version ranges.** `7.x: All versions` has no upper bound and the CVE structure has no
   way to say so. Omitting the upper bound and relying on `status` is the cleanest representation,
   but it makes "is 7.17.99 affected?" a two-branch query. Worth a deliberate decision.
5. **`vulnerability.scanner.vendor`.** Recommended as `Elastic` on precedent
   (`ti_google_threat_intelligence`), but Elastic is not a scanner, and the closest analogue
   (`github/security_advisories`) omits it. Low stakes either way; flagging that it is a judgement
   call, not a derivation.
6. **CVSS v4.0.** Only 2 of 340 Elastic CVE records use `cvssV4_0`. The v4 metric set differs
   substantially from v3.1 (`attackRequirements`, `vulnerable*`/`subsequent*` impact splits), so the
   decomposed `…advisory.cvss.*` fields in §3.2 are v3.1-shaped and would need extension if Elastic
   migrates. `vulnerability.score.base` and `.score.version` are version-agnostic and unaffected.
   The precedent for carrying both metric sets side by side is
   `packages/hackerone/data_stream/report/fields/fields.yml`, which keeps a separate
   `cvss_4_point_0_metrics` group alongside its v3 fields rather than overloading one set.
7. **Product-name normalisation.** `package.name` is only useful as a join key if
   `Kibana`/`kibana`, `Elastic Cloud Enterprise`/`Elastic Cloud Enterprise (ECE)`, and the three
   spellings of Enterprise Search collapse to canonical values. No such table exists; someone has to
   write one. The raw form should be retained in `…advisory.products` regardless.
8. **Revision collapse.** The recommended `_id` (ESA ID + blob SHA) preserves every amendment as its
   own document. Whether "current state per ESA ID" should be materialised, and where, is an open
   design question — and note that `entity-mappings/SKILL.md` explicitly lists latest-transform
   policy as unresolved deferred scope.
9. **Two representations of the same bytes.** `event.original` (the verbatim advisory file) and
   `…advisory.body` (the advisory body as prose) carry largely overlapping content, and `message`
   is a third possible home for the latter. That overlap is a property of the data worth flagging;
   which representations a data stream keeps is not a research question.
