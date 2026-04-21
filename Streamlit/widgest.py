import pandas as pd
import streamlit as st

st.title("Streamlit Widgets")

st.write("This is a simple Streamlit app with widgets.")

st.sidebar.header("User Input")
name = st.sidebar.text_input("Enter your name:")

age = st.sidebar.slider("Select your age:", 0, 100, 25)

st.write("Name:", name)
st.write("Age:", age)

options = st.sidebar.multiselect("Select your favorite colors:", ["Red", "Green", "Blue", "Yellow"])
st.write("Selected colors:", options)

choice = st.sidebar.selectbox("Select your favorite color:", ["Red", "Green", "Blue", "Yellow"])
st.write("Selected color:", choice)

data = {
    'Name': ['John', 'Jane', 'Doe'],
    'Age': [28, 34, 29]
}
df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")

st.dataframe(df)

upload_file = st.file_uploader("Upload a CSV file", type=["csv"])
if upload_file is not None:
    st.write("File uploaded:", upload_file.name)