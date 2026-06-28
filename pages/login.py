import streamlit as st
from models.parent_model import login_parent
st.title('Parent Login')
phone = st.text_input('Enter Phone Number ')


password = st.text_input('Enter Password',type='password')

if st.button('login'):
    user=login_parent(phone,password)
    if user:
        #save login session
        st.session_state['logged_in']=True
        st.session_state['parent_id']=user['parent_id']
        st.session_state['parent_name']=user['parent_name']
        st.success('login successful')
    else:
        st.error('invalid phone or password')