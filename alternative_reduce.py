import sys
import os
import matplotlib.pyplot as plt

def main():
    hashtags = sys.argv[1:]
    if not hashtags:
        print("Usage: python3 src/alternative_reduce.py \"#hashtag1\" \"#hashtag2\"")
        return

    # initialize dictionary with ALL 366 days set to 0
    data = {
        tag: {day: 0 for day in range(1, 367)}
        for tag in hashtags
    }

    # scan through outputs folder
    for filename in os.listdir("outputs"):
        if not filename.endswith(".output"):
            continue

        with open(os.path.join("outputs", filename)) as f:
            for line in f:
                tag, day, count = line.strip().split()
                day = int(day)
                count = int(count)

                if tag in data:
                    data[tag][day] += count
  
    plt.figure(figsize=(10,6))
    days = list(range(1, 367))

    for tag in hashtags:
        counts = [data[tag][d] for d in days]
        plt.plot(days, counts, label=tag, linewidth=2)

    plt.xlabel("Day of the Year")
    plt.ylabel("Number of Tweets")
    plt.title("Daily Hashtag Usage in 2020")
    plt.legend()
    plt.tight_layout()
    plt.savefig("task4_plot.png")
    print("Saved task4_plot.png")

if __name__ == "__main__":
    main()
