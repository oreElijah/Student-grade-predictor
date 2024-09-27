import streamlit as st
import numpy as np
import joblib

model = joblib.load("Student_grade_prediction_model.model")

st.title("Student Grade Predictor")

st.write("This app predicts the grade of a student based on their the amount of hours they studied.")
st.write("")
hours_studied = float(st.number_input("Enter The amount of hours studied per week: ", step=0.1,min_value=0.0, max_value=80.0))

predict_button = st.button(label="Predict grade")
if predict_button:
    if hours_studied == 0.0:
        st.write("No input provided. Please enter hours studied for the exam.")
    else:
        try:
            hours_studied_reshaped = np.array([[hours_studied]])
            score = model.predict(hours_studied_reshaped)[0]
            if score>100:
                score=100
            if score>=70:
                st.write(f"Grade: A, with a score of {score:.2f}")
            elif score>=60 and score<=69:
                st.write(f"Grade: B, with a score of {score:.2f}")
            elif score>=50 and score<=59:
                st.write(f"Grade: C, with a score of {score:.2f}")
            elif score>=45 and score<=49:
                st.write(f"Grade: D, with a score of {score:.2f}")
            elif score>=0 and score<=44:
                st.write(f"Grade: F, with a score of {score:.2f}")
            else:
                st.write("Prediction returned an invalid score.")           
        except Exception as e:
            st.write(f"An error occurred: {e}")
