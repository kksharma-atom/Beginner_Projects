import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.txt")


figure = px.line(x=df["date"],
                 y=df["temperature"], 
                 labels={"x":"Date", "y":"Temperature"})
        
st.plotly_chart(figure)
