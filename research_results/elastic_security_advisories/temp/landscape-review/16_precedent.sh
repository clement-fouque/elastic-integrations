#!/usr/bin/env bash
# Verify every file path + line range cited in references/integrations-precedent.md.
set -u
cd /workspace
GH=packages/github/data_stream/security_advisories

show() {  # show <file> <start> <end> <what-is-claimed>
  echo "----- $1:$2-$3   [$4]"
  if [ ! -f "$1" ]; then echo "   !! FILE DOES NOT EXIST"; return; fi
  sed -n "$2,$3p" "$1" | sed 's/^/   /'
}

echo "###### §1.2 github/manifest.yml:86-125 / 86-103 cel input + proxy_url + ssl"
show packages/github/manifest.yml 86 103 "cel input decl"
echo "###### §1.2 github/manifest.yml:53-61 agentless"
show packages/github/manifest.yml 53 61 "agentless"
echo "###### package version / owner"
grep -nE '^(name|version|owner|  github):' packages/github/manifest.yml | head
grep -n 'categories' -A3 packages/github/manifest.yml | head -6

echo; echo "###### §2 audit/manifest.yml:59-63 api_url (claimed 'host-only')"
show packages/github/data_stream/audit/manifest.yml 59 63 "api_url"
echo "###### §2 audit/manifest.yml:25-28 enterprise var"
show packages/github/data_stream/audit/manifest.yml 25 28 "enterprise"
echo "###### §2 issues/manifest.yml:75-82"
show packages/github/data_stream/issues/manifest.yml 75 82 "api_url identical block"
echo "###### §2 security_advisories/manifest.yml:9-16 api_url full-URL"
show $GH/manifest.yml 9 16 "api_url"
echo "###### §2 README:53 GHES incompatibility"
show packages/github/_dev/build/docs/README.md 53 53 "GHES note"
grep -n "Enterprise server" packages/github/_dev/build/docs/README.md

echo; echo "###### §3 security_advisories/manifest.yml:17-24 api_key"
show $GH/manifest.yml 17 24 "api_key"
echo "###### §3 cel.yml.hbs:9-21 redact"
show $GH/agent/stream/cel.yml.hbs 9 21 "redact"
echo "###### §3 cel.yml.hbs:36-40 header triple"
show $GH/agent/stream/cel.yml.hbs 36 40 "headers"

echo; echo "###### §4 cel.yml.hbs:22-24 regexp+max_executions"
show $GH/agent/stream/cel.yml.hbs 22 24 "regexp"
echo "###### §4 cel.yml.hbs:26-34 next_url"
show $GH/agent/stream/cel.yml.hbs 26 34 "request"
echo "###### §4 cel.yml.hbs:63-79 cursor"
show $GH/agent/stream/cel.yml.hbs 63 79 "cursor"

echo; echo "###### §5.1 manifest.yml:16 endpoint / :22 auth optional / :25-37 advisory_type / :38-45 interval"
sed -n '16p;22p' $GH/manifest.yml | sed 's/^/   /'
show $GH/manifest.yml 25 37 "advisory_type"
show $GH/manifest.yml 38 45 "interval"
echo "###### §5.1 cel.yml.hbs:28-34 query params"
show $GH/agent/stream/cel.yml.hbs 28 34 "query params"

echo; echo "###### §5.4 ingest pipeline line refs"
P=$GH/elasticsearch/ingest_pipeline/default.yml
for r in "12 25" "62 66" "86 90" "141 145" "187 191" "241 245" "280 287" "8 11"; do
  set -- $r; show $P $1 $2 "pipeline"
done

echo; echo "###### §6 ti_recordedfuture cel.yml.hbs:48-68"
show packages/ti_recordedfuture/data_stream/threat/agent/stream/cel.yml.hbs 48 68 "etag HEAD"

echo; echo "###### §7 abnormal_security refs"
A=packages/abnormal_security/data_stream/threat/agent/stream/cel.yml.hbs
for r in "28 40" "78 83" "137 149" "151 157" "219 223"; do
  set -- $r; show $A $1 $2 "abnormal"
done

echo; echo "###### §8 qualys_vmdr:95-119 / mimecast:147-154"
show packages/qualys_vmdr/data_stream/user_activity/agent/stream/cel.yml.hbs 95 119 "rate_limit"
show packages/mimecast/data_stream/threat_intel_malware_grid/agent/stream/cel.yml.hbs 147 154 "429"

echo; echo "###### §9 tracer"
show $GH/agent/stream/cel.yml.hbs 3 6 "tracer"
show $GH/manifest.yml 80 88 "enable_request_tracer var"

echo; echo "###### §10 error shape"
show $GH/agent/stream/cel.yml.hbs 41 56 "error event"

echo; echo "###### §11 mock config 14-19"
show $GH/_dev/deploy/docker/files/config.yml 14 19 "mock Link header"
ls $GH/_dev/test/system/ $GH/_dev/test/pipeline/ 2>&1

echo; echo "###### §5.4 snyk / ti_flashpoint refs"
S=packages/snyk/data_stream/issues/elasticsearch/ingest_pipeline/default.yml
for n in 73 82 94 106 118; do echo "--- snyk:$n"; sed -n "${n}p" $S | sed 's/^/   /'; done
sed -n '1,40p' packages/ti_flashpoint/data_stream/vulnerability/fields/ecs.yml | grep -nE 'observer|scanner' | sed 's/^/   /'
