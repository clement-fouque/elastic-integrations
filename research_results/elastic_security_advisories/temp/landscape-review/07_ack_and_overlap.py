#!/usr/bin/env python3
"""Chase the residual discrepancies: Acknowledgements=4?, Severity 43 vs 44,
   and whether 'bold N + ATX M' can exceed the sample size."""
import os, re, json, glob

BASE = os.path.join(os.path.dirname(__file__), "..")
meta = json.load(open(os.path.join(BASE, "sampled_meta.json")))
sampled = [os.path.basename(m["file"]) for m in meta]
bodies = {n: open(os.path.join(BASE, "raw", n), encoding="utf-8").read() for n in sampled}
allfiles = {os.path.basename(f): open(f, encoding="utf-8").read()
            for f in glob.glob(os.path.join(BASE, "raw", "topic_*.md"))}

print("=== any mention of acknowledgement/credit/thanks anywhere ===")
for corpus, label in [(bodies, "53-sample"), (allfiles, "57 on disk")]:
    hits = {n for n, b in corpus.items() if re.search(r"(?i)acknowledge|we (would like to )?thank|thanks to|credit", b)}
    print(f"  {label}: {len(hits)} files -> {sorted(hits)}")
    for n in sorted(hits):
        for m in re.finditer(r"(?i)^.*(acknowledge|thank|credit).*$", corpus[n], re.M):
            print(f"     {n}: {m.group(0).strip()[:110]}")
    print()

print("=== Affected Versions / Solutions: bold+ATX overlap on the 53-sample ===")
for lab, core in [("Affected Versions", r"Affected Versions?"),
                  ("Solutions and Mitigations", r"Solutions? and Mitigations?")]:
    bold = {n for n, b in bodies.items() if re.search(r"^\*\*\s*" + core, b, re.M)}
    atx = {n for n, b in bodies.items() if re.search(r"^#{1,6}\s*\**\s*" + core, b, re.M)}
    anyf = {n for n, b in bodies.items() if re.search(r"(?i)" + core, b)}
    neither = set(bodies) - bold - atx
    print(f"  {lab}: bold={len(bold)} atx={len(atx)} both={len(bold & atx)} "
          f"neither={len(neither)} anywhere={len(anyf)}  bold+atx={len(bold)+len(atx)}")
    for n in sorted(neither):
        m = re.search(r"(?i)^.*" + core + r".*$", bodies[n], re.M)
        print(f"     neither -> {n}: {m.group(0).strip()[:100] if m else '<label absent entirely>'}")

print("\n=== Severity: forms on the 53-sample ===")
sev_bold = {n for n, b in bodies.items() if re.search(r"^\*\*\s*Severity", b, re.M)}
sev_atx = {n for n, b in bodies.items() if re.search(r"^#{1,6}\s*\**\s*Severity", b, re.M)}
sev_any = {n for n, b in bodies.items() if re.search(r"(?i)severity", b)}
print("  bold:", len(sev_bold), "atx:", len(sev_atx), "any-mention:", len(sev_any))
print("  no severity at all:", sorted(set(bodies) - sev_any))

print("\n=== CVE ID: forms on the 53-sample ===")
c_bold = {n for n, b in bodies.items() if re.search(r"^\*\*\s*CVE ID", b, re.M)}
c_any = {n for n, b in bodies.items() if re.search(r"(?i)CVE ID", b)}
print("  bold:", len(c_bold), "any:", len(c_any))
print("  files with a CVE-\\d id anywhere:",
      len({n for n, b in bodies.items() if re.search(r"CVE-\d{4}-\d+", b)}))
