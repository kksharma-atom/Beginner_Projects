import streamlit as st
import pandas
from send_email import send_email

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    selectbox_label = "What topic do you want to discuss?"
    # selectbox_options = ["Project Proposals", "Job Inquiries", "Other"]
    option = st.selectbox(selectbox_label, df["topic"])
    raw_message = st.text_area("Message")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {option}
{raw_message}
"""
    
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Your email was sent successfully")