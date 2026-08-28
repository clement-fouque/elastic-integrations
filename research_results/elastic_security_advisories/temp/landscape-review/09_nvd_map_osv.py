#!/usr/bin/env python3
"""NVD totals, CVE->ESA mapping count, community esas.json count,
   CVE-year distribution, reference hosts, product counts, ESA-ID padding in slugs."""
import os, json, collections, re, urllib.parse

BASE = os.path.join(os.path.dirname(__file__), "..")

nvd = json.load(open(os.path.join(BASE, "nvd_elastic_all.json")))
print("NVD totalResults:", nvd.get("totalResults"), " resultsPerPage:", nvd.get("resultsPerPage"),
      " vulnerabilities in file:", len(nvd.get("vulnerabilities", [])))
yr = collections.Counter(v["cve"]["id"].split("-")[1] for v in nvd["vulnerabilities"])
print("CVE-year distribution:", dict(sorted(yr.items())))
STATED_YR = {"2015": 1, "2016": 15, "2017": 30, "2018": 25, "2019": 14, "2020": 13,
             "2021": 27, "2022": 15, "2023": 22, "2024": 37, "2025": 31, "2026": 110}
print("stated       :", STATED_YR)
print("match:", {k: (yr.get(k, 0) == v) for k, v in STATED_YR.items()})

m = json.load(open(os.path.join(BASE, "cve_to_esa.json")))
print("\ncve_to_esa.json type:", type(m).__name__, "entries:", len(m))
sample = list(m.items())[:3] if isinstance(m, dict) else m[:3]
print("sample:", sample)

# reference hosts across cve5
import glob
hosts = collections.Counter()
esa_from_slug = set()
for f in glob.glob(os.path.join(BASE, "cve5", "CVE-*.json")):
    r = json.load(open(f))
    for ref in r.get("containers", {}).get("cna", {}).get("references", []) or []:
        u = ref.get("url", "")
        h = urllib.parse.urlparse(u).netloc
        if h: hosts[h] += 1
        mm = re.search(r"esa-(\d{4})-(\d+)", u, re.I)
        if mm: esa_from_slug.add((f, mm.group(0).upper()))
print("\nreference hosts (top 6):", dict(hosts.most_common(6)))
print("cve5 records whose reference slug yields an ESA id:", len({f for f, _ in esa_from_slug}))

# ESA-ID zero padding in Discourse slugs
topics = json.load(open(os.path.join(BASE, "cat31_all_topics.json")))
pads = collections.Counter()
for t in topics:
    for mm in re.finditer(r"esa-(\d{4})-(\d+)", t.get("slug", "") or ""):
        pads[len(mm.group(2))] += 1
print("\nESA sequence digit-length in Discourse SLUGS:", dict(pads))
zero_padded4 = [t["slug"] for t in topics if re.search(r"esa-\d{4}-0\d{3}", t.get("slug", "") or "")]
print("slugs with a 4-digit zero-padded sequence:", len(zero_padded4))

# community esa-search dataset
p = os.path.join(BASE, "esa-search")
for root, dirs, fs in os.walk(p):
    for fn in fs:
        if fn == "esas.json":
            d = json.load(open(os.path.join(root, fn)))
            recs = d if isinstance(d, list) else d.get("esas", d)
            print("\nesa-search esas.json:", os.path.join(root, fn), "records:", len(recs))
            ids = [r.get("esa_id") for r in recs if isinstance(r, dict)]
            print("  distinct esa_id:", len(set(ids)))
            pp = collections.Counter(len(x.split("-")[-1]) for x in ids if x)
            print("  esa_id sequence digit-length:", dict(pp))
            yrs = collections.Counter(x.split("-")[1] for x in ids if x)
            print("  by ESA year:", dict(sorted(yrs.items())))
