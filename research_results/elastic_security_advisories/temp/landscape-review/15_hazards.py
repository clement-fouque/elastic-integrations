#!/usr/bin/env python3
"""Verify each brief §4.6 / landscape §3.2 formatting-hazard claim against the samples."""
import os, re, glob

HERE = os.path.dirname(__file__)
SE = os.path.join(HERE, "..", "..", "references", "sample-events")
RAW = os.path.join(HERE, "..", "raw")

def body(p):
    return re.sub(r"\A\s*<!--.*?-->\s*", "", open(p, encoding="utf-8").read(), flags=re.S)

S = {os.path.basename(p): body(p) for p in glob.glob(os.path.join(SE, "ESA-*.md"))}
R = {os.path.basename(p): open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(RAW, "*.md"))}

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if detail else ""))

print("=== 1. unstable heading style: bold vs ATX ===")
for f in sorted(S):
    b = "**" if re.search(r"^\*\*\s*(Affected Versions|Solutions and Mitigations)", S[f], re.M) else ""
    a = "ATX" if re.search(r"^#{1,6}\s*\**\s*(Affected Versions|Solutions and Mitigations)", S[f], re.M) else ""
    print(f"   {f:20} bold={b or '-':3} atx={a or '-':3}")
check("both bold and ATX styles present across the 9 samples",
      any(re.search(r"^\*\*\s*Affected Versions", v, re.M) for v in S.values()) and
      any(re.search(r"^#{1,6}\s*\**\s*Affected Versions", v, re.M) for v in S.values()))

print("\n=== 2. colon inside vs outside the bold markers ===")
inside = [f for f, v in S.items() if re.search(r"\*\*CVE ID:\*\*", v)]
outside = [f for f, v in S.items() if re.search(r"\*\*CVE ID\*\*\s*:", v)]
check("both `**CVE ID:**` and `**CVE ID**:` occur in the samples",
      bool(inside) and bool(outside), f"inside={inside} outside={outside}")

print("\n=== 3. ESA-2026-128 duplicated 'For Users that Cannot Upgrade:' ===")
v = S.get("ESA-2026-128.md", "")
hits = re.findall(r"(?im)^.*For Users that [Cc]annot [Uu]pgrade.*$", v)
check("heading appears twice in ESA-2026-128.md", len(hits) == 2, f"{len(hits)} occurrence(s): {hits}")

print("\n=== 4. ESA-2026-02 bare CVSS vector with no CVSS:3.1/ prefix ===")
v = S.get("ESA-2026-02.md", "")
sev = re.findall(r"(?im)^.*Severity.*$", v)
bare = bool(re.search(r"(?<!CVSS:3\.1/)\bAV:[NALP]/AC:", v))
check("ESA-2026-02 severity line carries a bare vector", bare, str(sev))

print("\n=== 5. severity orderings ===")
pats = {"Medium (6.5)": r"Medium\s*\(\s*6\.5\s*\)",
        "High ( 7.7 )": r"High\s*\(\s*7\.7\s*\)",
        "8.8(High)": r"8\.8\s*\(\s*High\s*\)"}
for lab, pat in pats.items():
    in_samples = [f for f, x in S.items() if re.search(pat, x)]
    in_raw = [f for f, x in R.items() if re.search(pat, x)]
    check(f"ordering {lab!r} reproducible", bool(in_samples or in_raw),
          f"samples={in_samples} raw={in_raw[:4]}{'...' if len(in_raw) > 4 else ''}")
# generic score-first form anywhere
sf = [(f, m.group(0)) for f, x in {**S, **R}.items()
      for m in re.finditer(r"\d+\.\d\s*\(\s*(Low|Medium|High|Critical)\s*\)", x)]
print("   score-first `N.N(Label)` occurrences:", len(sf), sf[:6])
lf = [(f, m.group(0)) for f, x in {**S, **R}.items()
      for m in re.finditer(r"(Low|Medium|High|Critical)\s*\(\s*\d+\.\d\s*\)", x)]
print("   label-first `Label (N.N)` occurrences:", len(lf), lf[:4])

print("\n=== 6. escaped hyphens \\- ===")
esc = [f for f, x in S.items() if "\\-" in x]
check("escaped hyphens present in samples", bool(esc), str(esc))

print("\n=== 7. non-standard MPR metric in ESA-2025-14 ===")
v = S.get("ESA-2025-14.md", "")
mpr_here = "MPR" in v
mpr_any = {f: re.findall(r"CVSS:[\d.]+/[A-Z:/]*MPR:[A-Z]", x) for f, x in {**S, **R}.items()
           if re.search(r"/MPR:", x)}
check("MPR appears in ESA-2025-14.md", mpr_here, "not found in that file" if not mpr_here else "")
print("   files anywhere containing an /MPR: metric:", mpr_any)

print("\n=== 8. 'Description:' label variant in ESA-2026-128 ===")
v = S.get("ESA-2026-128.md", "")
check("Description: label present in ESA-2026-128.md",
      bool(re.search(r"(?im)^\s*(\*\*|#+)?\s*Description\s*:?", v)),
      str(re.findall(r"(?im)^.*Description.*$", v)))
rss = open(os.path.join(SE, "ESA-2026-128.discourse-rss-item.xml"), encoding="utf-8").read()
print("   'Description' in the RSS item body:", bool(re.search(r"Description", rss)))
