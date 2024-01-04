import streamlit as st


col1,  col2 = st.columns(2)

with col1:
    st.header("My Life Goals:")
    st.text("1-Find happiness")
    st.text("2-Make success")
    st.text("3-To be proud of my self")

with col2:
    st.header("My 2024 Goals:")
    st.text("1-Start working and earning money")
    st.text("2-Develop my self")
    st.text("3-Gym")
    st.text("4-Have more friends")


col3, col4 = st.columns(2)

with col3:
    st.text("")
    st.text("")
    st.title("Previous goals:")
    st.text("")
    st.text("")
    st.text("")
    st.header("2023 goals")

with col4:
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("1-Start working and earning money  ✕")
    st.text("2-Play a new sport  ✓")
    st.text("3-Learn Laravel  ✓")
