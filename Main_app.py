import pickle
import pandas as pd
import streamlit as st

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make prediction
def predict_heart_disease(x_new):
    x_new = pd.DataFrame({
        'age': [age],
        'impluse': [impulse],
        'pressurehight': [pressure_high],
        'pressurelow': [pressure_low],
        'glucose': [glucose],
        'kcm': [kcm],
        'troponin': [troponin],
        'female': [female],
        'male': [male]
    })

    y_pred_new = model.predict(x_new)
    return y_pred_new

# Streamlit app
def main():
    st.title("Heart Disease Prediction App")

    age = st.text_input("Enter age:")
    impulse = st.text_input("Enter impulse:")
    pressurehigh = st.text_input("Enter high blood pressure:")
    pressurelow = st.text_input("Enter low blood pressure:")
    glucose = st.text_input("Enter glucose level:")
    kcm = st.text_input("Enter KCM:")
    troponin = st.text_input("Enter troponin level:")
    female = st.checkbox("Female")
    male = st.checkbox("Male")

    if st.button("Predict"):
        result = predict_heart_disease(x_new)
        st.success(f'AI for Heart Disease Predicted is: {result}')

if __name__ == '__main__':
    main()
