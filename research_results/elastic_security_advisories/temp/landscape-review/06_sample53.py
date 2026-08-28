#!/usr/bin/env python3
"""Restrict to the 53 files named in sampled_meta.json and re-run the census,
   to test whether the doc's numbers reproduce on ITS OWN declared sample."""
import os, re, json, glob

BASE = os.path.join(os.path.dirname(__file__), "..")
meta = json.load(open(os.path.join(BASE, "sampled_meta.json")))
print("sampled_meta.json entries:", len(meta))
sampled = [os.path.basename(m["file"]) for m in meta]
ondisk = {os.path.basename(f) for f in glob.glob(os.path.join(BASE, "raw", "topic_*.md"))}
print("files on disk:", len(ondisk))
extra = sorted(ondisk - set(sampled))
missing = sorted(set(sampled) - ondisk)
print("on disk but NOT in sampled_meta (%d):" % len(extra), extra)
print("in sampled_meta but NOT on disk:", missing)

bodies = {n: open(os.path.join(BASE, "raw", n), encoding="utf-8").read() for n in sampled if n in ondisk}
print("\ncensus over the %d-file declared sample" % len(bodies))

CORES = {
    "CVE ID": r"CVE ID", "Severity": r"Severity",
    "Affected Versions": r"Affected Versions?",
    "Solutions and Mitigations": r"Solutions? and Mitigations?",
    "Affected Configurations": r"Affected Configurations?",
    "For Users that Cannot Upgrade": r"For Users that [Cc]annot [Uu]pgrade",
    "Problem Type": r"Problem Type", "Impact": r"Impact",
    "Indicators of Compromise": r"Indicators of Compromise",
    "Elastic Cloud Serverless": r"Elastic Cloud Serverless",
    "Acknowledgements": r"Acknowledge?ments?",
}
STATED = {"CVE ID": 47, "Severity": 43, "Affected Versions": 42,
          "Solutions and Mitigations": 42, "Affected Configurations": 18,
          "For Users that Cannot Upgrade": 17, "Problem Type": 13, "Impact": 13,
          "Indicators of Compromise": 4, "Elastic Cloud Serverless": 4,
          "Acknowledgements": 4}

print(f"{'label':30} {'anybold':>8} {'ATX':>5} {'any':>5} {'stated':>7}  verdict")
for lab, core in CORES.items():
    anyb = sum(1 for b in bodies.values() if re.search(r"^\*\*\s*" + core, b, re.M))
    atx = sum(1 for b in bodies.values() if re.search(r"^#{1,6}\s*\**\s*" + core, b, re.M))
    anyx = sum(1 for b in bodies.values() if re.search(r"^\s*(?:#{1,6}\s*)?\**\s*" + core, b, re.M | re.I))
    s = STATED[lab]
    v = "reproduces (bold)" if anyb == s else ("reproduces (any)" if anyx == s else "NO MATCH")
    print(f"{lab:30} {anyb:>8} {atx:>5} {anyx:>5} {s:>7}  {v}")

# ATX split on the 53-sample
print("\nATX-vs-bold on the 53-file sample:")
for lab, core in [("Affected Versions", r"Affected Versions?"),
                  ("Solutions and Mitigations", r"Solutions? and Mitigations?")]:
    atx = sum(1 for b in bodies.values() if re.search(r"^#{1,6}\s*\**\s*" + core, b, re.M))
    bold = sum(1 for b in bodies.values() if re.search(r"^\*\*\s*" + core, b, re.M))
    print(f"  {lab}: ATX={atx} bold={bold} (doc claims ATX 12 / 13)")
