#!/usr/bin/env python3
import sys
import json

hashtags = set()
with open("./hashtags") as f:
    for line in f:
        hashtags.add(line.strip().lower())

for line in sys.stdin:
    try:
        tweet = json.loads(line)
    except json.JSONDecodeError:
        continue

    lang = tweet.get("lang")
    if not lang:
        continue

    for h in tweet.get("entities", {}).get("hashtags", []):
        tag = h.get("text", "").lower()
        if tag in hashtags:
            print(f"{tag}\t{lang}\t1")

