#!/usr/bin/env python3
"""Audit ESA-2026-24.mapped-ecs.json: ECS field existence, value traceability."""
import os, json, re, glob, csv, difflib

HERE = os.path.dirname(__file__)
BASE = os.path.join(HERE, "..", "..")
SE = os.path.join(BASE, "references", "sample-events")

doc = json.load(open(os.path.join(SE, "ESA-2026-24.mapped-ecs.json")))
cve = json.load(open(os.path.join(SE, "ESA-2026-24.cve-record-5.1.json")))
md = open(os.path.join(SE, "ESA-2026-24.md"), encoding="utf-8").read()
md_body = re.sub(r"\A\s*<!--.*?-->\s*", "", md, flags=re.S).strip()

# ---------- 1. flatten the doc's leaf paths ----------
def leaves(o, pre=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, f"{pre}.{k}" if pre else k)
    else:
        yield pre, o

paths = dict(leaves(doc))
CUSTOM_PREFIXES = ("elastic_security_advisories.", "_comment")
ecs_paths = sorted({p for p in paths
                    if not p.startswith(CUSTOM_PREFIXES)})
print("non-custom (=claimed ECS) leaf paths:", len(ecs_paths))

# ---------- 2. check against the ECS schema CSVs in temp/ecs ----------
ecs_dir = os.path.join(HERE, "..", "ecs")
csvs = glob.glob(os.path.join(ecs_dir, "*.csv"))
print("ECS schema CSVs available:", [os.path.basename(c) for c in csvs])
known = {}
for c in csvs:
    names = set()
    with open(c) as fh:
        for row in csv.DictReader(fh):
            n = row.get("Field") or row.get("field") or row.get("Name") or row.get("name")
            if n: names.add(n)
    known[os.path.basename(c)] = names

if known:
    print(f"\n{'path':40} " + " ".join(f"{os.path.basename(k)[:14]:>15}" for k in known))
    for p in ecs_paths:
        base = re.sub(r"\.\d+$", "", p)          # strip array indices
        row = []
        for k in known:
            row.append("yes" if base in known[k] else "NO")
        flag = "   <-- NOT IN ANY ECS VERSION" if all(x == "NO" for x in row) else ""
        print(f"{base:40} " + " ".join(f"{x:>15}" for x in row) + flag)
else:
    print("!! no ECS CSVs found under temp/ecs — cannot verify field existence offline")

# ---------- 3. value traceability ----------
print("\n=== value traceability against the CVE record and the advisory .md ===")
cna = cve["containers"]["cna"]
checks = [
    ("vulnerability.id", doc["vulnerability"]["id"], cve["cveMetadata"]["cveId"]),
    ("cvss vector", doc["elastic_security_advisories"]["advisory"]["cvss"]["vector_string"],
     cna["metrics"][0]["cvssV3_1"]["vectorString"]),
    ("cvss base score", doc["vulnerability"]["score"]["base"],
     cna["metrics"][0]["cvssV3_1"]["baseScore"]),
    ("cvss severity", doc["vulnerability"]["severity"],
     cna["metrics"][0]["cvssV3_1"]["baseSeverity"].title()),
    ("title", doc["elastic_security_advisories"]["advisory"]["title"], cna.get("title")),
    ("cwe id", doc["elastic_security_advisories"]["advisory"]["cwe"]["id"],
     cna["problemTypes"][0]["descriptions"][0].get("cweId")),
    ("capec id", doc["elastic_security_advisories"]["advisory"]["capec"]["id"],
     "CAPEC-" + str(cna["impacts"][0]["capecId"]) if cna.get("impacts") else None),
    ("generator", doc["elastic_security_advisories"]["advisory"]["generator"],
     (cna.get("x_generator") or {}).get("engine")),
    ("discovery", doc["elastic_security_advisories"]["advisory"]["discovery"],
     (cna.get("source") or {}).get("discovery")),
    ("default_status", doc["elastic_security_advisories"]["advisory"]["default_status"],
     cna["affected"][0].get("defaultStatus")),
    ("cve_published_date", doc["elastic_security_advisories"]["advisory"]["cve_published_date"],
     cve["cveMetadata"].get("datePublished")),
    ("reserved_date", doc["elastic_security_advisories"]["advisory"]["reserved_date"],
     cve["cveMetadata"].get("dateReserved")),
    ("updated_date", doc["elastic_security_advisories"]["advisory"]["updated_date"],
     cve["cveMetadata"].get("dateUpdated")),
]
for name, got, exp in checks:
    ok = "OK" if str(got) == str(exp) else "MISMATCH"
    print(f"  {name:22} doc={got!r:66} source={exp!r}  {ok}")

# description byte-identity: CVE vs advisory paragraph
cve_desc = cna["descriptions"][0]["value"]
doc_desc = doc["vulnerability"]["description"]
print("\n  vulnerability.description == cna.descriptions[0].value ?",
      "YES (byte-identical)" if doc_desc == cve_desc else "NO")
# the advisory's own description paragraph
para = md_body.split("\n\n")
adv_desc = next(p for p in para if p.startswith("Incorrect Authorization (CWE-863)")).replace("\n", " ")
adv_desc = re.sub(r"\s+", " ", adv_desc).strip()
cve_norm = re.sub(r"\s+", " ", cve_desc).strip()
print("  advisory paragraph == CVE description (whitespace-normalised) ?",
      "YES" if adv_desc == cve_norm else "NO")
if adv_desc != cve_norm:
    print("   adv:", adv_desc[:200]); print("   cve:", cve_norm[:200])

# body field vs the verbatim advisory
body = doc["elastic_security_advisories"]["advisory"]["body"]
print("\n  advisory.body == verbatim ESA-2026-24.md body ?",
      "YES" if body.strip() == md_body else "NO")
if body.strip() != md_body:
    d = list(difflib.unified_diff(md_body.split("\n"), body.split("\n"),
                                  fromfile="ESA-2026-24.md", tofile="mapped-ecs body", lineterm=""))
    print("  diff (%d lines):" % len(d))
    print("\n".join(d))

# fixed versions traceable to the advisory prose?
fx = doc["elastic_security_advisories"]["advisory"]["fixed_versions"]
sol = re.search(r"The issue is resolved in versions? ([^\n]+)", md_body).group(1)
print("\n  fixed_versions", fx, "| advisory prose:", sol)

# affected versions vs CVE record
print("\n  affected_versions vs CVE cna.affected[0].versions:")
print("   doc:", [(v["version"], v.get("less_than_or_equal")) for v in
                  doc["elastic_security_advisories"]["advisory"]["affected_versions"]])
print("   cve:", [(v["version"], v.get("lessThanOrEqual")) for v in cna["affected"][0]["versions"]])

# file.* / git.* synthetic?
print("\n  file.size =", doc["file"]["size"], "| actual sample body bytes =", len(md_body.encode()))
print("  file.path =", doc["file"]["path"], "| git.path =",
      doc["elastic_security_advisories"]["advisory"]["git"]["path"])
print("  NOTE: filename shown as ESA-2026-24.md, but the human-reported real filename is",
      "ESA-2026-0081.json (zero-padded, JSON).")
