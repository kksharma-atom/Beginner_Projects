import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
content1 = """
Lorem ipsum dolor sit amet. Hic nemo debitis et blanditiis magnam et sapiente debitis? Aut libero officia sed tempore praesentium vel rerum facere sit atque architecto aut amet maiores id quidem suscipit qui praesentium internos!
"""
st.write(content1)

st.subheader("Our Team")

col1,empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# In data.csv, the data are separated by a comma. Therefore, not including sep=","
df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        name = row["first name"] + " " + row["last name"]
        st.subheader(name.title())
        st.write(row["role"])
        st.image("images/"+row["image"])
