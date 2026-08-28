#!/usr/bin/env bash
# Check every URL cited in research-brief.md §3.5 and §9 plus the three reference docs.
set -u
cd "$(dirname "$0")/../.."

URLS=$(grep -ohE 'https?://[^ )>"`,]+' \
        research-brief.md \
        references/esa-publication-landscape.md \
        references/integrations-precedent.md \
        references/deployment-and-setup.md \
      | sed 's/[.,;:]*$//' | sed 's/\\$//' | sort -u)

printf '%-6s %-6s %s\n' CODE FINAL URL
for u in $URLS; do
  read -r code final < <(curl -sSL -o /tmp/lk.out -m 45 \
      -w '%{http_code} %{url_effective}\n' \
      -H 'User-Agent: Mozilla/5.0 (link-check)' "$u" 2>/dev/null || echo "ERR -")
  redir=""
  [ "$final" != "$u" ] && redir="  ->  $final"
  printf '%-6s %s%s\n' "${code:-ERR}" "$u" "$redir"
done
