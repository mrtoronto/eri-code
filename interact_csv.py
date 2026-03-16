from __future__ import annotations

import csv
import random
import sys
from pathlib import Path


CSV_PATH = Path(__file__).with_name("random_data.csv")
NAMES = ["Indigo", "Jordan", "Kai", "Logan", "Morgan", "Parker"]
CATEGORIES = ["alpha", "beta", "gamma", "delta"]


def load_rows() -> list[dict[str, str]]:
    with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))


def show_summary(rows: list[dict[str, str]]) -> None:
    scores = [int(row["score"]) for row in rows]
    average_score = sum(scores) / len(scores)
    sample = random.choice(rows)

    print(f"Loaded {len(rows)} rows from {CSV_PATH.name}")
    print(f"Average score: {average_score:.1f}")
    print(
        "Random sample: "
        f'{sample["name"]} in {sample["category"]} with score {sample["score"]}'
    )


def append_random_row(rows: list[dict[str, str]]) -> dict[str, str]:
    new_row = {
        "id": str(max(int(row["id"]) for row in rows) + 1),
        "name": random.choice(NAMES),
        "category": random.choice(CATEGORIES),
        "score": str(random.randint(10, 99)),
    }

    with CSV_PATH.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "category", "score"])
        writer.writerow(new_row)

    return new_row


def main() -> None:
    rows = load_rows()
    show_summary(rows)

    if "--add" not in sys.argv:
        print("Run with --add to append another random row.")
        return

    new_row = append_random_row(rows)
    print(f"Added row: {new_row}")


if __name__ == "__main__":
    main()
