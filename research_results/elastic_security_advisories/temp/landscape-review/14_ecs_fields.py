#!/usr/bin/env python3
"""Verify every non-custom field in mapped-ecs.json exists in the ECS 9.3.0 schema
   (temp/ecs/ecs-9.3.0.yml is a flat map keyed by dotted field name), and that the
   event.kind / category / type values are in ECS's allowed-value lists."""
import os, json, sys
try:
    import yaml
except ImportError:
    os.system(f"{sys.executable} -m pip install --quiet pyyaml"); import yaml

HERE = os.path.dirname(__file__)
SE = os.path.join(HERE, "..", "..", "references", "sample-events")
schema = yaml.safe_load(open(os.path.join(HERE, "..", "ecs", "ecs-9.3.0.yml")))
print("ECS 9.3.0 flat field names:", len(schema))

doc = json.load(open(os.path.join(SE, "ESA-2026-24.mapped-ecs.json")))

def leaves(o, pre=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from leaves(v, f"{pre}.{k}" if pre else k)
    elif isinstance(o, list):
        for v in o:
            if isinstance(v, (dict, list)): yield from leaves(v, pre)
            else: yield pre, v
    else:
        yield pre, o

paths = sorted({p for p, _ in leaves(doc)
                if not p.startswith(("elastic_security_advisories", "_comment"))})
bad = [p for p in paths if p not in schema]
for p in paths:
    print(("  OK  " if p in schema else "  BAD ") + p)
print("\nfields NOT in ECS 9.3.0:", bad or "(none — no invented ECS fields)")

print("\n=== allowed values ===")
for f, got in [("event.kind", doc["event"]["kind"]),
               ("event.category", doc["event"]["category"]),
               ("event.type", doc["event"]["type"])]:
    av = schema[f].get("allowed_values") or []
    allowed = {a["name"] for a in av}
    got_list = got if isinstance(got, list) else [got]
    print(f"  {f}: {got_list} -> " +
          ", ".join(f"{g}={'allowed' if g in allowed else 'NOT ALLOWED'}" for g in got_list))

print("\n=== type sanity ===")
for f in paths:
    t = schema[f].get("type")
    v = None
    cur = doc
    for part in f.split("."):
        cur = cur[part] if isinstance(cur, dict) and part in cur else None
        if cur is None: break
    if t in ("float", "double", "long", "scaled_float") and cur is not None and not isinstance(cur, (int, float)):
        print(f"  {f}: ECS type {t} but value is {type(cur).__name__}")
print("  (no output above = no type violations found)")
