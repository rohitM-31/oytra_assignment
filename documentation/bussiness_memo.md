# Business Memo: Reducing COD RTO Without Losing Genuine Customers

**To:** Founder  
**From:** AI Automation Engineering Team  
**Subject:** COD Order Risk Management – Business Findings and Recommendations  
**Date:** October 31, 2026

## 1. Executive Summary

The objective of this project is to reduce Return to Origin (RTO) losses from Cash on Delivery (COD) orders while protecting genuine customer conversions.

The proposed system combines Machine Learning-based RTO prediction, Gemini AI-powered address validation, and financial decision rules to recommend four actions:

- Ship As-Is
- WhatsApp Confirmation
- Prepaid Discount
- Hold / Manual Review

Based on the supplied business assumptions, the business processes approximately 3,000 monthly orders, of which 1,650 are COD orders. At a 28% COD RTO rate, approximately 462 COD orders may return each month.

The estimated RTO cost is ₹169.40 per returned order, resulting in an estimated monthly COD RTO cost of **₹78,263**.

My recommendation is to introduce risk-based interventions rather than automatically cancelling high-risk COD orders.

## 2. Three Important Findings from the Data

The cleaned dataset contains 1,987 completed COD orders, including 1,422 delivered orders and 565 RTO orders. The observed RTO rate is 28.43%.

### Finding 1: Marketing source has different RTO patterns

| Marketing Source | Orders | RTO Rate |
|---|---:|---:|
| Meta Ads | 765 | 31.24% |
| Instagram Organic | 232 | 29.31% |
| Google Ads | 244 | 28.28% |
| Influencer | 225 | 27.11% |
| WhatsApp Broadcast | 268 | 26.12% |
| Direct | 253 | 22.92% |

**Business implication:** Meta Ads has the highest observed RTO rate. Marketing should investigate campaign quality, audience targeting, and customer intent before increasing acquisition spend.

This does not establish that Meta Ads causes RTO. Campaign-level and customer-level analysis is required.

### Finding 2: First-time customers have higher observed RTO rates

| Previous Orders | Total Orders | RTO Rate |
|---|---:|---:|
| 0 | 1,495 | 30.23% |
| 1 | 102 | 15.69% |
| 2–3 | 197 | 22.34% |
| 4–5 | 193 | 27.46% |

**Business implication:** First-time customers may benefit from a lightweight WhatsApp confirmation process. However, they should not be automatically rejected because they lack previous purchase history.

### Finding 3: Previous RTO behaviour is a useful risk signal

| Previous RTOs | Total Orders | RTO Rate |
|---|---:|---:|
| 0 | 1,845 | 27.15% |
| 1 | 108 | 35.19% |
| 2 | 34 | 76.47% |

**Business implication:** Customers with previous RTOs may need additional verification. The group with two previous RTOs has a high observed rate, but it contains only 34 orders. This is not enough evidence to justify automatic cancellation.

## 3. Proposed Decision Rules

The system uses predicted RTO probability to recommend the following actions:

| Predicted Risk | Recommended Action | Reason |
|---|---|---|
| Below 10% | Ship As-Is | Avoid unnecessary customer friction. |
| 10%–24.99% | WhatsApp Confirmation | Confirm delivery intent before dispatch. |
| 25%–44.99% | Prepaid Discount | Encourage prepaid payment using a ₹20 discount. |
| 45% and above | Hold / Manual Review | Review high-risk orders before dispatch or cancellation. |

These are initial configurable thresholds, not proven optimal thresholds.

First-time customers should receive fair treatment and manual review when their predicted risk is high.

## 4. Financial Impact and Business Trade-off

### Current estimated COD RTO cost

| Metric | Value |
|---|---:|
| Monthly orders | 3,000 |
| COD share | 55% |
| Monthly COD orders | 1,650 |
| COD RTO rate | 28% |
| Expected monthly COD RTOs | 462 |
| Expected cost per RTO | ₹169.40 |
| Estimated monthly COD RTO cost | ₹78,262.80 |

The expected RTO cost includes:

- Forward shipping: ₹65
- Return shipping: ₹65
- Packaging and handling: ₹25
- Expected damage cost: ₹14.40

### Prepaid conversion opportunity

The assumed prepaid RTO rate is 4%, compared with 28% for COD.

For every COD order successfully converted to prepaid, the estimated reduction in expected RTO cost is:

(28% − 4%) × ₹169.40 = ₹40.66

After a ₹20 prepaid discount, the simplified estimated benefit is approximately **₹20.66 per converted order**, before payment gateway fees and other costs.

For illustration, if 25% of the 1,650 monthly COD orders converted to prepaid:

- Converted orders: approximately 413
- Estimated net benefit: 413 × ₹20.66
- Illustrative monthly benefit: approximately ₹8,530

This is a scenario estimate, not a measured saving. Actual results depend on customer conversion, discount eligibility, payment costs, and the RTO behaviour of converted orders.

### Operations vs Marketing trade-off

**Operations perspective:**

- Reduce forward and return shipping expenses.
- Avoid dispatching orders with a high likelihood of RTO.
- Use confirmation and manual review to prevent unnecessary logistics costs.

**Marketing perspective:**

- Avoid rejecting genuine first-time customers.
- Protect customer acquisition investments.
- Preserve conversion opportunities and long-term customer relationships.

**Recommended balance:**

Use WhatsApp confirmation and prepaid incentives before considering cancellation. Reserve manual review for high-risk cases.

A genuine delivered order generates approximately ₹402.38 in gross profit under the supplied AOV and margin assumptions. Therefore, cancelling a genuine order can sacrifice that gross profit.

The ₹300 customer acquisition cost is already incurred for an acquired customer. It should not automatically be counted again as a cancellation loss. Future customer lifetime value should be considered separately.

## 5. Machine Learning Performance and Limitations

The initial Logistic Regression model achieved:

| Metric | Result |
|---|---:|
| Accuracy | 66% |
| ROC-AUC | 0.666 |
| RTO Precision | 0.39 |
| RTO Recall | 0.55 |
| RTO F1-score | 0.46 |

The model provides an initial risk-ranking capability, but its performance is not strong enough for automatic cancellation.

The low RTO precision means many orders classified as RTO may actually be delivered successfully.

The dataset also has important limitations:

- It contains only COD orders, so prepaid performance cannot be learned from it.
- Customer history features must be checked for historical data leakage.
- Some customer groups have small sample sizes.
- Observed courier and marketing differences do not prove causation.
- Predicted probabilities and decision thresholds need further calibration and backtesting.

Gemini address validation is an additional signal. If the API is unavailable or its quota is exceeded, the system falls back to manual review rather than treating the customer as suspicious.

## 6. Risks and Mitigation

| Risk | Proposed Mitigation |
|---|---|
| Genuine customers incorrectly classified as high risk | Use confirmation and manual review instead of automatic cancellation. |
| Incomplete or inaccurate address information | Request clarification and introduce postal PIN-code verification. |
| Gemini API quota limitations | Maintain fallback handling and monitor API usage. |
| Incorrect model predictions | Monitor precision, recall, and business outcomes. |
| Prepaid discount reduces margin | Measure actual conversion and incremental profit before scaling. |
| Unfair treatment of first-time customers | Avoid using first-time status alone as a reason for cancellation. |

## 7. Next Two Weeks: Action Plan

### Week 1 – Validation and Backtesting

1. Validate that customer-history features use only information available before each order.
2. Backtest different risk thresholds against historical orders.
3. Compare the expected financial outcomes of shipping, confirmation, prepaid conversion, and manual review.
4. Review false-positive predictions to understand how many genuine orders could be affected.
5. Test Gemini validation, API failures, and manual-review fallback behaviour.

**Expected outcome:** A more reliable decision policy with documented assumptions and estimated financial trade-offs.

### Week 2 – Controlled Pilot Preparation

1. Select a small group of eligible COD orders for a controlled pilot.
2. Introduce WhatsApp confirmation for selected medium-risk orders.
3. Test the ₹20 prepaid incentive with a limited customer segment.
4. Record customer responses, confirmation rates, prepaid conversion, delivery outcomes, and RTO costs.
5. Compare pilot results against a suitable control group.
6. Review results with Operations and Marketing before expanding the policy.

**Expected outcome:** Real conversion and delivery data to validate whether the proposed interventions reduce RTO costs without damaging genuine customer conversions.

## 8. Success Metrics

The pilot should track:

- COD RTO rate.
- WhatsApp confirmation success rate.
- Prepaid conversion rate.
- Delivery success rate.
- False-positive RTO predictions.
- RTO cost per order.
- Gross profit from delivered orders.
- Net financial impact after discounts and intervention costs.

The primary success metric should be **incremental net financial impact**, not just a reduction in RTO percentage.

## 9. Final Recommendation

I recommend launching this system as a decision-support solution with a controlled pilot rather than immediately enabling automatic COD cancellation.

The initial priority should be to identify high-risk orders, confirm customer intent, encourage prepaid conversion where appropriate, and send uncertain cases for manual review.

The business should scale the policy only after real pilot data demonstrates a positive financial impact while maintaining genuine customer conversions.

**The goal is not simply to prevent RTOs; it is to reduce avoidable losses without rejecting valuable customers.**