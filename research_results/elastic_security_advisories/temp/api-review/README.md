# API review scratch space

Reproduction material for `references/review-github-api.md`. Everything here was produced by
live calls against `api.github.com` using a GitHub App installation token scoped to
`elastic/integrations` (obtain with `gh auth token`).

| File | What it is |
|---|---|
| `contents_hdr.txt` / `contents_body.json` | Contents API on the 5,733-file directory — 1,000 entries, HTTP 200, no `Link`, no `truncated` |
| `trees_hdr.txt` / `trees_body.json` | Trees API on the same directory — 5,733 entries, `truncated: false`, 1,803,608 bytes |
| `h1.txt`–`h5.txt` | Trees ETag / `If-None-Match` sequence proving a 304 costs zero rate-limit budget |
| `bh1.txt`–`bh3.txt`, `bb1.json`, `bb3.raw` | Blobs API: base64 60-char MIME wrapping, free 304, and the `application/vnd.github.raw` comparison |
| `full_hdr.txt` | Headers of the full recursive tree of `elastic/integrations` (55,987 entries, 18,465,061 bytes, `truncated: false`) |
| `touched.txt` / `headcommits.txt` | Commit SHAs used for the sub-tree ETag stability test |
| `gotest/main.go` | Go program proving `base64.StdEncoding.DecodeString` ignores `\r`/`\n` but not other whitespace |
| `batch.cel` + `batch_state.json` | **The key test**: one CEL evaluation issuing 1 tree request + 10 blob requests |
| `cond.cel` + `cond_state.json` | CEL steady-state conditional poll returning 304 |
| `trees-doc.txt`, `blobs-doc.txt`, `ratelimits-doc.txt` | Text renderings of the official docs fetched during the review |
| `run1/`–`run7/` | `test-api.py` execution logs. Large `trace.json`/`.tar.gz` outputs were pruned |

The `token` field in `batch_state.json` and `cond_state.json` is redacted; refill it before use.
Rebuild the mito CLI with:

```
git clone --depth 1 https://github.com/elastic/mito.git && go build -o /tmp/mito ./mito/cmd/mito
/tmp/mito -data batch_state.json -max_executions 1 batch.cel
```
