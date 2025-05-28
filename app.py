import streamlit as st
import numpy as np
import joblib
model = joblib.load("model/alzheimers_xgb_model.pkl")


st.title("🧠 Alzheimer's Prediction App")

st.write("Please enter the following binary inputs (0 or 1):")

# Input fields for the 6 binary features
age = st.number_input("Age_binary (0 or 1)", min_value=0, max_value=1, step=1)
ses = st.number_input("SES_binary (0 or 1)", min_value=0, max_value=1, step=1)
cdr = st.number_input("CDR_binary (0 or 1)", min_value=0, max_value=1, step=1)
nwbv = st.number_input("nWBV_binary (0 or 1)", min_value=0, max_value=1, step=1)
educ = st.number_input("EDUC_binary (0 or 1)", min_value=0, max_value=1, step=1)
mmse = st.number_input("MMSE_binary (0 or 1)", min_value=0, max_value=1, step=1)

# Combine the inputs into a NumPy array and reshape
input_data = np.array([[age, ses, cdr, nwbv, educ, mmse]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Alzheimer's Detected")
    else:
        st.success("✅ Low Risk of Alzheimer's")
