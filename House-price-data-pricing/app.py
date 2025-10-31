import streamlit as st 
import joblib 
import numpy as np
import pandas as pd
from xgboost import XGBRegressor

# Load model
model = joblib.load("House-price-data-pricing/house_price_xgb.pkl")
locations = joblib.load("House-price-data-pricing/locations.pkl")

# App title
st.set_page_config(page_title="House Price Prediction App",layout="centered")
st.title("Bangalore House Price Prediction")
st.write("Enter property details below to estimate the house price (in lakhs).")

# Input fields
# --------------

# Dropdown for location
location = st.selectbox("Select Location",sorted(locations))
# Numeric input

total_sqft = st.number_input("Total Square Feet",min_value=300,max_value=50000,step=50)
bath = st.number_input("Number of Bathrooms",min_value=1,max_value=10,step=1)
bhk = st.number_input("Number of BHKs",min_value=1,max_value=10,step=1)

# Presiction
# ------------

if st.button("Predict  Price"):
    # Prepare input DataFrame
    input_data = pd.DataFrame([[location,total_sqft,bath,bhk]],
                              columns=["location","total_sqft","bath","bhk"])
    
    # recreate only valid engineered features
    input_data['sqft_per_bhk'] = input_data['total_sqft'] / input_data['bhk']
    input_data['bath_per_bhk'] = input_data['bath'] / input_data['bhk']

    # Make prediction
    predicted_price = model.predict(input_data)
    output = predicted_price[0]

    # Display result
    st.success(f"Estimated House Price: {output:.2f} Lakhs")

# Footer
st.write("----")
st.caption("Made with using Streamlit and XGBoost")

