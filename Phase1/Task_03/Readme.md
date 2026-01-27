# Task 3 – Heart Disease Prediction

## Overview
This task is part of my **AI/ML Engineering Internship at DevelopersHub Corporation**.  
The goal is to **predict whether a person is at risk of heart disease** using the Heart Disease UCI dataset from Kaggle.  
This task demonstrates skills in **binary classification, feature engineering, model evaluation, and explainable AI**.

---

## Dataset
- **Source:** [Kaggle – Heart Disease Prediction Competition](https://www.kaggle.com/competitions/bcdatall)  
- **Features include:**
  - `age` – Age of the patient  
  - `sex` – Gender  
  - `cp` – Chest pain type  
  - `trestbps` – Resting blood pressure  
  - `chol` – Cholesterol  
  - `thalach` – Maximum heart rate achieved  
  - `exang` – Exercise-induced angina  
  - `oldpeak` – ST depression induced by exercise relative to rest  
  - `slope` – Slope of the peak exercise ST segment  
  - `ca` – Number of major vessels colored by fluoroscopy  
  - `thal` – Thalassemia  
  - `target` – 0 = No heart disease, 1 = Heart disease  

---

## Steps Performed

### 1. Data Loading
- Loaded `train.csv` and `test.csv` from Kaggle.
- Checked for missing values, data types, and basic statistics using `.info()` and `.describe()`.

### 2. Feature Engineering
- Created new features to enhance model performance:
  - `chol_trestbps_ratio` → Cholesterol / Blood Pressure
  - `risk_score` → Sum of chest pain, exercise angina, oldpeak, ca, thal
  - `age_thalach_interaction` → Age * Max Heart Rate
- Applied one-hot encoding for categorical features: `sex`, `cp`, `fbs`, `restecg`, `exang`, `slope`, `ca`, `thal`.
- Scaled numerical features using `StandardScaler`.

### 3. Train/Validation Split
- Split training data into **80% train** and **20% validation** to evaluate model performance.

### 4. Model Selection
- Tested multiple classification models:
  - Logistic Regression
  - K-Nearest Neighbors
  - Support Vector Classifier
  - Decision Tree Classifier
  - Random Forest Classifier
  - Gradient Boosting Classifier
  - AdaBoost Classifier
  - Gaussian Naive Bayes

- Hyperparameter tuning performed using **GridSearchCV** for each model.

### 5. Model Evaluation
- Evaluated models on the validation set using:
  - **Accuracy**
  - Later, could include **Confusion Matrix**, **ROC-AUC**, **Precision**, **Recall** (optional for detailed analysis)
- The best performing model was selected based on **highest accuracy**.

### 6. Key Insights
- **Random Forest, Gradient Boosting, and Logistic Regression** performed strongly.  
- Feature engineering like `risk_score` and interaction terms improved model prediction.  
- Medical interpretability is crucial; important features like `cp`, `thal`, `age`, and `thalach` significantly affect predictions.

---

## Libraries Used
- `pandas` – Data handling  
- `scikit-learn` – Models, preprocessing, GridSearchCV, evaluation metrics  
- `numpy` – Numerical operations  
- `StandardScaler` – Feature scaling  
- `GridSearchCV` – Hyperparameter tuning

---
