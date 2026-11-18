import streamlit as st

st.set_page_config(page_title="Student Profile Application", page_icon="🎓")

st.title("🎓 Student Profile Application")
st.caption("Developed by Student Name")  # <- replace with your name

st.info("Fill in your details and click View My Profile.")

name = st.text_input("Student Name", placeholder="Enter your name")
roll = st.text_input("USN / Roll Number", placeholder="Enter roll number")
dept = st.selectbox("Department", ["CSE", "ISE", "ECE", "EEE", "ME", "CE", "AIML", "Other"])
year = st.radio("Current Year", ["1st Year", "2nd Year", "3rd Year", "4th Year"])

if st.button("View My Profile"):
    if not name.strip() or not roll.strip():
        st.warning("Please enter your name and roll number.")
    else:
        st.success("Profile submitted successfully!")
        st.write(f"Name: {name}")
        st.write(f"Roll Number: {roll}")
        st.write(f"Department: {dept}")
        st.write(f"Year: {year}")
