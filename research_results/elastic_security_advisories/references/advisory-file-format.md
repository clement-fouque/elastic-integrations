# On-disk file format of Elastic Security Advisories (`elastic/security-advisories`, `advisories/`)

**Scope.** Targeted hunt for public evidence about the format of the JSON files in the private
repository `elastic/security-advisories`, directory `advisories/`.

**Sole direct observation of repo contents** (reported by a human with repo access, not
independently verifiable from public sources):

```
ESA-2026-0081.json
```

**Evidence labels used throughout.**

| Label | Meaning |
|---|---|
| `[VERIFIED-LIVE]` | I fetched it / ran it and observed the result during this investigation |
| `[VERIFIED-DOC]` | Official documentation or specification states it |
| `[HUMAN]` | Reported by the human with private-repo access; more authoritative than public inference, but unverifiable here |
| `[UNVERIFIED]` | My inference or hypothesis |

**Bottom line up front.** No public artifact reveals the JSON schema of these files. Every
standard schema that could plausibly match the filename can be ruled out or heavily discounted
on concrete, specific grounds, leaving **a bespoke Elastic-internal schema as the most likely
answer**. The single best public proxy for its field set is the Elastic-authored CVE 5.x records
plus Elastic's own documented list of "what each advisory includes."

---

## 1. What the filename proves

Direct deductions from `advisories/ESA-2026-0081.json`. All of these follow from the filename
plus corroborating public evidence; the filename itself is `[HUMAN]`.

### 1.1 Serialization is JSON, one advisory per file

`[HUMAN]` + `[UNVERIFIED]` inference. The `.json` extension establishes JSON, not
Markdown-with-YAML-front-matter (which is what the Elastic Security Labs advisory-drafting
pipeline emits — see §4.2 — and so was a live alternative hypothesis worth killing).

The filename **is** the advisory identifier with no other component, which is the canonical
"one record per file, keyed by vulnerability ID" layout used by every major open vulnerability
database. Verified layouts of the three comparable databases:

| Database | Path convention | Evidence |
|---|---|---|
| GitHub Advisory Database | `advisories/github-reviewed/2026/08/GHSA-2223-f22x-24cq/GHSA-2223-f22x-24cq.json` | `[VERIFIED-LIVE]` `GET https://api.github.com/repos/github/advisory-database/contents/advisories/github-reviewed/2026/08/GHSA-2223-f22x-24cq` |
| CVE Program `cvelistV5` | `cves/2026/49xxx/CVE-2026-49000.json` | `[VERIFIED-LIVE]` `GET https://api.github.com/repos/CVEProject/cvelistV5/contents/cves/2026/49xxx` |
| OSV.dev distribution | `gs://osv-vulnerabilities/<ECOSYSTEM>/<ID>.json` | `[VERIFIED-DOC]` <https://google.github.io/osv.dev/data/> |

Note that GitHub's own database also uses a top-level directory literally named `advisories/`
— the same name Elastic uses. That is a structural echo, not evidence of a shared schema.

### 1.2 The ESA ID is the primary key, and it is *not* interchangeable with a CVE ID

`[VERIFIED-LIVE]`. The filename carries no product name and no CVE ID, so both must live inside
the document. This matters because the ESA↔CVE relationship is many-to-many. Measured over the
340 Elastic-assigned CVE 5.x records in `temp/cve5/` by extracting `esa-YYYY-NN` from the
`discuss.elastic.co` reference URLs:

```
distinct ESA ids seen in CVE refs: 185
distinct CVEs with an ESA ref:     187
ESAs mapping to >1 CVE:            8    e.g. ESA-2023-30 -> [CVE-2023-49922, CVE-2023-6687]
CVEs mapping to >1 ESA:            6    e.g. CVE-2024-37285 -> [ESA-2024-27, ESA-2024-28]
```

`[VERIFIED-DOC]` Additionally, Elastic states that third-party dependency advisories get **no
new CVE ID** and instead reference the upstream CVE
(<https://www.elastic.co/community/security>): "If a vulnerability exists in a third-party
library or dependency bundled with our software, we do not assign a new CVE ID. Instead, the
ESA will reference the existing upstream CVE ID defined by the third party."

Consequence for an ingest pipeline: the ESA ID is the only safe document `_id`. A CVE ID is
neither unique nor guaranteed present.

### 1.3 Numbering is per-calendar-year and resets annually

`[VERIFIED-LIVE]`. The `2026` component is the year, and sequence numbers restart each year.
Observed public maxima per year (§5) show independent per-year sequences, e.g. 2024 reaches 48,
2025 reaches 39, 2026 reaches 137.

### 1.4 The zero padding is width 4, implying a design capacity of 9,999/year

`[HUMAN]` + `[UNVERIFIED]`. `0081` is `%04d`. Nobody selects a 4-digit field for a series that
runs at 39/year (Elastic's 2025 public rate). This is corroborating evidence that Elastic
expects — or already handles internally — a per-year volume in the hundreds to low thousands.
That is directly consistent with the observed 2026 public rate of ~222/year (§5) and with the
`[HUMAN]` claim of >1000 files in the directory.

### 1.5 Operational consequence: the GitHub Contents API cannot enumerate this directory

`[VERIFIED-DOC]`. This is the single most actionable finding for anyone building against the
repo. GitHub's documentation for `GET /repos/{owner}/{repo}/contents/{path}` states verbatim:

> This API has an upper limit of 1,000 files for a directory. If you need to retrieve more
> files, use the Git Trees API.

(Source: `temp/github-contents-api-doc.txt` line 26, GitHub REST "Get repository content".)

Since the human reports `advisories/` may hold **more than 1000 files**, the Contents API will
silently truncate. Enumeration must use the Git Trees API
(`GET /repos/{owner}/{repo}/git/trees/{tree_sha}?recursive=1`), and callers must check the
response's `truncated` flag.

---

## 2. ESA ID convention: padded vs unpadded

### 2.1 Verdict

**Both the public forum and the repo zero-pad; they use different widths.** The premise that
public ESA IDs are "NOT zero-padded" is incorrect — the public form is zero-padded to a
*minimum width of 2*. The repo pads to a *fixed width of 4*.

| Context | Convention | Rendering of sequence 8 / 81 / 137 |
|---|---|---|
| Public (Discourse titles, advisory bodies, blog, official prompt) | minimum width 2, i.e. `%02d` | `ESA-2026-08` / `ESA-2026-81` / `ESA-2026-137` |
| Private repo filename | fixed width 4, i.e. `%04d` | `ESA-2026-0008` / `ESA-2026-0081` / `ESA-2026-0137` |

### 2.2 Evidence: the padded 2-digit form is unambiguously public

`[VERIFIED-LIVE]`. I harvested the raw Markdown body of **all 315 topics** in the Elastic
Discourse security-announcements category (category 31, 2015-06-06 through 2026-08-13) to
`temp/format-hunt/raw_all/`, then censused every `ESA-YYYY-NN` string across those bodies plus
all 315 topic titles/slugs plus all 340 CVE 5.x records.

Suffix-width distribution across advisory bodies:

```
suffix_digits=2 leading_zero=False -> 181 occurrences
suffix_digits=2 leading_zero=True  ->  88 occurrences
4-digit suffix (ESA-YYYY-NNNN)     -> NONE
3-digit with leading zero (0NN)    -> NONE
single-digit unpadded (ESA-YYYY-N) -> NONE
```

So: **88 public occurrences of the zero-padded form, and zero occurrences of an unpadded
single-digit form anywhere in the entire public corpus.**

Representative `[VERIFIED-LIVE]` examples, spanning 2017–2026, showing the convention is stable
over nine years:

| ESA ID | Where observed |
|---|---|
| `ESA-2017-24` | Body of discuss topic 112520: "**Kibana arbitrary code execution issue (ESA-2017-24)**" |
| `ESA-2019-08` | Body of discuss topic 192960: "**Elastic APM agent for Ruby client authentication flaw (ESA-2019-08)**" |
| `ESA-2020-05`, `-06`, `-07` | Body of discuss topic 235571 (one topic, three advisories) |
| `ESA-2021-18`, `-19`, `-20` | Body of discuss topic 280344 |
| `ESA-2024-01` | Topic title "Kibana 8.12.1 Security Update (ESA-2024-01)", slug `...-esa-2024-01` |
| `ESA-2025-01` | Topic title "APM Server (Windows Installer) 8.16.3, 8.17.1 Security Update (ESA-2025-01)" |
| `ESA-2026-01` … `ESA-2026-09` | Nine separate topics, e.g. "Metricbeat 8.19.10, 9.1.10, 9.2.4 Security Update (ESA-2026-01)" |

`[VERIFIED-DOC]` Two official Elastic sources independently document the 2-digit padded form as
the canonical rendering:

1. Elastic's own agent prompt in the public `elastic/elasticsearch-labs` repo defines the field
   as: "**ESA Number** — The internal Elastic Security Advisory identifier (e.g.,
   **ESA-2025-01**)."
   (<https://github.com/elastic/elasticsearch-labs/blob/main/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder/agent-creation-prompt.md>,
   line 34 of the local copy at `temp/agent-creation-prompt.md`.)
2. The Elastic Security Labs blog announcing that pipeline uses the same form in prose:
   "**ESA-2026-01** is already in production as an example of output that went through this
   pipeline."
   (<https://www.elastic.co/security-labs/security-advisory-automation-rag-elastic-agent-builder>)

Note the prompt's wording — "the **internal** Elastic Security Advisory identifier" — which is
consistent with the ID originating in an internal system of record (the repo) and being
projected outward.

### 2.3 The 4-digit form is never public

`[VERIFIED-LIVE]`. Regex sweeps for `ESA-\d{4}-0\d{3}` and `ESA-\d{4}-\d{4}` across the entire
research corpus — all 315 harvested advisory bodies, `temp/cat31_all_topics.json` (315 topics),
`temp/cat31.rss`, all 340 Elastic CVE 5.x records in `temp/cve5/`, `temp/nvd_elastic_all.json`,
all `temp/osv_*.json` samples, `temp/community_security.html`, and
`temp/format-hunt/product-security.html` — returned **zero matches**.

The padded 4-digit form appears to exist only inside the private repo.

### 2.4 `ESA-2026-0081` and `ESA-2026-81` are almost certainly the same advisory

`[UNVERIFIED]` conclusion resting on `[VERIFIED-LIVE]` facts. Advisory 81 of 2026 exists
publicly:

- **Topic 389501**, created `2026-08-13T10:47:06.886Z`
- Title: *Elasticsearch 8.19.20, 9.4.5 Security Update (ESA-2026-81)*
- URL: <https://discuss.elastic.co/t/elasticsearch-8-19-20-9-4-5-security-update-esa-2026-81/389501>
- Body (via <https://discuss.elastic.co/raw/389501>): "Uncontrolled Recursion in Elasticsearch
  Leading to Denial of Service"
- **CVE ID:** CVE-2026-72679
- **Problem Type:** CWE-674 — Uncontrolled Recursion
- **Severity:** CVSSv3.1 Medium (6.5), `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H`
- Affected: 8.19.0–8.19.19, 9.0.0–9.4.4; fixed in 8.19.20 and 9.4.5

I cannot prove identity without repo access, but there is only one plausible per-year sequence
and `81 == 0081` under any sane interpretation.

**This gives a cheap, decisive first test the moment anyone gets repo access:** open
`advisories/ESA-2026-0081.json` and check whether it describes CVE-2026-72679 / CWE-674 /
Elasticsearch. If yes, the repo ID space is confirmed identical to the public one modulo
padding. If it describes something else, the repo uses a *different* numbering space and every
join assumption below must be rebuilt.

### 2.5 Normalization an ingest pipeline must perform

`[UNVERIFIED]` (design recommendation grounded in the verified facts above).

Do **not** join on the literal ID string. Canonicalize by parsing into `(year, sequence:int)`:

```python
m = re.fullmatch(r'(?i)ESA-(\d{4})-(\d+)', esa_id)
year, seq = int(m.group(1)), int(m.group(2))          # "ESA-2026-0081" -> (2026, 81)
canonical      = f"ESA-{year}-{seq:04d}"              # repo / storage form
forum_form     = f"ESA-{year}-{seq:02d}"              # matches Discourse titles for seq < 100
discourse_slug = f"esa-{year}-{seq}"                  # lowercase, no padding beyond %02d
```

Three specific gotchas:

1. **`%02d` is a *minimum* width, not fixed.** `f"{seq:02d}"` correctly yields `08`, `81`, and
   `137`. Naive fixed-width formatting breaks at 100+.
2. **Discourse slugs are lowercase.** Observed: `.../elasticsearch-8-19-20-9-4-5-security-update-esa-2026-81/389501`.
   Any regex extracting ESA IDs from URLs must be case-insensitive.
3. **Enrichment from CVE records requires slug parsing.** `[VERIFIED-LIVE]` The
   Elastic-authored CVE 5.x records carry **no structured ESA field at all**. The ESA ID is
   recoverable only by parsing it out of the `references[].url` Discourse slug. Full example
   (`temp/cve5/CVE-2026-49089.json`, generated by `Elastic CVE Publisher 1.0.0`) — its only
   reference is
   `https://discuss.elastic.co/t/kibana-8-19-20-9-4-5-security-update-esa-2026-137/389511`,
   and nowhere in the record does the string `ESA-2026-137` appear as a field value. Across all
   340 records, only **3** mention an ESA ID in free text at all (`ESA-2017-23` in
   CVE-2018-3819's description, `ESA-2023-25` in CVE-2023-46675, `ESA-2025-17` in
   CVE-2025-37732) — all narrative prose, none structured.

---

## 3. Candidate schemas, evaluated

| Candidate | Verdict | Evidence | Confidence |
|---|---|---|---|
| **Bespoke Elastic schema** | **Most likely** | Every standard alternative has a concrete disqualifier (below). Elastic ships a purpose-built `Elastic CVE Publisher` engine (§4.1) that must read *some* internal record to emit CVE 5.x, and the ESA ID is the primary key of that record rather than a CVE ID (§1.2). No public schema, registry entry, or feed exists for ESA records anywhere. | High |
| **CVE Record Format 5.x** (`cve-schema`) | Unlikely as-is; plausible as an *embedded sub-object* | Elastic is a CNA (`CNA-2017-0011`, `assignerOrgId 271b6943-45a9-4f3a-ab4e-976f3fa05b5a`) and demonstrably produces 5.x JSON. **But:** (a) the CVE convention is to name the file by CVE ID — verified `cves/2026/49xxx/CVE-2026-49000.json`; naming a CVE record `ESA-...json` inverts the key; (b) ESA↔CVE is many-to-many (§1.2) so a CVE record cannot be the whole document; (c) third-party-dependency ESAs have **no Elastic-assigned CVE** at all `[VERIFIED-DOC]`; (d) CVE 5.x has no field for the IOC / "For Users that Cannot Upgrade" / Serverless-remediation content that every published ESA carries (§4.3). | Medium-high (as a ruling-out) |
| **OSV schema** (`ossf/osv-schema`) | Strong *structural* analogy, but almost certainly not the format | Filename-equals-vuln-ID is exactly the OSV convention `[VERIFIED-DOC]` `gs://osv-vulnerabilities/<ECOSYSTEM>/<ID>.json`. **But:** (a) `ESA` is **not** among OSV's 47 registered database prefixes — verified full list contains `ELA` and `OESA` but no `ESA`; (b) OSV requires local/non-aggregated databases to use an `x_` prefix (`x_ESA-2026-0081`), which the filename does not; (c) `GET https://api.osv.dev/v1/vulns/{ESA-2026-0081, ESA-2026-81, ESA-2025-01, ESA-2024-01}` all return **HTTP 404** `{"code":5,"message":"Vulnerability not found"}`; (d) Elastic is absent from the osv.dev data-source list; (e) zero mentions of "elastic" or "ESA" in `osv-schema`'s README or `docs/schema.md`, and zero ESA-prefix requests in that repo's issues; (f) no OSV/GHSA record carries an `ESA-` alias — the GitHub advisory objects in `temp/gh_adv_*.json` expose only `GHSA` and `CVE` identifier types, and `ESA-` appears in none of the `temp/osv_*.json` samples. | High |
| **CSAF 2.0 JSON** | **Ruled out** | Two independent disqualifiers. (1) `[VERIFIED-DOC]` CSAF 2.0 §5.1 mandates that the filename be `/document/tracking/id` **converted into lower case** with non-`[+\-a-z0-9]` runs replaced by `_`. A CSAF-conformant file for tracking ID `ESA-2026-0081` would therefore be `esa-2026-0081.json`; the observed filename is uppercase. (2) `[VERIFIED-LIVE]` CSAF distribution Requirements 7/8/9 mandate `provider-metadata.json` at a well-known URL plus `security.txt`; `https://www.elastic.co/.well-known/csaf/provider-metadata.json` → **404**, `https://www.elastic.co/.well-known/security.txt` → **404**, `security.elastic.co` → NXDOMAIN. Elastic is not a CSAF publisher. | High |
| **GitHub repository-advisory JSON** | Ruled out | GitHub repository security advisories are API objects, not repo files; and GitHub's file-based database is `[VERIFIED-DOC]` "formatted in the Open Source Vulnerability (OSV) format" (`github/advisory-database` README line 17), so this candidate collapses into the OSV row. Its leaf files are also named by GHSA ID, not by a vendor ID. | High |
| **ECS-shaped JSON** (`vulnerability.*` fieldset) | Interesting historical lead; likely not the format | See §4.4 — Elastic Product Security publicly stated in 2020 that the plan was to publish advisories "in ECS format," but the required ECS changes never landed and the ECS `vulnerability.*` fieldset cannot express core advisory content. | Medium |

---

## 4. Best available evidence on the actual schema

**No public artifact contains the schema, an example advisory JSON, or a field list for these
files.** I searched exhaustively; §6 lists what that leaves open. What follows is the strongest
indirect evidence, strongest first.

### 4.1 Elastic operates purpose-built advisory publishing automation that went 1.0.0 in 2026

`[VERIFIED-LIVE]`. The `x_generator.engine` field across the 340 Elastic-assigned CVE 5.x
records reveals the tooling history precisely:

| Publish year | `x_generator.engine` values |
|---|---|
| 2017–2020 | none (136 records total have no `x_generator`) |
| 2021 | `Vulnogram 0.2.0` ×1 |
| 2023 | `Vulnogram 0.1.0-dev` ×23 |
| 2024 | `Vulnogram 0.2.0` ×15, `Vulnogram 0.1.0-dev` ×6 |
| 2025 | `Vulnogram 0.2.0` ×33, `Vulnogram 0.5.0` ×4, **`Elastic CVE Publisher 0.0.1` ×12** |
| 2026 | **`Elastic CVE Publisher 0.0.1` ×62, `Elastic CVE Publisher 1.0.0` ×48** |

Interpretation `[UNVERIFIED]`: Elastic moved off Vulnogram (a generic third-party web form for
authoring CVE 5.x records) onto a bespoke engine that first appears in 2025 and reaches 1.0.0
in 2026. A tool named "CVE **Publisher**" publishes *from* something. The private
`advisories/ESA-YYYY-NNNN.json` corpus is the natural candidate for that input, which would
make the ESA JSON a **superset source record** that the publisher projects into (a) a CVE 5.x
record for the CVE Program and (b) Discourse Markdown for the forum.

Corroborating timing: the 2026 public advisory rate is ~5.7× the 2025 rate (§5), exactly what
you would expect when publication becomes automated.

I found **no public repository, package, or documentation** for "Elastic CVE Publisher".
`[VERIFIED-LIVE]` `api.github.com/repos/elastic/{security-advisories, cve-publisher, cve,
advisories}` all return 404; `GET /search/repositories?q=org:elastic+advisor` returns
`total_count: 0`. Web search surfaces only the Security Labs blog and the prompt file.
Independent code-search engines were unusable (grep.app is behind a Vercel bot checkpoint;
searchcode.com returned non-JSON), and per the brief the `gh` token cannot use GitHub code
search.

### 4.2 The public advisory-drafting pipeline emits Markdown prose, not JSON — so it is not the schema

`[VERIFIED-DOC]`. I re-read the full prompt at `temp/agent-creation-prompt.md` (identical to the
only file in the public labs directory — `[VERIFIED-LIVE]`
`GET /repos/elastic/elasticsearch-labs/contents/supporting-blog-content/security-labs/security-advisory-automation-rag-elastic-agent-builder`
returns exactly one entry, `agent-creation-prompt.md`, 18535 bytes). Its `## OUTPUT FORMAT`
section is an explicit **Markdown template**, with headings like `**Affected Versions:**` and
`**Severity:** CVSSv3.1: [Severity Label] ( [Score] ) - [Vector String]`. There is no JSON
output contract, no JSON keys, and no schema anywhere in the prompt.

This is a genuine negative result and it matters: it means the *drafting* stage is prose, and
the JSON structure is imposed at a later stage the blog does not describe. The rendered public
advisories match that Markdown template near-verbatim — compare the prompt's template to the
live body of ESA-2026-81 (<https://discuss.elastic.co/raw/389501>), which reproduces the
section order exactly.

The prompt does, however, enumerate the **intake fields** Elastic's process treats as
first-class, which is the closest thing to a field list it offers:

1. Product Name, 2. ESA Number, 3. CVE Number, 4. Release Fix Versions, 5. Affected Versions —
plus derived Affected Configurations, Solutions and Mitigations, "For Users that Cannot
Upgrade", Indicators of Compromise, an Elastic Cloud Serverless block, Severity (CVSS v3.1
label + score + vector), Problem Type (CWE), and Impact (CAPEC).

### 4.3 Elastic officially documents what every advisory contains

`[VERIFIED-DOC]`. <https://www.elastic.co/community/security> states: "Each advisory includes:"

- An ESA identifier
- The applicable CVE ID (either Elastic-assigned or Upstream)
- A summary of the issue
- Affected Versions
- Remediation and mitigation details
- Severity rating using Common Vulnerability Scoring System (CVSS)

This is Elastic's own normative field list for an advisory record. Combined with §4.2's template
and the observed published bodies, the union of fields an `ESA-YYYY-NNNN.json` almost certainly
carries is:

ESA ID; title; product/vendor; affected version ranges; fixed versions; affected
configurations; summary/description; solutions and mitigations; cannot-upgrade workarounds
(sometimes split Self-Managed vs Cloud); IOC guidance; Elastic Cloud Serverless applicability;
CVSS v3.1 score + severity label + vector string; CWE ID and title; CAPEC ID and title; CVE ID;
and the Discourse publication URL.

Note `[VERIFIED-LIVE]` that the `cna` container of the Elastic CVE records uses exactly this
vocabulary (`affected[].versions[]` with `versionType: semver` and `lessThanOrEqual`,
`descriptions[]`, `metrics[].cvssV3_1`, `problemTypes[].descriptions[].cweId`,
`impacts[].capecId`, `title`, `references[]`, `source.discovery: "Elastic"` in 121 of 122
Publisher-generated records). If the ESA JSON were designed alongside the Publisher, reusing
CVE 5.x vocabulary for the overlapping fields would be the path of least resistance —
but that is `[UNVERIFIED]`.

### 4.4 A 2020 Elastic Product Security statement of intent: "publish all of our advisories in ECS format"

`[VERIFIED-LIVE]`, from `temp/thread_228477.md` /
<https://discuss.elastic.co/t/security-announcements-rss-versions/228477>. Josh Bressers,
Elastic Product Security, on 2020-04-17, replying to a request for machine-readable advisories:

> We are working on a project as we speak to tackle the challenges you lay out. It is going to
> take some time however. The plan is to publish all of our advisories in **ECS format** (this
> will also require some modifications to ECS), then allow the **JSON to be downloaded** as
> well as having a much nicer looking advisory page.

This is the only public statement I found from Elastic about advisories as JSON. It is six
years old and I judge it **weak evidence for the current format**, for three specific reasons:

1. `[VERIFIED-LIVE]` The promised deliverables never shipped. There is no downloadable advisory
   JSON and no advisory page: `https://www.elastic.co/security/advisories.json` → 404, and both
   `https://www.elastic.co/product-security` and `https://www.elastic.co/community/security`
   link out to the Discourse category and its RSS feed as the *only* ways to consume advisories
   ("How to stay informed: View Advisories: Elastic Security Announcements / Subscribe via
   Discuss / Subscribe via RSS Feed"). The CVE Program's CNA registry entry for `elastic`
   likewise lists only `https://www.elastic.co/community/security` as the advisories URL.
2. `[VERIFIED-LIVE]` The "modifications to ECS" never landed. The ECS `vulnerability` fieldset
   was added *before* this statement — commit history of `schemas/vulnerability.yml` shows it
   introduced 2019-11-19 by `peasead` in #581 — and the only subsequent commits are formatting,
   licensing, and the `match_only_text` migration (last substantive change 2021-11-18). Twelve
   commits total, none advisory-driven.
3. The ECS `vulnerability.*` fieldset is structurally incapable of representing an ESA.
   `[VERIFIED-LIVE]` its complete field list is `classification`, `enumeration`, `reference`,
   `score.{base,temporal,environmental,version}`, `category`, `description`, `id`,
   `scanner.vendor`, `severity`, `report_id`, `status`. There is **no** field for affected
   version ranges, fixed versions, mitigations, workarounds, IOCs, CWE, or CAPEC — i.e. most of
   an advisory. It is designed for vulnerability-*scanner findings*, not vendor advisories.

Worth flagging for the reader: an ECS-shaped ingest target is still the right *destination*
schema for an Elastic integration; this section is only about the *source* file format.

### 4.5 Explicitly not evidence: `temp/esa-search/`

`[VERIFIED-LIVE]`, flagged to prevent contamination. `temp/esa-search/esas.json` (244 records,
with keys `esa_id`, `title`, `url`, `affected_product`, `affected_ranges`, `fixed_version`,
`severity`) is **not** an Elastic artifact and reveals nothing about the private repo. Its own
README states the data is "sourced from the official Elastic Security Announcements forum," and
web search identifies the upstream as the community tool
<https://github.com/jmoon-elastic/esa-search>. It is a *derived forum scrape* whose field names
were invented by its author. Do not cite it as schema evidence.

---

## 5. Corpus size and layout

### 5.1 Public census: 341 distinct ESA IDs, 2016–2026

`[VERIFIED-LIVE]`. Method: harvest the raw Markdown body of all 315 topics in Discourse
category 31 (saved to `temp/format-hunt/raw_all/`, 315/315 fetched, 0 failures), then extract
every `ESA-YYYY-N{1,4}` from those bodies **plus** all 315 topic titles and slugs **plus** all
340 CVE 5.x records. Census written to `temp/format-hunt/esa_census_combined.json`.

Harvesting bodies rather than titles alone was essential: 134 ESA IDs appear only in bodies
(pre-2022 titles were CVE-based, e.g. "Elasticsearch remote code execution CVE-2015-5377", and
a single topic often bundled three advisories), while 110 appear only in titles (2026 bodies
omit the ESA ID entirely — it lives only in the topic title).

| Year | Distinct IDs found | Max sequence | Coverage | Gaps below max |
|---|---|---|---|---|
| 2016 | 4 | 10 | 40% | 6 |
| 2017 | 17 | 24 | 71% | 7 |
| 2018 | 19 | 19 | 100% | 0 |
| 2019 | 17 | 17 | 100% | 0 |
| 2020 | 15 | 16 | 94% | 1 |
| 2021 | 31 | 31 | 100% | 0 |
| 2022 | 14 | 14 | 100% | 0 |
| 2023 | 28 | 31 | 90% | 3 |
| 2024 | 44 | 48 | 92% | 4 |
| 2025 | 36 | 39 | 92% | 3 |
| 2026 (to Aug 13) | 116 | 137 | 85% | 21 |
| **Total** | **341** | — | — | **45** |

Sum of per-year maxima = **386**, a floor on the number of ESA IDs *allocated* 2016–2026.

Two supporting observations. `[VERIFIED-LIVE]` The harvest is current and complete: re-fetching
`https://discuss.elastic.co/c/announcements/security-announcements/31.json` live returned no
topic absent from the harvest, and the newest topics are dated 2026-08-13. And the ESA scheme
appears to begin in 2016 — the 10 topics from 2015 use CVE-only titles ("Kibana Cross-Site
Scripting Vulnerability CVE-2015-4093") and contain no ESA IDs.

### 5.2 Growth rate and a granularity change in 2026

`[VERIFIED-LIVE]` for the counts, `[UNVERIFIED]` for the explanation.

Published advisories ran 14–48/year from 2018 through 2025, then jumped sharply: 137 by
2026-08-13 (day 225), an annualized rate of **~222/year** and **~5.7× the 2025 figure**.

The most likely driver is a change in advisory *granularity* rather than a surge in
vulnerabilities: Elastic now issues one ESA per product-and-issue instead of bundling. Two
`[VERIFIED-LIVE]` data points support this. Bundling used to be routine — topic 280344 carries
ESA-2021-18, -19, and -20 in one post. And 2026's product distribution is dominated by
fine-grained per-product posts: of 116 topics, Kibana 73, Elasticsearch 25, Fleet Server 4,
Packetbeat 3, then single-digit counts for ECK, Logstash, Metricbeat, Elastic Defend, Kibana
Fleet, Elastic Package Registry, Elastic OTel Java, and Synthetics Recorder. The 2024 pairs
that share CVEs (ESA-2024-27 and -28 both → CVE-2024-37285 and CVE-2024-37288) look like the
transition: one vulnerability, two products, two ESA numbers. This aligns with the
`Elastic CVE Publisher 1.0.0` rollout (§4.1) and the AI drafting pipeline (§4.2), both of which
lower the marginal cost of issuing a separate advisory.

### 5.3 Reserved-but-unpublished IDs exist

`[VERIFIED-LIVE]`. 45 sequence numbers below the per-year maxima have no public advisory,
including 21 in 2026 alone (23, 31, 47, 48, 61, 62, 84, 85, 103, 107, 109, 114, 115, 117, 122,
125, 130, 131, 132, 134, …). Because the 2026 harvest is verified complete, roughly **15% of
allocated 2026 ESA numbers were never published to the forum.** `[UNVERIFIED]` these are
plausibly IDs reserved at triage and then withheld, embargoed, withdrawn, duplicated, or
published only through a non-forum channel — and a repo that is the system of record would
still hold files for them.

### 5.4 Corpus-size estimate, and the discrepancy with the human figure

The `[HUMAN]` figure of **more than 1000 files** in `advisories/` is more authoritative than any
public count and should be what you design against. Public evidence supports only **~340
published and ~386 allocated** advisory IDs for 2016–2026 — so roughly **600+ files are not
explained by the public forum record**. Honest accounting of that gap:

- **Reserved/withheld/withdrawn allocations** (§5.3) add only ~15%, i.e. ~45 files. Not enough
  on its own.
- **Products and services never announced on the forum.** `[UNVERIFIED]` Elastic ships far more
  products than the 12 that appear in 2026's forum posts, and the forum is aimed at
  self-managed and Cloud-Hosted stack users. Advisories covering Elastic Cloud infrastructure,
  internal services, or dependency updates handled via release notes could be tracked in the
  repo without ever being posted.
- **The `%04d` width is itself evidence** (§1.4). A fixed 4-digit field implies a series
  designed for up to 9,999/year. Choosing that width is hard to explain if the internal series
  only ever tracked the ~40/year Elastic published before 2026; it is easy to explain if the
  internal series is several times larger than the published one.
- **Non-advisory files in the same directory** `[UNVERIFIED]` — schema files, indexes, or
  per-advisory subdirectories would inflate a naive file count.
- **The figure may be forward-looking or approximate.** It was stated as "may contain more than
  1000 files." At the current ~222/year publication rate, the published series alone crosses
  1000 within a few years regardless.

**Practical recommendation** `[UNVERIFIED]`: assume 1,000–2,000 files today growing by
200–500/year, and treat 10,000 as the hard ceiling implied by the 4-digit ID width. Concretely
this means (a) enumerate with the **Git Trees API**, never the Contents API (§1.5); (b) support
incremental sync via the Commits API rather than full re-enumeration; and (c) do not assume the
set of files corresponds one-to-one with the set of public Discourse topics — expect files with
no public counterpart, and design the pipeline so an advisory with no forum URL and no CVE ID
is still ingestible.

### 5.5 Layout

`[HUMAN]` The directory is `advisories/`. `[UNVERIFIED]` Whether it is flat or year-nested is
unknown; the single observed path `advisories/ESA-2026-0081.json` was reported without an
intervening `2026/` component, which suggests **flat**. A flat directory of >1000 entries is
unusual but entirely workable, and is precisely the configuration that breaks the Contents API.
By contrast, both comparison databases shard by year and/or ID (§1.1), likely for exactly this
reason.

---

## 6. What remains unknown

Precise questions that only private-repo access can answer, ordered by how much each one
unblocks.

**Schema**

1. What are the top-level JSON keys of `advisories/ESA-2026-0081.json`, and what is the exact
   nesting? This is the whole ballgame; everything else is refinement.
2. Is the document a bespoke Elastic object, or does it embed/extend a standard (a CVE 5.x
   `cnaContainer`, an OSV record)? Is there a `schema_version`, `dataVersion`, or `$schema`
   field?
3. Is there a JSON Schema, TypeScript type, Go struct, or Pydantic model committed anywhere in
   the repo (e.g. `schema/`, `.github/`, `tools/`) that validates these files?
4. What are the exact key names for the fields §4.3 says must be present — affected version
   ranges, fixed versions, CVSS vector, CWE, CAPEC, IOC text, workarounds, Serverless
   applicability?
5. How are affected version ranges encoded — CVE 5.x style (`version` +
   `lessThanOrEqual` + `versionType: semver`), OSV style (`ranges[].events[]`), a `vers` string,
   or free text? This determines whether an ingest pipeline can do version-range matching at all.
6. Is the CVSS score stored as a vector string, a decomposed object, or both? Is CVSS v4
   present anywhere?
7. Are `product`/`vendor` free text or drawn from a controlled vocabulary? Can one file cover
   multiple products?
8. Are there `x_`-prefixed or otherwise internal-only fields (triage owner, HackerOne report
   ID, embargo date, internal ticket) that must be stripped before ingestion?
9. Is there a `state`/`status` field distinguishing draft / reserved / published / withdrawn?
   Critical for filtering, given §5.3.
10. Is there a stable modification timestamp inside the document, or must change detection rely
    on git commit metadata?
11. Are there timezone/format conventions for dates (RFC 3339? date-only?), and is publication
    date distinct from disclosure date?

**Identity and joins**

12. **Does `ESA-2026-0081.json` describe CVE-2026-72679 / CWE-674 in Elasticsearch?** (§2.4.)
    The cheapest possible confirmation that the repo and forum share one ID space.
13. Is the padded ID also stored *inside* the document, and in which form — `ESA-2026-0081` or
    `ESA-2026-81`? If both appear, which is canonical?
14. Is the Discourse topic URL or ID stored as a field? Without it, joining to public advisories
    requires fuzzy title matching.
15. How are the 45 gap IDs (§5.3) represented — absent files, or present files in a
    non-published state?

**Corpus and layout**

16. Exact file count and the earliest year present. Does the corpus predate 2016?
17. Is `advisories/` flat or year-nested, and are there non-`ESA-*.json` files in it?
18. Are there sibling directories (`schema/`, `tools/`, `templates/`) that document the format?
19. Is `advisories/` the input or the output of `Elastic CVE Publisher` (§4.1), and does the
    repo contain that tool?
20. Does the repo hold advisory revision history in-file (a `revision_history` array) or rely
    solely on git history?
