# Task 2 – Predict Future Stock Prices (Short-Term)

## Overview
This task is part of my **AI/ML Engineering Internship at DevelopersHub Corporation**.  
The goal is to **predict the next day's closing price** of a stock using historical stock market data and machine learning models.  
This exercise helps in understanding **time series data handling, regression modeling, and API-based data fetching**.

---

## Dataset
- **Source:** Yahoo Finance (via `yfinance` Python library)  
- **Stock Symbol:** AAPL (Apple) – can be changed to Tesla, Google, etc.  
- **Features Used:** `Open`, `High`, `Low`, `Volume`  
- **Target:** `Close`  

---

## Steps Performed

### 1. Data Loading
- Historical stock data from 2020-01-01 to 2024-12-25 was fetched using `yfinance`.
- Checked for missing values and basic dataset info (`.head()`, `.info()`, `.describe()`).

### 2. Data Preprocessing
- Feature selection: `Open, High, Low, Volume` → X  
- Target: `Close` → y  
- Split data into **train (80%) and test (20%)** using `train_test_split` with `random_state=42`.

### 3. Model Selection & Training
- Multiple regression models were tested:
  - Linear Regression
  - Huber Regressor
  - RANSAC Regressor
  - TheilSen Regressor
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting Regressor
  - AdaBoost Regressor
  - Support Vector Regressor (SVR)
  - K-Neighbors Regressor
  - XGBoost Regressor

- Hyperparameter tuning was done using `GridSearchCV` for applicable models.  
- Each model was trained on the training data.

### 4. Model Evaluation
- Models were evaluated on the test set using:
  - **Mean Absolute Error (MAE)**  
  - **Mean Squared Error (MSE)**

- The best model was identified based on **lowest MAE** and **MSE**.  

### 5. Final Model
- **RANSAC Regressor** was selected as the final model for its robust performance.  
- Predicted vs actual closing prices were visualized using a scatter plot with reference line.

---

## Libraries Used
- `pandas`, `numpy` – data handling  
- `yfinance` – API to fetch stock data  
- `matplotlib`, `seaborn` – plotting and visualization  
- `sklearn` – regression models, metrics, train/test split, GridSearchCV  
- `xgboost` – advanced gradient boosting model

---

## Key Insights
- Random Forest, Gradient Boosting, and RANSAC generally performed best for short-term prediction.  
- Linear Regression works but may not capture non-linear trends.  
- Stock price prediction is inherently volatile; results are indicative of **short-term trends**, not investment advice.  

---

## Visualizations
- **Bar plots:** MAE and MSE comparison for all models  
- **Scatter plot:** Actual vs Predicted closing prices for the final model  
- **Insights:** Helps identify model performance and prediction accuracy visually.

---