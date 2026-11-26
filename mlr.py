
import streamlit as st
import joblib
model = joblib.load("tes.joblib")
st.title("teslay_prediction")
year= st.text_input(label = "Year", placeholder = "Enter your year : ")
km= st.text_input(label = "km", placeholder = "how many kilometres?: ")
color_mapping = {"black":0,"Blue":1,"burgendy":2,"gray":3,"navy blue":4,"red":5,"silver gray":6,"smoke gray":7,"white":8}
color = st.selectbox("select teslay color : ",list(color_mapping.keys()) )
color_num = color_mapping[color]
if st.button("predict"):
    result = model.predict([[float(year), float(km),float(color_num) ]])
    st.success(f"predicted tesla price:{result[0]:.2f}")






