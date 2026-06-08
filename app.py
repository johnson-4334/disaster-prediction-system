import streamlit as st
import pandas as pd
import joblib

model = joblib.load("disaster_pipeline_v2.joblib")

st.title("Disaster Prediction System")

severity = st.selectbox(
    "Severity Level",
    ["Low", "Medium", "High"]
)

population = st.number_input(
    "Affected Population",
    min_value=0
)

loss = st.number_input(
    "Estimated Economic Loss (USD)",
    min_value=0.0
)

response = st.number_input(
    "Response Time (Hours)",
    min_value=0.0
)

damage = st.slider(
    "Infrastructure Damage Index",
    0.0, 10.0, 5.0
)

aid = st.selectbox(
    "Aid Provided",
    ["Yes", "No"]
)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "severity_level": [severity],
        "affected_population": [population],
        "estimated_economic_loss_usd": [loss],
        "response_time_hours": [response],
        "infrastructure_damage_index": [damage],
        "aid_provided": [aid]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Major Disaster")
    else:
        st.success("Non-Major Disaster")