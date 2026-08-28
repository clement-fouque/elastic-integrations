# Review of the Elastic Security Advisories research

> **Review date:** 2026-08-28
> **Scope:** everything under `research_results/elastic_security_advisories/` as of commit `a0c2ef182d`
> **Method:** four independent audit tracks, each re-deriving pass 1's claims from primary sources rather than accepting them

This document is the answer to "review the current research". It records what held up, what did not,
what changed as a result, and what a reader should now trust. The detailed evidence lives in four
companion reviews:

| Review | Covers |
|---|---|
| `references/advisory-file-format.md` | The JSON format discovery, the ESA ID convention, candidate schemas, corpus size |
| `references/review-ecs-and-config.md` | `ecs-mapping-analysis.md`, `configuration-plan.md` |
| `references/review-github-api.md` | `references/github-api-collection-notes.md`, `test-api.py` |
| `references/review-landscape-and-precedent.md` | `references/esa-publication-landscape.md`, `references/integrations-precedent.md`, `references/deployment-and-setup.md`, `references/sample-events/` |

---

## 1. Headline

**The research is sound in its conclusions and unreliable in some of its numbers.**

Every architectural recommendation pass 1 made survived audit: the Git Trees + Blobs API with ETag
conditional requests, the `enrichment` / `[vulnerability]` / `[info]` categorization, `nested` version
ranges with the Elasticsearch `version` type, a fingerprint document `_id`, a `1h` poll interval, and
the seven-variable configuration surface. Several were verified more thoroughly than pass 1 had
verified them, and two of its riskiest technical claims — that Go's base64 decoder tolerates GitHub's
line wrapping, and that a sub-tree ETag is sensitive only to that sub-tree — were confirmed
experimentally rather than assumed.

Against that, roughly a quarter of the quantitative claims did not reproduce. The pattern is
consistent and worth knowing: **anything machine-derived was exact; anything hand-counted was not.**
All fourteen CVE container-key counts, the REJECTED count, the CVSS metric split, the full twelve-year
NVD distribution, the reference-host distribution, and about fifty in-repo file-and-line citations
reproduced digit for digit and line for line. The advisory-body heading frequencies, the
precedent-survey scope, and two corpus counts did not.

And one external fact — supplied by a person with repository access, not discoverable from the
research environment — invalidated the single largest inference in the brief.

---

## 2. What the external facts changed

Two facts arrived after pass 1 completed:

1. A real file in `advisories/` is named **`ESA-2026-0081.json`**.
2. The directory **may hold more than 1000 files**.

### 2.1 The format question is resolved, and pass 1 guessed wrong

Pass 1's central unknown was the on-disk format. Its inference table rated
"YAML front matter + Markdown body, **or** plain YAML" at **Medium** confidence and named it the most
likely answer, while rating "CVE Record 5.x JSON directly" at **Low–Medium** and JSON generally as the
less likely family. The answer is JSON.

The miscalibration is instructive rather than embarrassing. The reasoning that a *structured source of
truth exists* was rated High and was correct — the "Elastic CVE Publisher" evidence, the batched
publication, the reserved-then-published ID space and the slot-filling template all pointed the right
way. What went wrong was one step further: pass 1 reasoned that because advisory *bodies* contain
multi-paragraph Markdown with bullets and inline code, "something must carry rich text", and treated
Markdown-as-carrier as more probable than JSON-with-embedded-strings. JSON string fields carry
Markdown perfectly well, so the argument never actually discriminated between the two.

**What is still unknown is the schema inside the JSON**, and that is now the only blocking item. The
review narrowed the candidates considerably by ruling out the standards on concrete grounds rather
than impressions: CSAF mandates lowercase filenames and Elastic publishes no CSAF discovery metadata
at all; `ESA` is not among OSV's 47 registered database prefixes and every `ESA-` ID 404s from
`api.osv.dev`; and CVE Record 5.x cannot be the primary record because such records are conventionally
keyed by CVE ID while this file is keyed by ESA ID, and because the ESA↔CVE relationship is
many-to-many with dependency advisories carrying no Elastic-assigned CVE at all. A **bespoke Elastic
schema** is the most likely answer.

One live lead is worth flagging because it would be good news: in 2020 Elastic's Product Security lead
stated the plan was to publish advisories "in ECS format… allow the JSON to be downloaded". Re-probed
on this pass, no such public feed exists — `/product-security/advisories`, `.json`, `/feed` and both
`security.txt` locations all 404. But a JSON-per-advisory private repository is exactly what that
project would have produced internally. The counter-argument is that ECS's `vulnerability.*` fieldset
still has no fields for version ranges, fixed versions, CWE or CAPEC, so an ECS-shaped advisory record
would need heavy custom extension.

### 2.2 The ESA ID has two renderings, which nothing in pass 1 anticipated

The repository pads the sequence to **four digits**; every public rendering pads to a **minimum of
two** and widens naturally. Verified across 315 forum titles, 57 advisory bodies and 340 CVE records:
the four-digit form appears nowhere publicly, and a bare single-digit form appears nowhere either.
`ESA-2026-0081` is the public `ESA-2026-81`, which exists and was captured (Elasticsearch,
CVE-2026-72679, posted 2026-08-13).

This is a small fact with wide reach. It breaks the natural key, every join to the public corpus, and
the document `_id` unless the pipeline normalizes to the pair *(year, integer sequence)*. String
comparison fails in both directions, and fixed-width two-digit formatting fails above sequence 99
where the public form widens to three digits. The `_id` consequence is the sharp one: fingerprinting
the raw filename form and adding normalization later would change every `_id` in the index and
silently duplicate the entire corpus.

### 2.3 The corpus is larger than pass 1 thought, and the gap is unexplained

Re-derived from a full crawl, with the older years spot-verified live against the Discourse search API:

| Measure | Value |
|---|---|
| Distinct **published** ESA IDs, 2016–2026 | **341** |
| **Allocated** upper bound (sum of per-year maxima) | **~386** |
| Published in 2026 | 116, highest sequence 137 |
| Files reported in `advisories/` | **>1000** |

Pass 1's "roughly 200–500 advisories" was a floor mistaken for a total: it counted only forum topics
whose *title* carries an ESA ID, and 106 further advisory-like topics from 2015–2025 predate that
convention. Its growth-rate figure of ~15/month was correct.

So the public record accounts for at most ~386 IDs and the directory reportedly holds >1000 files,
leaving **~600+ files unexplained**. The best-supported explanation is that the repository holds
advisories that were never published — internal-only, silently fixed, embargoed or withdrawn. The
four-digit padding supports this independently: it provides capacity for 9,999 IDs per year against a
published peak of 137, which is the signature of a much denser series. Alternatives, in descending
order: a recursive count including year subdirectories and non-advisory files; more than one file per
advisory; or the ">1000" being a general caution about the GitHub Contents API cap rather than a
measured count of this directory.

**This raised a question nobody had asked.** If most of the files are unpublished advisories, an
integration that ingests the directory indiscriminately will index non-public vulnerability
information about Elastic products, and everyone with access to the resulting index inherits that
exposure. That is a policy question, not a technical one, and it is now question 11 in the brief.

### 2.4 The scale consequences

| Quantity | Pass 1 | Corrected |
|---|---|---|
| Backfill API calls | 201–501 | 1,001 at 1,000 files; 3,001 at 3,000 |
| Backfill wall time (serial) | 1.5–3.5 min | ~3.5 min at 1,000; ~10.5 min at 3,000 |
| Share of a 5,000/hr budget | 4–10% | 20% at 1,000; 60% at 3,000; **100% at ~5,000** |
| Cursor size in the Filebeat registry | 40–50 KB | 88 KiB at 1,000; 185–264 KiB at 3,000 |
| Corpus on disk | 2–10 MB, from 500 × 4–20 KB | ~10 MB, from ~3,000 × 3.3 KB mean / 1.4 KB median |

The interval recommendation of `1h` gets **stronger**, not weaker: a `5m` interval would now sit well
inside the backfill window and risk overlapping work. Steady state is unaffected, because a 304 costs
zero rate-limit budget regardless of corpus size — reconfirmed by holding `x-ratelimit-used` at 999
across three consecutive conditional 304s while three unconditional 200s advanced it.

**The one number that actually breaks, and the capability that fixes it.** `max_executions` defaults
to **1,000**, so a backfill fetching one advisory per execution stalls partway through a >1000-file
corpus — not loudly, but by exhausting its budget, logging a warning and resuming next interval.
The audit then established experimentally that the one-blob-per-execution model is not forced: mito
v1.27.0 was built from source and a single CEL evaluation was made to issue one tree request plus ten
blob requests, all returning HTTP 200 with `x-ratelimit-used` advancing monotonically 129→139. At
50–100 blobs per execution a 3,000-file backfill needs 31–61 executions rather than 3,001, fitting
comfortably inside the default. Blobs-per-execution is therefore a free design variable, and the
constraint dissolves.

A second free improvement surfaced alongside it: the Blobs endpoint honours
`Accept: application/vnd.github.raw`, which is **29% cheaper on the wire** (916,962 versus 1,292,920
bytes over 100 blobs) and removes base64 decoding entirely.

---

## 3. Errors found in pass 1

Corrected in place. Severity is about consequence for the integration builder, not about how wrong the
statement was.

### Blocking or major

| Where | Claim | Actually |
|---|---|---|
| brief §4.6, landscape §5.3 | Format most likely Markdown+YAML front matter or plain YAML | **JSON** |
| brief §1.3 | "roughly 200–500 advisories" in the complete corpus | 341 published, ~386 allocated, >1000 files reported |
| brief §4.3, landscape §3.2 | Heading frequencies presented as field presence: `Affected Versions:` 42 of 53, `Solutions and Mitigations:` 42 of 53 | Both are **53 of 53**. The stated numbers counted only the bold-label spelling, then mislabelled the result as presence. Arithmetically impossible against the same document's "12 were ATX" (42+12=54>53) |
| config plan §1.1, §5.2 | `preserve_original_event` is valid for filestream and syslog only, "never CEL"; its presence in a CEL stream is a legacy artifact | Declared by **327 of 361 CEL data streams** and functional in CEL. The exclusion is still right on guardrail grounds, but the reason given was false |
| ECS analysis §1.3, brief §5.1 | "All 34 vulnerability-touching streams in the monorepo were surveyed" | **75 streams across 58 packages**. No reading of the criterion yields 34; the tables enumerate ~30 |
| ECS analysis §1.3, brief §5.1 | Vulnerability streams "split cleanly": catalog streams lean `enrichment` | True in one direction only. Zero asset-finding streams use `enrichment`, but only 4 of ~10 catalog streams do. The recommendation survives on the `github/security_advisories` twin plus ECS's `expected_event_types`, not on consensus |
| brief §4.6, landscape §5.3 | "137 advisories in 2026 alone" | **116**. 137 is the highest 2026 *sequence number* |

### Medium

| Where | Claim | Actually |
|---|---|---|
| brief §4.3 | CVE and ESA descriptions "byte-identical in every case checked" | Identical in **24 of 44** comparable pairs (55%); 13 of 18 in 2026. Of the mismatches, 8 differ only by flattened Markdown links, 6 are truncated CVE text, 6 are genuinely different |
| landscape §1.2 | "8 gaps in 2024: 28, 30, 33, 42–46" | **5 gaps**. 28, 30 and 33 are published as the second ID on dual-ID topics that the same document lists elsewhere |
| landscape §3.2 | `Acknowledgements:` in 4 of 53 | **2** carry the heading; a third credits a reporter in prose |
| landscape §3.2 | `Severity:` 43, `For Users that Cannot Upgrade:` 17 | 44 and 16 |
| landscape §8, brief §4.4 | "54 raw advisory bodies" in `temp/raw/` | **57** |
| deployment guide §1.8 | All four failure modes return a byte-identical `{"message":"Not Found"}` | Byte-identical *within* an endpoint (md5 confirmed across five variants), but the `documentation_url` differs *between* endpoints. Separately, pointing the path at a file returns **HTTP 422** with a distinct message — a usable diagnostic signal the ladder discards |
| deployment guide §1.8 step 3a | A 404 on the repo-root tree means the permission is missing | A nonexistent branch produces the identical 404, so the step cannot distinguish the two faults it claims to |
| ECS analysis §1.3 | `ti_google_threat_intelligence/vulnerability_weaponization` corroborates `enrichment`/`vulnerability`/`info` | It sets `category: threat` / `type: indicator`. Only the `kind` matches. Its sibling `vulnerability` stream does match |
| ECS analysis §2.1 vs brief §5.2 | "Nine usable" `vulnerability.*` fields | **Ten**. The companion's own table marks ten; the disputed field is `vulnerability.scanner.vendor`, which the same document recommends populating |
| brief §5.2 | `package.fixed_version` custom in "ten packages" | **12**. Pass 1's companion said "at least ten"; the brief dropped the hedge and the number was also low |
| ECS analysis §0/§2.1/§2.2 | Three different counts (13 / 14 / 14) for the `vulnerability.*` fieldset | 13 distinct fields at v9.3.0, 14 at v9.5.0. The brief had this right; the companion counted the `.text` multi-field inconsistently |
| config plan §5.3 | `enable_request_tracer` is a "deliberate departure" from the standard variable set | Declared by **297 of 361 CEL streams**; the `github` CEL stream's own description links the CEL input's tracer docs. It is a first-class CEL variable |

### Minor and cosmetic

Documented in full in the companion reviews: an off-by-three line range in
`integrations-precedent.md`, a `554` vs `558` internal inconsistency in the version-object census, a
2023 gap count computed against an inconsistent range, four non-existent ECS CSV paths cited as local
provenance, `event.dataset`/`event.module` described as inheriting `constant_keyword` from ECS when
that is an integrations convention, `aws/securityhub_findings` miscategorized in one table row, and a
seven-versus-eight key count for the proposed version-range object.

---

## 4. What held up, and should not be re-litigated

This matters as much as the error list, because the temptation after reading section 3 is to distrust
everything.

**Verified exactly, by re-derivation from primary sources:**

- Every ECS field-existence claim. The `vulnerability.*` member list and types; `vulnerability.status`
  being v9.5.0-only, beta, and scoped to a finding *on an asset*; the absence of
  `vulnerability.title`, `.published_date`, `.cwe`, `.capec`, `.vector`, `.solution`, `.workaround` at
  every version from v9.3.0 to `main`; ECS having no CWE and no CAPEC fieldset anywhere;
  `package.fixed_version` not being ECS; `related.*` having exactly four members; the twelve allowed
  values of `entity.type`; `event.category: vulnerability` declaring `expected_event_types: [info]`.
- All fourteen CVE CNA container-key counts, the 27-of-340 REJECTED count, the `cvssV3_1` ×201 /
  `cvssV4_0` ×2 split, the 558-object version-shape census, the `versionType` distribution, the
  `x_generator` breakdown (204 records: 122 Elastic CVE Publisher, 82 Vulnogram — no contradiction),
  the NVD total of 340 and its full twelve-year distribution, the reference-host distribution.
- About fifty in-repo file-and-line citations, opened and compared at HEAD `e7090bd7b4`. Every
  quotation verbatim; one line range off by three. All five document-`_id` fingerprint precedents
  match field for field. Both headline monorepo counts (370 streams declaring
  `enable_request_tracer`, 290 declaring `http_client_timeout`) are exactly right, as is the
  reproduction of all three `github` manifests.
- The three negative precedent claims: no package reads files from a git repository, none sends
  `If-None-Match` from a CEL template, and `github/data_stream/security_advisories` targets the global
  GitHub Advisory Database rather than repository files.
- Every GitHub documentation quotation in the deployment guide, and the SAML SSO probe
  (`orgs/elastic/sso` → 200 with a single-sign-on prompt; `google`, `jquery`, `expressjs`, `octokit`,
  `nodejs` → 404).

**Verified experimentally, and these were the risky ones:**

- **The Contents API truncates silently at 1,000 entries** — reproduced: HTTP 200, exactly 1,000 of
  5,733 entries, no `truncated` flag, no `Link` header, no warning. The Trees API returned all 5,733
  with `"truncated": false`. With >1000 advisory files this is the difference between a complete
  corpus and a quietly incomplete one.
- **A 304 costs zero rate-limit budget** — `x-ratelimit-used` held at 999 across three conditional
  304s, advancing only on unconditional 200s.
- **The sub-tree ETag is sensitive only to its sub-tree** — stable across six unrelated repo-wide
  commits, distinct for each of three commits that touched the directory. This was the design's
  largest untested assumption; had it failed, the zero-cost steady state would have collapsed.
- **Go's `base64.StdEncoding.DecodeString` tolerates GitHub's line wrapping** — compiled and run.
  Worth noting the guarantee's exact scope: it ignores `\r` and `\n` and nothing else, so it holds
  because GitHub emits `\n` alone. Preferring the raw media type sidesteps the question.
- **The undocumented `{ref}:{path}` tree-ish form works** and scopes recursion to one subdirectory.
- **A GitHub App installation token cannot be minted in CEL** — mito's registered function list
  contains no RSA signing primitive and no JWT builder, only symmetric HMAC. The conclusion holds.

**Reasoning that stands:** the categorization triple; event stream rather than entity stream, on the
decisive `entity.type` argument; `nested` rather than `object` for version ranges, with the
false-positive walkthrough being correct Elasticsearch behaviour; the Elasticsearch `version` type
over `keyword` for bounds, with 89 in-repo precedents and package-spec support; the git blob SHA not
belonging in `file.hash.sha1`; nothing belonging in `related.*`; the IOC section being detection
guidance rather than indicators; `owner` and `repo` as separate variables; host-only `api_url`; and
`interval: 1h`.

**Sample data is genuinely verbatim.** All nine advisory Markdown files were re-fetched from
`discuss.elastic.co/raw/<topic_id>` and diffed: byte-identical once Discourse's own post banner and
trailing separator are accounted for. Nothing paraphrased, reformatted or fabricated. Three defects,
all fixed: the RSS sample was not well-formed XML because its provenance comment preceded the
`<?xml?>` declaration; four JSON files lacked the provenance header the documents claimed they all
carried; and `ESA-2026-24.mapped-ecs.json` carried undeclared synthetic values, including a
`file.name` that is now wrong on both extension and padding.

---

## 5. Guardrail violations

The research skill prohibits research output from prescribing ingest-pipeline, CEL-program or
`fields/*.yml` implementation detail. Both analysis documents open by asserting they do not, and both
then do — six instances, quoted in `references/review-ecs-and-config.md` §Guardrail violations. The
substantive ones are the document-`_id` fingerprint recommendation (an ingest-processor decision),
a complete field-by-field type specification that is `fields/*.yml` authoring in table form, a
`redact.fields` instruction attached to a configuration variable, an ECS dependency-pin prescription,
and a glob-versus-RE2 recommendation that contradicts the same document's own open-questions entry.

None of it is *wrong* — the `_id` reasoning in particular is well-argued and its precedents verified
— but it pre-empts decisions that belong to the builder skills, which have authoritative patterns the
research phase cannot see. This review has not stripped that content, because deleting verified
analysis to satisfy a process rule would destroy value; it is flagged so the builder knows to treat it
as input rather than instruction. The same care applies to this review's own most useful finding: that
a single CEL evaluation can issue many HTTP requests is recorded as a **verified capability and a
sizing constraint**, deliberately not as an instruction about how to structure the program.

Notably, neither document ever recommends `preserve_duplicate_custom_fields`, `event.ingested` or an
`event.original`-removal toggle. All three appear only in explicit do-not-copy tables, which is the
sanctioned form.

---

## 6. What to do next

1. **Get one file.** `ESA-2026-0081.json` for preference, since its public twin is already captured
   for side-by-side comparison. This closes the last blocking unknown and settles whether the
   fixed-version gap in §4.6 of the brief is real.
2. **Get a path listing.** `gh api repos/elastic/security-advisories/git/trees/main:advisories?recursive=1`
   counted by path shape answers the corpus-size question, the flat-versus-nested question, and
   whether unpublished advisories are present — all at once.
3. **Resolve the governance question** (brief §8, question 11) before building, because it may
   determine who the integration is for.
4. **Start the token approval early.** Fine-grained tokens against org resources need owner approval,
   and owners are notified by a once-daily digest.
5. Treat `test-api.py` as ready to run against the real repository. It was executed end to end against
   a 5,733-file directory during this review, exiting 0 with no token leakage and a correct free-304
   revalidation, and its `KeyboardInterrupt` summary bug has been fixed.

---

## 7. Confidence, restated honestly

| Area | Confidence | Why |
|---|---|---|
| GitHub API collection mechanics | **High** | Every load-bearing claim reproduced live, including the three riskiest assumptions |
| Rate limits, backfill and cursor sizing | **High** | Re-measured across the plausible corpus range |
| ECS field existence and targets | **High** | Independently re-verified against four ECS versions |
| Categorization and mapping-type decisions | **High** | Conclusions verified; supporting framing corrected |
| Configuration surface | **High** | Every cited manifest reproduced exactly; one justification replaced |
| Advisory content and field semantics | **Medium-High** | Sample data verbatim; CVE analysis exact; hand-counted body statistics corrected |
| Corpus size and composition | **Medium** | Public census solid; the >600-file gap is unexplained |
| **The JSON schema itself** | **Low** | Format known, field names unknown. The one blocking item |
