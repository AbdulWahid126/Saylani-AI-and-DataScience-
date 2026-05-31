import streamlit as st
import requests

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Income AI Predictor",
    page_icon="💰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    color: #00C853;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: gray;
    margin-bottom: 30px;
}

.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

.success {
    background-color: #14532d;
    color: #4ade80;
}

.low {
    background-color: #7f1d1d;
    color: #f87171;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='main-title'>💰 Income Prediction AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Advanced Machine Learning Web App</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- LAYOUT ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👤 Personal Info")

    age = st.slider("Age", 18, 90, 30)
    workclass = st.selectbox("Workclass", ["Private", "Self-emp", "Gov", "Other"])
    education = st.selectbox("Education", ["Bachelors", "Masters", "HS-grad", "Doctorate"])
    marital_status = st.selectbox("Marital Status", ["Married", "Single", "Divorced"])
    gender = st.radio("Gender", ["Male", "Female"])

with col2:
    st.markdown("### 💼 Work Info")

    occupation = st.text_input("Occupation", "Tech")
    relationship = st.text_input("Relationship", "Husband")
    race = st.selectbox("Race", ["White", "Black", "Asian", "Other"])
    native_country = st.text_input("Country", "United-States")

st.markdown("---")

# ---------------- EXTRA FEATURES ----------------
st.markdown("### 📊 Financial Info")

col3, col4, col5 = st.columns(3)

with col3:
    capital_gain = st.number_input("Capital Gain", 0)

with col4:
    capital_loss = st.number_input("Capital Loss", 0)

with col5:
    hours_per_week = st.slider("Hours/Week", 1, 100, 40)

st.markdown("---")

# ---------------- PREDICT BUTTON ----------------
btn = st.button("🚀 Predict Income", use_container_width=True)

if btn:
    
    url = "http://localhost:8000/predict"

    data = {
        "age": age,
        "workclass": workclass,
        "education": education,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }

    try:
        res = requests.post(url, json=data)

        if res.status_code == 200:
            result = res.json()["prediction"]

            st.markdown("### 🎯 Prediction Result")

            if result == ">50K":
                st.markdown(f"<div class='result-box success'>💰 {result}</div>", unsafe_allow_html=True)
                st.balloons()
                st.success("High Income Category Detected")
            else:
                st.markdown(f"<div class='result-box low'>📉 {result}</div>", unsafe_allow_html=True)
                st.warning("Low Income Category Detected")

            # Fake insight section (UI enhancement)
            st.markdown("### 📊 AI Insight")
            st.info("Model analyzed demographic + financial features to predict income class.")

        else:
            st.error("API Error Occurred")

    except Exception as e:
        st.error(f"Connection Error: {e}")