#!/usr/bin/env python3
"""Where does the '418 discuss.elastic.co' reference-host table come from?
   And: the union of every publicly-known ESA ID across all harvested sources."""
import os, json, glob, collections, re, urllib.parse

BASE = os.path.join(os.path.dirname(__file__), "..")

# --- reference hosts, three different populations ---
cna = collections.Counter(); allcont = collections.Counter()
for f in glob.glob(os.path.join(BASE, "cve5", "CVE-*.json")):
    r = json.load(open(f)); c = r.get("containers", {})
    for ref in c.get("cna", {}).get("references", []) or []:
        h = urllib.parse.urlparse(ref.get("url", "")).netloc
        if h: cna[h] += 1; allcont[h] += 1
    for adp in c.get("adp", []) or []:
        for ref in adp.get("references", []) or []:
            h = urllib.parse.urlparse(ref.get("url", "")).netloc
            if h: allcont[h] += 1

nvd = json.load(open(os.path.join(BASE, "nvd_elastic_all.json")))
nvdh = collections.Counter()
for v in nvd["vulnerabilities"]:
    for ref in v["cve"].get("references", []) or []:
        h = urllib.parse.urlparse(ref.get("url", "")).netloc
        if h: nvdh[h] += 1

STATED = {"discuss.elastic.co": 418, "www.elastic.co": 194, "security.netapp.com": 51,
          "access.redhat.com": 17, "www.oracle.com": 12}
print(f"{'host':24} {'stated':>7} {'cve5 CNA':>9} {'cve5 all':>9} {'NVD':>6}")
for h, s in STATED.items():
    print(f"{h:24} {s:>7} {cna.get(h,0):>9} {allcont.get(h,0):>9} {nvdh.get(h,0):>6}")
print("\nNVD top hosts:", dict(nvdh.most_common(8)))

# --- union of all publicly-known ESA IDs ---
esa = collections.defaultdict(set)   # source -> {(year,seq)}
R = re.compile(r"ESA[-\s]?(\d{4})[-\s]?(\d{1,4})", re.I)

topics = json.load(open(os.path.join(BASE, "cat31_all_topics.json")))
for t in topics:
    for y, s in R.findall(t.get("title", "") or ""):
        esa["discourse_title"].add((int(y), int(s)))
    for y, s in R.findall(t.get("slug", "") or ""):
        esa["discourse_slug"].add((int(y), int(s)))
    for y, s in R.findall(t.get("excerpt", "") or ""):
        esa["discourse_excerpt"].add((int(y), int(s)))

for f in glob.glob(os.path.join(BASE, "raw", "topic_*.md")):
    for y, s in R.findall(open(f, encoding="utf-8").read()):
        esa["raw_body"].add((int(y), int(s)))

for f in glob.glob(os.path.join(BASE, "cve5", "CVE-*.json")):
    txt = open(f, encoding="utf-8").read()
    for y, s in R.findall(txt):
        esa["cve5"].add((int(y), int(s)))

d = json.load(open(os.path.join(BASE, "esa-search", "esas.json")))
recs = d if isinstance(d, list) else d.get("esas", d)
for r in recs:
    for y, s in R.findall(json.dumps(r)):
        esa["esa_search"].add((int(y), int(s)))

txt = open(os.path.join(BASE, "nvd_elastic_all.json"), encoding="utf-8").read()
for y, s in R.findall(txt):
    esa["nvd"].add((int(y), int(s)))

for k in sorted(esa):
    print(f"\n{k}: {len(esa[k])} distinct ESA IDs; years " +
          str(dict(sorted(collections.Counter(y for y, s in esa[k]).items()))))

union = set().union(*esa.values())
print("\nUNION of all sources:", len(union), "distinct ESA IDs")
print("union by year:", dict(sorted(collections.Counter(y for y, s in union).items())))
print("union min/max seq per year:")
by = collections.defaultdict(list)
for y, s in union: by[y].append(s)
for y in sorted(by):
    ss = sorted(by[y])
    print(f"  {y}: n={len(ss)} min={min(ss)} max={max(ss)} "
          f"missing_from_1_to_max={len([n for n in range(1, max(ss)+1) if n not in ss])}")
tot_reserved = sum(max(by[y]) for y in by)
print("\nsum of per-year MAX sequence (= upper bound on IDs ever minted, "
      "assuming dense allocation from 1):", tot_reserved)
