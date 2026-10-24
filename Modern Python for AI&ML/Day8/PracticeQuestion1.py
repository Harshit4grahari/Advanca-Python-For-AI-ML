# Turn Your Python Project in Web Page

# What is StreamLit?
# Streamlit is an open-source Python library that lets you create beautiful webapps for
# datascience, machine learning, AI, and automation-without needing HTML, CSS, JavaScript.


import streamlit as st

st.title("Welcome to my Python WEBPAGE")
st.header("AI/ML Automation Demo")

if st.button("Click me!"):
    st.success("You Clicked the Button!")

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age", 0, 100)

st.write("Your Age is", age)