
import pandas as pd
import joblib

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# Get the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 1. Load cleaned data
DATA_PATH = BASE_DIR / "data" / "cleaned_orders.csv"

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Cleaned dataset not found at: {DATA_PATH}. "
        "Run scripts/data_cleaning.py first."
    )

df = pd.read_csv(DATA_PATH)

# 2. Prepare date-related features
df["order_datetime"] = pd.to_datetime(
    df["order_datetime"],
    errors="coerce"
)

# Remove rows with invalid dates
df = df.dropna(subset=["order_datetime"])

df["order_hour"] = df["order_datetime"].dt.hour
df["order_day"] = df["order_datetime"].dt.day_of_week

# 3. Create target variable
# RTO = 1, DELIVERED = 0
df["rto_target"] = (df["final_status"] == "RTO").astype(int)

# 4. Select model features
numeric_features = [
    "customer_prior_orders",
    "customer_prior_rto",
    "order_value",
    "num_items",
    "order_hour",
    "order_day"
]

categorical_features = [
    "courier",
    "utm_source",
    "city",
    "state"
]

features = numeric_features + categorical_features

# Check required columns
missing_columns = [col for col in features if col not in df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

# 5. Sort data chronologically
df = df.sort_values("order_datetime").reset_index(drop=True)

X = df[features]
y = df["rto_target"]

# 6. Split chronologically (80% training, 20% testing)
split_index = int(len(df) * 0.80)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# 7. Preprocess numeric features
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# 8. Preprocess categorical features
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# 9. Combine preprocessing
preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

# 10. Create Logistic Regression model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    ))
])

# 11. Train the model
model.fit(X_train, y_train)

# 12. Evaluate the model
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

print("\nCLASSIFICATION REPORT")

print(classification_report(
    y_test,
    predictions,
    labels=[0, 1],
    target_names=["DELIVERED", "RTO"],
    zero_division=0
))

print("\nCONFUSION MATRIX")
print(confusion_matrix(y_test, predictions, labels=[0, 1]))

print("\nROC-AUC SCORE")

if y_test.nunique() == 2:
    print(round(roc_auc_score(y_test, probabilities), 3))
else:
    print("ROC-AUC cannot be calculated because the test set has only one class.")

# 13. Save trained model
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = MODEL_DIR / "rto_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Model location:", MODEL_PATH)
