# **Customer Churn Prediction – End-to-End ML Pipeline**

[Try the App Online](https://churn-prediction-by-maroofiums.streamlit.app/)

---

## **Task 2 – Phase 2 | ML/AI Internship @ DeveloperHub Corporation**

**Objective:**
Develop a **reusable, production-ready machine learning pipeline** for predicting customer churn using Scikit-learn’s Pipeline API. The focus is on **automation, scalability, and model reusability**.

---

## **Problem Statement**

Customer churn is a critical business problem: predicting which customers are likely to leave allows companies to take **preventive actions**. The goal of this task was to **build a predictive system** that can process raw customer data and output churn predictions reliably.

**Dataset:**

* **Telco Churn Dataset** – includes demographic, account, and service usage features.
* Key features: `tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `OnlineSecurity`, etc.

---

## **Approach & Implementation**

1. **Data Preprocessing Pipeline:**

   * Handle missing values (`TotalCharges` and categorical features).
   * Encode categorical features using **manual mappings** instead of LabelEncoder to avoid version conflicts and maintain control.
   * Scale numerical features (optional for tree-based models, mandatory for linear models).
   * Built a **reusable Scikit-learn Pipeline** combining preprocessing + model training.

2. **Model Selection:**

   * Trained **Logistic Regression** for interpretability.
   * Trained **Random Forest** for higher accuracy and feature importance insights.
   * Compared using **cross-validation** and performance metrics (Accuracy, Precision, Recall, ROC-AUC).

3. **Hyperparameter Tuning:**

   * Used **GridSearchCV** to find optimal hyperparameters.
   * Ensured that the best model generalizes well to unseen data.

4. **Model Export & Reusability:**

   * Exported the final pipeline using **joblib**, including all preprocessing steps.
   * This allows loading the pipeline directly in production or in a Streamlit app.

5. **Deployment:**

   * Integrated the trained pipeline into a **Streamlit app** for interactive predictions.
   * Users can enter customer information and get **churn predictions with probabilities**.

---

## **Challenges & Limitations**

1. **Version Compatibility:**

   * Original models were trained on `scikit-learn 1.6.1`, current environment uses `1.7.2`.
   * Manual encoding mappings were used to avoid LabelEncoder errors and mismatches.

2. **Categorical Feature Complexity:**

   * Multiple “No internet service” categories caused encoding challenges.
   * Resolved by mapping manually and keeping consistent feature order for model input.

3. **Feature Order Requirement:**

   * Models require input features in the **exact order** as during training.
   * Streamlit inputs were reordered programmatically before prediction.

4. **Scalability:**

   * Dataset size was moderate; for larger datasets, preprocessing and prediction may need **batch handling**.

---

## **Final Product**

* A **fully functional ML pipeline** that can:

  1. Preprocess raw input.
  2. Predict churn probability.
  3. Be exported and reused in production.

* **Interactive Streamlit App:** [Click to test](https://churn-prediction-by-maroofiums.streamlit.app/)

**Skills Gained:**

* Building Scikit-learn pipelines
* Feature encoding & preprocessing
* Hyperparameter tuning with GridSearchCV
* Exporting models for production use
* Streamlit deployment for real-time predictions

---

### **Key Takeaways**

* Manual label mapping is sometimes safer than LabelEncoder for **production-ready ML apps**.
* Always ensure **feature order and names** match during deployment.
* Combining **pipeline + model export + Streamlit UI** allows rapid prototyping and production deployment.
