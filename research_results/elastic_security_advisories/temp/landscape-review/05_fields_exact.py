#!/usr/bin/env python3
"""Exact per-variant heading census, so the doc's 'bold-label' numbers can be
   reproduced or falsified precisely."""
import os, re, glob, collections

BASE = os.path.join(os.path.dirname(__file__), "..")
files = sorted(glob.glob(os.path.join(BASE, "raw", "topic_*.md")))
bodies = {os.path.basename(f): open(f, encoding="utf-8").read() for f in files}
N = len(bodies)

CORES = {
    "CVE ID": r"CVE ID",
    "Severity": r"Severity",
    "Affected Versions": r"Affected Versions?",
    "Solutions and Mitigations": r"Solutions? and Mitigations?",
    "Affected Configurations": r"Affected Configurations?",
    "For Users that Cannot Upgrade": r"For Users that [Cc]annot [Uu]pgrade",
    "Problem Type": r"Problem Type",
    "Impact": r"Impact",
    "Indicators of Compromise": r"Indicators of Compromise",
    "Elastic Cloud Serverless": r"Elastic Cloud Serverless",
    "Acknowledgements": r"Acknowledge?ments?",
}

print(f"corpus = {N} files\n")
hdr = f"{'label':30} {'bold**L:**':>11} {'bold**L**:':>11} {'anybold':>8} {'ATX':>5} {'any':>5}"
print(hdr)
for lab, core in CORES.items():
    b1 = b2 = anyb = atx = anyx = 0
    for name, body in bodies.items():
        if re.search(r"^\*\*" + core + r":\*\*", body, re.M): b1 += 1
        if re.search(r"^\*\*" + core + r"\*\*\s*:", body, re.M): b2 += 1
        if re.search(r"^\*\*\s*" + core, body, re.M): anyb += 1
        if re.search(r"^#{1,6}\s*\**\s*" + core, body, re.M): atx += 1
        if re.search(r"^\s*(?:#{1,6}\s*)?\**\s*" + core, body, re.M | re.I): anyx += 1
    print(f"{lab:30} {b1:>11} {b2:>11} {anyb:>8} {atx:>5} {anyx:>5}")

print("\n-- Acknowledgements: which files, and in what form --")
for name, body in bodies.items():
    for m in re.finditer(r"(?i)^.{0,10}Acknowledge?ments?.{0,20}$", body, re.M):
        print(f"  {name}: {m.group(0)!r}")

print("\n-- Update Log / Change log / Updates --")
for name, body in bodies.items():
    for m in re.finditer(r"(?i)^\s*(?:#{1,6}\s*)?\**\s*(Update Log|Change ?log|Updates)\s*\**\s*:?\s*\**\s*$", body, re.M):
        print(f"  {name}: {m.group(0).strip()!r}")

print("\n-- IOC & Serverless: which files --")
for lab, core in [("IOC", r"Indicators of Compromise"), ("Serverless", r"Elastic Cloud Serverless")]:
    hits = [n for n, b in bodies.items() if re.search(r"(?i)^\s*(?:#{1,6}\s*)?\**\s*" + core, b, re.M)]
    print(f"  {lab}: {len(hits)} -> {sorted(hits)}")
