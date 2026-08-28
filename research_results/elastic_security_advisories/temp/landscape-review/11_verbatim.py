#!/usr/bin/env python3
"""Verbatim check: strip the HTML provenance header from each sample .md, strip the
   Discourse '<user> | <ts> | #N' post banner from the live /raw/ body, and diff."""
import os, re, sys, subprocess, difflib, json

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
SAMPLES = os.path.join(BASE, "references", "sample-events")
RAWDIR = os.path.join(os.path.dirname(__file__), "live")
os.makedirs(RAWDIR, exist_ok=True)

MAP = {  # sample file -> discourse topic id
    "ESA-2026-24.md": 385812, "ESA-2026-128.md": 389539, "ESA-2026-02.md": 384520,
    "ESA-2024-01.md": 352686, "ESA-2025-14.md": 381427, "ESA-2026-01.md": 384519,
    "ESA-2026-41.md": 387438, "ESA-2023-16.md": 343385, "ESA-2021-31.md": 291476,
}

BANNER = re.compile(r"^[^\n|]{1,60}\|\s*\d{4}-\d\d-\d\d[ T][^\n|]*\|\s*#\d+\s*$", re.M)

def strip_header(text):
    """Remove the leading <!-- ... --> provenance block."""
    m = re.match(r"\s*<!--.*?-->\s*", text, re.S)
    return text[m.end():] if m else text

def strip_banner(text):
    """Remove Discourse's per-post 'username | timestamp | #N' banner lines."""
    return BANNER.sub("", text)

SEP = re.compile(r"\n-{5,}\s*$")   # Discourse /raw/ appends a '-----' post separator

def norm(t):
    t = t.replace("\r\n", "\n")
    t = "\n".join(l.rstrip() for l in t.split("\n")).strip("\n")
    return SEP.sub("", t).strip("\n")

results = []
for fn, tid in sorted(MAP.items()):
    p = os.path.join(SAMPLES, fn)
    if not os.path.exists(p):
        results.append((fn, tid, "MISSING SAMPLE", 0, 0)); continue
    lp = os.path.join(RAWDIR, f"raw_{tid}.md")
    if not os.path.exists(lp):
        rc = subprocess.run(["curl", "-sS", "-m", "60", "-o", lp,
                             f"https://discuss.elastic.co/raw/{tid}"]).returncode
        if rc != 0:
            results.append((fn, tid, "FETCH FAILED", 0, 0)); continue
    live = norm(strip_banner(open(lp, encoding="utf-8").read()))
    samp = norm(strip_header(open(p, encoding="utf-8").read()))
    if samp == live:
        verdict = "IDENTICAL"
    else:
        sm = difflib.SequenceMatcher(None, samp, live)
        verdict = f"DIFFERS (similarity {sm.ratio():.4f})"
        dp = os.path.join(os.path.dirname(__file__), f"diff_{fn}.txt")
        with open(dp, "w") as fh:
            fh.write("\n".join(difflib.unified_diff(
                samp.split("\n"), live.split("\n"),
                fromfile=f"sample/{fn}", tofile=f"live/raw/{tid}", lineterm="")))
    results.append((fn, tid, verdict, len(samp), len(live)))

print(f"{'sample':22} {'topic':>7} {'sample B':>9} {'live B':>8}  verdict")
for fn, tid, v, a, b in results:
    print(f"{fn:22} {tid:>7} {a:>9} {b:>8}  {v}")
