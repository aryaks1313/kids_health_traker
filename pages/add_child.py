import streamlit as st
from models.child_model import add_child
#login protection
if 'logged_in' not in st.session_state:
    st.warning('Please login first')
    st.stop()
st.title('Add Child')
child_name=st.text_input('Child Name')
gender=st.selectbox('Select Gender',['Male','Female'])
dob=st.date_input('Date of Birth')
blood_group=st.selectbox('Blood Group',['A+','A-','B+','B-','O+','O-'])

if st.button('Add Child'):
    #get logged-in parent_id
    parent_id=st.session_state['parent_id']
    add_child(parent_id,child_name,dob,blood_group,gender)
    st.success('Child Added Successfully')