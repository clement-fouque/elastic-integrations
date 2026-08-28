# Review — `ecs-mapping-analysis.md` and `configuration-plan.md`

Reviewer pass date: 2026-08-28. Adversarial accuracy audit. Nothing in the audited documents was
modified.

**Verification basis actually used by this review** (not inherited from the documents):

```
https://raw.githubusercontent.com/elastic/ecs/v9.3.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/v9.4.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/v9.5.0/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/main/generated/csv/fields.csv
https://raw.githubusercontent.com/elastic/ecs/v9.5.0/generated/ecs/ecs_flat.yml
/workspace/research_results/elastic_security_advisories/temp/ecs/ecs-9.3.0.yml
https://raw.githubusercontent.com/elastic/package-spec/main/spec/integration/data_stream/fields/fields.spec.yml
https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/version
/workspace/packages/**  (mechanical re-derivation of every count and citation)
```

---

## Verdict

**`ecs-mapping-analysis.md` is highly accurate on ECS facts and on file/line citations, and
noticeably weaker on the counts and the survey-completeness claims it uses to justify its
headline recommendation.** Every substantive ECS existence claim I checked is correct — the
`vulnerability.*` member list, the absence of `vulnerability.title`/`.published_date`/CWE/CAPEC/vector,
`vulnerability.status` being v9.5.0-only, beta, asset-scoped and enumerated `open|fixed|reopened|unknown`,
`package.fixed_version` not being ECS, the exact `entity.type` allowed-value list, `related.*` having
exactly four members, `package.*` having exactly thirteen, `vulnerability.score.base` being `float`,
`url.full`/`.original` being `wildcard`, and `event.category: vulnerability` declaring
`expected_event_types: [info]`. Roughly twenty in-repo file/line citations were spot-checked and
all but one are exact to the line. Against that, three things are wrong: the precedent survey's
stated scope ("34 streams across 23 packages" — the real number is 75 streams across 58 packages),
one of the two streams cited as independent corroboration for `enrichment`
(`ti_google_threat_intelligence/vulnerability_weaponization` is `threat`/`indicator`, not
`vulnerability`/`info`), and one table row (`aws/securityhub_findings` sets `event.category: configuration`).
The "definition versus finding-on-an-asset" split is real but weaker than stated: `enrichment` is
used *only* by catalog streams, but only 4 of ~10 catalog streams use it. The recommendation itself
(`enrichment` / `[vulnerability]` / `[info]`) is nevertheless well-founded, because it rests on an
exact structural twin rather than on the aggregate. The `nested`, `version`-type and fingerprint-`_id`
recommendations are all correct and all five cited fingerprint precedents match field-for-field.

**`configuration-plan.md` is well-researched on the `github` package and precise on its monorepo
counts, but contains one significant factual error that drives a recommendation.** Its reproduction
of the three `github` manifests is exact — every variable, type, default, `required`, `show_user`
and `secret` flag I checked matched, as did every cited line number (`:252`/`:443`/`:638`/`:782`,
`64-71`, `80-88`, `17-24`, `56-63`, `32-39`). Its two headline counts are exactly right: 370 data
streams declare `enable_request_tracer` and 290 declare `http_client_timeout`. The error is the
claim that `preserve_original_event` "is a legitimate variable *only* for file (filestream) and
syslog (tcp/udp) inputs" and that its presence in a CEL stream is "a legacy artifact": it is
declared by **327 of 361 CEL data streams** (90.6%) and is wired into `cel.yml.hbs` templates
across the monorepo. The related framing that `enable_request_tracer` is a "deliberate departure"
is likewise overstated — 297 of 361 CEL streams declare it, and the `github` CEL stream's own
description links the *CEL input* tracer documentation. Both documents also stray past their own
stated scope in places, and both are built on a file-format premise that the JSON discovery
invalidates.

---

## Errors

Only claims that are definitively wrong.

| Document | Location | Claim | What's actually true | Severity |
|---|---|---|---|---|
| `configuration-plan.md` | §1.1 L51-53 and §5.2 L428 | "`preserve_original_event` is present here and must not be copied. Per `data-collection-methods.md`, that variable is valid for file and syslog inputs only, **never for CEL**. Its presence in this CEL stream is a legacy artifact." / "It is a legitimate variable *only* for file (filestream) and syslog (tcp/udp) inputs." | `preserve_original_event` is declared by **327 of 361 CEL data streams across 113 packages** and is functional in CEL: `github/data_stream/security_advisories/agent/stream/cel.yml.hbs:83-84` emits `{{#if preserve_original_event}} - preserve_original_event {{/if}}` into `tags`, which the ingest pipeline reads at `default.yml:320` and `:340`. The same pattern appears in `cisa_kevs`, `claroty_xdome`, `checkpoint_harmony_endpoint` and ~320 others. It is the single most common CEL variable after `tags`, `processors` and `interval`. Calling it "never valid for CEL" and "a legacy artifact" is wrong. (The *decision* to exclude it may still be right on guardrail grounds — see Guardrail violations — but the stated justification is false and must be replaced.) | **major** |
| `ecs-mapping-analysis.md` | §1.3 L103 | "Surveyed every data stream whose ingest pipeline mentions `vulnerability` (34 streams across 23 packages)." | Case-insensitive: **78 streams / 58 packages**. Case-sensitive: **75 / 58**. Restricted to `default.yml`: **65 / 51**. Restricted to streams that actually set `event.category: vulnerability`: **44 / 38**. Streams whose *name* contains `vuln`: 24. No reading of "mentions `vulnerability`" produces 34/23. The tables list roughly 30 streams, so the survey is substantial — but it is not the exhaustive survey it claims to be, and the brief repeats the claim as "All 34 vulnerability-touching streams in the monorepo were surveyed" (`research-brief.md` L389). | **major** |
| `ecs-mapping-analysis.md` | §1.3 L115, and §1.4 L167-169 | `ti_google_threat_intelligence` / `vulnerability_weaponization` listed as `enrichment` / `vulnerability` / `info`; §1.4 then says "both `ti_google_threat_intelligence` vulnerability streams reach the same conclusion independently." | `ti_google_threat_intelligence/data_stream/vulnerability_weaponization/elasticsearch/ingest_pipeline/default.yml:45-55` sets `event.kind: enrichment`, `event.category: threat`, `event.type: indicator`. Only the `kind` matches; the category and type do not. It is a threat-intel stream, not a vulnerability-categorised one, so it is not independent corroboration for the `[vulnerability]`/`[info]` pairing. The sibling `vulnerability` stream (`default.yml:46-56`) *is* exactly as claimed. | **major** |
| `ecs-mapping-analysis.md` | §1.3 L133 | `aws` / `securityhub_findings` listed as `event.kind: state`, `event.category: [vulnerability]…`, `event.type: info`. | `packages/aws/data_stream/securityhub_findings/elasticsearch/ingest_pipeline/default.yml:28-32` appends `event.category: configuration`. The string `vulnerability` never appears in an `event.category` context anywhere in that pipeline (it appears only as `vulnerability.score.base`, `.score.version`, `.id`, `.reference`, `.scanner.vendor` field targets at L2618-2743). `event.kind: state` is correct. | minor |
| `ecs-mapping-analysis.md` | §0 L52 vs §2.1 L276 vs §2.2 L287 | "9 of the 13 (14 at v9.5.0) members" / "**Nine of the fourteen members are usable**" / "The complete ECS `vulnerability` fieldset is the fourteen members above." | Three different counts for the same thing. The fieldset has **13 distinct fields at v9.3.0** (14 CSV rows, one of which is the `vulnerability.description.text` multi-field) and **14 at v9.5.0** (15 rows). And the §2.1 table itself marks **ten** fields usable, not nine: `classification`, `description`, `enumeration`, `id`, `reference`, `report_id`, `scanner.vendor`, `score.base`, `score.version`, `severity`. `vulnerability.scanner.vendor` is marked "**Yes**, semantically loose" and §2.5/§3 go on to recommend setting it — but it is excluded from the count, and dropped entirely from `research-brief.md` §5.2's nine-row list. | minor |
| `ecs-mapping-analysis.md` | §4.2 L647 | "`flattened` … is for unbounded unknown keys; these keys are a known, fixed set of **seven**." | The proposed `affected_versions` object has **eight** keys in both §2.2 (L322-328) and §4.5 (L774-775): `vendor`, `product`, `version`, `less_than`, `less_than_or_equal`, `status`, `version_type`, `range`. | minor |
| `ecs-mapping-analysis.md` | L30-31 | "Local copies: `temp/ecs/fields-9.3.0.csv`, `temp/ecs/fields-v9.4.0.csv`, `temp/ecs/fields-v9.5.0.csv`, `temp/ecs/fields-main.csv`, `temp/ecs/ecs-9.3.0.yml`." | `temp/ecs/` contains **only** `ecs-9.3.0.yml`. The four CSVs do not exist. Relatedly, §1.5 L190 says the `entity.type` allowed-value list was "verified in `temp/ecs/fields-9.3.0.csv`" — the generated ECS CSV has columns `ECS_Version, Indexed, Field_Set, Field, Type, Level, Normalization, Example, Description` and carries **no allowed-values column at all**, so that verification could not have come from that file. (The claim itself is correct; I confirmed the twelve values from `ecs-9.3.0.yml`. Only the stated provenance is wrong.) | minor |
| `ecs-mapping-analysis.md` | §4.5 L739-740 | Table headed "**ECS fields** (types inherited from ECS)" lists `event.dataset`, `event.module` as `constant_keyword`. | ECS declares both as `keyword` at every version from v9.3.0 to `main`. `constant_keyword` is an *integrations convention* — 954 of 1037 in-repo `event.dataset` declarations use it, almost all in `fields/base-fields.yml` — not an ECS-inherited type. Note that `github/data_stream/security_advisories/fields/base-fields.yml` does not declare `event.dataset` at all; it declares only the three `data_stream.*` fields and `@timestamp`. | minor |
| `ecs-mapping-analysis.md` | §2.2 L301-304 | `package.fixed_version` is "defined as a custom field in `fields/package.yml` in at least ten packages (`sysdig`, `aws/inspector`, `tenable_io`, `rapid7_insightvm`, `google_scc`, `m365_defender`, `aws_securityhub`, **`wiz`**, and their latest-CDR transforms)." | The "at least ten" holds — **12 packages** define a `fixed_version` field, 11 of them in a file literally named `fields/package.yml` (`aws`, `aws_securityhub`, `cloud_security_posture`, `google_scc`, `m365_defender`, `microsoft_defender_cloud`, `microsoft_defender_endpoint`, `prisma_cloud`, `qualys_vmdr`, `rapid7_insightvm`, `sysdig`, `tenable_io`). But **`wiz` is the exception**: it defines `package.fixed_version` in `wiz/data_stream/vulnerability/fields/fields.yml:180-184`, not in a `fields/package.yml`. The quoted `sysdig` snippet at L306-313 is verbatim and exact. `research-brief.md` L413 drops the "at least" hedge and states "ten packages", which is a precise number that is also low. | minor |

---

## Overstated or unverifiable claims

| Document | Location | Claim | What's actually true | Severity |
|---|---|---|---|---|
| `ecs-mapping-analysis.md` | §1.3 L104-107, echoed in `research-brief.md` L389 | "The results split cleanly along the axis that matters: does the document describe a **vulnerability itself** … or a **vulnerability found on an asset**" / "the split falls along a clean line: streams describing a vulnerability *definition* lean `enrichment`". | The split is **real in one direction only**. Of the ~14 asset-finding streams surveyed, **zero** use `enrichment` — that half is solid. But of the ~10 catalog/reference streams, only **four** use `enrichment` (`github/security_advisories`, `first_epss/vulnerability`, and the two `ti_google_threat_intelligence` streams); the other six use `state` (`ti_flashpoint`, `tenable_io/plugin`), `event` (`tenable_sc/plugin`, `rapid7_insightvm/vulnerability`, `crowdstrike/vulnerability`) and `alert` (`qualys_vmdr/knowledge_base`). "Catalog streams lean `enrichment`" is false; the majority of them do not. The companion is more honest than the brief here — it concedes at L148-150 that "the repo is genuinely inconsistent" and rests the argument on the closest analogue instead — but the "splits cleanly" sentence at L104 and the brief's "clean line" sentence overstate it, and the brief drops the concession entirely. **The recommendation survives** on the strength of `github/security_advisories` alone, which is an exact structural twin (advisory ID, CVE ID, CVSS score and vector, CWE list, description, version ranges, credits, published/updated/withdrawn dates) and does set `enrichment`/`[vulnerability]`/`[info]` at `default.yml:12-25`, verified line-exact. Recommend rewriting the framing rather than the conclusion. | major |
| `configuration-plan.md` | §5.3 L432-434, L446-448 | "`enable_request_tracer` is **not** in the CEL standard-variable table … it is a deliberate departure from the authoritative standard table and should be reviewed as such rather than waved through as 'everyone does it'." | The **370** figure is exactly right (370 data streams, 124 packages). But within CEL specifically it is declared by **297 of 361 CEL streams across 102 packages** (82%), and `github/data_stream/security_advisories/manifest.yml:87` describes it with a link to `filebeat-input-cel.html#_resource_tracer_filename` — the *CEL input's own* tracer documentation. Whatever the skill's table says, this is a first-class CEL variable by every observable measure in the monorepo. Framing its inclusion as a departure needing special review inverts the burden of proof. The operational argument for including it (every failure is an information-free 404) is sound and does not need the "departure" framing to stand. | major |
| both | `configuration-plan.md` L17-18, L52, L419, L432; `ecs-mapping-analysis.md` L80, L87, L718, L813 | Load-bearing appeals to `data-collection-methods.md` ("the authoritative standard-variable table"), `cdr-field-requirements.md`, `ecs-field-mappings/references/categorization-cheatsheet.md`, `entity-mappings/references/entity-datastream-classification.md`. | None of these files exist anywhere on this filesystem, so every quotation from them is unverifiable from the artifact set. That matters most for the `preserve_original_event` claim, which is attributed verbatim to `data-collection-methods.md` and is contradicted by 327 CEL streams — either the skill text was misread or the skill is wrong, and the reader cannot tell which. Recommend that any claim sourced only from a skill reference be marked as such, and cross-checked against the monorepo before it drives an exclusion. | major |
| `ecs-mapping-analysis.md` | §1.6 L204-247 | "Advisories are mutable, so …" / "This gives idempotent re-reads … while preserving each amendment as a separate document." | **The precedent is verified and exact.** All five cited fingerprint pipelines exist and use the claimed field lists: `qualys_vmdr/knowledge_base` (`json.QID`, `json.LAST_SERVICE_MODIFICATION_DATETIME`, `json.CVE_LIST` → `_id`, L45-52); `tenable_io/plugin` (`json.id`, `json.attributes.plugin_modification_date`, L54-60); `ti_google_threat_intelligence/vulnerability` (`gti.vulnerability.attributes.cve_id`, `…last_modification_date`, L38-44); `ti_flashpoint/vulnerability` (`json.id`, `json.timelines.last_modified_at`, L48-54); `rapid7_insightvm/vulnerability` (`json.id`, `json.modified`, `json.added`, `json.description`, `json.cves`, `json.published`, L56-66). The *mutability premise*, however, rests on a single sample: `ESA-2021-31` is the only advisory in the 53-sample set with an `## Update Log`, and that update log lives in the **Discourse post**, not in a verified repository file. Whether the repo file is amended in place — and whether it carries any revision marker — is `[UNVERIFIED]`, as the document itself concedes at L234. Also worth stating explicitly, since it is a one-way door: **a custom `_id` and a TSDS are mutually exclusive.** Nothing in the document proposes TSDS (§4.5 L781 explicitly rules out `metric_type`, `unit` and `dimension`), so there is no conflict today, but the choice forecloses TSDS permanently and that consequence is not flagged. On the merits the trade-off is defensible: at 12-15 publication events a year the document-count growth from keeping revisions is negligible, and the document does flag the corollary at L239-242 that "current state" then requires a most-recent-per-`esa_id` collapse. | minor |
| `ecs-mapping-analysis.md` | §4.2 L665-677 | "**Type of the bound fields: `version`, not `keyword`.**" | **Correct and well-supported**, with two unstated caveats. Precedent is real and broader than cited: `type: version` appears **89 times across 9 packages** (`tychon` ×63, `ti_rapid7_threat_command` ×8, `checkpoint_harmony_endpoint` ×7, `tanium` ×4, `tenable_io` ×3, `trend_micro_vision_one`, `tenable_sc`, `cyberarkpas`, `crowdstrike` ×1 each). `version` is an allowed `type` in package-spec's `fields.spec.yml` enum, and `nested` accepts a `fields:` list, so nothing here fails validation. The semver claims match the Elasticsearch reference exactly: range queries honour semver precedence, and invalid-semver strings "can still be indexed and retrieved as exact matches, however they will all appear after any valid version with regular alphabetical ordering" — precisely what the document asserts about `1.x.x` / `8.x.x`. **Unstated caveat 1:** under synthetic `_source`, ES "may sort `version` field values and remove duplicates", so a multi-valued `version` field does not round-trip in source order. **Unstated caveat 2:** ES documents `version` as "not optimized for heavy wildcard, regex, or fuzzy searches". Neither is disqualifying for single-valued bounds inside a `nested` object; both belong in the caveat list. | minor |
| `ecs-mapping-analysis.md` | §4.1 L591-592 | "Plain `text` would be the choice only if BM25 scoring quality across advisories mattered. It does not; there are a few hundred documents." | Superseded — see the JSON section. The corpus is now known to be **>1000 files**, and the recommended `_id` scheme multiplies that by the number of revisions. The `match_only_text` conclusion still holds (relevance ranking across ~1000 advisories is still not the use case), but the supporting number is wrong. The "108 package `fields/*.yml` files use `match_only_text`" figure at L593 is **exactly right**, as is the claim that `github/security_advisories` maps its description to `match_only_text` (`fields/fields.yml:120-121`). | minor |
| `ecs-mapping-analysis.md` | §2.1 L268 | `vulnerability.scanner.vendor` — "Recommend setting it to `Elastic` for cross-integration query symmetry". | Honestly flagged as a judgement call at §7 item 5, and the precedent is exact: `ti_google_threat_intelligence/data_stream/vulnerability/elasticsearch/ingest_pipeline/default.yml:58` does set `vulnerability.scanner.vendor: Google`, with `observer.vendor: Google` at L62 and `observer.product: Threat Intelligence` at L66. The counter-precedent is also correct: `github/security_advisories` omits it. No correction needed — noted only because the count discrepancy above turns on whether this field is "usable". | minor |
| `configuration-plan.md` | §4.6 L379-381, and `research-brief.md` §6.3 L516 | "An initial backfill of 200-500 files takes **1.5-3.5 minutes** of serial requests" / "Initial backfill is 201-501 requests, 4-10% of a single hour". | Superseded by the >1000-file discovery — see below. The *conclusion* (`1h`, not `5m`) gets stronger, not weaker. The supporting claim that `5m` is a common default is correct: of CEL streams declaring an `interval` default, `5m` is the modal value at 131, ahead of `24h` (70) and `1h` (49). | minor |

---

## Impact of the JSON format discovery

The advisory files are JSON (`ESA-2026-0081.json`), the directory may hold **more than 1000 files**,
and the ESA ID in the filename is **zero-padded to four digits** while published ESA IDs are not
(`ESA-2026-24`). Every passage below is now either wrong, obsolete, or in need of a rewritten
justification. Grouped by what has to change.

### A. Format-dependent field values that are now simply wrong

| Location | What it says | What it needs to say |
|---|---|---|
| `ecs-mapping-analysis.md` §2.4 L366-369 | `file.path` = `advisories/2026/ESA-2026-24.md`, `file.name` = `ESA-2026-24.md`, `file.extension` = `md` | `.json` throughout; `file.name` = `ESA-2026-0081.json` |
| `ecs-mapping-analysis.md` §3 legend L400 | "**ESA** — parsed from the advisory **Markdown** body / template section" | The repo record is JSON; the legend's parsing model is obsolete |
| `ecs-mapping-analysis.md` §3.1 L424 | "Full advisory body (**Markdown**)" → `…advisory.body` | Depends on whether the JSON embeds a rendered body at all (see C) |
| `ecs-mapping-analysis.md` §5.1 L806-808 | "A git object hash of a **Markdown** file" | Cosmetic, but the reasoning about `related.hash` is unaffected and still correct |
| `ecs-mapping-analysis.md` §6 L847-871 | The sample mapped document is built from `references/sample-events/ESA-2026-24.md` with a synthetic `git.*` block | The `git.*` placeholders now have a known-wrong `path`/`name`/`extension`, and the whole document was derived from the Discourse rendering rather than the repo record. It should be regenerated, or its `_comment_provenance` marked as pre-discovery. |
| `configuration-plan.md` §4.5 L314-320 | "**Why the default must be empty, not `*.md`.** … `esa-publication-landscape.md` §5.3 rates the format as *medium* confidence between 'Markdown with YAML front matter' and 'plain YAML' … A default of `*.md` against a `.yaml` corpus would produce **zero documents and no error**" | The premise is dead: the format is known. `*.json` is now a defensible default. Keeping the empty default is still arguably the safer choice (filename casing and the presence of non-advisory JSON such as schemas remain unverified), but the argument has to be rebuilt from "we cannot guess" to "we know the extension; the residual risk is sibling JSON files". |
| `configuration-plan.md` §8 gap 1 L595-599 | "File format, naming convention, directory nesting, and file count are all unknown" | Format known (JSON), naming partly known (`ESA-YYYY-NNNN.json`, zero-padded), file count known to exceed 1000. Only directory nesting remains open — and `path`/`branch` remain justified as variables on the relocation argument alone. |
| `ecs-mapping-analysis.md` §7 gap 1 L877-882 | "**The repo file format is unverified.** … the source-side field names are `[UNVERIFIED]`" | Format resolved; source-side *field names* inside the JSON are still unverified, so the `RECON` markers in §3 stand. Narrow the gap rather than delete it. |

### B. The zero-padded ID — a new, unaddressed normalization requirement

Neither document anticipates this, and it touches the natural key, the join keys and the `_id`.

- `ecs-mapping-analysis.md` §1.2 L68 ("**Stable natural key.** The ESA ID (`ESA-2026-24`)") and §3.1
  L411 (`esa_id` = `ESA-2026-24`, "**Canonical natural key**") both assume the unpadded form. If
  `esa_id` is populated verbatim from the filename it will be `ESA-2026-0081`, which will **not**
  join to the published form used everywhere else — the Discourse slug, the CVE record's reference
  URL, `esa-publication-landscape.md`'s entire corpus, and the community `esas.json` dataset. A
  normalization step (strip leading zeros from the sequence component) is now mandatory, and the
  document should say whether `esa_id` holds the normalized or the raw form. Recommend both:
  normalized in `esa_id`, raw in a `…advisory.esa_id_raw` or reuse `file.name`.
- `ecs-mapping-analysis.md` §3.1 L414-415 proposes `…advisory.esa_year` and `…advisory.esa_sequence`
  as `integer`. `esa_sequence` as an integer is *already* the normalization (`0081` → `81`), so this
  is fine and is in fact the cleanest join key — worth promoting to a stated recommendation rather
  than "Convenience".
- `ecs-mapping-analysis.md` §1.6 L224 (`_id` = fingerprint of ESA ID + blob SHA) — the fingerprint
  must be computed over the **normalized** ID, or every document's `_id` changes the day someone
  adds normalization, silently duplicating the entire corpus.
- `ecs-mapping-analysis.md` §7 gap 3 L888-892 (multi-ESA advisories breaking the `_id` fingerprint)
  becomes *less* likely, not more: a one-file-per-padded-ID layout implies one advisory per file.
  Worth downgrading.

### C. The >1000-file count and the JSON shape change the collection and complexity arithmetic

- `configuration-plan.md` §4.6 L379-381: the backfill is no longer "200-500 files … 1.5-3.5 minutes"
  but >1000 serial blob fetches, on the order of 7+ minutes. This **strengthens** the `1h`
  recommendation (a 5m interval would now certainly overlap a backfill) but every number in the
  paragraph, and in `research-brief.md` §6.3 L516 ("201-501 requests, 4-10% of a single hour"),
  needs restating: >1000 blob GETs is >20% of a 5,000/hour budget in one go.
- `configuration-plan.md` §5.1 L418 excludes `batch_size`/`page_size` because "Neither endpoint
  paginates … A page-size knob would be inert", dismissing a per-execution blob budget as "an
  implementation detail, not a documented vendor-side requirement". With >1000 files this is no
  longer safely inert: `research-brief.md` §7.4 L548 itself notes `max_executions` defaults to
  **1,000** and that "a 500-file backfill fetching one blob per execution needs ~500 of them" — at
  >1000 files the *default* is insufficient and the corpus size becomes a vendor-side fact driving a
  configuration decision. The exclusion needs re-argument, not deletion.
- `configuration-plan.md` §4.3 L268-271 argues `path` must be configurable partly because "with 116
  advisories in 2026 alone, year-nesting would be the sane engineering choice". >1000 files makes
  year-nesting close to certain. The conclusion holds; the confidence should go up.
- `ecs-mapping-analysis.md` §4.1 L591-592 "there are a few hundred documents" → >1000, times revisions.
- `research-brief.md` §7.4 L547 estimates pipeline complexity as "**moderate to complex**, and the
  uncertainty is entirely in the file format. If the files are structured YAML or JSON, this is
  simple — decode and rename." That uncertainty is now resolved in the favourable direction: the
  estimate should drop toward **simple-to-moderate**, and the whole §4.6 "special parsing
  considerations" risk register (unstable heading style, inconsistent colons, duplicated headings,
  bare CVSS vectors, prose version ranges) applies only to the *Discourse fallback path*, not to the
  GitHub path.

### D. The one thing that gets *harder*, and that neither document flags loudly enough

`ecs-mapping-analysis.md` §7 gap 2 (L883-887) — "if the repo file turns out to be CVE Record 5.x
JSON rather than a superset, then fixed versions, affected configurations, workarounds, IOC
guidance, the Serverless statement, and the ESA ID itself are all absent from it" — has moved from a
hypothetical to the **live question**. A `.json` file in a CNA's advisory repository is more likely
than not to be a CVE Record 5.x document. If it is:

- `…advisory.fixed_versions` cannot be populated at all from the repo. §2.2 L331-334 already states
  that "the **CVE record does not carry the fixed version**" and that fixed versions "exist only in
  the ESA prose (`Solutions and Mitigations`)". That is the single largest data gap in the whole
  mapping and it is now the most likely outcome.
- The entire §3.5 block (`affected_configurations`, `workarounds`, `has_workarounds`,
  `workaround_deployment_types`, `indicators_of_compromise`, `serverless_statement`,
  `serverless_affected`, `update_log`) and the §3.6 acknowledgements prose may have no source.
- Conversely §3.4's structured version ranges, §3.2's eight decomposed CVSS metrics and §3.3's
  CWE/CAPEC become directly available rather than derived — which is exactly the CVE5 column the
  mapping table already anticipates.
- The `…advisory.title` filename note is unaffected, but the filename becomes the only carrier of
  the ESA ID, since `esa-publication-landscape.md` §4.2 establishes the CVE record has no ESA ID field.

The honest revision is: **the mapping targets survive intact, the source column collapses toward
`CVE5` + `GIT`, and the fixed-version gap becomes a blocking design question** requiring either a
second source (Discourse) or confirmation that the JSON is an ESA superset.

---

## Guardrail violations

The research phase is not supposed to prescribe ingest-pipeline or manifest implementation detail,
and specifically must not propose `preserve_duplicate_custom_fields`, `event.ingested`, or
`event.original`-removal toggles as configuration variables or recommended behaviours. Both
documents open by asserting they do not do this. Both then do it.

**1. `ecs-mapping-analysis.md` L3-6 — the disclaimer is contradicted by the document's own content.**

> "Research output only: this document describes **the data and its target field mapping**. It
> contains no pipeline processors, no `fields/*.yml` content, and no recommendations about pipeline
> configuration or error handling."

It contains `fields/*.yml` content at L306-313 (a literal six-line YAML block in `fields/*.yml`
authoring form), and §4.5 "Every proposed field, with its type" (L731-779) is a complete
field-by-field type specification — that is `fields/*.yml` authoring in table form.

**2. `ecs-mapping-analysis.md` §1.6 L224 — an ingest-pipeline processor decision, stated as a recommendation.**

> "**Recommendation: `_id` = fingerprint of (ESA ID, git blob SHA).**"

`_id` assignment is implemented by a `fingerprint` processor writing to `target_field: _id` — the
document's own precedent table at L212-218 cites five such processors by pipeline path. This is a
pipeline-construction prescription, and the surrounding §1.6 also prescribes *what to fingerprint*
and rejects an alternative scheme. It is well-argued and verified, but it is downstream work.

**3. `ecs-mapping-analysis.md` §1.5 L200-201 — a `_dev/build/build.yml` prescription.**

> "Note the deliberate consequence: `event.kind: enrichment` means the ECS pin stays at the repo
> default `git@v9.3.0`. The conditional `git@v9.5.0` pin exists only for entity streams."

The ECS dependency pin is build configuration, not a property of the data.

**4. `ecs-mapping-analysis.md` §2.5 L391 and §4.5 L744, L746 — mapping-authoring directives.**

> "Legitimate but overlaps `…advisory.body`; **pick one, do not populate both**"

> "`observer.vendor`, `observer.product` | `keyword` — **`constant_keyword` is the better choice**
> (one value per package)"

> "`vulnerability.scanner.vendor` | `keyword` — **`constant_keyword` is the better choice**"

Overriding an ECS-declared type with `constant_keyword` is a `fields/*.yml` authoring decision, and
"pick one, do not populate both" is a pipeline-behaviour instruction. (The document's §7 item 9
gets this right — "which representations a data stream keeps is not a research question" — and then
L391 answers it anyway.)

**5. `configuration-plan.md` §5.3 L448-450 — a CEL template prescription attached to a variable.**

> "the tracer writes full request and response bodies to disk, so it **must be paired with a
> `redact.fields` entry covering `api_key`** — the two features are configured together"

`redact.fields` is a CEL input template setting, not a configuration variable.

**6. `configuration-plan.md` §4.1 L220-223 and §4.5 L322-324 — CEL program structure.**

> "the CEL program builds **two different paths** from the same base:
> `{api_url}/repos/{owner}/{repo}/git/trees/{branch}:{path}?recursive=1` /
> `{api_url}/repos/{owner}/{repo}/git/blobs/{sha}`"

> "Whether the filter is implemented as glob matching or RE2 regex is an implementation choice for
> the CEL-program author; the description must state which. **Glob is recommended** as the more
> approachable of the two for a user-facing field."

The URL construction is defensible as API documentation, and it does load-bearing work justifying
host-only `api_url`, so I would leave it. The glob-versus-RE2 recommendation is a straightforward
implementation prescription and should be dropped to a flagged open question, which is where §8
item 2 already puts it — the two passages disagree with each other.

**Not violations.** `configuration-plan.md` §5.2 L425-427 lists `preserve_duplicate_custom_fields`,
`event.ingested` toggles and `event.original`-removal flags in a PROHIBITED / do-not-copy table.
That is explicitly the sanctioned form. Neither document recommends any of them.

**One tension worth naming.** `preserve_original_event` *is* an `event.original`-removal toggle, so
excluding it is consistent with the guardrail — but `configuration-plan.md` excludes it on a false
technical premise (§5.2 L428) rather than on the guardrail, while `ecs-mapping-analysis.md` §2.5
L388 and §3.1 L425 recommend populating `event.original` with "Verbatim advisory file bytes"
unconditionally. The combined effect is a design where `event.original` is always retained with no
operator control, arrived at by accident. That should be a deliberate, stated decision.

---

## Internal inconsistencies

Brief section 5/6 versus the two companions.

| # | Brief | Companion | Assessment |
|---|---|---|---|
| 1 | §5.2 L395: "**Nine are usable**", listing exactly nine and **omitting `vulnerability.scanner.vendor`** | `ecs-mapping-analysis.md` §2.1 L268 marks `vulnerability.scanner.vendor` "**Yes**, semantically loose … Recommend setting it to `Elastic`", and §2.5/§3.1 carry it into the mapping | Real disagreement about a field the builder will or will not populate. The companion's own "nine" (L276) contradicts its own table, which marks ten. Resolve to **ten**, or state that scanner.vendor is optional and excluded from the count. |
| 2 | §5.2 L395: "exactly **13 members** at ECS v9.3.0, plus `vulnerability.status` added at v9.5.0" | `ecs-mapping-analysis.md` §0 L52 "the 13 (14 at v9.5.0)"; §2.1 L276 "the **fourteen** members"; §2.2 L287 "the **fourteen** members above" | The brief is the one that is right (13 distinct fields at v9.3.0, 14 at v9.5.0). The companion counts the `vulnerability.description.text` multi-field as a member in two places and not in a third. |
| 3 | §5.2 L413: "`package.fixed_version` … is a custom field in **ten** packages' `fields/package.yml`" | `ecs-mapping-analysis.md` L302: "in **at least ten** packages" | The brief drops the hedge and turns a lower bound into a count. Actual is 12 packages. |
| 4 | §6.2 L492: `enable_request_tracer` is a row in the "**Optional configuration variables**" table | `configuration-plan.md` §3 L163-170 has a six-row optional table **without** it; it lives in §5.3 as "Outside the standard table — one convention variable, flagged", and §6 L459 counts it separately as "**Convention, flagged (1)**" | Same variable, same properties (`bool`, default `false`, `show_user: false`, not secret) — but a different classification and therefore a different variable count (brief: 7 required + 7 optional; plan: 7 required + 6 optional + 1 flagged). Cosmetic, but a builder reading only the brief will not know it was flagged for review. |
| 5 | §6.1 L478: "**`api_key` is the only secret.**" | `configuration-plan.md` §7.2 L511, L515 proposes a second data stream whose variable set includes `nvd_api_key` as `password` + `secret: true` | Not a contradiction within the GitHub stream, but the brief's §7.2 L537 does list `advisory_public` as a candidate data stream, so the package-level "only secret" statement is conditional on a decision the brief leaves open (§8 question 4). Worth qualifying. |
| 6 | §6 has no counterpart to `configuration-plan.md` §7 at all — the entire credential-free fallback configuration surface (`url`, `category_id`, `enrich_from_cve`, `cve_api_url`, `enrich_from_osv`, `osv_api_url`, `nvd_api_url`, `nvd_api_key`, `max_pages`) is companion-only | `configuration-plan.md` §7.2 L494-513 | Omission rather than disagreement, but §7 is 120 lines of substantive configuration design that a brief-only reader will never see, and the brief's §7.3 L543 leans on it ("If the token cannot be obtained in reasonable time, build the public stream"). |
| 7 | §5.6 L458: "A deterministic `_id` additionally means an accidental multi-agent enrolment **dedupes rather than duplicates**" | Absent from `ecs-mapping-analysis.md` §1.6 | The claim is correct and is a genuinely good point (it pairs with §6.3 L522's single-agent warning), but it appears only in the summary, which is backwards — the companion is where the `_id` argument is made. |

Everything else agrees. Brief §6.1's required-variable table matches `configuration-plan.md` §2
exactly on all seven variables — name, type, title, default, `show_user`, and secret flag — and
brief §6.2 matches §3 on `file_pattern`, `http_client_timeout`, `proxy_url`, `ssl`, `tags` and
`processors`, including the non-obvious `show_user: false` on `tags` and `show_user: true` on
`file_pattern`. Brief §5.1's categorization triple matches companion §0 and §1.4. Brief §5.3's
`related.*` conclusion matches companion §5.1.

---

## What holds up

Do not re-litigate these; I verified each mechanically.

**ECS facts — all correct.**

- `vulnerability.*` member list at v9.3.0/v9.4.0 (13 fields + the `.text` multi-field) and at
  v9.5.0/`main` (14 + `.text`), with types exactly as tabulated in §2.1.
- `vulnerability.status` is v9.5.0+ only, `keyword`, marked beta ("This field is beta and subject to
  change"), allowed values exactly `open, fixed, reopened, unknown`, and described as "The lifecycle
  state of a vulnerability finding **on an asset**". Absent from v9.3.0 and v9.4.0.
- `vulnerability.title`, `vulnerability.published_date`, `vulnerability.cwe`, `vulnerability.capec`,
  `vulnerability.vector`, `vulnerability.solution`, `vulnerability.workaround` — none exist at
  v9.3.0, v9.4.0, v9.5.0 or `main`. ECS has no CWE fieldset and no CAPEC fieldset anywhere.
- `package.fixed_version` is not ECS. `package.*` has exactly the thirteen members listed at L295-297.
- `related.*` has exactly four members (`hash`, `hosts`, `ip`, `user`) at every version checked.
- `entity.type` allowed values are exactly `bucket, database, container, function, queue, host, user,
  application, service, session, cloud, orchestrator`, and the field is beta.
- `event.category: vulnerability` carries `expected_event_types: ["info"]` and the quoted description
  ("Relating to vulnerability scan results. Use this category to analyze vulnerabilities detected by
  Tenable, Qualys, internal scanners, and other vulnerability management sources."). So `[info]` is
  the only ECS-sanctioned `event.type` pairing.
- `vulnerability.severity` has **no** `allowed_values` and its documented example is `Critical`
  (Title Case) — the §4.4 casing argument's premise is sound.
- `vulnerability.score.base` is `float`. `url.full` and `url.original` are `wildcard`; `url.path` is
  `wildcard`; `url.domain` and `url.scheme` are `keyword`. `event.original`, `event.id`,
  `event.reference`, `event.url` are `keyword`. `message` is `match_only_text`. `file.hash.sha1` is
  `keyword`.

**In-repo citations — every one of these is exact to the line.**

- `github/data_stream/security_advisories/elasticsearch/ingest_pipeline/default.yml`: `event.kind:
  enrichment` at L12-15, `event.category: [vulnerability]` at L16-20, `event.type: [info]` at L21-25;
  CVSS `type: float` converts at L71-76, L95-100, L114-119; `uri_parts` over `json.html_url` into
  `url.*` at L192-206; `vulnerability.classification: CVSS` at L280-283.
- `hackerone/data_stream/report/elasticsearch/ingest_pipeline/default.yml:82` copies `event.id` into
  `vulnerability.report_id`.
- `hackerone/data_stream/report/fields/fields.yml:477-489` — `attack_complexity`, `attack_vector`,
  `availability`, `confidentiality` present as claimed, with the separate `cvss_4_point_0_metrics`
  group at L491.
- `google_scc/data_stream/finding/fields/fields.yml:786-806` — `availability_impact`, `base_score`,
  `confidentiality_impact`, `integrity_impact`, `privileges_required`, `scope`, `user_interaction`,
  exactly that set and exactly those bounds. (`base_score` is `float` there, not `keyword`; the
  sentence lumps it into a "decomposed metrics as `keyword`" list. Trivial.)
- `aws_securityhub/data_stream/finding/fields/fields.yml:3631-3636` — `affected_code` and
  `affected_packages` both `type: nested`.
- `tenable_sc/data_stream/plugin/fields/fields.yml:190-191` — `- name: version` / `type: version`.
- All five `_id` fingerprint precedents, with their exact field lists (see the table above).
- Severity casing: `github/dependabot/…/default.yml:318` lowercases `vulnerability.severity`;
  `xm_cyber/…/default.yml:451` likewise; `jupiter_one/…/pipeline_risks_and_alerts.yml:429` likewise;
  `tenable_io/vulnerability/…/default.yml` sets `None` (at L524; the citation says L525, which is the
  processor's `tag` line — within tolerance).
- `github/security_advisories/sample_event.json` has `tags: ["forwarded", "github-security-advisories"]`
  and `vulnerability.severity: "unknown"` (lowercase), exactly as §4.4 and §5.2 state.
- `github/dependabot` and `github/code_scanning` set `event.kind: alert` with `event.type` of
  `creation`/`deletion` conditional on `fixed_at`/`dismissed_at` (dependabot `default.yml:104-113`).
- `github/security_advisories/fields/fields.yml` — description is `match_only_text` (L120-121);
  `vulnerable_version_range` is `keyword` (L176-177).
- `match_only_text` appears in exactly **108** package `fields/*.yml` files.

**`configuration-plan.md` manifest reproduction — exact.**

- §1.1: every one of the nine `security_advisories` variables matches on type, title, default,
  `required`, `show_user` and `secret`, including `api_key` being `required: false` with the quoted
  description "You may leave this field blank for public repositories, as authentication is not
  required for them." `preserve_original_event` is at L64-71 and `enable_request_tracer` at L80-88,
  both as cited.
- §1.2: every `audit` httpjson variable matches, including `interval: 1h` with the description "The
  value must be between 2m and 1h", `initial_interval: 730h`, `api_url` host-only at L56-63 with
  `show_user: false`, `http_client_timeout` at L32-39 with `default: 60s`, `proxy_url` as `text` not
  `url`, and `tags` with `show_user: true` (versus the CEL stream's `false`).
- §1.2's `preserve_duplicate_custom_fields` claim: present at exactly L252, L443, L638 and L782,
  `bool` / `required: true` / `show_user: false` / `default: false`, and those four positions fall
  inside the `azure-eventhub` (L104), `aws-s3` (L268), `azure-blob-storage` (L495) and `gcs` (L664)
  streams respectively — so "all four of these streams" is right.
- §1.3: `github/manifest.yml` is `version: "2.26.0"`, `format_version: "3.4.0"`,
  `categories: [security, productivity_security]`, `owner: elastic/security-service-integrations`,
  one policy template with `default` and `agentless` (release beta, organization security, division
  engineering, team security-service-integrations); the `cel` input declares `proxy_url` and `ssl`
  and nothing else at policy-template level, and `enable_request_tracer` sits on the `httpjson`
  input. All exact.
- §1.4 / §4.2: `code_scanning`, `dependabot`, `issues` and `secret_scanning` each declare separate
  `owner` and `repo` `text` variables titled "Repository owner" and "Repository", with `owner`
  `required: true` and `repo` `required: false`. Exactly four streams, exactly as described.
- §4.4's claim that there is **no** monorepo precedent for a `branch`, `ref`, `git_ref`, `directory`
  or `repository` variable name: confirmed — zero occurrences in any `data_stream/*/manifest.yml`.
  (`path` exists only in four `apache_spark` streams, with an unrelated meaning. `file_pattern`: zero.)
- §4.6: `github/security_advisories` does default `interval` to `24h`; `github/audit` does default to
  `1h` with the stated 2m-1h range. `research-brief.md` §6.3's `max_executions: 5000` claim is
  correct, though it lives in `github/data_stream/security_advisories/agent/stream/cel.yml.hbs:24`,
  not in a manifest.
- §3's "**290** data streams" for `http_client_timeout` — exactly 290 (109 packages).
- §5.3's "**370** data streams" for `enable_request_tracer` — exactly 370 (124 packages).

**Reasoning that stands.**

- `event.kind: enrichment` / `event.category: ["vulnerability"]` / `event.type: ["info"]` /
  `event.outcome` unset. Well-founded on the `github/security_advisories` twin and on ECS's own
  `expected_event_types`, notwithstanding the overstated "clean split" framing.
- Event stream, not entity stream. The `entity.type` argument is factually correct and decisive.
- `nested`, not `object`, for the version-range array. The false-positive walkthrough (Kibana 8.19.20
  matching a lower bound from one range against an upper bound from another) is correct
  Elasticsearch behaviour and is the standard `nested` motivation. Denormalising `product`/`vendor`
  into each range rather than nesting twice is the right call. `nested` with sub-`fields:` is valid
  package-spec.
- `version` over `keyword` for the bounds, with `keyword` named as the fallback. Verified against the
  Elasticsearch reference and against 89 in-repo usages; `version` is in the package-spec type enum.
- The git blob SHA must not go in `file.hash.sha1`. Correct, and the reasoning (it hashes
  `"blob <len>\0" + content`, so it will never match a genuine content hash in a `related.hash` pivot)
  is right.
- Nothing belongs in `related.*`, and the three tempting candidates are each correctly rejected.
- The IOC section is detection guidance, not indicators, and must not go in `threat.indicator.*`.
- `owner` + `repo` as two variables; `path` and `branch` as variables rather than constants;
  `api_url` host-only rather than full-URL. All well-argued, all consistent with precedent.
- `interval: 1h`. The reasoning survives the JSON discovery intact and in fact gets stronger.
- `proxy_url` as `text` rather than `url`, with the residual-credential-exposure risk noted.
