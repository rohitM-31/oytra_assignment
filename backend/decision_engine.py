
import json
import joblib
import pandas as pd

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "config.json", "r") as file:
    config = json.load(file)


model = joblib.load(BASE_DIR / "models" / "rto_model.pkl")


def predict_rto_probability(order):
    """
    Predict the probability of an order becoming RTO.
    """

    order_datetime = pd.to_datetime(order["order_datetime"])

    input_data = pd.DataFrame([{
        "customer_prior_orders": order["customer_prior_orders"],
        "customer_prior_rto": order["customer_prior_rto"],
        "order_value": order["order_value"],
        "num_items": order["num_items"],
        "order_hour": order_datetime.hour,
        "order_day": order_datetime.day_of_week,
        "courier": order["courier"],
        "utm_source": order["utm_source"],
        "city": order["city"],
        "state": order["state"]
    }])

    probability = model.predict_proba(input_data)[0][1]

    return float(probability)


def make_decision(order):


    risk = predict_rto_probability(order)

   
    thresholds = config["risk_thresholds"]

    ship_limit = thresholds["ship"]
    confirmation_limit = thresholds["confirmation"]
    prepaid_limit = thresholds["prepaid"]

    if risk >= prepaid_limit and order["customer_prior_orders"] == 0:
        action = "HOLD / MANUAL REVIEW"
        reason = (
            "This is a first-time customer with high predicted RTO risk. "
            "Review the order before deciding, rather than automatically "
            "cancelling a potential new customer."
        )

    elif risk < ship_limit:
        action = "SHIP AS-IS"
        reason = (
            "The predicted RTO risk is low. "
            "The order can be shipped without additional confirmation."
        )

    elif risk < confirmation_limit:
        action = "SHIP AFTER CONFIRMATION"
        reason = (
            "The order has moderate RTO risk. "
            "Ask the customer to confirm through WhatsApp before shipping."
        )

    elif risk < prepaid_limit:
        action = "NUDGE TO PREPAID"
        reason = (
            "The order has elevated RTO risk. "
            "Offer a small prepaid discount to encourage online payment."
        )

    else:
        action = "HOLD / CANCEL"
        reason = (
            "The predicted RTO risk is very high. "
            "Hold the order for manual review before cancellation."
        )

    return {
        "order_id": order["order_id"],
        "rto_probability": round(risk * 100, 2),
        "action": action,
        "reason": reason
    }


# Test with a sample order
if __name__ == "__main__":

    sample_order = {
        "order_id": "TEST1001",
        "order_datetime": "2026-10-30 10:30",
        "customer_prior_orders": 2,
        "customer_prior_rto": 1,
        "order_value": 649,
        "num_items": 2,
        "courier": "Delhivery",
        "utm_source": "meta_ads",
        "city": "Hyderabad",
        "state": "Telangana"
    }

    result = make_decision(sample_order)

    print("\nCOD ORDER DECISION")
    print("------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
