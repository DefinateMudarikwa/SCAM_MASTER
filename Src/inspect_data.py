from pathlib import Path
import pandas as pd

# Locate the dataset from the project folder.
root = Path(__file__).resolve().parents[1]
path = root / "data" / "Raw" / "meajor_cleaned_preprocessed.csv"

if not path.is_file():
    raise FileNotFoundError(f"Dataset not found: {path}")

# Read the full dataset. This does not modify the original CSV.
df = pd.read_csv(path, low_memory=False)

print("\nTOTAL ROWS:", len(df))
print("TOTAL COLUMNS:", len(df.columns))

print("\nCOLUMNS:")
print(df.columns.tolist())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nMISSING VALUES — FULL DATASET:")
missing = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percent": (df.isna().mean() * 100).round(2),
})
print(missing.to_string())

print("\nLABEL COUNTS — INCLUDING MISSING LABELS:")
print(df["label"].value_counts(dropna=False).to_string())

print("\nSOURCE COUNTS — INCLUDING MISSING SOURCES:")
print(df["source"].value_counts(dropna=False).to_string())

print("\nLABELS BY SOURCE:")
print(pd.crosstab(
    df["source"].fillna("<MISSING SOURCE>"),
    df["label"].fillna("<MISSING LABEL>"),
).to_string())

print("\nLANGUAGE COUNTS:")
print(df["language"].value_counts(dropna=False).to_string())

print("\nEXACT DUPLICATE ROWS:")
print(df.duplicated().sum())

# Check blank text, including whitespace-only values.
subject = df["subject"].fillna("").astype(str).str.strip()
body = df["body"].fillna("").astype(str).str.strip()

print("\nEMPTY SUBJECTS:")
print(subject.eq("").sum())

print("\nEMPTY BODIES:")
print(body.eq("").sum())

print("\nROWS WITH BOTH SUBJECT AND BODY EMPTY:")
print((subject.eq("") & body.eq("")).sum())

# Repeated text may have different metadata or conflicting labels.
text_pairs = pd.DataFrame({"subject": subject, "body": body})
has_text = subject.ne("") | body.ne("")

print("\nREPEATED SUBJECT/BODY PAIRS — EXCLUDING EMPTY TEXT:")
print(text_pairs.loc[has_text].duplicated().sum())

print("\nINSPECTION COMPLETE — ORIGINAL DATASET UNCHANGED.")