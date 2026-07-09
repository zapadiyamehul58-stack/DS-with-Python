import streamlit as st
st.title("BCA Student App")
name = st.text_input("Enter Ypur name :")
course = st.selctbox("Select course ",["bca","Bsc.it","mca"])
if st.button("Submit"):
    st.success("Student Details")
    st.write("name :",name)
    st.write("couse :",course)
