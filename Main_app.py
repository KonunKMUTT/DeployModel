# Streamlit app
def main():
    st.markdown('<p style="text-align:center; font-weight:bold; font-size:30px;">Heart Disease Prediction App</p>', unsafe_allow_html=True)

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
        color = "red" if result == 1 else "green"  # Adjust this condition based on your model's output

        # Apply styling with HTML
        styled_result = f'<p style="color:{color}; font-size:20px; text-align:center; font-weight:bold; background-color:#82A0AA; padding:10px; border-radius: 15px;">{result}</p>'
        
        # Display the styled result
        st.markdown(styled_result, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
