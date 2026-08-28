# Critical review: `esa-publication-landscape.md`, `integrations-precedent.md`, `deployment-and-setup.md`, `sample-events/`, and brief §1/§4/§8/§9

Review date: **2026-08-28**. Reviewer: independent audit pass. All analysis scripts are in
[`../temp/landscape-review/`](../temp/landscape-review/) and are re-runnable against the artifacts in
`../temp/`; every recomputed number below names the script that produced it.

**Verification legend** — `[VERIFIED-LIVE]` reproduced against the live source during this review;
`[VERIFIED-DOC]` confirmed against official vendor documentation fetched during this review;
`[UNVERIFIED]` not confirmable from here.

**Three externally supplied facts** frame this review. A human with repo access reports that (1) the
advisory files are **JSON**, (2) a real filename is **`ESA-2026-0081.json`** — zero-padded to four
digits, where the published corpus renders the same advisory as `ESA-2026-81` — and (3) the
`advisories/` directory **may hold more than 1000 files**. None of these was known to the original
research pass.

---

## Verdict

**`references/esa-publication-landscape.md` — accurate on everything machine-derived from the CVE and
NVD corpora, materially wrong on the hand-counted advisory-body statistics, and its headline
inference is now known to be false.** The CVE Record 5.x analysis is the strongest work in the whole
research set: all fourteen CNA container-key counts, the REJECTED count, the metric-type split, the
version-object shape census, the `x_generator` breakdown, the NVD total and its full twelve-year
per-year distribution, and the reference-host distribution all reproduce **exactly**, digit for
digit, from `temp/cve5/` and `temp/nvd_elastic_all.json`. Against that, the §3.2 heading-frequency
table — which is the table a pipeline author would actually build a parser from — does not
reproduce: five of its eleven rows are wrong, and the two most consequential rows (`Affected
Versions:` 42, `Solutions and Mitigations:` 42) are not merely off but **arithmetically impossible**
against the doc's own companion claim that 12 and 13 of the same 53 advisories used ATX headings
(42 + 12 = 54 > 53). The real numbers are 39 bold + 12 ATX + 2 unmarked, and 38 bold + 13 ATX + 2
unmarked; **all 53 sampled advisories carry both labels**, which is a different and more useful fact
than "42 of 53". Separately, §5.3's format inference put the true answer (JSON) at *lower* confidence
than the false one (YAML/Markdown) — see [How the format inference held up](#how-the-format-inference-held-up).

**`references/integrations-precedent.md` — the most accurate document of the three; essentially
clean.** I opened every one of the ~35 cited file paths and line ranges at repo HEAD `e7090bd7b4` and
compared the quoted text to the file. **Every quotation is verbatim and every line range is correct
except one**, a three-line off-by-N on `packages/github/data_stream/audit/manifest.yml` (the quoted
block is lines 56–63, cited as 59–63, in both §2 and the §12 summary table). The three negative
claims — no package reads files from a git repository, none sends `If-None-Match` from a `.hbs`
template, and `packages/github/data_stream/security_advisories` targets the global GitHub Advisory
Database rather than repository files — all hold under adversarial searching, and I confirmed the
last one live against `api.github.com`. The per-data-stream input table, the "only one `cel` stream"
claim, and the ECS-target list in §5.4 are all correct.

**`references/deployment-and-setup.md` — the documentation-sourced material is exact; one live claim
is overstated and one diagnostic step is logically unsound.** Every GitHub-docs quotation I checked
reproduces verbatim against the current pages: the org PAT-policy quotes, "Require administrator
approval… **This is the default value**", the 366-day org lifetime default, `expires_in` "Integer
between 1 and 366", the 50-token-per-user cap, the `pending`/public-resources-only behaviour, "GitHub
will notify organization owners with a **daily email**", the four SSO-revocation triggers, and
"Fine-grained personal access tokens are authorized during token creation" — all `[VERIFIED-DOC]`.
The SAML probe reproduces `[VERIFIED-LIVE]`: `github.com/orgs/elastic/sso` returns HTTP 200 rendering
"Single sign-on to… Authenticate your account by logging into… single sign-on provider", while
`google`, `jquery`, `expressjs`, `octokit` and `nodejs` all return 404. Two defects: the
"byte-identical `{"message":"Not Found"}`" claim is **false across endpoints** (the
`documentation_url` field differs by endpoint), and **ladder Step 3a is wrong** — it tells the
operator that a 404 on the repo-root tree means the permission is missing, but a nonexistent branch
produces the identical 404 there, so the step cannot distinguish the two faults it claims to.

**`references/sample-events/` — the advisory samples are genuinely verbatim; nothing is fabricated.**
I re-fetched all nine `.md` files from `discuss.elastic.co/raw/<topic_id>` and diffed. **All nine are
byte-identical** to the live source once Discourse's own per-post `username | timestamp | #N` banner
and its trailing `-----` post separator are accounted for. No paraphrasing, no reformatting, no
invention. Three defects: the RSS sample is **not well-formed XML** (the provenance comment is placed
*before* the `<?xml?>` declaration, so every conforming parser rejects it); four of the JSON files
carry **no provenance header at all**, contradicting the "each with a provenance header" claim in both
§3.5 and brief §4.4; and `ESA-2026-24.mapped-ecs.json` has correct ECS but contains **undeclared
synthetic values outside the block it labels as synthetic**.

**Brief §1 / §4 / §8 / §9 — inherits every landscape error and adds two of its own.** §1.3's "roughly
200–500 advisories" and "about 15 per month" are defensible against the public record but are now
superseded. §4.3's field-inventory table repeats the wrong heading counts and, worse, relabels them
as field *presence* ("Occurrences (of 53)"), which turns a heading-style census into a false claim
that 11 of 53 advisories lack `Affected Versions:`. §4.6 states "**137 advisories in 2026 alone**"
where 137 is the highest 2026 *sequence number*, not a count — the count is 116, which the same brief
states correctly elsewhere. §4.6 also says "21 missing in 2026, **8 in 2024**"; 2026 is right, 2024 is
5. §4.3's "byte-identical in every case checked" holds in only 24 of 44 checkable cases. §9's source
table is accurate and all its URLs resolve.

---

## Recomputed quantitative claims

Scripts: `01_topics.py`, `02_year_detail.py`, `03_nonesa.py`, `04_fields.py`, `05_fields_exact.py`,
`06_sample53.py`, `07_ack_and_overlap.py`, `08_cve5.py`, `09_nvd_map_osv.py`,
`10_refhosts_and_union.py`, `19_desc_identity.py`.

| Claim | Stated value | Actual value | Verdict | Severity |
| --- | --- | --- | --- | --- |
| Historical corpus size (brief §1.3) | "roughly 200–500 advisories" | 314 advisory topics in the Discourse category (315 minus the "About" topic); 237 distinct ESA IDs known across all public sources | Right for *published advisories*, **superseded** for *repo files* (>1000 reported) | **High** |
| Growth rate (brief §1.3) | "about 15 per month" | 116 ESA-2026 topics posted 2026-01-13 → 2026-08-13 = 14.7–16.5/month | **Correct** | — |
| ESA-tagged forum topics | 203 | **203** | **Correct** | — |
| Distinct publication dates | 52 | **52** | **Correct** | — |
| Largest single-day batch | 48 on 2026-08-13 | **48 topics, 48 distinct ESA IDs, on 2026-08-13** | **Correct** | — |
| Total forum topics harvested | 315 | **315** | **Correct** | — |
| "315" vs "203" reconciliation | (unreconciled in the docs) | Different populations, both right: 315 = every topic in category 31 (2015-06-06 → 2026-08-13); 203 = topics whose *title* carries an ESA ID; the other 112 are 1 "About" topic + **106 advisory-like posts from 2015–2025 that predate the ESA-in-title convention** + 5 non-advisory posts | Both correct; the docs never say this, which is why the corpus was undercounted | **Medium** |
| Advisory bodies sampled | "53 real advisory bodies" (landscape §3.2, brief §4.3) | `sampled_meta.json` names **53**; **57** `topic_*.md` files are on disk | Stated sample size correct; see next row | Low |
| Raw advisory bodies in `temp/raw/` | "54 raw advisory bodies" (landscape §8, brief §4.4, brief companion table) | **57** | **Wrong** | **Medium** |
| `CVE ID:` frequency | 47 of 53 | **47** bold-label on the 53-file sample. But **53 of 53** carry a `CVE ID` label in some form and 53/53 carry a `CVE-\d{4}-\d+` | Number correct as a *bold-label* count; **misleading** as field presence | **Medium** |
| `Severity:` frequency | 43 | **44** bold-label; 50 of 53 carry the label in some form; 3 have no severity at all | **Wrong** (off by 1) | **Medium** |
| `Affected Versions:` frequency | 42 | **39** bold + **12** ATX + **2** unmarked-plain = **53 of 53** | **Wrong**, and impossible against the doc's own "12 were ATX" | **High** |
| `Solutions and Mitigations:` frequency | 42 | **38** bold + **13** ATX + **2** unmarked-plain = **53 of 53** | **Wrong**, same impossibility | **High** |
| `Affected Configurations:` frequency | 18 | **18** bold (20 in any form) | **Correct** | — |
| `For Users that Cannot Upgrade:` frequency | 17 | **16** bold (23 in any form) | **Wrong** (off by 1) | **Medium** |
| `Problem Type:` frequency | 13 | **13** | **Correct** | — |
| `Impact:` frequency | 13 | **13** | **Correct** | — |
| IOC section frequency | 4 | **4** on the 53-file sample (**8** across all 57 on disk) | **Correct** for the declared sample | Low |
| `Elastic Cloud Serverless` frequency | 4 | **4** bold on the 53-file sample (**8** across all 57) | **Correct** for the declared sample | Low |
| `### Acknowledgements:` frequency | 4 (landscape §3.2, §3.3 "4 of 53 sampled", brief §4.3) | **2**. Only `topic_380558.md` and `topic_384520.md` carry the heading; a third (`topic_360898.md`) credits a reporter in prose with no heading | **Wrong** | **Medium** |
| `Update Log`/`Change log`/`Updates` | 6 (split 1 / 2 / 3) | **6**, split exactly **1** `## Update Log`, **2** `### Change log`, **3** `### Updates` | **Correct** | — |
| ATX-vs-bold split | "12 `Affected Versions:` and 13 `Solutions and Mitigations:` were ATX" | **12** and **13** on the 53-file sample | **Correct** | — |
| Elastic-assigned CVE records | 340 | **340** files in `temp/cve5/`, all parse as valid JSON | **Correct** | — |
| REJECTED CVE records | 27 of 340 | **27** (`cveMetadata.state`: 313 PUBLISHED / 27 REJECTED) | **Correct** | — |
| CNA container key counts | `affected` 313, `descriptions` 313, `references` 313, `problemTypes` 311, `source` 204, `x_generator` 204, `metrics` 203, `title` 193, `impacts` 129, `x_legacyV4Record` 99, `datePublic` 92, `rejectedReasons` 27, `credits` 5, `providerMetadata` 340 | **All fourteen exact.** No other CNA keys exist in the corpus | **Correct** | — |
| Metrics split | `cvssV3_1` ×201, `cvssV4_0` ×2 | **201 / 2** (203 records carry `metrics`) | **Correct** | — |
| `x_generator` apparent contradiction | 74 + 48 = 122 "Elastic CVE Publisher" vs `x_generator` key count 204 | **No contradiction.** 204 records carry the key: 74 × `Elastic CVE Publisher 0.0.1`, 48 × `1.0.0` (=122), plus 49 × `Vulnogram 0.2.0`, 29 × `Vulnogram 0.1.0-dev`, 4 × `Vulnogram 0.5.0` (=82). 122 + 82 = 204 | **Correct as written**; the doc states the Vulnogram remainder explicitly. The "structured source of truth" argument stands | — |
| Version-object shapes | 346 / 120 / 75 / 17 | **346 / 120 / 75 / 17** (558 objects total) | **Correct** | — |
| `versionType` distribution | `semver` 432, absent 120, `custom` 4, `1.x.x` 1, `8.x.x` 1 | **Exact** | **Correct** | — |
| "…`semver` in 432 of **554** version objects" (§6.2) | 554 | **558** (346+120+75+17 = 558, which the same document states two paragraphs earlier) | **Wrong**, internally inconsistent | Low |
| ESA-year 2026 published count | "116 advisories" (landscape §1.2/§1.3) | **116** distinct ESA-2026 IDs, 116 topics | **Correct** | — |
| ESA-year 2026 published count | "**137** advisories in 2026 alone" (landscape §5.3, brief §4.6) | **116.** 137 is the highest 2026 *sequence number* | **Wrong** — conflates max sequence with count | **High** |
| Missing 2026 sequences | 21 | **21** (23, 31, 47, 48, 61, 62, 84, 85, 103, 107, 109, 114, 115, 117, 122, 125, 130, 131, 132, 134, 135) | **Correct** | — |
| Missing 2024 sequences | "8 gaps: 28, 30, 33, 42, 43, 44, 45, 46" | **5**: 42, 43, 44, 45, 46. **28, 30 and 33 are published** — each is the *second* ID on a dual-ID topic (`ESA-2024-27, ESA-2024-28`; `ESA-2024-29, ESA-2024-30`; `ESA-2024-32, ESA-2024-33`), which the same document lists in §1.2 | **Wrong** — the gap analysis parsed only the first ID per title | **Medium** |
| ESA-year per-year topic counts | 2021:1, 2023:10, 2024:40, 2025:36, 2026:116 | **Exact as topic counts.** As *distinct ESA IDs*: 2021:1, 2023:11, 2024:43, 2025:36, 2026:116 (4 dual-ID topics) | **Correct** as labelled ("Public topics") | — |
| 2023 gap count | "21 gaps" with `Min seq 7` | **14** within the stated [7, 31] range; 21 only if 1–6 are counted as gaps, which contradicts the `Min seq` column | Inconsistent methodology | Low |
| Two- vs three-digit sequences | 178 two-digit, 25 three-digit | **178 / 25** counting one ID per topic (182 / 25 counting all IDs) | **Correct** | — |
| Resolved CVE→ESA mappings | 177 | `temp/cve_to_esa.json` holds **177**. A plain slug regex over the same 340 records resolves **187** | File count correct; the achievable figure is 187, so 10 joins were left on the table | Low |
| NVD total | 340 | **`totalResults: 340`**, 340 records in the file | **Correct** | — |
| NVD per-year CVE distribution | 1/15/30/25/14/13/27/15/22/37/31/110 | **All twelve years exact** | **Correct** | — |
| Reference-host distribution | `discuss.elastic.co` 418, `www.elastic.co` 194, `security.netapp.com` 51, `access.redhat.com` 17, `www.oracle.com` 12 | **All five exact** against the NVD records, which is the population §4.3 is describing. (The CVE 5.x *CNA containers* alone give 291/97/24/8/6 — the difference is ADP/NVD-added references) | **Correct** and correctly attributed | — |
| Community `esas.json` records | 244 | **244** records, **235** distinct `esa_id` | **Correct** | — |
| Full-corpus size | "≈ 2–10 MB", basis "500 documents × ~4–20 KB" | 57 raw bodies = **186 KB total**; **mean 3.3 KB, median 1.4 KB**, min 545 B, max 53 KB. 500 docs × mean ≈ **1.6 MB** of raw text | Range plausible for an *index*; the stated **per-document basis (4–20 KB) overstates the median advisory by ~3–10×** | Low |
| `descriptions[].value` "byte-identical in every case checked" | every case | **24 of 44** comparable ESA↔CVE pairs (55%). By year: 2026 **13/18**, 2025 6/9, 2024 3/10, 2023 2/9. Non-identical cases split into `md-stripped-equal` (8 — the ESA has Markdown links the CVE record flattens), `cve-is-prefix` (6 — the CVE text is truncated relative to the ESA) and genuinely different text (6) | **Wrong** as a general claim; defensible only if the checks were confined to 2026 advisories, and even there it is 13/18 | **Medium** |
| RSS page size | 25 items/page | **25** on page 0 and page 1 | **Correct** `[VERIFIED-LIVE]` | — |
| Category JSON page size / page count | 30/page, 315 topics, 11 pages | **`per_page: 30`**, 30 topics returned, `more_topics_url` present; 315/30 → **11 pages** | **Correct** `[VERIFIED-LIVE]` | — |
| `ESA-2026-99` immediately followed by `ESA-2026-100` | asserted | **Both exist**, both posted 2026-08-13 | **Correct** | — |
| `/meta` `api` CIDR blocks | 26 | **26** | **Correct** `[VERIFIED-LIVE]` | — |
| GHSA for CVE-2026-33461 | `GHSA-jf72-2wmj-p2f3`, `unreviewed`, empty `vulnerabilities[]` | **Exact** | **Correct** `[VERIFIED-LIVE]` | — |
| CNA registry entry | `CNA-2017-0011`, shortName `elastic`, Netherlands, scope text | **Exact**, including the stale scope string | **Correct** `[VERIFIED-LIVE]` | — |
| "304 on an authorized conditional request consumes zero rate-limit budget" | 0 units | **Confirmed.** Three consecutive `If-None-Match` 304s held `x-ratelimit-used` at 999; three unconditional 200s took it to 1000, 1001, 1002 | **Correct** `[VERIFIED-LIVE]` | — |

---

## Errors

| Location | Claim | What's actually true | Severity |
| --- | --- | --- | --- |
| landscape §5.3 confidence table; §0 bullet 5; brief §4.1, §4.6, §8 Q1, "Read this first" | File format is "most likely Markdown-with-YAML-front-matter or plain YAML" at **Medium**, with JSON ranked **Low–Medium** | The files are **JSON**. The true answer was ranked *below* the false one. See [How the format inference held up](#how-the-format-inference-held-up) | **Critical** |
| landscape §5.3; `mapped-ecs.json` `file.*` and `git.*`; brief §4.6 | ESA ID as filename, exemplified throughout as `advisories/ESA-2026-24.md` / `advisories/2026/ESA-2026-24.md` | The ESA-ID-as-filename inference is **right**, but the concrete form is wrong on two axes: the extension is `.json`, and the sequence is **zero-padded to four digits** (`ESA-2026-0081.json` ↔ published `ESA-2026-81`, verified as a real advisory posted 2026-08-13) | **High** |
| landscape §1.1, §0; brief §4.6 | "ESA IDs are… zero-padded to two digits for 1–99, three digits from 100" — stated as a universal property of the identifier | True of the **published** corpus (title and slug) only. No document anywhere distinguishes the published rendering from the repo rendering, and none anticipates that they might differ. An ESA-ID regex derived from the public corpus (`ESA-\d{4}-\d{2,3}`) will not match `ESA-2026-0081`, and joining repo records to Discourse/CVE data requires a zero-strip normalisation step that is described nowhere | **High** |
| landscape §5.3 "Filename casing (`ESA-2026-24.md` vs `esa-2026-24.yaml`) — Cannot determine"; brief §8 Q1 "What is the filename convention and casing?" | The only filename axis flagged as uncertain is **casing** | Casing turned out not to be the variable axis. Padding width and extension were, and neither is mentioned | **Medium** |
| landscape §3.2 table + §3.3 "Rare (4 of 53 sampled)"; brief §4.3 | `### Acknowledgements:` occurs 4 times | **2** | **Medium** |
| landscape §3.2 table; brief §4.3 | `**Affected Versions:**` 42, `**Solutions and Mitigations:**` 42 | 39 and 38 bold. Both labels are present in **53 of 53** advisories; the residue is 12/13 ATX plus 2 unmarked. The stated numbers are arithmetically impossible against the same documents' "12 / 13 were ATX" | **High** |
| brief §4.3 table header "Occurrences (of 53)" | Presents the bold-label heading counts as *field* occurrences | Silently converts a heading-**style** census into a field-**presence** claim. A pipeline author reading "Affected Versions: 42 of 53 — Effectively always" will build an optional-field handler for a field that is in fact universal, and will miss the 14 non-bold renderings entirely | **High** |
| landscape §3.2; brief §4.3 | `**Severity:**` 43; `For Users that Cannot Upgrade:` 17 | 44 and 16 bold | **Medium** |
| landscape §5.3, §7 note 3; brief §4.6 | "137 advisories in 2026 alone" | 116 published. 137 is the highest 2026 sequence number | **High** |
| brief §4.6 | "21 missing in 2026, **8** in 2024" | 2026: 21 ✓. 2024: **5** | **Medium** |
| landscape §1.2 table, 2024 row | "8 gaps: 28, 30, 33, 42, 43, 44, 45, 46" | 28, 30 and 33 are published as the second ID on dual-ID topics. True gaps: 42–46 | **Medium** |
| landscape §1.2 table, 2023 row | "21 gaps" with `Min seq` 7 | 14 gaps within [7, 31]. The count was computed over [1, max] while the neighbouring column reports min = 7 | Low |
| landscape §6.2 | "`versionType` is `semver` in 432 of **554** version objects" | 558. The document's own shape table (346+120+75+17) sums to 558 | Low |
| landscape §8 raw-artifact table; brief §4.4 and companion table | "54 raw advisory bodies" | **57** | **Medium** |
| landscape §4.2, §3.2 note; brief §4.3 | `descriptions[].value` "byte-identical" to the ESA description "in every case checked" / "in the cases I checked" | 24 of 44 checkable pairs. The claim is safe only for 2026 advisories, and even there it is 13/18 | **Medium** |
| landscape §3.5 "each with a provenance comment header"; brief §4.4 "each with a provenance header" | All samples carry provenance | **Four of seventeen do not**: `ESA-2025-20.osv.json`, `ESA-2026-128.discourse-topic.json`, `ESA-2026-24.cve-record-5.1.json`, `ESA-2026-24.github-advisory.json` are raw upstream dumps with no in-band provenance | **Medium** |
| `sample-events/ESA-2026-128.discourse-rss-item.xml` | Presented as a usable RSS sample | **Not well-formed XML.** The `<!-- ... -->` provenance comment precedes the `<?xml version="1.0"?>` declaration; `xml.etree` rejects it with *"XML or text declaration not at start of entity"*. Any XML-based test fixture built from it will fail to parse | **Medium** |
| `sample-events/ESA-2026-24.mapped-ecs.json` `_comment_provenance` | Flags only the `git.*` block as synthetic | `file.path`, `file.directory`, `file.name`, `file.extension` and `file.size` at the **top level** are equally synthetic and are not flagged. `file.size: 3412` does not match the 2,287-byte real advisory body, and all five are now known to be wrong (`.json`, four-digit ID) | **Medium** |
| `sample-events/ESA-2026-24.mapped-ecs.json` `…advisory.body` | Implied to be the advisory body | **Silently normalised, not verbatim**: Markdown hard-line-break trailing double-spaces removed, one blank line dropped, and every `\-` de-escaped to `-`. Since brief §4.6 lists escaped hyphens as a hazard a parser must survive, the "expected output" document quietly assumes a de-escaping step that is specified nowhere | **Medium** |
| deployment §1.8 preamble + brief §2.3 | Four faults return a **byte-identical** `{"message":"Not Found"}` | `[VERIFIED-LIVE]` **True within an endpoint, false across endpoints.** `documentation_url` is `…/rest/repos/repos#get-a-repository` on the repo endpoint and `…/rest/git/trees#get-a-tree` on the tree endpoint. Within the tree endpoint, bogus branch and bogus path *are* byte-identical. The ladder still works — better than claimed, since the doc URL identifies which endpoint failed | Low |
| deployment §1.8 Step 3a | "404 here, with Step 2 passing => the permission is missing. Re-mint with `Contents: Read-only`." | `[VERIFIED-LIVE]` **Unsound.** `GET /repos/elastic/integrations/git/trees/nosuchbranch` returns exactly the same 404 body as a permission failure. If the repo's default branch is not `main`, Step 3a misdirects the operator into re-minting a token that was fine. Step 3a must read the `default_branch` returned by Step 2 rather than hardcoding `main`, and its comment must list *branch* alongside *permission* | **Medium** |
| deployment §1.6 | Cites `…/organizations/managing-saml-single-sign-on-for-your-organization/managing-bots-and-service-accounts-with-saml-single-sign-on` | **404.** Correct URL: `https://docs.github.com/en/enterprise-cloud@latest/organizations/granting-access-to-your-organization-with-saml-single-sign-on/managing-bots-and-service-accounts-with-saml-single-sign-on`. The underlying claim is confirmed there | Low |
| precedent §2 and §12 row 6 | `packages/github/data_stream/audit/manifest.yml:59-63` | The quoted block (`- name: api_url` … `default: https://api.github.com`) is lines **56–63**. Line 59 is the `description:` line | Low |
| landscape §2.2, quoted LinkedIn block | "*And Up until 08/13 **it** has been less than 25 per release*" | Source reads "*And Up until 08/13 **is** has been…*" `[VERIFIED-LIVE]`. A silent typo-fix inside a block presented as verbatim | Trivial |
| landscape §3.2 table | `**Description:**` — "seen in RSS body of ESA-2026-128" | It is in the **raw Markdown body** of ESA-2026-128 too, not only the RSS rendering | Trivial |
| landscape §3.2 | "A non-standard `MPR` metric appears **once**" | Appears in **two** raw bodies (`topic_381427.md`, `topic_381428.md` — sibling advisories sharing a vector) | Trivial |
| landscape §6.1 | "`vendor` is `Elastic` in 313 of 313 records that have an `affected` block (3 legacy records use `n/a`)" | Self-contradictory as phrased. 313 records carry `affected`, containing 316 `affected` entries: 313 say `Elastic`, 3 say `n/a`. The `n/a` entries are additional entries, not additional records | Trivial |

---

## Sample data integrity

Scripts: `11_verbatim.py` (live re-fetch + diff), `12_sample_integrity.py`, `13_mapped_ecs_audit.py`,
`14_ecs_fields.py`, `15_hazards.py`.

### Per-file assessment

| File | Bytes | Well-formed | Provenance header | Notes |
| --- | --- | --- | --- | --- |
| `ESA-2021-31.md` | 35,646 | Markdown | yes | Verbatim ✓. Multi-post topic; sample correctly retains all 9 posts with their banners |
| `ESA-2023-16.md` | 1,599 | Markdown | yes | Verbatim ✓ |
| `ESA-2024-01.md` | 1,594 | Markdown | yes | Verbatim ✓ |
| `ESA-2025-14.md` | 4,508 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-01.md` | 1,777 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-02.md` | 1,830 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-24.md` | 2,915 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-41.md` | 1,907 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-128.md` | 2,169 | Markdown | yes | Verbatim ✓ |
| `ESA-2026-24.cve-record-5.1.json` | 5,191 | valid JSON | **no** | Raw upstream dump; every field I cross-checked matches `temp/cve5/CVE-2026-33461.json` |
| `ESA-2026-24.github-advisory.json` | 2,093 | valid JSON | **no** | Matches the live `api.github.com/advisories?cve_id=…` response |
| `ESA-2025-20.osv.json` | 33,566 | valid JSON | **no** | Raw OSV dump |
| `ESA-2026-128.discourse-topic.json` | 12,515 | valid JSON | **no** | Raw Discourse dump |
| `ESA-2026-128.discourse-rss-item.xml` | 3,879 | **INVALID XML** | yes | Comment precedes the XML declaration |
| `discourse-category-topic-list.json` | 4,463 | valid JSON | yes (`_source`, `_retrieved`) | |
| `community-esas-json-sample.json` | 2,564 | valid JSON | yes (`_source`, `_retrieved`, `_total_records: 244`) | 244 matches the real dataset ✓ |
| `ESA-2026-24.mapped-ecs.json` | 11,346 | valid JSON | yes (`_comment_provenance`) | See audit below |

No file is empty. The `.md` count is **nine**, matching brief §4.4's "nine verbatim real advisories".

### Verbatim-ness verdict — **PASS. Nothing is fabricated.**

Every `.md` sample was re-fetched from `https://discuss.elastic.co/raw/<topic_id>` during this review
and diffed against the on-disk file with the provenance comment stripped. After normalising for two
Discourse artefacts that the sampler correctly chose to handle — the per-post
`username | YYYY-MM-DD HH:MM:SS UTC | #N` banner and the trailing `-------------------------`
separator the `/raw/` endpoint appends — **all nine are byte-for-byte identical** to the live source,
including the escaped hyphens, the irregular spacing inside `( 7.7 )`, the trailing double-spaces,
and the duplicated heading. The Discourse topic ID and `created_at` in each provenance header match
the live topic. This is exactly what the research standard requires and it is worth saying plainly:
the previous pass did not invent, paraphrase or tidy anything. `[VERIFIED-LIVE]`

### Formatting-hazard claims (brief §4.6, landscape §3.2)

Every hazard the brief lists reproduces in the samples. `15_hazards.py` output:

| Hazard | Reproducible? | Evidence |
| --- | --- | --- |
| Unstable heading style, bold vs ATX | **Yes** | ATX in `ESA-2023-16.md` and `ESA-2026-02.md`; bold in the other seven |
| Colon inside vs outside the bold markers | **Yes** | `**CVE ID:**` in ESA-2026-24/128/41 and ESA-2024-01; `**CVE ID**:` in ESA-2023-16, ESA-2025-14, ESA-2026-01/02 |
| ESA-2026-128 duplicated `For Users that Cannot Upgrade:` | **Yes** | Exactly two occurrences, the second with trailing double-space |
| ESA-2026-02 bare CVSS vector, no `CVSS:3.1/` prefix | **Yes** | `**Severity**: CVSSv3.1: Medium (6.5) - AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` |
| `Medium (6.5)` / `High ( 7.7 )` / `8.8(High)` | **Yes, all three** | ESA-2026-01/02/128; ESA-2026-24; ESA-2025-14. Corpus-wide: 23 label-first and 44 score-first occurrences, so score-first is the *majority* form historically — the brief's framing implies it is the exception |
| Escaped hyphens `\-` | **Yes** | ESA-2026-01, ESA-2026-24, ESA-2026-128 |
| Non-standard `MPR` in ESA-2025-14 | **Yes** | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/MPR:L`, in 2 raw bodies not 1 |
| `Description:` label variant in ESA-2026-128 | **Yes** | `**Description:**` in the raw Markdown body, not only in the RSS rendering |

**Important scope caveat now that the files are known to be JSON:** every hazard above is a property
of **Discourse-rendered Markdown**, i.e. of the *public fallback* data source. None of them is
evidence about the JSON repo records. Brief §4.6 already hedges with "If the files turn out to be
Markdown", but landscape §3.2 presents the same list unconditionally as "formatting caveats an
integration must survive", and the brief's §4.3 field-inventory table — derived from the same
Markdown census — is presented as *the* field inventory. All of that now applies only to the
alternative design in §2.2.

### `ESA-2026-24.mapped-ecs.json` audit

**Correct.** Valid JSON. **All 34 non-custom leaf paths exist in the ECS 9.3.0 schema**
(`temp/ecs/ecs-9.3.0.yml`) — **zero invented ECS fields**. `event.kind: enrichment`,
`event.category: [vulnerability]` and `event.type: [info]` are all in ECS's allowed-value lists for
those fields. `vulnerability.score.base` is a number, not a string. Every custom field is correctly
namespaced under `elastic_security_advisories.*`. The `_comment_deliberately_absent` block is a good
artifact and its reasoning (why `package.version`, `vulnerability.status`, `related.*` and
`event.outcome` are left unset) is sound.

Value traceability against `ESA-2026-24.cve-record-5.1.json` and `ESA-2026-24.md`: `vulnerability.id`,
CVSS vector, base score, severity label, title, CWE ID, CAPEC ID, `generator`, `discovery`,
`default_status`, `cve_published_date`, `reserved_date` and `updated_date` **all match their source
exactly**. `vulnerability.description` is **byte-identical** to `containers.cna.descriptions[0].value`,
which is in turn identical (modulo line wrapping) to the advisory's own description paragraph — so for
*this* advisory the byte-identity claim is true. `fixed_versions` and `affected_versions` are correctly
derived (the three ranges match the CVE record's, merely reordered ascending).

**Defects.**

1. **Undeclared synthetic values.** `_comment_provenance` labels only `git.*` as synthetic, but the
   top-level `file.path`, `file.directory`, `file.name`, `file.extension` and `file.size` are equally
   invented. `file.size: 3412` does not match the real 2,287-byte advisory body, so a reader has no
   cue that it is a placeholder. **All five are now known to be wrong** (`.json`, and `ESA-2026-0081`
   rather than `ESA-2026-24` as the filename stem). `git.html_url` is likewise a dead link built from
   the same wrong assumptions.
2. **`…advisory.body` is normalised, not verbatim.** Trailing double-spaces stripped, one blank line
   dropped, `\-` de-escaped to `-`. Whether or not that normalisation is desirable, it is an
   undeclared transformation in a document whose whole purpose is to specify expected output — and it
   quietly contradicts the escaped-hyphen hazard the brief raises three sections earlier.
3. **Self-refuting evidence, unnoticed.** This file's own `advisory.body` is a multi-paragraph
   Markdown document carrying bullets, bold labels and newlines, stored as a **JSON string**. It is a
   working demonstration that JSON carries rich Markdown perfectly well — which is precisely the
   argument landscape §5.3 rejected when it reasoned that "Markdown is the natural carrier for that"
   and downgraded JSON. The counterexample was sitting in the same directory.

Given the JSON revelation, the ECS half of this file survives intact and remains the most useful
artifact in the set. The `file.*` and `git.*` blocks should be corrected to `ESA-2026-0081.json` (or
marked as unknown) before anyone builds a pipeline test from it.

---

## Corpus size reconciliation

**The public record cannot produce 1000 advisories, so `advisories/` is not one file per published
advisory.** The arithmetic is decisive.

**What the harvested data actually supports** (`01_topics.py`, `03_nonesa.py`, `10_refhosts_and_union.py`):

- **315** topics in Discourse category 31, spanning **2015-06-06 → 2026-08-13**. One is the category
  "About" post, leaving **314** substantive topics, of which **106** are advisory-like posts from
  2015–2025 that predate the ESA-in-title convention (e.g. *"Elasticsearch remote code execution
  CVE-2015-5377"*, 2015-07-16).
- **207** distinct ESA IDs appear in Discourse titles/slugs. Widening to every harvested source — CVE
  5.x reference slugs, NVD, raw bodies, and the community `esa-search` scrape — the **union is 237
  distinct ESA IDs**, spanning 2017, 2021, and 2022–2026. The community dataset alone contributes 11
  `ESA-2022-*` IDs and 17 extra `ESA-2023-*` IDs that never appear in a forum title.
- **Highest sequence observed per year:** 2017→23, 2021→31, 2022→14, 2023→31, 2024→48, 2025→39,
  2026→137. **Sum = 323.** Adding a generous 20–30 per year for the five years with no observed ESA
  ID (2015, 2016, 2018, 2019, 2020) gives an **upper bound of roughly 420–475 ESA IDs ever minted**,
  assuming the ID space is dense from 1 in every year — which it is not (2026 is 85% dense).
- **The repo filename uses the same per-year sequence as the public record.** `ESA-2026-0081.json`
  corresponds to `ESA-2026-81` — a real, published advisory (*"Elasticsearch 8.19.20, 9.4.5 Security
  Update (ESA-2026-81)"*, topic 389501, posted 2026-08-13). So the padding is cosmetic; the numbering
  space is identical. There is no hidden four-digit ID space to absorb the difference.

**Ranked explanations for >1000 files:**

1. **More than one file per advisory** — *most likely, and sufficient on its own.* If each advisory
   contributes 2–4 tree entries (for example a source record plus the emitted CVE 5.x JSON plus a
   rendered publication artifact, or a per-advisory subdirectory), then 300–450 advisories × 3 ≈
   900–1350 files. Supporting evidence: `x_generator: "Elastic CVE Publisher 0.0.1"/"1.0.0"` on 122
   of 340 CVE records proves a bespoke tool **emits** CVE 5.x JSON from some other input, so both the
   input and the output are natural repo contents; the ESA carries five sections (Affected
   Configurations, For Users that Cannot Upgrade, IOC, Serverless statement, Acknowledgements) that
   CVE 5.x has no slot for, so the two documents cannot be the same file; and a `.json` extension on
   an ESA-ID-keyed file is exactly what you would expect the *input* record to look like. This is the
   only explanation that reaches 1000 without contradicting the observed ID space.
2. **The count is recursive and includes non-advisory entries** — *very likely as a contributing
   factor.* If the directory is year-nested (which landscape §5.3 itself argues is the sane layout at
   this volume, and which `mapped-ecs.json` assumes with `advisories/2026/…`), a
   `git ls-files advisories | wc -l` or a `?recursive=1` tree fetch counts every descendant, plus
   schemas, templates, indexes, READMEs and per-year directory entries. The human said "may contain",
   which reads like an approximation rather than an exact count. Combined with (1) this comfortably
   clears 1000.
3. **Internal advisories that were never published** — *plausible but insufficient alone.* The public
   2026 sequence is 85% dense (116 of 137), so unpublished IDs add at most ~15% within the observed
   ID space. It could be larger if Elastic mints records for issues remediated before disclosure that
   never reach the forum, and the four-digit zero-padding is weak evidence that the ID space was
   designed for volumes far above 137/year. But it cannot be the primary explanation without implying
   sequence numbers well above the 137 we observe.
4. **A longer history than the forum shows** — *contributes at most a couple of hundred.* The
   Discourse category starts 2015-06 and the earliest ESA ID reachable from any public source is
   `ESA-2017-23`, so the scheme predates the title convention by years. But even a fully dense
   2015–2026 space lands at ~420–475 by the arithmetic above.
5. **Per-CVE rather than per-advisory files** — *ruled out.* The filename is keyed by ESA ID, and
   `0081` matches the published `ESA-2026-81`. There are only 340 Elastic-assigned CVEs in total,
   which is fewer than 1000 anyway.

**Downstream consequences the existing documents get wrong at >1000 files.** Deployment §2.5's
"Documents on initial backfill ≈ 200–500" and §2.6's "201–501 serial HTTPS requests / ≈30 s–3.5 min"
are understated by 2–5×. More seriously, §2.6's own caveat says `max_executions` defaults to **1,000**
and "a 500-file corpus leaves only 2× headroom" — at >1000 files the **default budget is exceeded
outright**, so raising it to 5,000 stops being a nicety and becomes mandatory. §2.4's backfill row
becomes ~1,001+ requests (20% of the hourly budget) rather than 4–10%. And brief §2.2's rejection of
the Contents API for its **silent 1,000-file truncation** goes from a theoretical objection to a live
one: a >1000-entry directory is exactly the case where the Contents API returns 1,000 entries with
HTTP 200 and no warning. That decision is now strongly vindicated, and the `truncated` flag check on
the Trees response goes from box-ticking to load-bearing.

---

## How the format inference held up

**Grade: C+ on the structural reasoning, F on the format call and its calibration.**

The inference chain has two independent links, and they came out very differently.

**What held up (and deserves credit):**

- *"One file per advisory, named after the ESA ID" — **High** confidence.* **Correct.**
  `ESA-2026-0081.json` is exactly that. Well-calibrated.
- *"The file contains structured, machine-parseable fields, not free prose" — **High** confidence.*
  **Correct.** A JSON document is as structured as it gets. Evidence A — that
  `x_generator: "Elastic CVE Publisher"` on 122 of 340 records implies a bespoke tool reading
  structured input — is the single best piece of reasoning in the document, and it is numerically
  exact (I reproduced 74 + 48 = 122 against 82 Vulnogram records, totalling the stated 204). Evidences
  C (batch publication) and D (reserved-then-published ID space) are also correct and correctly
  computed. Well-calibrated.
- *"CSAF JSON" — **Low**.* Almost certainly still correct, and the negative evidence (all six
  well-known CSAF/`security.txt` paths return 404 against a 200 control) reproduces exactly.
- *"Flat vs year-nested — cannot determine".* Honest, and still undetermined.

**What failed:**

- *"Format is YAML front matter + Markdown body, **or** plain YAML" — **Medium**.* **False.** This is
  the miscalibration that matters, and it is worse than a single wrong row: the document assigned
  **Medium** to the false answer and **Low–Medium** to the true one, so a reader ranking the
  hypotheses by the document's own confidence would have bet against JSON. The §0 executive summary
  ("Markdown with YAML front matter, or plain YAML"), brief §4.1, brief §4.6 and brief §8 Q1 all
  propagate the same ordering, with JSON listed last in every enumeration.
- *The specific reasoning error is identifiable and instructive.* The stated basis was: *"The advisory
  body contains multi-paragraph Markdown with bullet lists, inline code, numbered steps, and
  hyperlinks. Markdown is the natural carrier for that, and YAML front matter the natural carrier for
  the scalar fields."* This treats "the payload contains rich text" as evidence about the **container
  format**, which it is not — JSON strings carry Markdown perfectly well, and the research pass
  demonstrated this itself by writing `elastic_security_advisories.advisory.body` as a
  newline-and-bullet-laden JSON string inside `ESA-2026-24.mapped-ecs.json`. The counter-evidence was
  authored by the same pass, in the same directory, and went unnoticed.
- *"CVE Record 5.x JSON directly" — **Low–Medium**.* The *reasoning* here was good and probably
  remains correct: CVE 5.x has no slot for the ESA ID, Affected Configurations, workarounds, IOC
  guidance or the Serverless statement, so the repo record is likely a **superset** JSON schema with
  CVE 5.x as a rendering target. The **error was conflating two distinct hypotheses** — "the format is
  literally CVE Record 5.x" and "the format is JSON" — under one row. Rejecting the former dragged the
  latter down with it. Splitting that row would have produced the right answer at High confidence from
  evidence the document already had.
- *Confidence hygiene.* Nine of the thirteen `[UNVERIFIED]` / confidence-rated items in this cluster
  concern the repo. The document was scrupulous about labelling them, which is good practice, but
  labelling uncertainty is not the same as ordering the hypotheses correctly, and here the ordering
  was inverted on the one question the brief itself calls "BLOCKING".

**No document anticipated the ID-format difference.** I searched all four files for any
padding/filename-convention discussion (`02_year_detail.py` context plus a direct grep). Landscape
§1.1 states "zero-padded to two digits for 1–99, then three digits from 100" as a **property of the
identifier**, not of the published rendering. The only adjacent hedges are §5.3's "Filename casing
(`ESA-2026-24.md` vs `esa-2026-24.yaml`) — Cannot determine" and brief §8 Q1's "What is the filename
convention and casing?" — both of which flag **casing**, not padding width. The possibility that the
repo and the forum render the same ID differently is raised nowhere. This has a concrete cost: an
ESA-ID regex built from the public corpus will not match `ESA-2026-0081`, and joining repo records to
Discourse or CVE data now needs a zero-strip normalisation step that no document specifies.

**What is superseded and should be revised, not just annotated:**

| Location | Status |
| --- | --- |
| landscape §5.3 confidence table (rows 4–6) | Superseded. Format is JSON |
| landscape §0 bullet 5, §7 gap 1 | Superseded. The blocking unknown is largely closed |
| landscape §3.2, §3.3 (heading census, field inventory) | Now describes **only** the public Discourse fallback, not the repo records. Must be re-scoped, and its numbers corrected |
| brief "Read this first", §4.1, §4.6, §8 Q1, and the MEDIUM-HIGH confidence banner | Superseded; confidence can be raised |
| brief §4.6 formatting-hazard list | Applies only to the §2.2 alternative design |
| `mapped-ecs.json` `file.*` / `git.*` | Wrong filename, extension and path |
| deployment §2.5, §2.6, §2.4 backfill rows | Understated 2–5×; `max_executions` now mandatory |

**What is *not* superseded and should not be re-litigated:** the ESA-ID-as-primary-key inference; the
field-superset hypothesis; the Trees-over-Contents API decision (now more strongly supported); the
decision to leave `file_pattern` empty rather than defaulting to `*.md` (configuration-plan §4.5
explicitly reasoned that "a default of `*.md` against a `.yaml` corpus would produce zero documents
and no error" — that call just saved the integration from a silent-zero failure); and the entire CVE
Record 5.x / NVD / OSV enrichment analysis, which is independent of the repo format.

---

## Bad references and dead links

I extracted and resolved every URL in `research-brief.md` (including the §3.5 reference table and the
§9 source-attribution table) and in the three reference documents — 85 unique URLs (`18_links.sh`).

**Genuinely broken:**

| URL | Status | Where cited | Fix |
| --- | --- | --- | --- |
| `docs.github.com/en/enterprise-cloud@latest/organizations/managing-saml-single-sign-on-for-your-organization/managing-bots-and-service-accounts-with-saml-single-sign-on` | **404** | deployment §1.6 | `…/organizations/granting-access-to-your-organization-with-saml-single-sign-on/managing-bots-and-service-accounts-with-saml-single-sign-on`. Content confirms the claim |

**Redirects worth noting (all resolve 200, content still supports the claim):**

| URL | Redirects to |
| --- | --- |
| `…/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on` | `…/authenticating-with-single-sign-on/authorizing-a-personal-access-token-for-use-with-single-sign-on` (page renamed; the quoted sentence is present verbatim) |
| `www.elastic.co/community/security` | `www.elastic.co/product-security` — **as the doc claims** ✓ |
| `discuss.elastic.co/c/announcements/security-announcements.rss` | `…/31.rss` — as claimed ✓ |
| `www.elastic.co/guide/en/beats/filebeat/current/*` (2 URLs) | `www.elastic.co/docs/reference/beats/filebeat/*`. These are quoted from package manifests, so they are correct as *quotations* |
| `docs.github.com/rest/repos/repos#get-a-repository` | `docs.github.com/en/rest/repos/repos` (inside a quoted 404 body — correct as a quotation) |

**Bad file/line reference:**

| Reference | Problem |
| --- | --- |
| `packages/github/data_stream/audit/manifest.yml:59-63` (precedent §2 and §12 row 6) | Quoted block is lines **56–63** |

**Intentional 404s that correctly reproduce** (these are evidence, not errors): all six CSAF and
`security.txt` probes; `github.com/elastic/security-advisories` and its API forms;
`api.github.com/repos/elastic/this-repo-does-not-exist-zzz9`. The `www.elastic.co/community/security`
control returns 200, so landscape §2.4's CSAF table is fully reproduced. `[VERIFIED-LIVE]`

**Not URLs** (placeholders in code samples, correctly not dead links): `https://HOSTNAME/api/v3`,
`https://ghes.example.com/api/v3`, `https://api.SUBDOMAIN.ghe.com`, `http://{{ .request.host }}`,
and the `<CVE-ID>` / `<id>` template forms.

**Content spot-checks of cited pages** — all confirmed the quoted material: the Elastic advisory
generator prompt on `elasticsearch-labs`; the Security Labs advisory-automation blog; the CVE Program
CNA list (`CNA-2017-0011`, shortName `elastic`, the stale scope string); the 2020 Josh Bressers
Discourse thread (topic 228477); the Adam Tischler LinkedIn post (reachable, quote present, one
transcription slip noted above); and all eleven GitHub docs pages cited in `deployment-and-setup.md`.

---

## What holds up

Do not re-verify these. Each was independently recomputed or re-fetched during this review.

**Discourse corpus.** 315 total topics harvested; 203 ESA-tagged; 52 distinct publication dates; the
48-advisory batch on 2026-08-13; the recent batch-size table (19, 11, 11, 10, 7, 7, 7, 6, 6); 116
ESA-2026 advisories and the ~15/month 2026 run rate; 178 two-digit / 25 three-digit sequence
renderings; the 21 missing 2026 sequences, listed correctly; `ESA-2026-99` immediately followed by
`ESA-2026-100`; the four dual-ID topics; the late-backfill observation (`ESA-2024-20` posted
2025-05-01, `ESA-2024-21` posted 2025-06-10) and the conclusion that ESA year and post date are
independent — I found 18 such backfills; RSS 25 items/page and category JSON 30/page with 11 pages;
category ID 31 stable since 2015-06-06; staff-only posting.

**CVE / NVD / OSV / GHSA.** All 340 Elastic-assigned records held and parseable; 27 REJECTED; every
one of the fourteen CNA container-key counts; the `x_generator` breakdown (122 Elastic CVE Publisher
+ 82 Vulnogram = 204) — **there is no contradiction here and the "structured source of truth" argument
stands**; `cvssV3_1` ×201 vs `cvssV4_0` ×2; the four version-object shapes and the `versionType`
distribution; NVD `totalResults: 340` with all twelve per-year figures; the reference-host
distribution (418/194/51/17/12); `credits` on 5 of 340; the CVE→ESA join working only through the
Discourse slug with no ESA ID field in the record; GHSA-jf72-2wmj-p2f3 being `unreviewed` with an
empty `vulnerabilities[]`; the OSV `database_specific.cna_assigner: "elastic"` shape; Elastic not
being a CSAF provider; the community `esas.json` holding 244 records.

**Sample data.** All nine advisory `.md` files are **verbatim, live-verified, unfabricated**. Every
formatting hazard listed in brief §4.6 and landscape §3.2 reproduces in the actual files. The ATX
split (12 / 13) is correct. `ESA-2026-24.mapped-ecs.json` uses **34 real ECS 9.3.0 fields with zero
inventions**, correct allowed values for `event.kind`/`category`/`type`, correct namespacing of
custom fields, and every CVE-derived value traceable and exact.

**`integrations-precedent.md`.** Every quoted excerpt is verbatim at HEAD `e7090bd7b4`, and every line
range is correct except the `audit/manifest.yml` one noted above — including all seven ingest-pipeline
ranges, the four `abnormal_security` ranges, `ti_recordedfuture:48-68`, `qualys_vmdr:95-119`,
`mimecast:147-154`, and all seven `github/security_advisories` ranges. The negative claims hold:
**no package reads repository file contents** (the only `git/trees`/`git/blobs` hits in `packages/`
are echoed GitHub API payloads inside test fixtures; the `gitlab` hits are `/home/git/gitlab/log/`
filesystem paths; the `cloud_asset_inventory` hit is a `raw.githubusercontent.com` URL inside an Azure
ARM-template deep link, not a data-collection path), and **no `.hbs` template sends `If-None-Match` or
`If-Modified-Since`** (the single repo-wide hit is a Go mock server in `packages/azure/_dev/scripts/`
that *receives* the header). The `github` package has exactly one `cel` data stream; the
per-data-stream input table is correct; `api.github.com/advisories` is confirmed live to be the global
Advisory Database with no repository-file parameter; and
`GET /repos/elastic/integrations/security-advisories` returns 200 as the doc says.

**`deployment-and-setup.md`.** Every GitHub-documentation quotation reproduces verbatim on the current
pages: the restrict/allow PAT policy text, "Require administrator approval… **This is the default
value**", the 366-day org default, `expires_in` "Integer between 1 and 366, or `none`" with a 30-day
default, "Infinite lifetimes are allowed but may be blocked by a maximum lifetime policy", the
50-fine-grained-token cap, "Tokens always include read-only access to all public repositories", the
Resource-owner paragraph, the `pending`/"only be able to read public resources until it is approved"
behaviour, "GitHub will notify organization owners with a **daily email**", the classic-PAT-exempt-
from-approval note, the `repo` scope description, the four SSO-revocation triggers, the
linked-external-identity prerequisite and the "even if SSO is not enforced" gotcha, and "Fine-grained
personal access tokens are authorized during token creation" — so **the claim that fine-grained tokens
need no separate Configure-SSO step is correct** `[VERIFIED-DOC]`. The Metadata-is-implicit argument
is well supported: the docs describe a `contents=read`-only pre-fill URL as producing "a token with
`contents:read` **and** `metadata:read`", and the repository-permissions table lists `metadata` with
the single access level `read`. Live: `github.com/orgs/elastic/sso` → 200 with a single-sign-on
prompt while five non-SAML orgs → 404; `x-accepted-github-permissions: contents=read` on both Trees
and Blobs and `metadata=read` on the repo endpoint; `/meta` `api` returns 26 CIDR blocks;
`x-ratelimit-limit: 5000`; and **the "304 is free" property is confirmed** — three authorized
conditional 304s left `x-ratelimit-used` at 999 while three unconditional 200s incremented it to
1002.

**Brief §9.** The source-attribution table is accurate; every URL in it resolves and contains what is
claimed.
