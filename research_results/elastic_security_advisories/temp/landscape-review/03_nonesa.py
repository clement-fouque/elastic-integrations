#!/usr/bin/env python3
"""What are the 112 non-ESA-tagged topics? Key to the corpus-size reconciliation."""
import json, re, collections, os

BASE = os.path.join(os.path.dirname(__file__), "..")
topics = json.load(open(os.path.join(BASE, "cat31_all_topics.json")))
ESA_RE = re.compile(r"ESA-(\d{4})-(\d+)")
non = [t for t in topics if not ESA_RE.search(t.get("title", "") or "")]
print("non-ESA topics:", len(non))
byyear = collections.Counter(t["created_at"][:4] for t in non)
print("by post year:", dict(sorted(byyear.items())))

# how many look like security advisories anyway?
adv_like = [t for t in non if re.search(r"(?i)security (update|fix|announcement|advisor)|vulnerab|CVE-\d{4}", t["title"])]
print("non-ESA topics that still look advisory-like:", len(adv_like))
print("\nearliest 25 non-ESA topics:")
for t in sorted(non, key=lambda x: x["created_at"])[:25]:
    print(" ", t["created_at"][:10], t["id"], t["title"][:95])
print("\nlatest 15 non-ESA topics:")
for t in sorted(non, key=lambda x: x["created_at"])[-15:]:
    print(" ", t["created_at"][:10], t["id"], t["title"][:95])

# whole-category post year distribution
allyears = collections.Counter(t["created_at"][:4] for t in topics)
print("\nALL topics by post year:", dict(sorted(allyears.items())))
print("category date range:", min(t["created_at"][:10] for t in topics), "->",
      max(t["created_at"][:10] for t in topics))
