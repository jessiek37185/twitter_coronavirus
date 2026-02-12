# Twitter Coronavirus Analysis

## Project Overview
In this project, I analyzed Twitter data relating to COVID-19 using the GeoTwitter dataset.  
The goal was to understand how related hashtags were used across **languages**, **countries**, and **time** using a MapReduce-style data pipeline followed by visualization.

---

## Task 3: Bar Chart Visualizations
For Task 3, I generated bar charts showing the **top 10 languages** and **top 10 countries** associated with specific hashtags.  
Each bar chart displays:
- **X-axis:** Language or country code
- **Y-axis:** Number of tweets
- Results sorted from lowest to highest count

I generated visualizations for two hashtags:
- `#coronavirus`
- `#코로나바이러스`

### Generated Bar Charts
- `all.lang.#coronavirus.png`
- `all.country.#coronavirus.png`
- `all.lang.#코로나바이러스.png`
- `all.country.#코로나바이러스.png`

These visualizations show how discussion of COVID-19 varied by region and language.

---

## Task 4: Alternative Reduce (Time Series Plot)
For Task 4, I implemented an alternative reduce program (`alternative_reduce.py`) that combines reduction and visualization into a single script.

This program:
- Accepts a list of hashtags from the command line
- Scans daily output files from the mapping step
- Produces a **line plot** where:
  - Each hashtag is represented by one line
  - **X-axis:** Day of the year
  - **Y-axis:** Number of tweets using that hashtag on that day

This visualization shows how attention to different coronavirus-related hashtags changed over time.

---

## Tools and Technologies
- Python
- argparse
- matplotlib
- MapReduce-style processing
- GeoTwitter COVID-19 dataset

---

## Summary
This project demonstrates my  ability to:
- Work with large-scale textual datasets
- Apply MapReduce concepts in practice
- Design clear and informative data visualizations
- Translate raw data into interpretable insights

The resulting figures provide a concise view of how COVID-19 discussions evolved across languages, countries, and time.

