# Task 6 – House Price Prediction

**Internship:** AI/ML Engineering Internship – DevelopersHub Corporation
**Due Date:** 14th January, 2026

---

## **Objective**

Predict house prices using various property features such as:

* Size (area in square feet)
* Number of bedrooms and bathrooms
* Parking availability, stories, and location-related features

The goal is to build a **regression model** that can accurately estimate house prices based on these features.

---

## **Dataset**

* **Source:** Kaggle – House Price Prediction Dataset
* **Key Features:**

  * `price` (target variable)
  * `area`, `bedrooms`, `bathrooms`, `stories`
  * `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `parking`, `prefarea`
* Categorical features are **label-encoded** for modeling.

---

## **Steps Performed**

1. **Data Loading & Inspection**

   * Loaded dataset using **pandas**
   * Checked shape, columns, data types, and missing values
   * Performed initial **EDA** (scatter plots, histograms, boxplots)

2. **Data Preprocessing**

   * Dropped less impactful features (`furnishingstatus`)
   * Encoded categorical features using **LabelEncoder**
   * Split data into **training (67%)** and **testing (33%)** sets

3. **Model Training & Hyperparameter Tuning**

   * Trained multiple regression models using **GridSearchCV**:

     * Linear Regression
     * Ridge Regression
     * Lasso Regression
     * Random Forest Regressor
     * Gradient Boosting Regressor
   * Selected the best model based on **cross-validated R² score**

4. **Model Evaluation**

   * Predicted on test set
   * Evaluated using:

     * **R² Score**
     * **Root Mean Squared Error (RMSE)**

5. **Saved Artifacts**

   * `best_model.pkl` – Trained regression model
   * `label_encoders.pkl` – Label encoders for categorical features
   * `model_columns.pkl` – Column order for deployment

---

## **Skills Applied**

* Regression modeling (Linear, Ensemble, Gradient Boosting)
* Feature scaling and selection
* Model evaluation using R² and RMSE
* Data preprocessing and categorical encoding
* Real estate data understanding

---

## **Outcome**

* Developed a **production-ready house price prediction model**
* Completed an **end-to-end ML pipeline**, ready for deployment via Streamlit or FastAPI
* Gained experience in **model comparison, hyperparameter tuning, and artifact saving**

---

## **Future Improvements**

* Include **interactive visualization dashboard** for predictions
* Experiment with **XGBoost, CatBoost, or LightGBM** for better performance
* Add **feature importance plots** to highlight key drivers of price

---
