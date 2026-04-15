import streamlit as st
import numpy as np
import pandas as pd

## Title of the app
st.title("My First Streamlit App")

## Description
st.write("This is a simple Streamlit app.")

## Displaying a DataFrame
data = {
    'Column 1': [1, 2, 3],
    'Column 2': [4, 5, 6]
}
df = pd.DataFrame(data)
st.write("Here is a sample DataFrame:")
st.dataframe(df)

## Displaying a Chart
st.write("Here is a sample line chart:")
st.line_chart(df)
