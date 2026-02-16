#!/usr/bin/env python3

import os
import sys
import matplotlib.pyplot as plt
from datetime import datetime

hashtags = sys.argv[1:]

if len(hashtags) == 0:
    print("Usage: python3 alternative_reduce.py <hashtag1> <hashtag2> ...")
    sys.exit(1)

days = []
counts_by_tag = {tag: [] for tag in hashtags}

if not os.path.isdir("outputs"):
    print("Error: outputs/ folder not found.")
    sys.exit(1)

for filename in sorted(os.listdir("outputs")):

    filepath = os.path.join("outputs", filename)

    if not os.path.isfile(filepath):
        continue

    try:
        date = datetime.strptime(filename, "%Y-%m-%d")
    except ValueError:
        continue

    day_of_year = date.timetuple().tm_yday
    days.append(day_of_year)

    counts_today = {tag: 0 for tag in hashtags}

with open(filepath, "r") as f:
    for line in f:
        parts = line.strip().split()

        if len(parts) < 2:
            continue

        tag = parts[0]
        count = parts[1]

        if tag in counts_today:
            counts_today[tag] = int(count)

# VERY IMPORTANT — append after reading file
for tag in hashtags:
    counts_by_tag[tag].append(counts_today[tag])

