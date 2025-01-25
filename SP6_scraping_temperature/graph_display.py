import streamlit as st
import plotly.express as px
import sqlite3
# import pandas as pd
# df = pd.read_csv("data.txt")
# Establish a database connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Obtain dates from the table
cursor.execute("SELECT date FROM temperatures")
dates = cursor.fetchall()
dates = [item[0] for item in dates]

# Obtain temperatures from the table
cursor.execute("SELECT temperature FROM temperatures")
temperatures = cursor.fetchall()
temperatures = [item[0] for item in temperatures]

figure = px.line(x=dates,
                 y=temperatures, 
                 labels={"x":"Date", "y":"Temperature"})
        
st.plotly_chart(figure)
    


