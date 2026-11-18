import streamlit as st

st.title("🎓 Student Profile Application")
st.caption("Developed by LIKHITHA SK")

st.info("Fill in your details and click View My Profile.", icon="ℹ️")

name = st.text_input("Student Name", placeholder="Enter your name")
roll = st.text_input("USN / Roll Number", placeholder="Enter roll number")
dept = st.selectbox("Department", ["CSE", "ISE", "ECE", "EEE", "ME", "CE"])
year = st.radio("Current Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

if st.button("View My Profile"):
    st.success("Profile submitted successfully!", icon="✅")
    st.write("Name: ", name)
    st.write("Roll Number:", roll)
    st.write("Department:", dept)
    st.write("Year: ", year)
