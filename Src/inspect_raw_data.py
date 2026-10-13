from pathlib import Path

import pandas as pd


root = Path(__file__).resolve().parents[1]
path = root / "data" / "Raw" / "meajor_cleaned_preprocessed.csv"

df = pd.read_csv(path, nrows=100)

print("COLUMNS:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES IN FIRST 100 ROWS:")
print(df.isna().sum())

print("\nFIRST TWO RECORDS:")
print(df.head(2).to_string(index=False))
