#!/usr/bin/env python3
"""Recompute every Discourse-corpus claim from temp/cat31_all_topics.json."""
import json, re, collections, os, sys

BASE = os.path.join(os.path.dirname(__file__), "..")
topics = json.load(open(os.path.join(BASE, "cat31_all_topics.json")))

print("total topics harvested:", len(topics))

ESA_RE = re.compile(r"ESA-(\d{4})-(\d+)")

esa_topics = []       # (topic, [ (year,seq), ... ])
for t in topics:
    ids = ESA_RE.findall(t.get("title", "") or "")
    if ids:
        esa_topics.append((t, ids))

print("topics whose TITLE carries >=1 ESA id:", len(esa_topics))

# distinct ESA IDs (a topic may carry 2)
all_ids = []
for t, ids in esa_topics:
    for y, s in ids:
        all_ids.append((int(y), int(s), t["id"], t["created_at"][:10]))
uniq_ids = sorted(set((y, s) for y, s, _, _ in all_ids))
print("distinct ESA IDs in titles:", len(uniq_ids))
print("topics carrying >1 ESA id:", sum(1 for t, ids in esa_topics if len(set(ids)) > 1))

# padding
two = sum(1 for y, s, _, _ in all_ids if s < 100)
three = sum(1 for y, s, _, _ in all_ids if s >= 100)
print("occurrences with seq<100:", two, " seq>=100:", three)
# by literal rendering in title
lit = collections.Counter()
for t, ids in esa_topics:
    for m in ESA_RE.finditer(t["title"]):
        lit[len(m.group(2))] += 1
print("literal digit-length of sequence in titles:", dict(lit))

# zero padding check: is ESA-2026-1 ever rendered unpadded?
unpadded = [t["title"] for t, ids in esa_topics
            if re.search(r"ESA-\d{4}-\d(?!\d)", t["title"])]
print("titles with a 1-digit sequence (i.e. NOT zero-padded to 2):", len(unpadded), unpadded[:5])

# per-year
print("\n-- per ESA-year (distinct IDs) --")
byyear = collections.defaultdict(list)
for y, s in uniq_ids:
    byyear[y].append(s)
for y in sorted(byyear):
    seqs = sorted(byyear[y])
    missing = [n for n in range(min(seqs), max(seqs) + 1) if n not in seqs]
    print(f"{y}: count={len(seqs)} min={min(seqs)} max={max(seqs)} missing={len(missing)} -> {missing}")

# distinct publication dates over ESA-tagged topics
dates = collections.Counter(t["created_at"][:10] for t, _ in esa_topics)
print("\ndistinct posting dates (ESA-tagged topics):", len(dates))
print("top 12 batch days (topics):")
for d, c in dates.most_common(12):
    print("  ", d, c)

# batch sizes counted by distinct ESA IDs rather than topics
date_ids = collections.defaultdict(set)
for y, s, tid, d in all_ids:
    date_ids[d].add((y, s))
print("\ntop 12 batch days (distinct ESA IDs):")
for d, ss in sorted(date_ids.items(), key=lambda kv: -len(kv[1]))[:12]:
    print("  ", d, len(ss))

# non-ESA topics
print("\nnon-ESA topics:", len(topics) - len(esa_topics))
for t in topics[:0]:
    pass
