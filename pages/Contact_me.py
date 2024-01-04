import streamlit as st
from send_email import send_email
st.title("Contact Me!")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")
    raw_message = st.text_area("Message:")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    st.info("You can send me a challenge for the 2024 year to my email")

    button = st.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        st.info("Your email was sent successfully!")
