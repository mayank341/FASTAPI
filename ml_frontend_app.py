# Install Libraries: pip install streamlit requests
# Execution Command (Development): streamlit run ml_frontend_app.py

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict" 

st.title("Insurance Premium Amount Predictor")
st.markdown("Enter your details below:")


# Input fields
age = st.number_input("Age", min_value=18, max_value=119, value=30)
sex = st.selectbox("Gender", options=["male", "female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=20, value=2)
smoker = st.selectbox("Smoker?", options=["yes", "no"])
region = st.selectbox("Region", options=["southwest", "southeast", "northwest", "northeast"])



if st.button("Predict Premium Amount"):
    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    try:
        response = requests.post(API_URL, json=input_data)
        print(response)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Amount: **{result['predicted_amount']}**")
        else:
            st.error(f"API Error: {response.status_code}) - {response.text}")
        
    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running on port 8000.")