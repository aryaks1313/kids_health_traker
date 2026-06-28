import streamlit as st

st.set_page_config(
    page_title="Kids Health Tracker",
    layout="wide"
)

if "logged_in" not in st.session_state:

    st.title("Kids Health Tracker")

    st.write("Please Login or Register")

    pg = st.navigation([
        st.Page("pages/login.py"),
        st.Page("pages/register.py")
    ])

else:

    pg = st.navigation([
        st.Page("pages/dashboard.py"),
        st.Page("pages/add_child.py"),
        st.Page("pages/vaccination.py"),
        st.Page("pages/bmi_tracker.py"),
        st.Page("pages/nutrition_analysis.py")
    ])

pg.run()




