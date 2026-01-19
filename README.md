🏠 House Price Prediction | Machine Learning Project

This project predicts house prices using supervised machine learning techniques.
It includes data preprocessing, model training, evaluation, and a user-friendly Streamlit web application deployed on Render.

🚀 Live Demo

🔗 Deployed App (Render):
https://house-price-prediction-streamlit.onrender.com

📸 Application Preview

📌 Problem Statement

Accurately predicting house prices is important for buyers, sellers, and real estate businesses.
The goal of this project is to build a regression model that can predict house prices based on features such as location, size, number of rooms, and other property-related attributes.

🧠 Machine Learning Approach
✔️ Models Used

Linear Regression

Ridge & Lasso Regression

Random Forest Regressor

XGBoost Regressor (Best Performing Model)

✔️ Final Model

XGBoost Regressor selected based on evaluation metrics.

📊 Model Evaluation

R² Score

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Visualization:

!(images/Screenshot 2026-01-19 160830.png)

🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib

Web App: Streamlit

Deployment: Render

Version Control: Git & GitHub

🧩 Project Workflow

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Feature Engineering

Model Training & Hyperparameter Tuning

Model Evaluation

Streamlit App Development

Deployment on Render

📂 Project Structure
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

End-to-end machine learning workflow

Model comparison and selection

Regression evaluation metrics

Deploying ML apps using Streamlit & Render

Translating ML models into real-world applications

