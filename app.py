import streamlit as st
import requests

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.title("🫀 Heart Disease Prediction App")

with st.form("prediction_form"):
    st.subheader("Enter Patient Details")

    male = st.selectbox("Gender", ["Female", "Male"])
    age = st.slider("Age", 20, 80, 50)
    education = st.selectbox("Education Level", [1, 2, 3, 4])
    currentSmoker = st.selectbox("Currently Smokes?", ["No", "Yes"])
    cigsPerDay = st.slider("Cigarettes per Day", 0, 60, 0)
    BPMeds = st.selectbox("On BP Medication?", ["No", "Yes"])
    prevalentStroke = st.selectbox("History of Stroke?", ["No", "Yes"])
    prevalentHyp = st.selectbox("Hypertension?", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes?", ["No", "Yes"])
    totChol = st.slider("Total Cholesterol", 100, 400, 200)
    sysBP = st.slider("Systolic BP", 90, 200, 120)
    diaBP = st.slider("Diastolic BP", 60, 120, 80)
    BMI = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
    heartRate = st.slider("Heart Rate", 40, 120, 70)
    glucose = st.slider("Glucose Level", 50, 300, 100)

    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "male": 1 if male == "Male" else 0,
        "age": age,
        "education": education,
        "currentSmoker": 1 if currentSmoker == "Yes" else 0,
        "cigsPerDay": cigsPerDay,
        "BPMeds": 1 if BPMeds == "Yes" else 0,
        "prevalentStroke": 1 if prevalentStroke == "Yes" else 0,
        "prevalentHyp": 1 if prevalentHyp == "Yes" else 0,
        "diabetes": 1 if diabetes == "Yes" else 0,
        "totChol": totChol,
        "sysBP": sysBP,
        "diaBP": diaBP,
        "BMI": BMI,
        "heartRate": heartRate,
        "glucose": glucose
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=payload)
        result = response.json()
        prediction = result.get("CHD_Prediction")

        if prediction == 1:
            st.success("High risk of Coronary Heart Disease (CHD)")
        else:
            st.success("Low risk of Coronary Heart Disease (CHD)")
    except Exception as e:
        st.error(f"Error: {e}")
