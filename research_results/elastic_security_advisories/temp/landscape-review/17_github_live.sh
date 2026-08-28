#!/usr/bin/env bash
# Live re-verification of the deployment-and-setup.md claims.
set -u
TOKEN="$(gh auth token 2>/dev/null || true)"
H=(-H "Accept: application/vnd.github+json" -H "X-GitHub-Api-Version: 2022-11-28")
[ -n "$TOKEN" ] && H+=(-H "Authorization: Bearer $TOKEN")

echo "############ 1. SAML SSO probe: /orgs/<org>/sso ############"
for org in elastic google jquery expressjs octokit microsoft nodejs; do
  code=$(curl -sS -o /tmp/sso_$org.html -w '%{http_code}' -L "https://github.com/orgs/$org/sso")
  title=$(grep -oiE '<title>[^<]*</title>' /tmp/sso_$org.html | head -1)
  echo "  $org -> HTTP $code  $title"
done

echo
echo "############ 2. 404 diagnostic ladder: are the four bodies byte-identical? ############"
probe() {  # probe <label> <url>
  body=$(curl -sS "${H[@]}" -o /tmp/p.json -w '%{http_code}' "$2")
  printf '  %-46s HTTP %s  %s\n' "$1" "$body" "$(tr -d '\n' < /tmp/p.json | head -c 200)"
}
probe "valid repo (control)"            "https://api.github.com/repos/elastic/integrations"
probe "nonexistent repo"                "https://api.github.com/repos/elastic/this-repo-does-not-exist-zzz9"
probe "private repo we cannot see"      "https://api.github.com/repos/elastic/security-advisories"
probe "valid repo, bogus BRANCH (tree)" "https://api.github.com/repos/elastic/integrations/git/trees/no-such-branch-zzz9"
probe "valid repo, bogus PATH (tree)"   "https://api.github.com/repos/elastic/integrations/git/trees/main:no-such-dir-zzz9"
probe "valid repo, good tree (control)" "https://api.github.com/repos/elastic/integrations/git/trees/main:packages/github?recursive=1"
probe "bogus blob sha"                  "https://api.github.com/repos/elastic/integrations/git/blobs/0000000000000000000000000000000000000000"

echo
echo "############ 3. X-Accepted-GitHub-Permissions headers ############"
for u in "https://api.github.com/repos/elastic/integrations" \
         "https://api.github.com/repos/elastic/integrations/git/trees/main:packages/github/data_stream/security_advisories?recursive=1"; do
  echo "  $u"
  curl -sS -D- -o /dev/null "${H[@]}" "$u" \
    | grep -iE '^(HTTP/|x-accepted-github-permissions|etag|x-ratelimit-limit)' | sed 's/^/     /'
done

echo
echo "############ 4. repository security advisories endpoint (precedent §5.2) ############"
curl -sS -o /dev/null -w '  /repos/elastic/integrations/security-advisories -> %{http_code}\n' \
  "${H[@]}" "https://api.github.com/repos/elastic/integrations/security-advisories"

echo
echo "############ 5. /advisories is the GLOBAL advisory DB, not repo files ############"
curl -sS "${H[@]}" "https://api.github.com/advisories?per_page=2" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('  records:',len(d)); print('  keys:',sorted(d[0].keys())[:14]); print('  ghsa:',d[0]['ghsa_id'],'| type:',d[0].get('type'))"

echo
echo "############ 6. /meta 'api' CIDR count ############"
curl -sS "https://api.github.com/meta" | python3 -c "import json,sys; d=json.load(sys.stdin); print('  api key CIDR blocks:',len(d['api']))"

echo
echo "############ 7. rate limit shape ############"
curl -sS -D- -o /dev/null "${H[@]}" https://api.github.com/rate_limit | grep -iE '^(HTTP/|x-ratelimit-limit)' | sed 's/^/  /'
