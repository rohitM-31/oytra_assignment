
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "orders_sample.csv"

df = pd.read_csv(
    DATA_PATH,
    dtype={"pincode": "string"}
)

print("ORIGINAL DATASET SHAPE:", df.shape)




text_columns = [
    "final_status",
    "payment_method",
    "city",
    "state",
    "courier",
    "utm_source"
]

for column in text_columns:
    df[column] = df[column].str.strip().str.upper()




print("\nSTANDARDIZED STATUSES")
print(df["final_status"].value_counts(dropna=False))




print("\nINCOMPLETE ORDERS")

incomplete_orders = df[
    df["final_status"] == "IN_TRANSIT"
]

print(incomplete_orders)



duplicates = df[
    df.duplicated(subset=["order_id"], keep=False)
].sort_values("order_id")

print("\nDUPLICATE ORDER RECORDS")

print(
    duplicates[
        ["order_id", "order_datetime", "final_status"]
    ].to_string(index=False)
)




print("\nSTATUS CONFLICTS")

status_counts = (
    df.groupby("order_id")["final_status"].nunique()
)

conflicting_ids = status_counts[status_counts > 1]

print(conflicting_ids)



print("\nEXACT DUPLICATE ROWS")

print(df.duplicated().sum())




print("\nMISSING VALUES")

print(df.isnull().sum())




valid = df[
    df["final_status"].isin(["DELIVERED", "RTO"])
]

print("\nVALID ORDER OUTCOMES")

print(valid["final_status"].value_counts())




rto_rate = (
    valid["final_status"].eq("RTO").mean() * 100
)

print("\nRTO RATE")

print(round(rto_rate, 2), "%")
