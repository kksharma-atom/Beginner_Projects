import streamlit as st
import plotly.express as px
import pandas as pd

param_list = ["GDP", "Happiness", "Generosity", "corruption"]

st.title("In Search for Happiness")

x_value =st.selectbox(label="Select the data for X-axis", options=param_list)

y_value = st.selectbox(label="Select the data for Y-axis", options=param_list)

st.subheader(f"{x_value} and {y_value}")

df = pd.read_csv("happy.csv")
def get_data(x_value, y_value):
    xv = df[x_value]
    yv = df[y_value]
    return xv, yv

xv, yv = get_data(x_value.lower(), y_value.lower())

figure = px.scatter(x=xv, y=yv, labels={"x":x_value, "y":y_value})
st.plotly_chart(figure)
