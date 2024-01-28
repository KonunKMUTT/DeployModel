import pickle
import pandas as pd
import streamlit as st

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make prediction
def predict_heart_disease(age, impulse, pressure_high, pressure_low, glucose, kcm, troponin, female, male):
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
    pressure_high = st.text_input("Enter high blood pressure:")
    pressure_low = st.text_input("Enter low blood pressure:")
    glucose = st.text_input("Enter glucose level:")
    kcm = st.text_input("Enter KCM:")
    troponin = st.text_input("Enter troponin level:")
    female = st.checkbox("Female")
    male = st.checkbox("Male")

    if st.button("Predict"):
        result = predict_heart_disease(age, impulse, pressure_high, pressure_low, glucose, kcm, troponin, female, male)
        
        # Set color based on the result
        color = "red" if result == "positive" else "green"  # Adjust this condition based on your model's output

        # Display the result with the chosen color
        st.markdown(f'<p style="color:{color}; font-size:20px;">AI for Heart Disease Predicted is: {result}</p>', unsafe_allow_html=True)
        # Display the result with the chosen color and centered text
        styled_text = f'<p style="color:{color}; font-size:20px; text-align:center;">AI for Heart Disease Predicted is: {result}</p>'
        st.markdown(styled_text, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
