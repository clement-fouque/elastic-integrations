#!/usr/bin/env python3
"""Well-formedness + provenance-header audit for every file in references/sample-events/."""
import os, json, re, glob
import xml.etree.ElementTree as ET

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
SAMPLES = os.path.join(BASE, "references", "sample-events")

files = sorted(glob.glob(os.path.join(SAMPLES, "*")))
print(f"{'file':44} {'bytes':>7} {'wellformed':>11} {'provenance':>11}")
md = 0
for p in files:
    n = os.path.basename(p)
    b = os.path.getsize(p)
    txt = open(p, encoding="utf-8").read()
    wf = "n/a"
    if n.endswith(".json"):
        # strip a leading // or /* provenance comment if present, then parse
        stripped = re.sub(r"\A(\s*(//[^\n]*\n|/\*.*?\*/\s*))+", "", txt, flags=re.S)
        try:
            json.loads(stripped); wf = "JSON ok"
        except Exception as e:
            try:
                json.loads(txt); wf = "JSON ok"
            except Exception as e2:
                wf = "JSON BAD"
                print("   parse error:", n, e2)
    elif n.endswith(".xml"):
        try:
            ET.fromstring(txt); wf = "XML ok"
        except Exception as e:
            wf = "XML BAD"; print("   parse error:", n, e)
    elif n.endswith(".md"):
        md += 1
        wf = "markdown"
    has_prov = bool(re.match(r"\s*(<!--|//|/\*)", txt)) and bool(
        re.search(r"(?i)source|retrieved|https?://", txt[:1200]))
    print(f"{n:44} {b:>7} {wf:>11} {'yes' if has_prov else 'NO':>11}")
print("\n.md advisory files:", md)
print("total files:", len(files))
print("empty files:", [os.path.basename(p) for p in files if os.path.getsize(p) == 0])
