#!/usr/bin/env python3
import sys
import json
from datetime import datetime

hashtags = set()
with open("./hashtags") as f:
    for line in f:
        hashtags.add(line.strip().lower())

for line in sys.stdin:
    try:
        tweet = json.loads(line)
    except json.JSONDecodeError:
        continue

    created = tweet.get("created_at")
    if not created:
        continue

    try:
        dt = datetime.strptime(created, "%a %b %d %H:%M:%S %z %Y")
        date_str = dt.strftime("%Y-%m-%d")
    except:
        continue

    for h in tweet.get("entities", {}).get("hashtags", []):
        tag = h.get("text", "").lower()
        if tag in hashtags:
            print(f"{date_str}\t{tag}\t1")
