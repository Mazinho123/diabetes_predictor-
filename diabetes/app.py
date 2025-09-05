import streamlit as st
import numpy as np
import pickle
import os

# ---- Load model ----
st.title("🩺 Diabetes Prediction App")

model_path = "diabetes_model.pkl"

try:
    if not os.path.exists(model_path):
        st.error(f"❌ Model file not found: `{model_path}`")
        st.stop()
    else:
        model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    st.exception(f"❌ Error loading model:\n\n{e}")
    st.stop()

# ---- Sidebar inputs (with units and tooltips) ----
st.sidebar.header("👤 Patient Information")

pregnancies = st.sidebar.number_input(
    "Pregnancies (count)",
    min_value=0,
    max_value=20,
    value=1,
    help="Number of times the patient has been pregnant"
)

glucose = st.sidebar.number_input(
    "Glucose Level (mg/dL)",
    min_value=0,
    max_value=200,
    value=120,
    help="Plasma glucose concentration (measured via blood test)"
)

bp = st.sidebar.number_input(
    "Blood Pressure (mm Hg)",
    min_value=0,
    max_value=140,
    value=70,
    help="Diastolic blood pressure (measured with BP cuff)"
)

skin = st.sidebar.number_input(
    "Skin Thickness (mm)",
    min_value=0,
    max_value=100,
    value=20,
    help="Triceps skin fold thickness (measured with caliper)"
)

insulin = st.sidebar.number_input(
    "Insulin (μU/mL)",
    min_value=0,
    max_value=900,
    value=80,
    help="2-Hour serum insulin level after glucose intake (lab test)"
)

bmi = st.sidebar.number_input(
    "BMI (kg/m²)",
    min_value=0.0,
    max_value=70.0,
    value=25.0,
    help="Body Mass Index = weight (kg) / height² (m²)"
)

dpf = st.sidebar.number_input(
    "Diabetes Pedigree Function (no unit)",
    min_value=0.0,
    max_value=3.0,
    value=0.5,
    help="Function based on family history of diabetes"
)

age = st.sidebar.number_input(
    "Age (years)",
    min_value=1,
    max_value=120,
    value=30,
    help="Age of the patient in years"
)

# ---- Predict Button ----
if st.sidebar.button("🔍 Predict"):
    st.subheader("🧪 Prediction Result")

    try:
        input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.error("⚠️ The patient is **likely to have diabetes.** Please consult a doctor.")
        else:
            st.success("✅ The patient is **unlikely to have diabetes.**")

    except Exception as e:
        st.error(f"❌ Failed to make prediction: {e}")
