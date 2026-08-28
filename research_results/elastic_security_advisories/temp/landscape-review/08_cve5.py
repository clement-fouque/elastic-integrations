#!/usr/bin/env python3
"""Recompute every CVE-Record-5.x claim from temp/cve5/."""
import os, json, glob, collections

BASE = os.path.join(os.path.dirname(__file__), "..")
files = sorted(glob.glob(os.path.join(BASE, "cve5", "CVE-*.json")))
print("files in temp/cve5:", len(files))

recs, bad = [], []
for f in files:
    try:
        recs.append((os.path.basename(f), json.load(open(f))))
    except Exception as e:
        bad.append((os.path.basename(f), str(e)))
print("unparseable:", bad)
print("parsed records:", len(recs))

state = collections.Counter(r.get("cveMetadata", {}).get("state") for _, r in recs)
print("cveMetadata.state:", dict(state))

keys = collections.Counter()
for _, r in recs:
    for k in r.get("containers", {}).get("cna", {}):
        keys[k] += 1
STATED = {"providerMetadata": 340, "affected": 313, "descriptions": 313, "references": 313,
          "problemTypes": 311, "source": 204, "x_generator": 204, "metrics": 203,
          "title": 193, "impacts": 129, "x_legacyV4Record": 99, "datePublic": 92,
          "rejectedReasons": 27, "credits": 5}
print("\nCNA container key counts (stated -> actual):")
for k, s in STATED.items():
    a = keys.get(k, 0)
    print(f"  {k:20} stated={s:>4} actual={a:>4} {'OK' if a == s else '<-- MISMATCH'}")
extra = {k: v for k, v in keys.items() if k not in STATED}
print("  other keys present:", dict(sorted(extra.items(), key=lambda kv: -kv[1])))

# x_generator engines
eng = collections.Counter()
for _, r in recs:
    xg = r.get("containers", {}).get("cna", {}).get("x_generator")
    if xg is not None:
        eng[json.dumps(xg, sort_keys=True)] += 1
print("\nx_generator values (%d records carry the key):" % sum(eng.values()))
for v, c in eng.most_common():
    print(f"  {c:>4}  {v}")
elastic = sum(c for v, c in eng.items() if "Elastic CVE Publisher" in v)
print(f"  --> 'Elastic CVE Publisher' total: {elastic}")

# also check ADP container x_generator, in case the 204 came from there
adp_eng = collections.Counter()
for _, r in recs:
    for adp in r.get("containers", {}).get("adp", []) or []:
        if "x_generator" in adp:
            adp_eng[json.dumps(adp["x_generator"], sort_keys=True)] += 1
print("\nADP-container x_generator values:", dict(adp_eng))

# metrics
met = collections.Counter()
nmet = 0
for _, r in recs:
    ms = r.get("containers", {}).get("cna", {}).get("metrics")
    if ms:
        nmet += 1
        for m in ms:
            for k in m:
                if k != "other":
                    met[k] += 1
                else:
                    met["other:" + m["other"].get("type", "?")] += 1
print("\nrecords with cna.metrics:", nmet, " metric-type counts:", dict(met))

# version object shapes
shapes = collections.Counter(); vt = collections.Counter(); nver = 0
for _, r in recs:
    for a in r.get("containers", {}).get("cna", {}).get("affected", []) or []:
        for v in a.get("versions", []) or []:
            nver += 1
            shapes[tuple(sorted(v.keys()))] += 1
            vt[v.get("versionType", "<absent>")] += 1
print("\nversion objects:", nver)
for s, c in shapes.most_common(8):
    print("  ", c, list(s))
print("versionType:", dict(vt.most_common()))

# vendor
vend = collections.Counter()
naff = 0
for _, r in recs:
    aff = r.get("containers", {}).get("cna", {}).get("affected")
    if aff:
        naff += 1
        for a in aff:
            vend[a.get("vendor")] += 1
print("\nrecords with affected:", naff, "vendor counts:", dict(vend.most_common(6)))

# credits
cred = sum(1 for _, r in recs if r.get("containers", {}).get("cna", {}).get("credits"))
print("records with cna.credits:", cred)
