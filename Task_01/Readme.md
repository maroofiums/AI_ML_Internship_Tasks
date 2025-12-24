# Task 1 – Iris Dataset Exploration & Visualization

## Overview
This task is part of my **AI/ML Engineering Internship at DevelopersHub Corporation**.  
The goal of this task is to **explore and visualize the Iris dataset** to gain insights into data distributions, feature relationships, and species differentiation.

---

## Dataset
- **Name:** Iris Dataset  
- **Source:** Seaborn library (`sns.load_dataset('iris')`)  
- **Features:**  
  - `sepal_length`, `sepal_width`, `petal_length`, `petal_width`, `species`  
- **Task Objective:** Understand data trends, distributions, and outliers.

---

## Steps Performed

### 1. Data Loading & Inspection
- Loaded dataset using `pandas` and `seaborn`.
- Checked dataset **shape**, **columns**, **head**, **info**, and **summary statistics**.
- Explored **unique values per column** for better understanding.

### 2. Exploratory Data Analysis (EDA)
- Pairwise relationships between features using `pairplot`.
- Correlation heatmap to identify strong correlations.
- Boxplots to detect outliers across species.
- Violin plots for detailed distribution visualization.
- Joint plots for analyzing strongest feature relationships.

### 3. Observations & Insights
- Petal length and petal width **clearly separate species**, especially Setosa.
- Sepal width shows minor overlap between Versicolor and Virginica.
- Outliers detected in certain features, highlighted using boxplots.
- Correlation analysis confirms that petal features are highly correlated with species.

---

## Libraries Used
- `pandas` – data loading & inspection  
- `seaborn` – visualization & pairplots  
- `matplotlib` – plotting enhancements  

---

## Key Learnings
- How to **load, inspect, and summarize datasets** in Python.
- Visualization techniques for **feature relationships and distributions**.
- Identifying **outliers and correlations** for better understanding of the data.
- Creating a **unique and interpretable EDA workflow** for reporting and GitHub presentation.

---
