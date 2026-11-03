# Customer Recommendation Engine

This project builds a lightweight recommendation engine for grocery purchases. It reads purchase records, rejects invalid rows, finds similar customers using Jaccard similarity, and exports explainable product suggestions to CSV.

## Overview

- Validates purchase rows and records rejection reasons for bad data.
- Normalizes customer and product IDs so the same value is treated consistently.
- Tracks customer purchase histories as sets and product popularity as counts.
- Finds similar customers using Jaccard similarity.
- Generates recommendations for unseen products supported by similar shoppers.
- Ranks each recommendation with a custom score based on similarity, support, and popularity.
- Exports the final recommendations to CSV.

## Project structure

```text
day4assignment/
├── main.py
├── recommender.py
├── README.md
├── pyproject.toml
├── data/
│   └── purchases.csv
├── output/
│   └── recommendations.csv
├── src/
│   └── day4assignment/
│       └── __init__.py
├── tests/
├── .python-version
├── uv.lock
└── .venv/
```

## Run the project

From the project root, run:

```bash
python main.py --input data/purchases.csv --output output/recommendations.csv --count 3
```

## Notes

- Duplicate purchase IDs are rejected.
- Blank product values, zero or negative quantities, and malformed IDs are treated as invalid purchases.
- The engine keeps one output row per customer, using blank rows for customers with no recommendations.
