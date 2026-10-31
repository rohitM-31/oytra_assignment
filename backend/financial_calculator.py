
RTO_COST = 169.40
DELIVERED_GROSS_PROFIT = 402.38

PREPAID_RTO_RATE = 0.04
PREPAID_DISCOUNT = 20


def calculate_cod_profit(rto_probability):
    delivered_probability = 1 - rto_probability

    profit = (
        delivered_probability * DELIVERED_GROSS_PROFIT
        - rto_probability * RTO_COST
    )

    return round(profit, 2)


def calculate_prepaid_profit():
    discounted_profit = (
        DELIVERED_GROSS_PROFIT - PREPAID_DISCOUNT
    )

    profit = (
        (1 - PREPAID_RTO_RATE) * discounted_profit
        - PREPAID_RTO_RATE * RTO_COST
    )

    return round(profit, 2)


def calculate_prepaid_nudge(
    rto_probability,
    conversion_rate=0.25
):
    """
    conversion_rate is an illustrative assumption.
    Customers who decline continue with COD.
    """

    prepaid_profit = calculate_prepaid_profit()
    cod_profit = calculate_cod_profit(rto_probability)

    expected_profit = (
        conversion_rate * prepaid_profit
        + (1 - conversion_rate) * cod_profit
    )

    return round(expected_profit, 2)


def calculate_confirmation(
    rto_probability,
    confirmation_rate=0.70,
    confirmed_rto_probability=None
):
    """
    Illustrative assumptions:
    70% confirmation rate.
    Unconfirmed orders are held and not shipped.
    """

    if confirmed_rto_probability is None:
        confirmed_rto_probability = rto_probability

    confirmed_profit = calculate_cod_profit(
        confirmed_rto_probability
    )

    expected_profit = confirmation_rate * confirmed_profit

    return round(expected_profit, 2)


def compare_actions(rto_probability):

    return {
        "ship_as_is": calculate_cod_profit(rto_probability),

        "ship_after_confirmation": calculate_confirmation(
            rto_probability
        ),

        "nudge_to_prepaid": calculate_prepaid_nudge(
            rto_probability
        ),

        "hold_cancel": 0.0
    }


if __name__ == "__main__":

    risk = 0.40

    print("RTO probability:", risk * 100, "%")

    results = compare_actions(risk)

    print("\nExpected profit per order:")

    for action, profit in results.items():
        print(f"{action}: ₹{profit:.2f}")
