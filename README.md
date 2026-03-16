# eri-code

This is a very small Python practice project.

It has:

- `random_data.csv` - a simple data file
- `interact_csv.py` - a Python script that reads that file

## What the files do

### `random_data.csv`

This is a CSV file with 4 columns:

- `id`
- `name`
- `category`
- `score`

You can open it in a text editor and read it like a table.

### `interact_csv.py`

This script:

- reads all rows from `random_data.csv`
- prints how many rows it found
- prints the average score
- prints one random row
- can add one new random row if you use `--add`

## Install `uv`

This repo uses `uv` to run Python.

Install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Check that it worked:

```bash
uv --version
```

## Run the script

From this folder, run:

```bash
uv run python interact_csv.py
```

That will show a quick summary of the CSV file.

## Add a new row

If you want the script to also add a new random row to the CSV file, run:

```bash
uv run python interact_csv.py --add
```

This does two things:

- shows the summary
- adds one new row to `random_data.csv`

## What to expect

When you run the script, the output will look roughly like this:

```text
Loaded 8 rows from random_data.csv
Average score: 38.1
Random sample: Finley in beta with score 48
```

If you use `--add`, you will also see a line showing the row that got added.
