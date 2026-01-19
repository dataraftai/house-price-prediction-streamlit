## 🏠 House Price Prediction | Machine Learning Project

An end-to-end Machine Learning regression project that predicts house prices in Bengaluru based on location, size, and other property features.
The model is deployed as an interactive Streamlit web application using Render.

## 🚀 Live Demo

### 🔗 Deployed App (Render):
https://house-price-prediction-streamlit.onrender.com

### 📌 Project Overview

Real estate price prediction is a classic regression problem with messy real-world data.
This project focuses on:

- Extensive data cleaning
- Feature engineering based on domain knowledge
- Model comparison and hyperparameter tuning
- Deployment-ready ML pipeline

The final model uses XGBoost, which outperformed linear models by capturing non-linear relationships.

### 🗂️ Dataset

- Source: Bengaluru House Price Dataset
- Rows: ~13,000 (before cleaning)
- Target Variable: price (in lakhs)

## 📸 Application Preview

![Preview ](images/streamlitapp.png)

### 📌 Problem Statement

Accurately predicting house prices is important for buyers, sellers, and real estate businesses.
The goal of this project is to build a regression model that can predict house prices based on features such as location, size, number of rooms, and other property-related attributes.

### 🧹 Data Cleaning & Preprocessing

- Key preprocessing steps:
- Handled missing values in location, size, bath
- Converted total_sqft from text (ranges like 1133 - 1384) to numeric
- Extracted BHK from size
- Grouped rare locations (≤10 occurrences) into an other category
- Removed unrealistic outliers using:
- Square feet per BHK thresholds
- IQR-based outlier removal

### 🧠 Feature Engineering

Additional features created to improve model performance:

- bhk – number of bedrooms
- bath_per_bhk – captures luxury & comfort level
- sqft_per_bhk – captures space efficiency
- Cleaned and encoded location using One-Hot Encoding

These features significantly improved prediction accuracy.

### 🤖 Models Trained

The following models were trained and compared using pipelines:

- Linear Regression
- Ridge Regression
- Lasso Regression
- XGBoost Regressor (Final Model)

### 📊 Model Performance (R² Score)
Model	Test R²
Linear Regression	~0.76
Ridge Regression	~0.76
Lasso Regression	~0.76
XGBoost	~0.80

XGBoost performed best due to its ability to handle non-linear relationships.

### 📈 Model Evaluation

The model was evaluated using:

- R² score
- Train vs Test performance comparison
- Actual vs Predicted price scatter plot

This ensured the model generalized well without overfitting.

Visualization:

![Actual vs Predict](images/prediction.png)

### 🛠️ Tech Stack

- Programming Language: Python
- Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib
- Web App: Streamlit
- Deployment: Render
- Version Control: Git & GitHub

### 🧩 Project Workflow

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training & Hyperparameter Tuning
- Model Evaluation
- Streamlit App Development
- Deployment on Render

### 📂 Project Structure
```
├── app.py                  # Streamlit application
├── house_price_xgb.pkl     # Trained XGBoost model
├── locations.pkl           # Location encoder data
├── cleaned_data.csv        # Cleaned dataset
├── notebook.ipynb          # Model training & EDA
├── requirements.txt
├── screenshots/
│   ├── app_ui.png
│   └── render_deploy.png
└── README.md
```
✅ Key Learnings

- End-to-end machine learning workflow
- Model comparison and selection
- Regression evaluation metrics
- Deploying ML apps using Streamlit & Render
- Translating ML models into real-world applications

