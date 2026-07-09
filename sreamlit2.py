import streamlit as st
import datetime
from docx import Document

min_dob = datetime.date(1900, 1, 1) 
max_dob = today

st.title("Registration Form")
name=st.text_input("Enter Name: ")
dob=st.date_input("Select your Date of Birth",min_value=min_dob,max_value=max_dob,format="DD/MM/YYYY")
doj=st.date_input("Select your Date of Join",format="DD/MM/YYYY")
job=st.selectbox("Select Designation",["Intern","Web Dev","SDE","SWE","Data Analyst"])
gender=st.radio("Select Gender",options=["Male","Female","other"])
city=st.text_input("Enter Your City: ")
mono=st.text_input("Enter Your Mo. No.: ")

if st.button("Submit"):
    if mono.isdigit ():
        st.success("-:Empoyee details saved -:")
        st.success("-:Employee Details:-")
        st.write("Employee's Name Is:",name)
        st.write("Employee's DOB Is:",dob)
        st.write("Employee's DOJ Is:",doj)
        st.write("Employee's Designation Is:",job)
        st.write("Employee's Gender Is:",gender)
        st.write("Employee's City Is:",city)
        st.write("Employee's Mo. NO. Is:",mono)
        
        doc.save("employee.docx")


    else :
        st. error("Error, enter valid Number...!")

    

