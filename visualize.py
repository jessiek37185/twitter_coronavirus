#!/usr/bin/env python3

import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--input_path", required=True)
parser.add_argument("--key", required=True)
args = parser.parse_args()

data = []

with open(args.input_path, "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        k, v = parts
        data.append((k, int(v)))

# sort from low to high
data.sort(key=lambda x: x[1])

# take top 10
top10 = data[-10:]

keys = [k for k, _ in top10]
values = [v for _, v in top10]

plt.figure(figsize=(10, 6))
plt.bar(keys, values)
plt.xlabel("Key")
plt.ylabel("Count")
plt.title(f"Top 10 for {args.key}")
plt.xticks(rotation=45)

output_file = f"{args.input_path}.{args.key}.png"
plt.tight_layout()
plt.savefig(output_file)

