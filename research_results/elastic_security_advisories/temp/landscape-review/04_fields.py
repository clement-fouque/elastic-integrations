#!/usr/bin/env python3
"""Recompute the §3.2 / §4.3 heading-frequency table from temp/raw/topic_*.md."""
import os, re, glob, collections, json

BASE = os.path.join(os.path.dirname(__file__), "..")
files = sorted(glob.glob(os.path.join(BASE, "raw", "topic_*.md")))
print("raw body files on disk:", len(files))
print("empty files:", [os.path.basename(f) for f in files if os.path.getsize(f) == 0])
sizes = {os.path.basename(f): os.path.getsize(f) for f in files}
print("total bytes:", sum(sizes.values()), "min", min(sizes.values()), "max", max(sizes.values()))
big = sorted(sizes.items(), key=lambda kv: -kv[1])[:3]
print("largest:", big)

bodies = {os.path.basename(f): open(f, encoding="utf-8").read() for f in files}

# Which raw topics are ESA-tagged?  cross-ref topic list
topics = {t["id"]: t for t in json.load(open(os.path.join(BASE, "cat31_all_topics.json")))}
ESA_RE = re.compile(r"ESA-(\d{4})-(\d+)")
tagged, untagged = [], []
for name in bodies:
    tid = int(name[len("topic_"):-3])
    t = topics.get(tid)
    (tagged if t and ESA_RE.search(t["title"]) else untagged).append(name)
print("raw files whose topic title is ESA-tagged:", len(tagged), " untagged:", len(untagged))
for n in untagged:
    tid = int(n[len("topic_"):-3])
    print("   untagged:", n, topics.get(tid, {}).get("title", "<not in list>"))

def count(pattern, corpus, flags=re.M):
    rx = re.compile(pattern, flags)
    return sum(1 for b in corpus.values() if rx.search(b))

# Label matchers: match the label in ANY heading style (bold, ATX, plain), colon optional.
LABELS = {
    "CVE ID":                        r"^\s*(?:#{1,6}\s*)?\**\s*CVE ID\s*\**\s*:?\s*\**",
    "Severity":                      r"^\s*(?:#{1,6}\s*)?\**\s*Severity\s*\**\s*:?\s*\**",
    "Affected Versions":             r"^\s*(?:#{1,6}\s*)?\**\s*Affected Versions?\s*\**\s*:?\s*\**",
    "Solutions and Mitigations":     r"^\s*(?:#{1,6}\s*)?\**\s*Solutions? and Mitigations?\s*\**\s*:?\s*\**",
    "Affected Configurations":       r"^\s*(?:#{1,6}\s*)?\**\s*Affected Configurations?\s*\**\s*:?\s*\**",
    "For Users that Cannot Upgrade": r"(?i)^\s*(?:#{1,6}\s*)?\**\s*For Users that Cannot Upgrade\s*\**\s*:?\s*\**",
    "Problem Type":                  r"^\s*(?:#{1,6}\s*)?\**\s*Problem Type\s*\**\s*:?\s*\**",
    "Impact":                        r"^\s*(?:#{1,6}\s*)?\**\s*Impact\s*\**\s*:?\s*\**",
    "Indicators of Compromise (IOC)":r"(?i)^\s*(?:#{1,6}\s*)?\**\s*Indicators of Compromise",
    "Elastic Cloud Serverless":      r"(?i)^\s*(?:#{1,6}\s*)?\**\s*Elastic Cloud Serverless",
    "Acknowledgements":              r"(?i)^\s*(?:#{1,6}\s*)?\**\s*Acknowledge?ments?\s*\**\s*:?\s*\**",
    "Update Log/Change log/Updates": r"(?i)^\s*(?:#{1,6}\s*)?\**\s*(Update Log|Change ?log|Updates)\s*\**\s*:?\s*\**\s*$",
    "Description":                   r"^\s*(?:#{1,6}\s*)?\**\s*Description\s*\**\s*:?\s*\**",
}

STATED = {  # value asserted in esa-publication-landscape.md §3.2 / brief §4.3
    "CVE ID": 47, "Severity": 43, "Affected Versions": 42, "Solutions and Mitigations": 42,
    "Affected Configurations": 18, "For Users that Cannot Upgrade": 17, "Problem Type": 13,
    "Impact": 13, "Indicators of Compromise (IOC)": 4, "Elastic Cloud Serverless": 4,
    "Acknowledgements": 4, "Update Log/Change log/Updates": 6,
}

for corpus_name, corpus in [("ALL 57 raw files", bodies),
                            ("ESA-tagged only (%d)" % len(tagged), {k: bodies[k] for k in tagged})]:
    print(f"\n=== {corpus_name} ===")
    print(f"{'label':32} {'files w/ match':>14} {'stated':>7}")
    for lab, pat in LABELS.items():
        n = count(pat, corpus)
        s = STATED.get(lab, "")
        flag = "" if s == "" or s == n else "   <-- MISMATCH"
        print(f"{lab:32} {n:>14} {str(s):>7}{flag}")

# Bold vs ATX split for the two labels the docs quantify
print("\n=== heading STYLE split (all 57 files) ===")
for lab, core in [("Affected Versions", r"Affected Versions?"),
                  ("Solutions and Mitigations", r"Solutions? and Mitigations?")]:
    atx = bold = other = 0
    atx_f, bold_f = [], []
    for name, b in bodies.items():
        has_atx = re.search(r"^#{1,6}\s*\**\s*" + core, b, re.M)
        has_bold = re.search(r"^\*\*\s*" + core, b, re.M)
        if has_atx: atx += 1; atx_f.append(name)
        if has_bold: bold += 1; bold_f.append(name)
    print(f"{lab}: files with an ATX-heading form = {atx}; files with a bold form = {bold}")
