import streamlit as st

st.title("App")

col1,col2 = st.columns(2)

with col1 :
    st.image("134058444503921073.jpg")

with col2:
    st.write("this is picture")


st.header("What is Git?")
st.write("Git is a distributed version control system (DVCS) used to track changes to files over time. It is especially popular for software development, but it can also track documentation, data-processing scripts, configuration files, and many other text-based files.")