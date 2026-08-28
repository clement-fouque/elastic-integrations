#!/usr/bin/env bash
# Reproducibility script for the GitHub API claims in
# ../references/github-api-collection-notes.md
#
# Requires: an authenticated `gh` CLI (any token with public repo read access).
# All tests run against the public repo elastic/integrations so they are safe to re-run.

set -uo pipefail
TOKEN=$(gh auth token)
API=https://api.github.com
REPO=elastic/integrations
H=(-H "Authorization: Bearer $TOKEN" -H "X-GitHub-Api-Version: 2022-11-28")

hr() { printf '\n=== %s ===\n' "$1"; }

hr "Rate limit buckets for this token"
curl -s "${H[@]}" "$API/rate_limit" \
  | python3 -c "import json,sys; d=json.load(sys.stdin)['resources']; print(json.dumps({k:d[k] for k in ('core','search','code_search','graphql') if k in d}, indent=2))"

hr "Contents API: directory listing returns metadata only, no 'content'"
curl -s "${H[@]}" "$API/repos/$REPO/contents/packages/github/data_stream/security_advisories/agent/stream" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('is list:', isinstance(d,list)); print('entry keys:', list(d[0].keys())); print(\"'content' present:\", 'content' in d[0])"

hr "Contents API: single file DOES include base64 content (note embedded newlines)"
curl -s "${H[@]}" "$API/repos/$REPO/contents/packages/github/data_stream/security_advisories/manifest.yml" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('encoding:', d['encoding'], '| size:', d['size']); print('newlines in content:', chr(10) in d['content'])"

hr "Contents API: 1000-file cap is SILENT (dir actually has 5733 files)"
curl -s "${H[@]}" "$API/repos/$REPO/contents/packages/security_detection_engine/kibana/security_rule" \
  | python3 -c "import json,sys; print('entries returned:', len(json.load(sys.stdin)))"

hr "Contents API: directory listing does NOT paginate (per_page ignored, no Link header)"
curl -s -D /tmp/_h -o /tmp/_b "${H[@]}" "$API/repos/$REPO/contents/packages?per_page=5&page=1"
grep -i '^link:' /tmp/_h || echo "no Link header"
python3 -c "import json; print('entries with per_page=5:', len(json.load(open('/tmp/_b'))))"

hr "Trees API: same 5733-file dir returns ALL entries, truncated flag present"
curl -s "${H[@]}" "$API/repos/$REPO/git/trees/main:packages%2Fsecurity_detection_engine%2Fkibana%2Fsecurity_rule" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('truncated:', d['truncated'], '| entries:', len(d['tree']))"

hr "Trees API: undocumented {ref}:{path} tree-ish scopes recursion to one subdirectory"
curl -s "${H[@]}" "$API/repos/$REPO/git/trees/main:packages%2Fgithub%2Fdata_stream%2Fsecurity_advisories?recursive=1" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('truncated:', d['truncated'], '| entries:', len(d['tree'])); print('paths are subtree-relative:', [e['path'] for e in d['tree'][:3]]); print('entry:', json.dumps(d['tree'][1], indent=2))"

hr "Conditional request: 304 costs ZERO rate limit (this is the key finding)"
U="$API/repos/$REPO/contents/packages/github/data_stream/security_advisories/agent/stream"
curl -s -D /tmp/_h1 -o /dev/null "${H[@]}" "$U"
grep -iE '^(HTTP|etag|last-modified|x-ratelimit-(remaining|used))' /tmp/_h1
ETAG=$(grep -i '^etag:' /tmp/_h1 | sed 's/^[Ee][Tt][Aa][Gg]: //' | tr -d '\r')
echo "--- replaying with If-None-Match: $ETAG ---"
curl -s -D - -o /dev/null "${H[@]}" -H "If-None-Match: $ETAG" "$U" \
  | grep -iE '^(HTTP|x-ratelimit-(remaining|used))'

hr "Trees API also supports ETag / 304"
T="$API/repos/$REPO/git/trees/main:packages%2Fgithub?recursive=1"
E=$(curl -s -D - -o /dev/null "${H[@]}" "$T" | grep -i '^etag:' | sed 's/^[Ee][Tt][Aa][Gg]: //' | tr -d '\r')
curl -s -D - -o /dev/null "${H[@]}" -H "If-None-Match: $E" "$T" | grep -iE '^(HTTP|x-ratelimit-remaining)'

hr "Compare API: files[] capped at exactly 300, no pagination escape"
BASE=$(git -C /workspace log --format=%H -n1 --skip=40)
HEAD_SHA=$(git -C /workspace log --format=%H -n1)
curl -s "${H[@]}" "$API/repos/$REPO/compare/$BASE...$HEAD_SHA" \
  | python3 -c "
import json,sys
from collections import Counter
d=json.load(sys.stdin)
print('status:', d['status'], '| total_commits:', d['total_commits'], '| files:', len(d['files']))
print('status counts:', Counter(f['status'] for f in d['files']))
print('Diff Entry keys:', [k for k in d['files'][0] if k!='patch'])
"

hr "Commits API: list response OMITS files[] (the N+1 problem)"
curl -s -D /tmp/_ch "${H[@]}" "$API/repos/$REPO/commits?path=packages/github&since=2026-01-01T00:00:00Z&per_page=3" -o /tmp/_cm
grep -i '^link:' /tmp/_ch
python3 -c "import json; d=json.load(open('/tmp/_cm')); print(\"'files' in list entry:\", 'files' in d[0]); print('keys:', list(d[0].keys()))"
SHA=$(python3 -c "import json; print(json.load(open('/tmp/_cm'))[0]['sha'])")
echo "--- but Get-a-commit DOES include files[] (one extra call per commit) ---"
curl -s "${H[@]}" "$API/repos/$REPO/commits/$SHA" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(\"'files' present:\", 'files' in d, '| count:', len(d.get('files',[])))"

hr "Search code API: separate code_search bucket, 10 req/min"
curl -s -D - -o /dev/null "${H[@]}" "$API/search/code?q=repo:$REPO+path:packages/github+cel" \
  | grep -iE '^(HTTP|x-ratelimit-(limit|remaining|resource))'

hr "Private repo without access returns 404, NOT 403"
curl -s -o /dev/null -w "HTTP:%{http_code}\n" "${H[@]}" "$API/repos/elastic/security-advisories"

hr "raw.githubusercontent.com accepts an Authorization header (public repo only here)"
for scheme in Bearer token; do
  printf '%s: ' "$scheme"
  curl -s -o /dev/null -w "HTTP:%{http_code}\n" -H "Authorization: $scheme $TOKEN" \
    "https://raw.githubusercontent.com/$REPO/main/packages/github/manifest.yml"
done
