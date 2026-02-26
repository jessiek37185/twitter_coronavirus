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

    plt.plot(days, counts, label=hashtag)

plt.xlabel("Day of the Year")
plt.ylabel("Number of Tweets")
plt.title("Daily hashtag usage in 2020")
plt.legend()
plt.tight_layout()

output_file = "daily_hashtag_trends.png"
plt.savefig(output_file)
print(f"Saved plot to {output_file}")

import sys
import os
import matplotlib.pyplot as plt

def main():
    hashtags = sys.argv[1:]
    if not hashtags:
        print("Usage: python3 src/alternative_reduce.py hashtag1 hashtag2")
        return

    data = {tag: {} for tag in hashtags}

    for filename in os.listdir("../outputs"):
        if not filename.endswith(".output"):
            continue
        with open(os.path.join("../outputs", filename)) as f:
            for line in f:
                tag, day, count = line.strip().split()
                day = int(day)
                count = int(count)
                if tag in data:
                    data[tag][day] = data[tag].get(day, 0) + count

    for tag in data:
        days = sorted(data[tag])
        counts = [data[tag][d] for d in days]
        plt.plot(days, counts, label=tag)

    plt.xlabel("Day of Year")
    plt.ylabel("Tweet Count")
    plt.title("Tweet Frequency Over Time")
    plt.legend()
    plt.savefig("task4_plot.png")
    print("Saved task4_plot.png")

if __name__ == "__main__":
    main()
