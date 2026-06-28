import streamlit as st
from models.bmi_model import save_bmi
from models.child_model import get_children
from utils.bmi_calculator import (calculate_bmi,bmi_category)
from utils.charts import bmi_chart

#login protection
if 'logged_in' not in st.session_state:
    st.warning('Please login first')
    st.stop()
st.title('BMI Tracker')
parent_id=st.session_state['parent_id']
children=get_children(parent_id)
if not children:
    st.warning('no children added')
    st.stop()
#child dropdown
child_dict={child['child_name']:child['child_id'] for child in children}
selected_child=st.selectbox('select child',list(child_dict.keys()))
child_id=child_dict[selected_child]
height = st.number_input('Enter Height in meters')

weight= st.number_input('Enter weight in kg')
record_date=st.date_input('enter record taken date')

if st.button('Calculate BMI'):
    bmi=calculate_bmi(height,weight)
    category=bmi_category(bmi)
    save_bmi(child_id, height, weight,bmi, record_date)
    st.success(f'BMI = {bmi:.2f}')
    st.info(f'category:{category}')
    bmi_chart([record_date],[bmi])
