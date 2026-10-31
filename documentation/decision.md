# Decision Log – AI-Powered COD Order Risk Decision System

## 1. Project Objective

Build an AI-powered system that predicts COD order RTO risk and recommends suitable actions to reduce operational losses while protecting genuine customer conversions.

The system combines Machine Learning, Gemini AI, business rules, and financial calculations.

## 2. Key Technical and Business Decisions

| No. | Decision | Reason |
|---|---|---|
| 1 | Use Logistic Regression for RTO prediction. | Provides a simple, interpretable baseline for binary classification. |
| 2 | Use chronological 80:20 train-test split. | Evaluates the model on later orders rather than randomly mixing historical records. |
| 3 | Use class-weight balancing. | Helps the model learn from the smaller RTO class. |
| 4 | Use One-Hot Encoding for categorical variables. | Converts courier, city, state, and marketing source into model-readable features. |
| 5 | Use customer order history as model features. | Previous orders and RTO behaviour may provide useful risk signals. |
| 6 | Use four decision categories. | Balances operational risk and customer conversion opportunities. |
| 7 | Integrate Gemini for address validation. | Helps identify incomplete or unclear customer delivery details. |
| 8 | Use manual review when AI validation fails. | Prevents technical failures from being interpreted as customer risk. |
| 9 | Use FastAPI for backend APIs. | Provides a lightweight Python API layer for model and AI integration. |
| 10 | Use React for the dashboard. | Provides an interactive interface for viewing decisions and financial metrics. |
| 11 | Use configurable risk thresholds. | Allows decision policies to be adjusted after financial backtesting. |
| 12 | Use expected-value financial calculations. | Compares fulfillment options using expected revenue and operational costs. |

## 3. Order Decision Policy

The system recommends one of four actions based on predicted RTO probability.

| Predicted RTO Risk | Recommended Action | Business Reason |
|---|---|---|
| Below 10% | Ship As-Is | Low predicted risk; avoid unnecessary friction. |
| 10% to below 25% | WhatsApp Confirmation | Confirm customer intent before dispatch. |
| 25% to below 45% | Nudge to Prepaid | Encourage prepaid conversion using a ₹20 discount. |
| 45% and above | Hold / Manual Review | Review high-risk orders before deciding whether to dispatch. |

**Special handling:** First-time customers with high predicted risk should receive manual review rather than automatic cancellation.

These thresholds are initial prototype settings, not experimentally optimized production thresholds.

## 4. Dataset Analysis Decisions

The cleaned dataset contains 1,987 completed orders:

- Delivered: 1,422
- RTO: 565
- Overall RTO rate: 28.43%

Important observations:

1. Meta Ads orders had a 31.24% RTO rate, the highest among the observed marketing sources.
2. Xpressbees had a 30.95% RTO rate, the highest among the observed courier partners.
3. Customers with no previous orders had a 30.23% RTO rate.
4. Customers with two previous RTOs had a 76.47% RTO rate, but this group contained only 34 orders.

These observations are used as risk indicators, not proof of causation. Small groups are not sufficient to justify automatic rejection.

The dataset contains only COD orders, so prepaid performance cannot be learned directly from this dataset.

## 5. Machine Learning Evaluation Decision

The baseline Logistic Regression model achieved:

| Metric | Result |
|---|---:|
| Accuracy | 66% |
| ROC-AUC | 0.666 |
| RTO Precision | 0.39 |
| RTO Recall | 0.55 |
| RTO F1-score | 0.46 |

**Decision:** Use the model for decision support rather than automatic cancellation.

The RTO precision indicates that many orders predicted as RTO may still be delivered successfully. Therefore, high-risk orders should be reviewed or confirmed instead of immediately cancelled.

## 6. Financial Decisions and Assumptions

The financial calculator uses the following assumptions:

- Average order value: ₹649
- Gross margin: 62%
- Forward shipping: ₹65
- Return shipping: ₹65
- Packaging and handling: ₹25
- Expected damaged-product cost: ₹14.40
- COD RTO rate: 28%
- Prepaid RTO rate: 4%
- Prepaid discount: ₹20

Expected RTO cost:

₹65 + ₹65 + ₹25 + (8% × ₹180) = ₹169.40

The prototype uses an assumed 25% prepaid conversion rate and 70% WhatsApp confirmation success rate.

These rates are assumptions for scenario analysis, not measured results.

The system compares expected financial outcomes to help balance operational savings against lost customer conversion opportunities.

## 7. AI Integration Decision

Gemini AI is used to validate customer name and address information.

The response includes:

- Name validation status.
- Address completeness status.
- Risk level.
- Explanation.
- Suggested action.

If Gemini is unavailable or the API quota is exceeded, the application returns an uncertain result and recommends manual review.

AI validation is not treated as authoritative identity verification or postal address verification.

## 8. Risks and Mitigations

| Risk | Mitigation |
|---|---|
| False-positive RTO predictions | Avoid automatic cancellation and use confirmation or manual review. |
| Limited dataset | Treat the model as a baseline and collect more historical data. |
| Data leakage | Ensure customer history features use only information available before order placement. |
| Gemini API quota limitations | Provide fallback responses and manual review. |
| Incorrect address validation | Add authoritative PIN-code and postal verification. |
| Prepaid conversion uncertainty | Measure actual customer conversion before using financial projections operationally. |
| Customer experience impact | Avoid aggressive cancellation policies, especially for first-time customers. |

## 9. Future Decisions

The next development steps are:

1. Backtest different risk thresholds using historical orders.
2. Compare Logistic Regression with Random Forest and Gradient Boosting.
3. Calibrate predicted probabilities.
4. Integrate WhatsApp Business messaging.
5. Validate PIN codes using a reliable postal data source.
6. Measure actual prepaid conversion and confirmation rates.
7. Monitor model performance and business impact over time.

## 10. Final Decision

The system is designed as a decision-support tool rather than a fully automated cancellation engine.

The primary objective is to reduce avoidable RTO costs while preserving genuine customer orders and balancing the interests of Operations and Marketing.