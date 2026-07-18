st.markdown('<meta name="google-site-verification" content="cqX5qvVF9sy4ADtyfna9YjCobU6adCWPy-lQYwuEP-Q" />', unsafe_allow_html=True)
import streamlit as st
import numpy as np
import joblib

st.markdown('<meta name="google-site-verification" content="cqX5qvVF9sy4ADtyfna9YjCobU6adCWPy-lQYwuEP-Q" />', unsafe_allow_html=True)
saved = joblib.load("house_price_model.pkl")
model = saved["model"]
scaler = saved["scaler"]

st.title("🏠 California House Price Predictor")

med_inc = st.sidebar.slider("Median Income (in 10k $)", 0.5, 15.0, 3.87)
house_age = st.sidebar.slider("House Age (years)", 1.0, 52.0, 28.6)
ave_rooms = st.sidebar.slider("Average Rooms", 1.0, 15.0, 5.4)
ave_bedrms = st.sidebar.slider("Average Bedrooms", 0.3, 5.0, 1.1)
population = st.sidebar.slider("Population", 3.0, 5000.0, 1425.0)
ave_occup = st.sidebar.slider("Average Occupancy", 0.5, 10.0, 3.0)
latitude = st.sidebar.slider("Latitude", 32.5, 42.0, 35.6)
longitude = st.sidebar.slider("Longitude", -124.5, -114.0, -119.5)

input_data = np.array([[med_inc, house_age, ave_rooms, ave_bedrms,
                         population, ave_occup, latitude, longitude]])
input_scaled = scaler.transform(input_data)

if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    st.success(f"Predicted House Value: ${prediction * 100000:,.2f}")