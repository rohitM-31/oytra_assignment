
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "cleaned_orders.csv"

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found: {DATA_PATH}"
    )

df = pd.read_csv(
    DATA_PATH,
    dtype={"pincode": "string"}
)

print("Dataset loaded:", DATA_PATH)
print("Total records:", len(df))

def analyze_rto(column):

    result = (
        df.groupby(column, dropna=False, observed=True)
        .agg(
            total_orders=("order_id", "count"),
            rto_orders=(
                "final_status",
                lambda x: (x == "RTO").sum()
            )
        )
        .reset_index()
    )

    result["rto_rate"] = (
        result["rto_orders"] /
        result["total_orders"] * 100
    ).round(2)

    result = result[result["total_orders"] >= 10]

    return result.sort_values(
        "rto_rate",
        ascending=False
    )

print("\n1. OVERALL RTO RATE")

print(df["final_status"].value_counts())

print(
    "RTO rate:",
    round((df["final_status"] == "RTO").mean() * 100, 2),
    "%"
)
print("\n2. RTO RATE BY COURIER")

print(
    analyze_rto("courier").to_string(index=False)
)

print("\n3. RTO RATE BY MARKETING SOURCE")

print(
    analyze_rto("utm_source").to_string(index=False)
)


df["prior_orders_group"] = pd.cut(
    df["customer_prior_orders"],
    bins=[-1, 0, 1, 3, 5, float("inf")],
    labels=["0", "1", "2-3", "4-5", "Above 5"]
)

print("\n4. RTO RATE BY CUSTOMER ORDER HISTORY")

print(
    analyze_rto("prior_orders_group").to_string(index=False)
)

df["prior_rto_group"] = pd.cut(
    df["customer_prior_rto"],
    bins=[-1, 0, 1, 2, float("inf")],
    labels=["0", "1", "2", "Above 2"]
)

print("\n5. RTO RATE BY PREVIOUS RTO HISTORY")

print(
    analyze_rto("prior_rto_group").to_string(index=False)
)


df["order_value_group"] = pd.cut(
    df["order_value"],
    bins=[0, 250, 500, 750, 1000, float("inf")],
    labels=[
        "Below 250",
        "250-499",
        "500-749",
        "750-999",
        "1000+"
    ]
)

print("\n6. RTO RATE BY ORDER VALUE")

print(
    analyze_rto("order_value_group").to_string(index=False)
)


print("\n7. PINCODES WITH AT LEAST 20 ORDERS")

pincode_analysis = analyze_rto("pincode")

pincode_analysis = pincode_analysis[
    pincode_analysis["total_orders"] >= 20
]

print(
    pincode_analysis.head(15).to_string(index=False)
)


print("\n8. PAYMENT METHOD DISTRIBUTION")

print(df["payment_method"].value_counts(dropna=False))

print("\n9. DATA LIMITATION")

print(
    "Payment methods available:",
    df["payment_method"].nunique()
)

print(
    "This dataset should not be used to estimate "
    "prepaid versus COD performance if it contains "
    "only COD orders."
)

