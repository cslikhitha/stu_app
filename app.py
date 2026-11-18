import streamlit as st
st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
</style>
""", unsafe_allow_html=True)
st.title("🎓 Student Profile Application")
st.subheader("Developed by Student Name")

st.info("Fill in your details and click View My Profile.")

# Student details form
with st.form("student_form"):

    name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

    roll_number = st.text_input(
        "USN / Roll Number",
        placeholder="Enter roll number"
    )

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "ME", "Civil"]
    )

    year = st.radio(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )
    submit = st.form_submit_button("View My Profile")
if submit:

    if name.strip() == "" or roll_number.strip() == "":
        st.error("Please enter all details.")

    else:
        st.success("Profile submitted successfully!")

        st.write("### Student Profile")

        st.write("**Name:**", name)
        st.write("**Roll Number:**", roll_number)
        st.write("**Department:**", department)
        st.write("**Year:**", year)
