#!/usr/bin/env python3
"""Test the 'byte-identical in every case checked' claim about
   containers.cna.descriptions[].value vs the ESA description paragraph,
   at scale across every raw advisory body we hold."""
import os, re, json, glob, collections

BASE = os.path.join(os.path.dirname(__file__), "..")

# map topic id -> ESA id via the harvested topic list
topics = {t["id"]: t for t in json.load(open(os.path.join(BASE, "cat31_all_topics.json")))}
ESA = re.compile(r"ESA-(\d{4})-(\d+)")

# CVE -> ESA map produced by the previous research
cve2esa = json.load(open(os.path.join(BASE, "cve_to_esa.json")))
esa2cve = {}
for cve, v in cve2esa.items():
    esa = v[0] if isinstance(v, list) else v
    esa2cve.setdefault(esa, []).append(cve)

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def strip_md(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)   # links
    s = s.replace("\\-", "-").replace("\\_", "_").replace("\\*", "*")
    s = re.sub(r"[*`]", "", s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    return norm(s)

rows = []
for f in sorted(glob.glob(os.path.join(BASE, "raw", "topic_*.md"))):
    tid = int(os.path.basename(f)[6:-3])
    t = topics.get(tid)
    if not t: continue
    m = ESA.search(t["title"])
    if not m: continue
    esa_id = m.group(0)
    cves = esa2cve.get(esa_id, [])
    if not cves: rows.append((esa_id, None, "no CVE->ESA mapping", "", "")); continue
    cve = cves[0]
    p = os.path.join(BASE, "cve5", cve + ".json")
    if not os.path.exists(p): rows.append((esa_id, cve, "CVE record not held", "", "")); continue
    rec = json.load(open(p))
    descs = rec.get("containers", {}).get("cna", {}).get("descriptions") or []
    if not descs: rows.append((esa_id, cve, "record has no descriptions", "", "")); continue
    cve_desc = descs[0]["value"]

    body = open(f, encoding="utf-8").read()
    body = re.sub(r"^[^\n|]{1,60}\|[^\n|]*\|\s*#\d+\s*\n", "", body)   # banner
    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    # first paragraph that is not a heading/title and is prose-length
    cand = None
    for p_ in paras:
        s = p_.strip()
        if s.startswith("#") or (s.startswith("**") and s.endswith("**")) or len(s) < 60:
            continue
        cand = s; break
    if cand is None: rows.append((esa_id, cve, "no description paragraph found", "", "")); continue

    exact = "EXACT" if cand.strip() == cve_desc.strip() else ""
    ws = "ws-equal" if norm(cand) == norm(cve_desc) else ""
    md = "md-stripped-equal" if strip_md(cand) == strip_md(cve_desc) else ""
    pre = "cve-is-prefix" if strip_md(cve_desc) and strip_md(cand).startswith(strip_md(cve_desc)[:120]) else ""
    verdict = exact or ws or md or pre or "DIFFERENT"
    rows.append((esa_id, cve, verdict, cand[:80], cve_desc[:80]))

c = collections.Counter(r[2] for r in rows)
print("pairs examined:", len(rows))
for k, v in c.most_common():
    print(f"  {k:28} {v}")

comparable = [r for r in rows if r[2] in ("EXACT", "ws-equal", "md-stripped-equal", "cve-is-prefix", "DIFFERENT")]
ident = [r for r in comparable if r[2] == "EXACT"]
print(f"\ncomparable pairs: {len(comparable)}; byte-identical: {len(ident)} "
      f"({100*len(ident)/max(1,len(comparable)):.0f}%)")
print("\nnon-EXACT comparable cases:")
for r in comparable:
    if r[2] != "EXACT":
        print(f"  {r[0]:14} {r[1]:16} {r[2]}")
        print(f"     esa: {r[3]}")
        print(f"     cve: {r[4]}")
