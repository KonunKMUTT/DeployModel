
import pickle
import pandas as pd
import streamlit as st

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make prediction
def predict_heart_disease(x_new):
    y_pred_new = model.predict(x_new)
    return y_pred_new

    st.title("Heart Disease Prediction App")

    age = st.text_input("Enter age:")
    impulse = st.text_input("Enter impulse:")
    pressure_high = st.text_input("Enter high blood pressure:")
    pressure_low = st.text_input("Enter low blood pressure:")
    glucose = st.text_input("Enter glucose level:")
    kcm = st.text_input("Enter Creatine Kinase-MB:")
    troponin = st.text_input("Enter troponin level:")
    female = st.checkbox("Female")
    male = st.checkbox("Male")

    if st.button("Predict"):
        result = predict_heart_disease(age, impulse, pressure_high, pressure_low, glucose, kcm, troponin, female, male)
        st.success(f'AI for Heart Disease Predicted is: {result}')
