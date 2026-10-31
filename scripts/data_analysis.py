
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

possible_paths = [
    BASE_DIR / "data" / "orders_sample.csv",
    BASE_DIR / "dashboard" / "data" / "orders_sample.csv",
    BASE_DIR / "data" / "cleaned_orders.csv"
]

DATA_PATH = next(
    (path for path in possible_paths if path.exists()),
    None
)

if DATA_PATH is None:
    raise FileNotFoundError(
        "Dataset not found. Check the data folder."
    )

df = pd.read_csv(
    DATA_PATH,
    dtype={
        "phone": "string",
        "pincode": "string"
    }
)

print("Dataset loaded from:", DATA_PATH)
print("\nFIRST FIVE ORDERS")
print(df.head())

print("\nDATASET SHAPE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nDATASET INFORMATION")
df.info()



print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE ORDER IDS")
print(df["order_id"].duplicated().sum())

print("\nORDER STATUS DISTRIBUTION")
print(df["final_status"].value_counts())

print("\nRTO PERCENTAGE")

print(
    df["final_status"]
    .value_counts(normalize=True) * 100
)


print("\nPAYMENT METHOD DISTRIBUTION")
print(df["payment_method"].value_counts())
