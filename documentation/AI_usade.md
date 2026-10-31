Business Memo: Reducing COD Returns Without Losing Genuine Customers
To: Founder
Date: 31 October 2026
Subject: Recommendations for a Smarter COD Order Risk Decision System

What I found in the data

An analysis of the 1,987 finished orders showed that the overall Return to Origin (RTO) rate was 28.43 per cent, since 565 orders were returned and 1,422 were delivered. Three findings were particularly notable.

Finding 1: Customers who buy for the first time have a higher rate of RTO.

The number of customers who had no orders before was 30.23% (452 out of 1,495 orders).

The RTO for customers who had one prior order was 15.69% (16 out of 102 orders).

New customers form an important risk group, but they should not be automatically rejected since they could also account for future repeat business.

Finding 2: The various marketing channels have RTO rates that are notably different.

The Meta Ads figure is 31.24 percent (239 out of 765).

For Instagram the organic reach is 29.31 per cent (68 out of 232).

Google Ads: 28.28 per cent (69 out of 244).

22.92 per cent (58 out of 253).

Meta Ads showed the highest observed RTO rate, whereas direct orders had the lowest. This is a sufficient reason to look into campaign quality and customer intent, not something that warrants automatically blocking customers from a particular channel.

Previous RTO history is a warning signal but the sample size is small.

Customers with zero RTOs: 27.15% (501 out of 1,845).

Customers with one RTO: 35.19% (38 out of 108).

Customers with two RTOs: 76.47% (26 out of 34).

The 76.47 percent figure is concerning,. It comes from only 34 orders. I would use this as a reason for verification not as enough evidence for automatic cancellation.

Observation: Xpressbees had a 30.95 percent RTO rate, compared with 26.04 percent for Delhivery. This difference is worth investigating with the courier team.

These are associations, in the available dataset not proof that a marketing channel or courier caused an RTO.
I recommend four actions based on the model's predicted RTO probability:

Predicted RTO risk

Recommended action

Below 10%              Ship as-is

10% to below 25%       Send WhatsApp confirmation

25% to below 45%         Offer a prepaid discount

45% or above            Hold for manual 

What would these rules have done to month’s orders?

The cleaned historical dataset has 1,987 completed orders. The model was tested on a holdout of 398 orders. Its RTO precision was 39% recall was 55%. Roc-AUC was 0.666.

These results show that the model can help prioritize orders for review. It is not reliable enough for automatic cancellation.

The four risk thresholds are operating rules not proven optimal thresholds. I have not established verified counts for each decision bucket so I would not claim a specific number of orders saved or cancelled. The next step is to score every historical order calculate the actual bucket counts and backtest the outcomes, before using the rules in production.

Risk                                                   How we would detect it                Genuine customers are incorrectly flagged as high risk        Monitor delivery rates among held and high-risk orders.

Model performance changes over time                   Track weekly RTO rates, precision, recall, and prediction quality.

Marketing campaigns attract a different customer mix          Compare RTO rates by campaign and acquisition source each week.

Courier performance changes                           Monitor RTO rates by courier and delivery region.

Gemini API becomes unavailable or reaches its quota               Monitor API errors and fallback usage; send uncertain cases for manual review.

Prepaid discounts reduce margin without improving conversion         Track discount acceptance, conversion, payment fees, and contribution profit.