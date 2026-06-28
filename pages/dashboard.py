import streamlit as st
import pandas as pd
from models.child_model import get_children
from models.vaccination_model import get_nearest_vaccine


if 'logged_in' not in st.session_state:
    st.warning('please login first')
    st.stop()
st.title('Dashboard')
parent_id=st.session_state['parent_id']
parent_name=st.session_state['parent_name']

st.subheader('Kids Health Tracker')
st.write(f"Welcome{parent_name}")

st.write(f'parent id:{parent_id}')

children=get_children(parent_id)
st.metric('total children',len(children))
st.subheader('vaccination reminder')
nearest=get_nearest_vaccine(parent_id)
if nearest:
    st.warning(f"""child:{nearest['child_name']}
               vaccine:{nearest['vaccine_name']}
               due date :{nearest['due_date']}
               days left :{nearest['days_left']}""")
else:
    st.success('no pending vaccination')
if children:
    st.subheader('children')
    df=pd.DataFrame(children)
    st.dataframe(df,use_container_width=True)

if st.button('logout'):
    st.session_state.clear()
    st.success('logged out')