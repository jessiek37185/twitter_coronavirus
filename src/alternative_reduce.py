#!/usr/bin/env python3

import sys
import os
import matplotlib.pyplot as plt

hashtags = sys.argv[1:]

if not hashtags:
    print("Usage: python3 src/alternative_reduce.py hashtag1 hashtag2 ...")
    sys.exit(1)

data = {tag: {} for tag in hashtags}

for filename in os.listdir("outputs_by_day"):
    if not filename.endswith(".output"):
        continue

    filepath = os.path.join("outputs_by_day", filename)

    with open(filepath) as f:
        for line in f:
            date, tag, count = line.strip().split()
            count = int(count)

            if tag not in hashtags:
                continue

            if date not in data[tag]:
                data[tag][date] = 0

            data[tag][date] += count

dates = sorted({d for tag in data for d in data[tag]})
days = list(range(1, len(dates)+1))

plt.figure(figsize=(10,6))

for tag in hashtags:
    counts = [data[tag].get(date, 0) for date in dates]
    plt.plot(days, counts, label=tag)

plt.xlabel("Day of the Year")
plt.ylabel("Number of Tweets")
plt.title("Tweet Counts by Hashtag Over the Year")
plt.legend()

plt.tight_layout()
plt.savefig("daily_hashtag_trends.png")

print("Saved plot to daily_hashtag_trends.png")
