import streamlit as st
import pandas as pd

from models.child_model import get_children
from database.db_connection import connect_db

from pages.bmi_tracker import child_dict, selected_child

if 'logged_in' not in st.session_state:
    st.warning('please login first')
    st.stop()
st.title('vaccination Management')
parent_id=st.session_state['parent_id']
children=get_children(parent_id)
if not children:
    st.warning('no child added')
    st.stop()
child_dict={child['child_name']:child['child_id'] for child in children}
selected_child=st.selectbox('selected child',list(child_dict.keys()))
child_id=child_dict[selected_child]
conn=connect_db()
query=""" select vaccine_id,vaccine_name from vaccination_master"""
vaccines=pd.read_sql(query,conn)
conn.close()
vaccine_name=st.selectbox('select vaccine',vaccines['vaccine_name'])
selected_vaccine_id=vaccines.loc[vaccines['vaccine_name']==vaccine_name,'vaccine_id'].values[0]

vaccine_date=st.date_input('vaccination date')
status=st.selectbox('status',['pending','completed'])
if st.button('save vaccination'):
    conn=connect_db()
    cursor=conn.cursor()
    query=""" insert into child_vaccination(child_id,vaccine_id,vaccine_date,status)
    values(%s,%s,%s,%s)"""
    values=(child_id,int(selected_vaccine_id),vaccine_date,status)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()
    st.success('vaccination saved')