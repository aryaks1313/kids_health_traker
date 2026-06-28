import streamlit as st
import pandas as pd
from models.child_model import get_children
from models.nutrition_model import get_foods,save_food_intake
from models.nutrition_model import (get_child_age_days,get_required_nutrition,get_consumed_nutrition)
from utils.nutrition_helper import (generate_nutrition_report)
from utils.charts import nutrition_chart
if "logged_in" not in st.session_state:
  st.warning("Please Login First")
  st.stop()
st.title("Nutrition Analysis")
parent_id = st.session_state["parent_id"]
children = get_children(parent_id)
if not children:
  st.warning("No Child Added")
  st.stop()
child_dict = { child["child_name"]:child["child_id"]for child in children}
selected_child = st.selectbox("Select Child", list(child_dict.keys()))
child_id = child_dict[selected_child]
st.subheader("Daily Food Intake")

foods = get_foods()

food_dict = {
    food["food_name"]: food["food_id"]
    for food in foods
}

selected_food = st.selectbox(
    "Food",
    list(food_dict.keys())
)

food_id = food_dict[selected_food]
quantity = st.number_input(
    "Quantity",
    min_value=0.1,
    value=1.0
)

meal_type = st.selectbox(
    "Meal Type",
    ["Breakfast", "Lunch", "Dinner", "Snack"]
)

intake_date = st.date_input(
    "Date"
)

if st.button("Save Food Intake"):
    save_food_intake(
        child_id,
        food_id,
        quantity,
        meal_type,
        intake_date
    )

    st.success("Food Intake Saved Successfully")

st.markdown("---")

analysis_date = st.date_input("Analysis Date")
if st.button("Analyze Nutrition"):
    age_days = get_child_age_days(child_id )
    required = get_required_nutrition(age_days)
    consumed = get_consumed_nutrition(child_id,analysis_date)
    report = generate_nutrition_report(consumed,required)
    df = pd.DataFrame(report)
    st.subheader("Nutrition Report")
    st.dataframe(df,use_container_width=True)
    nutrition_chart(df["Nutrient"].tolist(),df["Consumed"].tolist(),df["Required"].tolist())

