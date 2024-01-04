import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Zain Abu Saleem")
intro = """Welcome to my website, I hope you will like my skills and works
thank you for your interesting"""
st.text(intro)


col1, col2 = st.columns(2)
with col1:
    st.image("images/me11.jpg")

with col2:
    personal_info = """
    Hi, I'm Zain! A computer software engineer and a programmer. I am working with my team.
    specialized with PHP Laravel and python.    
    """
    st.info(personal_info)
