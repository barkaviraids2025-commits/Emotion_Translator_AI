import streamlit as st
st.title("My First AI app")
name = st.text_input("Enter Your Name:")
if name:
    st.write("Hello",name,"Welcome to my First AI project.")
