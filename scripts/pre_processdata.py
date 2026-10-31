
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

possible_paths = [
    BASE_DIR / "data" / "orders_sample.csv",
    BASE_DIR / "dashboard" / "data" / "orders_sample.csv"
]

DATA_PATH = next(
    (path for path in possible_paths if path.exists()),
    None
)

if DATA_PATH is None:
    raise FileNotFoundError(
        "orders_sample.csv not found. Check the data folder."
    )

OUTPUT_DIR = BASE_DIR / "data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "cleaned_orders.csv"


df = pd.read_csv(
    DATA_PATH,
    dtype={
        "phone": "string",
        "pincode": "string"
    }
)

print("Dataset loaded from:", DATA_PATH)
print("Original records:", len(df))

df = df.drop_duplicates()

print("After removing duplicates:", len(df))

text_columns = [
    "customer_name",
    "city",
    "state",
    "address",
    "courier",
    "utm_source",
    "payment_method",
    "final_status"
]

for column in text_columns:
    df[column] = df[column].str.strip()

df["final_status"] = df["final_status"].str.upper()



df["order_datetime"] = pd.to_datetime(
    df["order_datetime"],
    errors="coerce"
)


df["city"] = df["city"].fillna("UNKNOWN")


completed_df = df[
    df["final_status"].isin(["DELIVERED", "RTO"])
].copy()


completed_df.to_csv(
    OUTPUT_PATH,
    index=False
)
print("\nCLEANING SUMMARY")

print("Total unique records:", len(df))
print("Completed orders:", len(completed_df))

print("\nFinal status distribution:")
print(completed_df["final_status"].value_counts())

print("\nMissing values:")
print(completed_df.isnull().sum())

print("\nCleaned dataset saved successfully!")
print("Output location:", OUTPUT_PATH)
