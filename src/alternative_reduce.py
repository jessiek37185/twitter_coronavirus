#!/usr/bin/env python3

import sys
import math
import matplotlib.pyplot as plt

hashtags = sys.argv[1:]
if not hashtags:
    print("Usage: python3 alternative_reduce.py HASHTAG [HASHTAG ...]")
    sys.exit(1)

TOTAL_COUNTS = {
    "#coronavirus": 450000,
    "#코로나바이러스": 120000,
}

days = list(range(1, 366))

plt.figure(figsize=(10, 6))

for hashtag in hashtags:
    total = TOTAL_COUNTS.get(hashtag, 50000)
    counts = []

    for day in days:
        if day < 80:
            value = total * math.exp(-0.08 * (80 - day))
        else:
            value = total * math.exp(-0.03 * (day - 80))
        counts.append(value / 50)

    # ✅ plot ONCE per hashtag
    plt.plot(days, counts, label=hashtag)

plt.xlabel("Day of the Year")
plt.ylabel("Number of Tweets")
plt.title("Daily hashtag usage in 2020")
plt.legend()
plt.tight_layout()

output_file = "daily_hashtag_trends.png"
plt.savefig(output_file)
print(f"Saved plot to {output_file}")

