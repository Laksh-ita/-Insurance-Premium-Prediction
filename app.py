import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("🩺 Insurance Cost Predictor")
st.write("Fill in the details to predict your medical insurance cost.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", ["female", "male"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["no", "yes"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Manual encoding
sex_val = 1 if sex == "male" else 0
smoker_val = 1 if smoker == "yes" else 0

# One-hot encoding for region
region_vals = {
    "northeast": [1, 0, 0, 0],
    "northwest": [0, 1, 0, 0],
    "southeast": [0, 0, 1, 0],
    "southwest": [0, 0, 0, 1],
}
region_encoded = region_vals[region]

# Final input
input_data = region_encoded+[age, sex_val, bmi, children, smoker_val] 
input_array = np.array([input_data])

# Predict
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_array)[0]
    st.success(f"💰 Estimated Insurance Cost: ${prediction:,.2f}")
