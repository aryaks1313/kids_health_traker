import streamlit as st
from models.parent_model import insert_parent
st.title('Parent Registration')

name = st.text_input('Enter Name')

phone = st.text_input('Enter Phone Number')
if len(phone)!=10:
    st.warning('enter valid phone number')
else:
    st.warning('valid phone number')

password = st.text_input('Create Password',type='password')
if len(password)<8:
    st.warning('give strong password')
else:
    st.warning('strong password')

if st.button('Register'):

    if name and phone and password:
      insert_parent(name,phone,password)

      st.success('Registration Successful')
    else:
        st.error('Please fill all fields')