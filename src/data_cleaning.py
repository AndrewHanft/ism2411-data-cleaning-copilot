"""
data_cleaning.py
----------------
This script loads a raw sales dataset, applies several data-cleaning steps,
and outputs a cleaned CSV that is ready for analysis. The script standardizes
column names, trims whitespace, handles missing values, and removes invalid rows.
"""

import pandas as pd


# ------------------------------------------------------
# Copilot-generated function #1
# Purpose: Load a CSV file into a pandas DataFrame.
# Why: Separating loading into its own function makes the
#      pipeline easier to test and maintain.
# ------------------------------------------------------
def load_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


# ------------------------------------------------------
# Copilot-generated function #2
# Purpose: Standardize column names by lowercasing and replacing
#          spaces with underscores.
# Why: Consistent naming avoids bugs and helps improve readability.
# ------------------------------------------------------
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# ------------------------------------------------------
# Hand-built function (you may let Copilot help, but it's not required)
# Purpose: Trim whitespace from all string columns.
# Why: Raw product/category data may include spaces that break grouping.
# ------------------------------------------------------
def strip_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()
    return df


# ------------------------------------------------------
# Copilot-generated function #3 (optional)
# Purpose: Handle missing values consistently.
# Why: Missing prices/quantities make analysis inaccurate.
# ------------------------------------------------------
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["price", "qty"])
    return df


# ------------------------------------------------------
# Hand-built function (or Copilot-assisted)
# Purpose: Remove any rows with negative prices or quantities.
# Why: These are clear data-entry errors and cannot be valid sales.
# ------------------------------------------------------
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df


# ------------------------------------------------------
# Main execution block
# ------------------------------------------------------
if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())
