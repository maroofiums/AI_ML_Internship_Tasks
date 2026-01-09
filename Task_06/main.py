import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_model.pkl")
label_encoders = joblib.load("label_encoders.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", min_value=500)
bedrooms = st.selectbox("Bedrooms", [1,2,3,4,5])
bathrooms = st.selectbox("Bathrooms", [1,2,3])
stories = st.selectbox("Stories", [1,2,3,4])
parking = st.selectbox("Parking", [0,1,2,3])

mainroad = st.selectbox("Main Road", ["yes","no"])
guestroom = st.selectbox("Guest Room", ["yes","no"])
basement = st.selectbox("Basement", ["yes","no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes","no"])
airconditioning = st.selectbox("Air Conditioning", ["yes","no"])
prefarea = st.selectbox("Preferred Area", ["yes","no"])

input_df = pd.DataFrame([{
    "area": area,
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "stories": stories,
    "parking": parking,
    "mainroad": mainroad,
    "guestroom": guestroom,
    "basement": basement,
    "hotwaterheating": hotwaterheating,
    "airconditioning": airconditioning,
    "prefarea": prefarea
}])

for col in label_encoders:
    input_df[col] = label_encoders[col].transform(input_df[col])

input_df = input_df[model_columns]

if st.button("Predict Price"):
    price_in_inr = model.predict(input_df)[0]

    conversion_rate = 3.6  # 1 INR = 3.6 PKR (update if needed)
    price_in_pkr = price_in_inr * conversion_rate

    st.success(f"Estimated House Price: ₨ {price_in_pkr:,.0f}")
