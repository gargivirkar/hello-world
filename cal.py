import streamlit as st

st.title("🧮 Simple Calculator")

num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

operation = st.selectbox(
    "Select an operation:",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            result = "Error: Cannot divide by zero!"
        else:
            result = num1 / num2

    st.success(f"Result: {result}")
