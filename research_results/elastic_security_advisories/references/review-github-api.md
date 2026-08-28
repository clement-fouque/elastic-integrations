# Critical review — GitHub REST API research and `test-api.py`

**Reviewer:** adversarial audit pass, 2026-08-28
**Artifacts audited:** `references/github-api-collection-notes.md`, `test-api.py`,
`research-brief.md` §2–§3
**Scratch space / reproducibility:** `temp/api-review/`

**New facts assumed for this review** (supplied by a human with repository access, not
verifiable from this sandbox — the token here 404s on `elastic/security-advisories`):

1. Advisory files are **JSON** (`ESA-2026-0081.json`).
2. `advisories/` **may contain more than 1,000 files**. All costing in the audited documents
   assumes **200–500**. Re-costed here at **1,000–3,000 and growing**.

**Verification legend:** `[VERIFIED-LIVE]` = I ran it and observed the result.
`[VERIFIED-DOC]` = current official documentation, fetched today. `[UNVERIFIED]` = inference.

---

## Verdict

**`github-api-collection-notes.md` — sound, and its central technical claims survive live
re-testing.** I reproduced every load-bearing empirical claim in §1–§3 independently: the
Contents API's silent 1,000-entry truncation, the Trees API returning all 5,733 entries with
`truncated: false`, the undocumented `{ref}:{path}` tree-ish form, the byte-identical 404 across
every access-failure mode, and the zero-rate-limit-cost 304. The recommendation of Strategy A
(sub-tree ETag + persisted `path → blob SHA` map) is correct and I found a stronger argument for
it than the notes make: I verified that the sub-tree ETag is **stable across six unrelated
repo-wide commits** and changes **only** when the sub-tree's own git tree SHA changes, which is
the precise property the strategy needs and which the notes assert without testing. The document's
defects are all in *sizing*, not mechanics: it is calibrated for 200–500 files, and §2's cost
tables, the 40–50 KB cursor estimate, and gap #5's `max_executions` reasoning are all wrong at
1,000–3,000 files. It also misses two free wins (the Blobs API supports free 304s; the
`application/vnd.github.raw` media type is 29% cheaper on the wire and eliminates base64
entirely) and one implementation trap (the CEL input will see a **weak** `W/"…"` ETag, not the
strong one the notes recorded from curl).

**`research-brief.md` §2–§3 — accurate as a summary, but it inherits and compounds the sizing
error.** Every mechanical claim I checked in §2.1, §3.1, §3.2 and §3.3 is correct, including the
`2022-11-28` / `2026-03-10` API-version claim, the rate-limit table, the header names, and the
"5,000/hr is per user" claim. Two things are wrong. §1.3's "roughly 200–500 advisories in the
complete historical corpus" is contradicted by the human report and is the root of every
downstream miscalculation; §3.4's "~500 entries … ≈ 40–50 KB" cursor figure is 3–6× too small.
Separately, §3.3's framing that the Trees response is a single un-paginated shot is right, but
the brief never states the practical consequence at 3,000 files: the **backfill**, not the tree
call, is the scaling problem.

**`test-api.py` — it works. I ran it end to end against public repositories and it did exactly
what it claims to do**, including against a 5,733-file directory, with exit 0, no token leakage,
and a correct 304 revalidation that proved zero rate-limit cost. It is standard-library-only and
meets almost every stated requirement. It has one genuinely bad bug (a `KeyboardInterrupt`
discards the entire execution summary and reports a successful run as all-zeros) and one that
matters specifically at the new scale (`trace.json` grows ~30 KB per blob and would reach ~90 MB
on a 3,000-file run). Its bigger conceptual gap is that it **never exercises the change-detection
mechanism the whole design rests on** — it fetches the first N files rather than diffing a
`path → blob SHA` map, so the one part of Strategy A that could actually be wrong in production
is the one part the test script does not test.

**Bottom line on the design: the recommended architecture survives a 3,000-file corpus, but only
because a fix the documents do not mention is available.** The backfill fits inside one hour's
rate-limit budget (60% of it at 3,000 files). The `max_executions` default of 1,000 **is exceeded**
by a naive one-blob-per-execution backfill at 1,000+ files — but I proved live that a single CEL
evaluation can issue many HTTP requests, which reduces the execution count by the batch factor
and removes the constraint entirely. The documents present the one-blob-per-execution model as if
it were forced. It is not.

---

## Live verification log

| Claim | Method | Result | Verdict |
|---|---|---|---|
| Contents API silently truncates a directory at 1,000 entries: HTTP 200, no `truncated`, no `Link`, no warning | `curl` on `elastic/integrations/contents/packages/security_detection_engine/kibana/security_rule` | **HTTP 200**, exactly **1,000** array entries, 1,427,807 bytes, **no `Link` header**, response is a bare JSON array so no `truncated` key can exist | **[VERIFIED-LIVE] Confirmed exactly** |
| Contents API ignores `per_page`/`page` | `…/contents/packages?per_page=5&page=1` | **481** entries returned, **0** `Link` headers. `?per_page=100&page=2` on the 5,733-file dir also returns 200 with no `Link` | **[VERIFIED-LIVE] Confirmed** |
| Trees API returns all 5,733 entries with `truncated: false` | `git/trees/main:packages/…/security_rule?recursive=1` | **5,733 entries**, all `type: blob`, `truncated: false`, **response size 1,803,608 bytes (1.72 MiB)** | **[VERIFIED-LIVE] Confirmed; exact size reported** |
| Undocumented `{branch}:{path}` tree-ish form works and scopes recursion | Same call as above; paths returned were `000047bb-…_415.json` etc. | Works. Returned `path` values are **relative to the sub-tree**, not the repo root. Literal `:` is accepted unencoded | **[VERIFIED-LIVE] Confirmed** |
| All access-failure modes return a byte-identical `{"message":"Not Found"}` | 5 variants (bad path, bad branch, bad repo, bad owner, real-but-private repo), md5 of each body | All five: **HTTP 404, 124 bytes, md5 `a11f74e873af40b9e9ea935139d48c61`** — byte-identical | **[VERIFIED-LIVE] Confirmed** |
| …but is 404 the *only* failure mode? | `git/trees/main:packages/github/manifest.yml?recursive=1` (path points at a **file**) | **HTTP 422**, different body: `"Invalid object requested. SHA must identify a commit or a tree."` | **[VERIFIED-LIVE] Undocumented in both artifacts — see Errors** |
| Documented Trees bound is 100,000 entries / 7 MB | Fetched `https://docs.github.com/en/rest/git/trees` today | Doc **unchanged**: "The limit for the `tree` array is 100,000 entries with a maximum size of 7 MB when using the `recursive` parameter" | **[VERIFIED-DOC] Confirmed, doc has not changed** |
| An 18.4 MB response returned `truncated: false`, contradicting the 7 MB bound | Full recursive tree of `elastic/integrations@main` | **55,987 entries, 18,465,061 bytes, `truncated: false`**. **gzip of that same body = 2,124,003 bytes (2.0 MB) — under 7 MB** | **[VERIFIED-LIVE] Confirmed, and the discrepancy is now explained** |
| `X-GitHub-Api-Version: 2022-11-28` still works; current is `2026-03-10` | Sent `2022-11-28`, `2026-03-10`, `2099-01-01`, and no header | `2022-11-28` → 200, `x-github-api-version-selected: 2022-11-28`. `2026-03-10` → 200. `2099-01-01` → **400**, error names both supported versions. **No header → defaults to `2022-11-28`** | **[VERIFIED-LIVE] Confirmed exactly** |
| Trees API supports `If-None-Match`; a 304 costs zero budget | 200 → capture etag → 2 × conditional → 1 × unconditional | `used: 104` (200) → `104` (304) → `104` (304) → **`105`** (200). Independently: `/rate_limit` `used=0` → **30 consecutive 304s** → `used=0` | **[VERIFIED-LIVE] Confirmed, twice** |
| **Blobs API** supports `If-None-Match` and a 304 is free | Blob 200 → capture etag → conditional | **HTTP 304**, `x-ratelimit-used: 122` → `122`, unchanged | **[VERIFIED-LIVE] New — not claimed in either artifact** |
| The ETag must be sent back **with** its surrounding quotes | Sent the digest with quotes stripped | Without quotes → **HTTP 200** and the counter incremented. With quotes → 304 | **[VERIFIED-LIVE] Confirmed** |
| **Does the sub-tree ETag change only when the sub-tree changes?** | Requested `{commit}:packages/github/data_stream/security_advisories` at 6 different repo-wide commits, then at 3 commits that touched that path | **Stable** across all 6 unrelated commits (same tree SHA `efcea1c7…`, same ETag). **Changed** exactly with the tree SHA on the touching commits (3 tree SHAs → 3 distinct ETags) | **[VERIFIED-LIVE] The strategy's core assumption is correct** |
| Is the ETag the tree SHA? | Compared values | **No.** ETag is 64 hex chars (SHA-256 of the representation); tree SHA is 40 hex (git SHA-1). They are 1:1 but **not equal** | **[VERIFIED-LIVE] Correction to an implicit assumption** |
| ETag strength / gzip | curl with and without `--compressed`; and via mito's Go HTTP client | No gzip → **strong** `"7a3b…"`. gzip → **weak** `W/"7a3b…"` (same digest). **mito/Go sees the weak form** because Go negotiates gzip automatically. GitHub returns 304 for **either** form | **[VERIFIED-LIVE] New — see Errors** |
| Blobs API base64 `content` is MIME-wrapped every 60 chars | Fetched a 6,143-byte blob | `content` is 8,329 chars in **138 segments**, first segments all exactly **60** chars, separated by `\n`, **no `\r`** | **[VERIFIED-LIVE] Confirmed exactly** |
| Go's `base64.StdEncoding.DecodeString` ignores `\r`/`\n` | Wrote and ran a Go program (go1.26.0) — `temp/api-review/gotest/main.go` | **TRUE but narrow.** `\n` OK, `\r\n` OK, leading/trailing `\n` OK. **Space, tab, `\v`, `\f`, NUL, `-` all ERROR** (`illegal base64 data at input byte 10`) | **[VERIFIED-LIVE] Claim is correct; not a blocking bug** |
| Blobs API size limit and media types | `https://docs.github.com/en/rest/git/blobs` | "This endpoint supports blobs up to **100 megabytes**." Media types: `application/vnd.github.raw+json` (raw data), `application/vnd.github+json` (base64, default) | **[VERIFIED-DOC] Confirmed** |
| Is `raw` the better media type? | Fetched the same blob both ways; then 100 blobs each way | Byte-identical payload. Default: 8,329-char base64 in a JSON envelope. Raw: **6,143 bytes**, `content-type: text/plain`. Over 100 blobs: **1,292,920 vs 916,962 wire bytes = 29% saving**, and no base64 decode | **[VERIFIED-LIVE] Yes — neither artifact recommends it** |
| 5,000/hr, 900 points/min, 100 concurrent, header names | `https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api` | All confirmed verbatim: "personal rate limit of 5,000 requests per hour"; "No more than 100 concurrent requests"; "No more than 900 points per minute … for REST API endpoints"; `x-ratelimit-{limit,remaining,used,reset,resource}` | **[VERIFIED-DOC] Confirmed** |
| "The 5,000/hr limit is per *user*, not per token" | Same doc | "All of these requests count towards **your personal rate limit** of 5,000 requests per hour… if an app with a 15,000 request limit makes 10,000 requests on your behalf, you will have exhausted the 5,000 request budget for your personal access tokens" | **[VERIFIED-DOC] Confirmed for PATs** |
| 429 with `x-ratelimit-remaining: 10` and no `retry-after` is plausible | Same doc, "Exceeding the rate limit" | GitHub's own guidance has exactly this branch: "If the `retry-after` … is present … If the `x-ratelimit-remaining` header is `0` … **Otherwise, wait for at least one minute before retrying.**" The "otherwise" case *is* 429-with-budget-remaining | **[VERIFIED-DOC] Observation plausible; recommendation is sound and matches GitHub's own ladder** |
| Rate-limit counters are trustworthy | Repeated `/rate_limit` reads with settling time | **They are not.** Consecutive reads returned `used=0/reset=1787936950`, then `used=25/reset=1787933782` (**reset moved backwards 3,168 s**), then `used=0/reset=1787936998`. Counters are per-edge and eventually consistent | **[VERIFIED-LIVE] New — independently reinforces "status code is authoritative"** |
| `max_executions` default is 1,000 | `temp/filebeat-cel-input-doc.txt` line 424 | "…maximum number of times a CEL program can request to be re-run with a `want_more` field… **Default: 1000.**" Also: `remaining_executions` is readable inside the program (Stack 9.2+) | **[VERIFIED-DOC] Confirmed** |
| The `github` package sets 5,000 | `packages/github/data_stream/security_advisories/agent/stream/cel.yml.hbs:24` | `max_executions: 5000` — **hardcoded in the template, not a Fleet config variable** (not present in `manifest.yml`) | **[VERIFIED-LIVE] Confirmed, with an important nuance** |
| **Can a CEL program fetch multiple blobs in one execution?** | Built mito v1.27.0's CLI from source; ran a program doing `front(tree, 10).map(e, get_request(e.url).with({…}).do_request())` against the live API | **YES.** One evaluation performed **1 tree request + 10 blob requests**, all HTTP 200. `x-ratelimit-used` went 129→139 monotonically, proving the requests are issued **serially** within the evaluation | **[VERIFIED-LIVE] This invalidates the documents' framing of the constraint** |
| The CEL 304 path works end to end | mito program sending `If-None-Match` with the weak `W/"…"` ETag | `status=304, body_size=0`, `x-ratelimit-used` unchanged across repeated polls | **[VERIFIED-LIVE] Confirmed** |
| mito registers no RSA/JWT primitive | Cloned `elastic/mito` v1.27.0; enumerated `cel.Function(…)` in `lib/crypto.go` and across `lib/*.go` | `crypto.go` registers **`base64`, `base64_decode`, `base64_raw`, `base64_raw_decode`, `hex`, `hex_decode`, `hmac`, `md5`, `sha1`, `sha256`, `uuid`**. Repo-wide the only other auth/signing helpers are `basic_authentication` and `sign_aws_from_{env,shared,static}` (HMAC-based SigV4). **No RSA, no JWT** | **[VERIFIED-LIVE] Conclusion holds; the listed set was slightly incomplete** |
| Serial blob-fetch throughput (needed for backfill costing) | 100 sequential blob fetches, both media types, from this sandbox | **4.6 req/s (216 ms/req)** base64; **4.8 req/s (207 ms/req)** raw. Used **0.210 s/req** for all arithmetic below | **[VERIFIED-LIVE] New measurement** |

---

## Errors

| Location | Claim | What's actually true | Severity |
|---|---|---|---|
| brief §1.3; notes §2 baseline; notes §2 Strategy A/D tables; brief §2.2 strategy table | "roughly 200–500 advisories in the complete historical corpus"; all cost tables built on 500 | The corpus is reported to be **>1,000 files**. Every "501 calls", "12,024 calls/day", and "40–50 KB" figure derived from 500 is wrong by **2–6×**. See the Scale section for corrected numbers | **major** — it is the root of every other sizing error, though no conclusion actually reverses |
| brief §3.4 "Cursor size"; notes §2 Strategy A "Cons" | "~500 entries × (~45-char path + 40-char SHA) ≈ **40–50 KB**" | Arithmetic is right for 500. At the real scale, with flat `ESA-2026-0081.json` (18-char) paths: **1,000 → 62 KiB, 2,000 → 123 KiB, 3,000 → 185 KiB**. With the brief's own 45-char assumption, **3,000 → 264 KiB**. This is the single largest recurring per-checkpoint write in the Filebeat registry | **major** |
| notes gap #5; brief §8 (summarised in the task as §2/§3) | "`max_executions` (default 1,000; the `github` package sets 5,000) bounds `want_more` re-requests, and a 500-file backfill fetching one blob per execution needs ~500 of them" | Two errors. (a) **At 1,000+ files the default 1,000 is exceeded** — 3,000 files needs 3,001 executions. The framing "500 is fine" no longer holds. (b) More importantly the premise is false: **a single CEL evaluation can issue many HTTP requests** via `map(…, get_request(…).do_request())`. I ran 11 requests in one evaluation. At 50 blobs/execution a 3,000-file backfill needs **61 executions**, not 3,001. The constraint the documents flag as "real" is an artefact of an unnecessary design choice | **major** — it is presented as a hard constraint on the implementer and it is not |
| notes §1.4; brief §3.2 endpoint table | Blobs fetched with the default `application/vnd.github+json` (base64 in a JSON envelope); `raw` is mentioned only for the *Contents* API | `application/vnd.github.raw` works on the **Blobs** endpoint too, returns byte-identical content, and is **29% smaller on the wire** (916,962 vs 1,292,920 bytes over 100 blobs). It also removes the base64 decode step and the MIME-wrapping concern entirely. At a 3,000-file backfill that is ~11 MB of avoided transfer | **major** — a free ~29% saving on the only expensive part of the design, not taken |
| notes §1.4; brief §2.1, §3.4 | The zero-cost 304 property is established for the Contents and Trees APIs only | The **Blobs API also honours `If-None-Match` at zero cost** (verified: `used: 122` → 304 → `122`). Because a blob URL is content-addressed this is of limited use for change detection, but it does make a re-fetch of an unchanged blob free — relevant to any retry or reconciliation path | **minor** (missed opportunity, not an error) |
| notes §1.3 "The Trees API supports conditional requests"; brief §3.4 | Records the ETag as the strong form `"6061b34d…"` | The **Go HTTP client — and therefore mito and the `cel` input — receives the weak form `W/"…"`**, because Go transparently sends `Accept-Encoding: gzip` and GitHub weakens the validator on a transformed representation. The digest is identical and **GitHub returns 304 for either form**, so this is not blocking. But any CEL code that parses, trims, or reconstructs the ETag rather than echoing it verbatim will break, and an implementer testing with curl will see a different value than production | **minor** — non-blocking but a real trap, documented nowhere |
| brief §2.3; notes §3.5; `test-api.py` docstring | "Four completely different faults … all return a **byte-identical** `{"message":"Not Found"}`" | **True — I confirmed byte-identity by md5 across five variants** (124 bytes, md5 `a11f74e873af40b9e9ea935139d48c61`). But the enumeration is incomplete: pointing the path at a **file** rather than a directory returns **HTTP 422** with `"Invalid object requested. SHA must identify a commit or a tree."` That is a genuinely useful, *distinguishable* diagnostic signal that the four-step 404 ladder never mentions | **minor** |
| notes §1.3 "Observed discrepancy"; brief §3.3; notes gap #2 | "An 18.4 MB response returned `truncated: false` … whether the documented 7 MB figure refers to a compressed size, is stale, or is simply not enforced is unresolved" | Reproduced (18,465,061 bytes, 55,987 entries, `truncated: false`) and **partially resolved**: **gzip of that body is 2,124,003 bytes = 2.0 MB, comfortably under 7 MB.** The compressed-representation interpretation is consistent with the observation; the "not enforced" interpretation is not required to explain it | **minor** — the practical advice ("trust the flag") was already correct |
| notes §4.3; brief §3.1 | mito "registers only `base64`, `base64_decode`, `base64_raw`, `base64_raw_decode`, `md5`, `sha1`, `sha256`, `hmac`, `hex`, and `uuid`" (brief's shorter list omits three more) | The actual `lib/crypto.go` set in v1.27.0 also includes **`hex_decode`**. Elsewhere in the library there are `basic_authentication` and `sign_aws_from_{env,shared,static}`. **None of this changes the conclusion** — there is still no RSA primitive and no JWT builder, so the GitHub App path remains infeasible | **minor** |
| notes §3.1 | "The authorization caveat is important: an **unauthenticated 304 does consume budget**" | Could not reproduce and the framing is misleading. An unauthenticated conditional request carrying an ETag obtained *with* auth returns **HTTP 200, not 304**, because the response `Vary`s on `Authorization`. The operationally important fact is the one the note does not state: **ETags are scoped to the credential**, so rotating the token invalidates every cached ETag and forces one full re-enumeration | **minor** |
| notes §2 Strategy A "Pros"; brief §3.4 | Asserts the sub-tree ETag gives exact change detection, without testing whether unrelated repo activity perturbs it | The claim is **correct** — I verified it (stable across 6 unrelated commits, changes 1:1 with the sub-tree tree SHA). Recording this as an error only because it was the design's single biggest untested assumption in a monorepo-adjacent context, and it was asserted rather than shown | **minor** (now verified — see What holds up) |

---

## Scale re-analysis at 1000–3000 files

All arithmetic uses a measured **0.210 s per serial request** (100 sequential blob fetches from
this sandbox: 21.64 s for base64, 20.73 s for raw → 4.6–4.8 req/s).

### Backfill cost — the headline number

One tree call plus one blob call per file:

| Files | API calls | Serial wall time | % of the 5,000/hr budget | Sustained rate | % of the 900-points/min secondary limit |
|---|---|---|---|---|---|
| 500 (the documents' assumption) | 501 | 105 s (1.8 min) | 10.0% | 285 req/min | 31.7% |
| **1,000** | **1,001** | **210 s (3.5 min)** | **20.0%** | 285 req/min | 31.7% |
| **2,000** | **2,001** | **420 s (7.0 min)** | **40.0%** | 285 req/min | 31.7% |
| **3,000** | **3,001** | **630 s (10.5 min)** | **60.0%** | 285 req/min | 31.7% |
| 5,733 (reference) | 5,734 | 1,204 s (20.1 min) | **114.7%** | 285 req/min | 31.7% |

**Does the backfill exceed a single hour's budget? No — not until roughly 4,999 files.** At
3,000 files it consumes 60% of the hourly budget in about ten and a half minutes. That is a
one-time cost and it fits. Three caveats the documents should state:

- The 5,000/hr is **per user, not per token** [VERIFIED-DOC]. If the same human's account runs
  other automation, 60% is a large shared draw, and the safe reading is "the backfill may fail
  once and need to resume", not "the backfill always fits".
- **Growth matters.** At the stated ~15 advisories/month the corpus reaches 5,000 files and
  crosses the one-hour boundary eventually. The design should be resumable across intervals
  rather than assume a single-shot backfill, which the Strategy A cursor already gives for free:
  a partial backfill just leaves entries missing from the `path → SHA` map and the next poll
  picks them up.
- Using `application/vnd.github.raw` does not reduce the **call count** (the rate limit is
  per request, not per byte) but cuts the transfer from ~13 MB to ~9 MB at 3,000 files.

**Secondary limits are not a concern.** 285 req/min is 31.7% of the 900-points/min ceiling
(a GET is 1 point [VERIFIED-DOC]), and mito issues requests **serially** within an evaluation
(verified: `x-ratelimit-used` incremented monotonically 129→139 across a 10-request `map`), so
the 100-concurrent limit is never approached.

### Steady state — unchanged and still excellent

The number of files does **not** affect the steady-state cost, because it is a single conditional
request:

- 24 polls/day, no changes: **24 requests, 0 rate-limit units** [VERIFIED-LIVE — 30 consecutive
  304s moved `/rate_limit` `used` from 0 to 0].
- The worst observed real day (48 advisories published on 2026-08-13, per brief §1.3):
  1 tree 200 + 48 blobs = **49 units, 1.0% of the hourly budget**.

This is the strongest part of the design and it is entirely scale-independent. It does not break.

### Cursor size — grows 3–6×, still workable

Cursor JSON is `{"<path>":"<40-hex sha>", …}`, i.e. `len(path) + 45` bytes per entry
(2 quotes + colon + 2 quotes + 40 hex + comma).

| Files | Flat `ESA-2026-0081.json` (18 ch) | Nested `2026/ESA-2026-0081.json` (23 ch) | Brief's 45-char assumption |
|---|---|---|---|
| 500 | 30.8 KiB | 33.2 KiB | **43.9 KiB** ← the brief's "40–50 KB" |
| **1,000** | **61.5 KiB** | 66.4 KiB | 87.9 KiB |
| **2,000** | **123.0 KiB** | 132.8 KiB | 175.8 KiB |
| **3,000** | **184.6 KiB** | 199.2 KiB | **263.7 KiB** |

The brief's 40–50 KB becomes **62–264 KiB** depending on layout and count. There is no documented
Filebeat registry cursor size limit, and a ~185 KiB JSON object rewritten on each checkpoint is
not dangerous, but it is no longer a footnote and should be stated honestly. Two cheap mitigations
if it becomes a problem, in preference order:

1. **Truncate the stored SHA to 12 hex characters.** Collision probability across 3,000 files is
   ~1.6 × 10⁻⁸ (birthday bound, 48 bits). This cuts the cursor to ~108 KiB. `[UNVERIFIED]` —
   arithmetic only, but the bound is standard.
2. Do **not** fall back to storing only the sub-tree SHA. That is Strategy D in disguise: any
   single-file change would force re-fetching all 3,000 blobs (60% of the hourly budget per
   change event), and advisories publish in batches, so it would fire often.

### Tree response size — a non-issue

The 5,733-entry tree was 1,803,608 bytes → **315 bytes/entry**. A 3,000-file `advisories/` tree is
therefore ~**945 KB**: 3% of the 100,000-entry bound and well under 7 MB even uncompressed. The
`truncated` flag will not trip. `[VERIFIED-LIVE + extrapolated]`

### `max_executions` — the one number that actually breaks

`max_executions` default is **1,000** [VERIFIED-DOC]. `packages/github/data_stream/security_advisories`
hardcodes **5,000** at `cel.yml.hbs:24`, and it is **not exposed as a Fleet variable**, so a new
package must set it in its own template — it is not inherited.

One blob per execution (the model both documents assume):

| Files | Executions needed | vs. default 1,000 | vs. `github`'s 5,000 |
|---|---|---|---|
| 500 | 501 | OK | OK |
| **1,000** | **1,001** | **EXCEEDS** | OK |
| **2,000** | **2,001** | **EXCEEDS** | OK |
| **3,000** | **3,001** | **EXCEEDS** | OK (60% consumed, little headroom) |

**So the answer to the key scale question is yes: at >1,000 files a one-blob-per-execution
backfill exceeds the default `max_executions`, and the documents' "a 500-file backfill needs ~500
of them" no longer reassures.** When the budget is exhausted, execution restarts at the next
interval with a warning in the log — so with a persisted cursor it would eventually converge, but
slowly and noisily.

**But the one-blob-per-execution model is not required.** [VERIFIED-LIVE] I built mito v1.27.0's
CLI and ran this against the live API — a single evaluation performing one tree request and ten
blob requests:

```
front(tree.tree.filter(e, e.type == "blob"), int(state.batch)).map(e,
  get_request(e.url).with({
    "Header": {
      "Accept": ["application/vnd.github.raw"],
      "X-GitHub-Api-Version": ["2022-11-28"],
      "Authorization": ["Bearer " + state.token],
    },
  }).do_request().as(blob, { "path": e.path, "sha": e.sha,
                             "blob_status": blob.StatusCode, "bytes": size(blob.Body) })
)
```

Result: **10 blobs fetched in one evaluation, all HTTP 200**, `x-ratelimit-used` 129→139
monotonically (i.e. issued serially, no concurrency risk). `do_request` is a member function on a
request map (`<map>.do_request() -> <map>`, `mito/lib/http.go`), so the standard CEL `map()` macro
composes over it. Reproduce with `temp/api-review/batch.cel`.

With batching the arithmetic collapses:

| Batch size | Executions for a 3,000-file backfill | Wall time per evaluation |
|---|---|---|
| 1 | 3,001 | 0.2 s |
| **50** | **61** | **10.5 s** |
| **100** | **31** | **21.0 s** |

**Recommended: batch 50–100 blobs per execution and use `want_more` only to advance between
batches.** That puts the backfill at 31–61 executions, comfortably inside even the default 1,000,
with no need to raise `max_executions` at all. Do not batch to 3,000-in-one: a single evaluation
would block the input for ~10.5 minutes.

### Design changes required

1. **Batch blob fetches with `map()` + `do_request()`** (50–100 per execution). Without this the
   default `max_executions` is exceeded at 1,000+ files. With it, the constraint disappears.
2. **Switch the blob fetch to `Accept: application/vnd.github.raw`.** 29% less wire traffic and no
   base64 decoding. Note that `size(resp.Body)` then gives the file bytes directly.
3. **Make the backfill resumable across intervals** rather than assuming it completes in one
   window. The `path → SHA` cursor already provides this; it just needs to be written
   incrementally after each batch rather than only at the end.
4. **Restate the cursor budget as ~185 KiB at 3,000 files**, not 40–50 KB, and set
   `max_executions` explicitly in the new package's template (it is not inherited from `github`).
5. Treat 403/429 as authoritative regardless of `x-ratelimit-remaining` — reinforced by my
   observation that the counters are per-edge and eventually consistent (`reset` moved backwards
   3,168 s between consecutive reads).

---

## test-api.py review

**It ran successfully.** `python3 -m py_compile` passes. Live runs against `elastic/integrations`
with a `gh auth token`:

- `--path packages/github/data_stream/security_advisories --max-pages 3` → **exit 0**, 26 tree
  entries, 14 blobs, ETag captured, **HTTP 304 on revalidation with `x-ratelimit-used: 159 → 159`
  ("conditional request was free")**, 3 blobs decoded.
- `--path packages/security_detection_engine/kibana/security_rule --max-pages 2` (the 5,733-file
  directory) → **exit 0**, `Tree entries: 5733`, `Files matched: 5733`, `Listing truncated: False`,
  304 revalidation free, both blobs decoded and correctly classified `format=json`.
- 400-blob run → exit 0, completed in ~85 s.

The limiting mechanism it offers is `--max-pages` (default **5**), which caps **blob fetches only**
— the tree enumeration is always full. That is **adequate** for a 5,733-file directory: the tree
call is a single request and the blob loop is bounded. The name is a misnomer (nothing paginates),
but the behaviour is right.

### Requirement conformance

| Requirement | Status | Evidence / note |
|---|---|---|
| Standard library only | **Pass** | AST scan of imports: `argparse, base64, fnmatch, json, logging, os, ssl, sys, tarfile, time, traceback, urllib`. Non-stdlib: **none** |
| Every credential & connection parameter as BOTH CLI and env var | **Partial** | Env vars exist for `--api-key`/`GITHUB_TOKEN`, `--url`, `--owner`, `--repo`, `--path`, `--branch`, `--proxy`/`HTTPS_PROXY`. **No env var for `--timeout`, `--max-pages`, `--file-pattern`, `--output-dir`, `--skip-revalidate`.** `--timeout` is a connection parameter |
| CLI takes precedence over env | **Pass** | Verified live: with `GITHUB_OWNER=WRONGOWNER GITHUB_REPO=WRONGREPO GITHUB_URL=https://wrong.example.com` plus CLI overrides, it used the CLI values and succeeded |
| Base URL configurable as a full URL including scheme | **Pass** | `--url` default `https://api.github.com`; docstring documents the GHES `/api/v3` and GHEC-residency forms |
| `--max-pages`-equivalent safety limit always present | **Pass** | `--max-pages`, default 5, always applied via `matched[:args.max_pages]` |
| TLS verification disabled | **Pass** | `ssl._create_unverified_context()` in `build_opener` |
| Step-by-step progress to stdout, no secrets, no raw bodies | **Pass** | Numbered `[1]`–`[5]` sections; prints counts/status/format only |
| Output dir with verbose `test-api.log` | **Pass** | DEBUG-level `FileHandler`, 13–194 KB across runs |
| Detailed `trace.json` with auth redacted | **Pass (with a caveat)** | `request.headers.Authorization` is `[REDACTED]`; **no token string found in any log or trace** (`grep -F` against the live token across 4 runs: all clean). Caveat: see bug 3 |
| Execution summary printed at the end | **Pass** | 78-char banner with status, counts, extensions, formats, rate-limit delta, errors |
| `.tar.gz` archive of the output dir | **Pass** | Created in every run; `--mock` correctly skips it |
| All exceptions caught and logged | **Pass** | `do_request` catches `HTTPError`/`URLError`/`Exception`; `main` wraps `run_collection` in `except Exception` with a redacted traceback |
| Rate-limit headers logged on 429 | **Pass** | `is_rate_limited()` returns True for **both 403 and 429**; `report_rate_limit_and_stop` logs `retry-after`, `x-ratelimit-{remaining,reset,limit,resource}`. Correctly treats the status code as authoritative |
| `KeyboardInterrupt` handled | **Pass, but broken** | Caught, artifacts written, exit 1 — but the summary is destroyed. See bug 1 |
| Exit 0 on success, 1 on failure | **Pass** | Verified: success → 0; bad path (404) → 1; path-is-a-file (422) → 1; interrupt → 1 |
| Handles the `truncated` flag | **Partial** | Reads it, sets `summary["truncated"]`, prints a WARNING telling the user to fall back to per-sub-tree enumeration. It does **not** implement the fallback. Acceptable for a test tool, and it cannot trip below 100,000 entries |
| Handles a >1,000-file directory | **Pass** | Verified at 5,733 files |
| Correctly exercises the ETag/304 path | **Pass** | Sends `If-None-Match` with the ETag **verbatim including quotes** (which I separately proved is mandatory), and compares `x-ratelimit-used` on the 200 against the 304 — the right anchor, as its own comment argues |
| Request sequence matches the brief's flow | **Mostly** | Steps 3/4/5 mirror the CEL program (tree → conditional tree → blob loop). Steps 1/2 are extra diagnostics, correctly labelled as not part of the CEL program. **But it never diffs a `path → blob SHA` map** — see bug 2 |

### Bugs

1. **`KeyboardInterrupt` discards the entire execution summary. (major)** In `main()`,
   `summary = run_collection(args, opener)` never completes, so `summary` is still `None` and the
   handler falls back to `{"status": "INTERRUPTED", …}`; the `setdefault` loop then fills
   everything with zeros. Verified by monkeypatching an interrupt into the third blob fetch: the
   run had reached the repository, enumerated 26 tree entries, confirmed a 304, and fetched 2
   blobs, yet the printed summary said `Repository accessible: False / Tree entries: 0 /
   Blobs fetched: 0`. `trace.json` still holds all 6 exchanges, so the data survives, but the
   headline output actively lies. On a 3,000-file corpus, interrupting a long run is the *expected*
   interaction. Fix: have `run_collection` accept (or `main` own) the summary dict so partial state
   survives, or catch `KeyboardInterrupt` inside `run_collection` and return what it has.
2. **It never tests the change-detection mechanism. (major, conceptual)** Step 5 fetches
   `matched[:max_pages]` — the *first* N files. The production design fetches *the files whose blob
   SHA differs from a persisted map*. The script has no cursor, no second enumeration, and no diff.
   Everything the script proves (tree works, 304 works, blobs decode) was already the safe part of
   the design; the part with real risk is untested. Adding a `--simulate-cursor` mode that writes
   the `path → SHA` map to the output dir, re-enumerates, and reports the delta would close this
   and would also let the operator report the real cursor size from their own corpus.
3. **`trace.json` grows ~30 KB per blob and embeds the full tree. (major at the new scale)**
   Measured: 3 blobs → 120 KB; 200 blobs → 6.2 MB; 400 blobs → **12 MB**. Two causes:
   `_try_parse_body` stores the **entire** tree response (all 5,733 entries) under
   `exchanges[2].response.body`, and every blob exchange stores the **full base64 `content`**
   (8,357 chars for a 6 KB file) *in addition to* the already-generous 4,000-char decoded preview.
   Extrapolated to a 3,000-file run: **~90 MB of `trace.json`** plus the tree, all held in the
   in-memory `TRACE` list first. Fix: cap the embedded tree at the first N entries plus a count,
   and drop or truncate the raw `content` field now that `decoded.preview` exists.
4. **Rate-limit delta can print nonsense. (minor, but misleading in a diagnostic tool)** Observed
   `Rate limit remaining: 4975 -> 5000 (consumed -25)` and, after 400 real blob fetches,
   `5000 -> 5000 (consumed 0)`. The cause is genuine — I independently confirmed GitHub's
   `/rate_limit` counters are per-edge and eventually consistent, with `reset` moving *backwards*
   3,168 s between consecutive reads — but the script should not present a negative or
   obviously-wrong consumption figure. It should prefer the `x-ratelimit-used` delta taken from the
   response headers of its own requests, and suppress the line when the delta is negative.
5. **No diagnostic for HTTP 422. (minor)** The 404 branch prints a four-item ladder and 401 gets a
   message, but a `--path` pointing at a **file** returns 422 (`"Invalid object requested. SHA must
   identify a commit or a tree."`) and the script prints only `FAILED (HTTP 422, 0.25s)`. This is
   the one access failure GitHub *does* distinguish, and the script throws the signal away.
6. **`decode_blob`'s docstring is wrong about Go. (minor)** It says GitHub's wrapping is safe
   because "Python's `b64decode` discards non-alphabet characters by default, so no stripping is
   needed — the same is true of Go's `base64.StdEncoding`". The Python half is correct. **The Go
   half is not**: Go ignores **only `\r` and `\n`** — I verified that space, tab, `\v`, `\f`, NUL
   and `-` all produce `illegal base64 data at input byte 10`. The conclusion still holds because
   GitHub emits only `\n` (verified: no `\r` in the response), but the stated reason is wrong and
   would mislead someone who later fed the same helper a differently-wrapped payload.
7. **`summary["revalidation_was_free"]` is set but never printed or defaulted. (trivial)** It is
   assigned in step 4, absent from `print_summary`, and absent from `main`'s `setdefault` list, so
   it appears in `trace.json` only on the happy path.
8. **`--max-pages` is a misnomer. (trivial)** Nothing paginates; it caps blob fetches. The
   docstring is accurate, the flag name is not.

### What needs to change for JSON and >1,000 files

- **JSON detection already works** — no change needed. Verified live: the `.json` rule files
  classified as `format=json` and the summary reported `.json 2 / json 2`. `detect_format` tries
  `json.loads` first for anything starting with `{` or `[`. The script does **not** assume Markdown
  and does **not** try to parse content beyond classification, so the JSON finding does not break it.
- **Update the docstring and defaults for the real corpus size.** `--max-pages`'s help text says
  "so a test run against a **500-file** corpus does not fetch all 500" — that number is now wrong
  everywhere it appears. Default 5 is still a sane sample.
- **Cap `trace.json`** (bug 3). At 1,000–3,000 files an operator raising `--max-pages` to sample
  broadly will produce a multi-tens-of-MB archive to email back.
- **Suggest `--file-pattern '*.json'` in the usage text** now that the extension is known, so the
  operator's run does not sample README or schema files.
- **Print the tree-entry count prominently and flag >1,000**, since that is the fact that
  invalidates the existing cost model and is the single most valuable number the operator can
  return. It is currently one line among ten in the summary.
- **Add the `path → SHA` cursor simulation** (bug 2). This is the highest-value addition: it would
  return the real cursor size and the real change rate from the actual corpus, which are the two
  numbers this review had to estimate.
- Consider switching the blob fetch to `Accept: application/vnd.github.raw` so the test exercises
  the media type the implementation should actually use.

---

## What holds up

These were re-verified today and should not be re-litigated.

**Trees API mechanics**

- The Contents API's 1,000-entry directory cap is real, silent, and returns HTTP 200 with no
  `truncated` field, no `Link` header, and no warning. [VERIFIED-LIVE]
- The Contents API ignores `per_page`/`page` for directory listings and never emits `Link`.
  [VERIFIED-LIVE]
- The Trees API returns all 5,733 entries of `packages/security_detection_engine/kibana/security_rule`
  with `truncated: false`, in a **1,803,608-byte** response. [VERIFIED-LIVE]
- The undocumented `{ref}:{path}` tree-ish form works, scopes recursion to one subdirectory,
  accepts a literal `:`, and returns paths relative to the sub-tree. [VERIFIED-LIVE]
- Documented bounds remain **100,000 entries / 7 MB**; the doc has not changed. [VERIFIED-DOC]
- Each tree entry carries a ready-made, directly-usable Blobs API `url`. [VERIFIED-LIVE]

**Conditional requests — the core of the design**

- The Trees API honours `If-None-Match` and **an authorized 304 costs zero rate-limit budget**.
  Confirmed twice, including 30 consecutive 304s that left `/rate_limit` `used` at 0. [VERIFIED-LIVE]
- The ETag must be echoed back **with its surrounding double quotes**; stripping them yields a 200
  and consumes budget. [VERIFIED-LIVE]
- **The sub-tree ETag changes if and only if the sub-tree's content changes.** Stable across six
  unrelated repo-wide commits; distinct for each of three commits that touched the path. It is
  functionally 1:1 with the sub-tree's git tree SHA (though not equal to it — SHA-256 vs SHA-1).
  This is the assumption Strategy A rests on and it is correct. [VERIFIED-LIVE]

**Blobs and encoding**

- Base64 `content` is MIME-wrapped at exactly 60 characters with `\n` and **no `\r`**.
  [VERIFIED-LIVE]
- **Go's `base64.StdEncoding.DecodeString` does ignore `\r` and `\n`**, so mito's `base64_decode`
  handles GitHub's wrapping with no stripping. Verified by compiling and running it (go1.26.0).
  The claim is correct — it is narrower than the documents imply (space/tab/`\v`/`\f`/NUL all
  fail), but GitHub never emits those. **Not a blocking bug.** [VERIFIED-LIVE]
- Blobs are supported up to **100 MB**. [VERIFIED-DOC]
- A blob is content-addressed, so its SHA is a sound change detector and document fingerprint.
  [VERIFIED-DOC + VERIFIED-LIVE]

**Authentication and versioning**

- `X-GitHub-Api-Version: 2022-11-28` still works and is in fact the **default when no header is
  sent**; `2026-03-10` also works; an unsupported value returns 400 naming both. [VERIFIED-LIVE]
- Both Trees and Blobs report `x-accepted-github-permissions: contents=read`. [VERIFIED-LIVE]
- **A CEL program cannot mint a GitHub App installation token.** mito v1.27.0 registers no RSA
  signing primitive and no JWT builder; the only signing helpers anywhere in the library are
  HMAC-based (`hmac`, `sign_aws_from_*`) plus `basic_authentication`. The conclusion is correct.
  [VERIFIED-LIVE against the cloned source]
- Every access failure — wrong owner, wrong repo, wrong branch, wrong path, real-but-invisible
  private repo — returns a **byte-identical 124-byte 404** (md5 `a11f74e873af40b9e9ea935139d48c61`).
  The diagnostic-ladder advice is justified. [VERIFIED-LIVE]

**Rate limits**

- 5,000/hr for PATs, and it is **per user**, shared with any app acting on that user's behalf.
  [VERIFIED-DOC]
- Secondary limits: 100 concurrent, 900 points/min per REST endpoint, GET = 1 point. [VERIFIED-DOC]
- Header names `x-ratelimit-{limit,remaining,used,reset,resource}` and `retry-after` are correct.
  [VERIFIED-DOC]
- **Both 403 and 429 are possible for either limit type**, and the recommendation to treat the
  status code as authoritative regardless of `x-ratelimit-remaining` is sound — GitHub's own
  retry ladder has exactly the "otherwise, wait at least a minute" branch that a
  429-with-budget-remaining falls into. The reported observation is fully consistent with the
  documented behaviour. [VERIFIED-DOC]
- `GET /rate_limit` does not count against the primary limit. [VERIFIED-DOC + VERIFIED-LIVE]

**Strategy selection**

- Strategy A (sub-tree ETag + `path → blob SHA` map) remains the correct choice at 1,000–3,000
  files. Its steady state is scale-independent and free; its backfill is a one-time 60%-of-budget
  cost at 3,000 files; and it detects deletions and renames for free. The competing strategies fail
  for the reasons given: Compare's 300-file cap is hard and unpaginated, Commits has a verified N+1
  and client-supplied timestamps, and full re-listing costs 3,001 calls **every poll** —
  72,024 requests/day at a 1h interval, permanently consuming **60% of the hourly budget** and
  re-indexing all 3,000 documents every hour. The documents cost this at 501 calls/poll and ~10%
  of budget; at the real scale it is six times worse, which turns Strategy D from "wasteful but
  self-healing" into something that could only ever be a bootstrap path, never a steady state.
