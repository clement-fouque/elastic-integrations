#!/usr/bin/env bash
# Verification script for the configuration/deployment research track.
# Reproduces every [VERIFIED-LIVE] claim in
#   references/deployment-and-setup.md  and  configuration-plan.md
#
# Requires: curl, python3, and a GitHub token in $GH_TOKEN (or `gh auth token`).
# Run from anywhere; writes nothing outside /tmp.

set -uo pipefail
TOK="${GH_TOKEN:-$(gh auth token 2>/dev/null)}"
H_ACCEPT="Accept: application/vnd.github+json"
H_VER="X-GitHub-Api-Version: 2022-11-28"
H_AUTH="Authorization: Bearer ${TOK}"

hr() { printf '\n=== %s ===\n' "$1"; }

hr "1. Private repo the token cannot see -> 404 (NOT 403), with x-accepted-github-permissions"
curl -sS -D- -o /tmp/v1.json -H "$H_ACCEPT" -H "$H_VER" -H "$H_AUTH" \
  https://api.github.com/repos/elastic/security-advisories \
  | grep -Ei '^HTTP|^x-accepted-github-permissions|^x-ratelimit-(remaining|used)'
cat /tmp/v1.json

hr "2. Repo that genuinely does not exist -> byte-identical 404 body (the core diagnosis problem)"
curl -sS -w '\nHTTP %{http_code}\n' -H "$H_AUTH" \
  https://api.github.com/repos/elastic/this-repo-does-not-exist-zzz9

hr "3. Unauthenticated request against the same private repo -> also 404"
curl -sS -w '\nHTTP %{http_code}\n' https://api.github.com/repos/elastic/security-advisories

hr "4. Git Trees API on a sub-tree -> 200, ETag, x-accepted-github-permissions: contents=read"
curl -sS -D- -o /tmp/v4.json -H "$H_ACCEPT" -H "$H_VER" -H "$H_AUTH" \
  "https://api.github.com/repos/elastic/integrations/git/trees/main:packages%2Fgithub%2Fdata_stream%2Fsecurity_advisories?recursive=1" \
  | grep -Ei '^HTTP|^etag|^x-accepted-github-permissions|^x-ratelimit-(limit|remaining|used|resource)'
python3 -c "import json;d=json.load(open('/tmp/v4.json'));print('entries:',len(d['tree']),'truncated:',d['truncated'])"

hr "5. Git Blobs API -> 200, x-accepted-github-permissions: contents=read"
SHA=$(python3 -c "import json;d=json.load(open('/tmp/v4.json'));print([t['sha'] for t in d['tree'] if t['type']=='blob'][0])")
curl -sS -D- -o /dev/null -H "$H_AUTH" \
  "https://api.github.com/repos/elastic/integrations/git/blobs/${SHA}" \
  | grep -Ei '^HTTP|^etag|^x-accepted-github-permissions'

hr "6. GET /repos on an ACCESSIBLE repo -> the operator's positive-control probe"
curl -sS -H "$H_AUTH" https://api.github.com/repos/elastic/integrations \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print({k:d[k] for k in ['full_name','private','default_branch','visibility']})"

hr "7. Tree request: repo reachable, PATH wrong -> 404 (indistinguishable from a token problem)"
curl -sS -w '\nHTTP %{http_code}\n' -H "$H_AUTH" \
  "https://api.github.com/repos/elastic/integrations/git/trees/main:no%2Fsuch%2Fdir?recursive=1"

hr "8. Tree request: repo reachable, REF wrong -> 404"
curl -sS -w '\nHTTP %{http_code}\n' -H "$H_AUTH" \
  "https://api.github.com/repos/elastic/integrations/git/trees/nosuchbranch:packages?recursive=1"

hr "9. GET /meta -> the 'api' key is the CIDR set an allow-list needs"
curl -sS -o /tmp/meta.json https://api.github.com/meta
python3 -c "
import json;d=json.load(open('/tmp/meta.json'))
for k in ('api','git','web','hooks'):
    print(f'{k}: {len(d[k])} CIDRs')
print('api CIDRs:'); [print(' ',x) for x in d['api']]
"

hr "10. Supported X-GitHub-Api-Version values"
curl -sS https://api.github.com/versions

hr "11. SAML SSO: is it configured on the elastic org? (200 + SSO prompt = yes, 404 = no)"
for o in elastic google jquery expressjs octokit nodejs; do
  code=$(curl -sS -o /tmp/sso.html -w '%{http_code}' -A 'Mozilla/5.0' "https://github.com/orgs/$o/sso")
  py=$(python3 -c "
import re,html
s=open('/tmp/sso.html',encoding='utf-8',errors='replace').read()
m=re.search(r'<title>(.*?)</title>',s,re.S)
print((html.unescape(m.group(1)).strip() if m else '(no title)'), '| sso_prompt=', 'single sign-on provider' in s)
")
  echo "  $o -> HTTP $code  $py"
done

hr "12. Fallback data sources: conditional-request support"
echo '-- discuss.elastic.co category JSON (expect NO etag, cache-control: no-store) --'
curl -sS -D- -o /dev/null -A 'Mozilla/5.0' \
  "https://discuss.elastic.co/c/announcements/security-announcements/31.json" \
  | grep -Ei '^HTTP|^etag|^last-modified|^cache-control'
echo '-- discuss.elastic.co category RSS --'
curl -sS -D- -o /dev/null -A 'Mozilla/5.0' \
  "https://discuss.elastic.co/c/announcements/security-announcements/31.rss" \
  | grep -Ei '^HTTP|^etag|^last-modified|^cache-control'
echo '-- cveawg.mitre.org (expect a weak etag) --'
curl -sS -D- -o /dev/null "https://cveawg.mitre.org/api/cve/CVE-2026-33461" \
  | grep -Ei '^HTTP|^etag|^last-modified'
echo '-- api.osv.dev --'
curl -sS -D- -o /dev/null "https://api.osv.dev/v1/vulns/CVE-2026-33461" \
  | grep -Ei '^HTTP|^etag'
