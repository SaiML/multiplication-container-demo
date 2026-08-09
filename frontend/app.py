
import streamlit as st
import requests

st.title("Simple Multiplication App")

# Get input from the user
number1 = st.number_input("Enter first number", value=5)
number2 = st.number_input("Enter second number", value=10)

if st.button("Multiply"):

    # Data to send to Flask backend
    data = {
        "number1": number1,
        "number2": number2
    }

    # Send POST request to Flask API
    response = requests.post(
        "http://backend:7860/multiply",
        json=data
    )

    # Get result from Flask
    result = response.json()["result"]

    # Display result
    st.success(f"Result: {result}")
