import streamlit as st
import pickle

# Model load
with open("dt_state_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🗺️ State Good / Bad Predictor")
st.write("Enter state details to predict the status!")

# Input fields
literacy = st.slider("Literacy", 0, 100, 45)
cleanliness = st.slider("Cleanliness", 0, 100, 67)
crime_rate = st.slider("Crime Rate", 0, 100, 45)

# Predict button
if st.button("Predict"):
    result = model.predict([[literacy, cleanliness, crime_rate]])
    if result == 1:
        st.success("✅ Good State!")
    else:
        st.error("❌ Bad State!")
