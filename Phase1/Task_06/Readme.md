
# Task 6 – House Price Prediction

**Internship:** AI/ML Engineering Internship – DevelopersHub Corporation
**Due Date:** 14th January, 2026

---

## **Objective**

Predict house prices using property features such as:

* Area (square footage)
* Number of bedrooms and bathrooms
* Parking, stories, and location-related attributes

The goal is to build a **regression-based ML model** that accurately estimates house prices and can be deployed as a real-world application.

---

## **Dataset**

* **Source:** Kaggle – House Price Prediction Dataset
* **Target Variable:** `price`
* **Key Features:**

  * `area`, `bedrooms`, `bathrooms`, `stories`
  * `mainroad`, `guestroom`, `basement`
  * `hotwaterheating`, `airconditioning`
  * `parking`, `prefarea`

Categorical features were converted into numeric form using **Label Encoding**.

---

## **Workflow & Implementation**

### 1️⃣ Data Loading & Exploration

* Loaded dataset using **pandas**
* Checked dataset shape, columns, data types, and missing values
* Performed basic **EDA** to understand feature distributions and relationships

### 2️⃣ Data Preprocessing

* Removed less relevant column (`furnishingstatus`)
* Encoded categorical features using `LabelEncoder`
* Split dataset into **training (67%)** and **testing (33%)**

### 3️⃣ Model Training & Selection

Trained and compared multiple regression models using **GridSearchCV**:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regressor
* Gradient Boosting Regressor

The best-performing model was selected based on **cross-validated R² score**.

### 4️⃣ Model Evaluation

* Evaluated on unseen test data
* Metrics used:

  * **R² Score**
  * **RMSE (Root Mean Squared Error)**

### 5️⃣ Model Saving

Saved trained components for deployment:

* `best_model.pkl`
* `label_encoders.pkl`
* `model_columns.pkl`

---

## **Deployment & Links**

🔗 **Live Streamlit App**
👉 [https://house-price-in-pkr.streamlit.app/](https://house-price-in-pkr.streamlit.app/)

🔗 **GitHub Repository**
👉 [https://github.com/maroofiums/House-Price-Prediction](https://github.com/maroofiums/House-Price-Prediction)

The application allows users to input house features and instantly receive a **predicted house price in PKR**, making it a real-world usable ML solution.

---

## **Skills Demonstrated**

* Regression Modeling (Linear & Ensemble Methods)
* Hyperparameter tuning with GridSearchCV
* Feature preprocessing & encoding
* Model evaluation (R², RMSE)
* Model serialization for deployment
* Streamlit-based ML app deployment
* Real estate data understanding

---

## **Outcome**

* Built an **end-to-end machine learning pipeline**
* Successfully deployed the model as a **live Streamlit web application**
* Completed **Task 6** as part of DevelopersHub Corporation AI/ML Internship
* Project is **production-ready and portfolio-worthy**

---
