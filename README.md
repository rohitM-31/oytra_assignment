# AI-Powered COD Order Risk Decision System

An AI-powered order risk management system for Direct-to-Consumer (D2C) businesses. It analyzes Cash on Delivery (COD) orders, predicts Return to Origin (RTO) risk, validates customer address details using Gemini AI, and recommends actions to reduce delivery losses while protecting genuine customer conversions.

## 1. Project Overview

Cash on Delivery orders can result in significant business losses when customers refuse delivery or provide incomplete delivery details.

This project combines Machine Learning, Generative AI, and financial analysis to help businesses make better order fulfillment decisions.

Based on the predicted RTO probability, the system recommends one of four actions:

- **Ship As-Is:** Process low-risk orders normally.
- **WhatsApp Confirmation:** Confirm customer intent before dispatch.
- **Nudge to Prepaid:** Encourage customers to switch to prepaid payment with a discount.
- **Hold / Manual Review:** Review high-risk orders before making a fulfillment decision.

The system is designed to reduce unnecessary RTO costs without automatically rejecting potentially genuine customers.

## 2. Key Features

### RTO Risk Prediction
- Uses Logistic Regression to predict the probability of an order becoming RTO.
- Analyzes customer order history, previous RTOs, order value, number of items, courier, marketing source, and location.
- Uses a preprocessing pipeline with missing-value imputation, feature scaling, and categorical encoding.
- Evaluates performance using classification reports, confusion matrices, and ROC-AUC.

### AI-Based Address Validation
- Integrates Google's Gemini API for customer name and address validation.
- Checks name format, address completeness, and delivery information.
- Returns structured JSON containing validation status, risk level, reason, and recommendation.
- Handles API errors and quota limitations with a manual-review fallback.

### Decision Engine
Uses predicted RTO probability and configurable thresholds to recommend:
- Ship As-Is
- WhatsApp Confirmation
- Prepaid Discount
- Hold / Manual Review

### Founder Dashboard
- Displays order and COD business metrics.
- Shows order decision categories.
- Displays estimated RTO costs and financial impact.
- Provides an order table with risk scores and recommended actions.
- Includes an AI address validation interface.

### Financial Analysis
- Estimates expected RTO costs.
- Compares COD and prepaid fulfillment outcomes.
- Estimates potential financial benefits of prepaid conversion.
- Considers customer confirmation and conversion assumptions.

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Frontend | React.js, Vite, CSS |
| Backend | Python, FastAPI |
| Machine Learning | Pandas, Scikit-learn, Logistic Regression |
| Generative AI | Google Gemini API |
| Data Processing | NumPy, Pandas |
| Model Storage | Joblib |
| API Integration | Axios, REST API |
| Development Tools | VS Code, Git, GitHub |

## 4. Project Structure

```text
oytra_assignment/
│
├── backend/
│   ├── main.py
│   ├── decision_engine.py
│   ├── financial_calculator.py
│   ├── llm_validator.py
│   └── .env
│
├── data/
│   ├── orders_sample.csv
│   └── cleaned_orders.csv
│
├── models/
│   └── rto_model.pkl
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Sidebar.jsx
│   │   │   ├── StatCard.jsx
│   │   │   ├── DecisionBuckets.jsx
│   │   │   ├── FinancialImpact.jsx
│   │   │   ├── OrdersTable.jsx
│   │   │   └── AddressValidation.jsx
│   │   │
│   │   ├── services/
│   │   │   └── validationService.js
│   │   │
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   └── package.json
│
├── scripts/
│   ├── data_cleaning.py
│   ├── data_analysis.py
│   ├── eda_analysis.py
│   └── train_model.py
│
├── documentation/
├── requirements.txt
├── config.json
└── .gitignore
```

## 5. Dataset and Analysis

The project uses historical order data containing customer, order, courier, marketing, location, payment, and delivery-status information.

Data preprocessing includes:
- Removing exact duplicate records.
- Standardizing text and delivery statuses.
- Handling missing values.
- Converting order timestamps.
- Excluding incomplete delivery outcomes from model training.

Exploratory Data Analysis examines RTO patterns across:
- Courier partners.
- Marketing channels.
- Customer order history.
- Previous customer RTO count.
- Order value ranges.
- Delivery locations.

### Key Dataset Findings

| Finding | Observed Result |
|---|---:|
| Completed orders | 1,987 |
| Delivered orders | 1,422 |
| RTO orders | 565 |
| Overall RTO rate | 28.43% |
| Highest courier RTO rate | Xpressbees – 30.95% |
| Highest marketing-source RTO rate | Meta Ads – 31.24% |
| First-time customer RTO rate | 30.23% |
| Customers with 2 previous RTOs | 76.47% |

These are historical associations, not proof of causation. Small customer and location groups require additional validation.

## 6. Machine Learning Model

The system uses a Logistic Regression classification model.

**Target variable:**
- `0` – Delivered
- `1` – RTO

**Input features:**
- Customer previous orders.
- Customer previous RTO count.
- Order value.
- Number of items.
- Order hour and day.
- Courier partner.
- Marketing source.
- City and state.

**Model training workflow:**
1. Load cleaned order data.
2. Prepare date-related features.
3. Create the RTO target variable.
4. Sort records chronologically.
5. Split data into 80% training and 20% testing.
6. Apply preprocessing using Scikit-learn pipelines.
7. Train Logistic Regression with balanced class weights.
8. Evaluate model performance.
9. Save the trained model using Joblib.

### Baseline Model Performance

Previously recorded baseline results:

| Metric | Result |
|---|---:|
| Accuracy | 66% |
| ROC-AUC | 0.666 |
| RTO Precision | 0.39 |
| RTO Recall | 0.55 |
| RTO F1-score | 0.46 |

The model is an initial prototype and should not be used for automatic order cancellation without further validation and improvement.

## 7. Gemini AI Address Validation

The application integrates the Gemini API to analyze customer delivery information.

The validation response contains:

```json
{
  "name_status": "VALID",
  "address_status": "INCOMPLETE",
  "risk_level": "MEDIUM",
  "reason": "The address is missing house or building details.",
  "suggestion": "Contact the customer to confirm the complete delivery address."
}
```

The AI response is used as an additional validation signal, not as a replacement for authoritative postal address verification.

If Gemini is unavailable or its API quota is exceeded, the system returns an uncertain result and recommends manual review.

## 8. Financial Assumptions

The prototype uses the following business assumptions:

| Parameter | Value |
|---|---:|
| Monthly orders | 3,000 |
| COD percentage | 55% |
| Prepaid percentage | 45% |
| COD RTO rate | 28% |
| Prepaid RTO rate | 4% |
| Average order value | ₹649 |
| Gross margin | 62% |
| Forward shipping cost | ₹65 |
| Return shipping cost | ₹65 |
| Packaging and handling | ₹25 |
| Product damage probability | 8% |
| Damaged product value | ₹180 |
| Prepaid discount | ₹20 |

The estimated expected RTO cost is ₹169.40 per returned order, including expected damage cost.

These are prototype assumptions. Financial projections depend on actual conversion rates, payment costs, customer behaviour, and operational performance.

## 9. Installation and Setup

### Prerequisites

- Python 3.10 or later (use a Python version supported by your installed dependencies).
- Node.js and npm.
- Git.
- Gemini API key.

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd oytra_assignment
```

### Step 2: Create and activate Python virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Python dependencies

```powershell
pip install -r requirements.txt
```

### Step 4: Configure Gemini API key

Create a `.env` file inside the `backend` folder:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not upload your API key to GitHub.

### Step 5: Prepare the dataset

From the project root:

```powershell
python scripts/data_cleaning.py
```

### Step 6: Train the RTO prediction model

```powershell
python scripts/train_model.py
```

This generates the trained model inside the `models` folder.

### Step 7: Start the FastAPI backend

Open a terminal:

```powershell
cd backend
uvicorn main:app --reload --port 8000
```

Backend URL:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 8: Start the React frontend

Open another terminal:

```powershell
cd frontend
npm install
npm run dev
```

Open the frontend URL displayed in the terminal, usually:

```text
http://localhost:5173
```

## 10. API Endpoint

### Validate Customer Address

**Endpoint:**

```http
POST /validate-address
```

**Example request:**

```json
{
  "customer_name": "Rahul Sharma",
  "address": "Flat 202, ABC Apartments, Anna Nagar",
  "city": "Chennai",
  "state": "Tamil Nadu",
  "pincode": "600040"
}
```

The API returns structured address-validation results and a recommendation.

## 11. Limitations and Future Improvements

- Improve RTO prediction performance with additional historical data and model comparison.
- Validate customer-history features to prevent data leakage.
- Calibrate predicted probabilities and optimize decision thresholds using financial backtesting.
- Integrate an actual WhatsApp Business API for customer confirmation.
- Add reliable postal PIN-code verification.
- Connect real-time order management and courier tracking systems.
- Improve financial calculations using observed prepaid conversion and customer retention rates.
- Add authentication, monitoring, and production deployment.

## 12. Conclusion

This project demonstrates how Machine Learning and Generative AI can work together to improve COD order management.

By combining RTO risk prediction, AI-based address validation, rule-based decision recommendations, and financial analysis, the system helps businesses make more informed fulfillment decisions while balancing operational costs and customer experience.
