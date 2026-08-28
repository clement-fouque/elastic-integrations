#!/usr/bin/env python3
"""Per-ESA-year topic counts vs distinct-ID counts; digit padding per topic;
   multi-ESA topics; late backfills."""
import json, re, collections, os

BASE = os.path.join(os.path.dirname(__file__), "..")
topics = json.load(open(os.path.join(BASE, "cat31_all_topics.json")))
ESA_RE = re.compile(r"ESA-(\d{4})-(\d+)")

esa_topics = [(t, ESA_RE.findall(t["title"])) for t in topics if ESA_RE.search(t.get("title", "") or "")]

# per-topic: assign the topic to the year of its FIRST id
topic_year = collections.Counter()
for t, ids in esa_topics:
    topic_year[int(ids[0][0])] += 1
print("topics per ESA-year (by first ID in title):", dict(sorted(topic_year.items())))

id_year = collections.Counter()
for t, ids in esa_topics:
    for y, s in set(ids):
        id_year[int(y)] += 1
print("distinct-ID occurrences per ESA-year:", dict(sorted(id_year.items())))

# padding, counted per topic (first id)
pt = collections.Counter(len(ids[0][1]) for t, ids in esa_topics)
print("per-topic first-ID sequence digit length:", dict(pt))

print("\nmulti-ESA topics:")
for t, ids in esa_topics:
    if len(set(ids)) > 1:
        print("  ", t["id"], t["title"], "| created", t["created_at"][:10])

print("\n2024 sequences present:", sorted({int(s) for t, ids in esa_topics for y, s in ids if y == "2024"}))
print("2023 sequences present:", sorted({int(s) for t, ids in esa_topics for y, s in ids if y == "2023"}))

print("\nlate backfills (ESA year < post year):")
for t, ids in esa_topics:
    y = int(ids[0][0]); py = int(t["created_at"][:4])
    if py > y:
        print(f"  ESA-{ids[0][0]}-{ids[0][1]} posted {t['created_at'][:10]}  ({t['title'][:70]})")

# 2026 run-rate
d26 = [t["created_at"][:10] for t, ids in esa_topics if int(ids[0][0]) == 2026]
print("\n2026 ESA-year topics:", len(d26), "post-date range:", min(d26), "->", max(d26))
# advisories posted during calendar 2026
posted26 = [t for t, ids in esa_topics if t["created_at"][:4] == "2026"]
print("ESA-tagged topics POSTED in calendar 2026:", len(posted26),
      min(x["created_at"][:10] for x in posted26), "->", max(x["created_at"][:10] for x in posted26))
