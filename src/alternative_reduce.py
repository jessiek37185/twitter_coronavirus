#!/usr/bin/env python3

import sys
import os
import json
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

hashtags = sys.argv[1:]
if not hashtags:
    print("Usage: python3 alternative_reduce.py HASHTAG [HASHTAG ...]")
    sys.exit(1)

data = {
    tag: defaultdict(int)
    for tag in hashtags
}

output_dir = "outputs"

for filename in os.listdir("."):
    if not filename.startswith("geoTwitter") or not filename.endswith(".lang"):
        continue

    try:
        date_part = filename.split("_")[0].replace("geoTwitter", "")
        date = datetime.strptime(date_part, "%y-%m-%d")
        day_of_year = date.timetuple().tm_yday
    except Exception:
        continue


    with open(filepath, "r") as f:
        daily_data = json.load(f)

    for tag in hashtags:
        if tag in daily_data:
            data[tag][day_of_year] += sum(daily_data[tag].values())

plt.figure(figsize=(10, 6))

for tag, counts in data.items():
    days = sorted(counts.keys())
    values = [counts[d] for d in days]
    plt.plot(days, values, label=tag)

plt.xlabel("Day of Year")
plt.ylabel("Number of Tweets")
plt.title("Daily hashtag usage in 2020")
plt.legend()
plt.tight_layout()

output_file = "daily_hashtag_trends.png"
plt.savefig(output_file)
print(f"Saved plot to {output_file}")
