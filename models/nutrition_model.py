from database.db_connection import connect_db
def get_foods():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT *
    FROM food_master
    ORDER BY food_name
    """)

    foods = cursor.fetchall()

    cursor.close()
    conn.close()

    return foods


def save_food_intake(
        child_id,
        food_id,
        quantity,
        meal_type,
        intake_date):

    conn = connect_db()

    cursor = conn.cursor()

    query = """
    INSERT INTO food_intake(
        child_id,
        food_id,
        quantity,
        mel_type,
        intake_date
    )
    VALUES(%s,%s,%s,%s,%s)
    """

    cursor.execute(
        query,
        (
            child_id,
            food_id,
            quantity,
            meal_type,
            intake_date
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_child_age_days(child_id):
   conn = connect_db()
   cursor = conn.cursor(dictionary=True)
   query = """SELECT DATEDIFF(CURDATE(),dob) AS age_days FROM children WHERE child_id=%s"""
   cursor.execute(query, (child_id,))
   result = cursor.fetchone()
   cursor.close()
   conn.close()
   return result["age_days"]
def get_required_nutrition(age_days):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    query = """SELECT * FROM nutrition_requirement WHERE age <= %s ORDER BY age DESC LIMIT 1"""
    cursor.execute(query, (age_days,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
def get_consumed_nutrition(child_id, intake_date):
   conn = connect_db()
   cursor = conn.cursor(dictionary=True)
   query = """SELECT
       COALESCE(SUM(fm.calories * fi.quantity),0) AS calories,
       COALESCE(SUM(fm.protein * fi.quantity),0) AS protein,
       COALESCE(SUM(fm.carbohydrate * fi.quantity),0) AS carbohydrate,
       COALESCE(SUM(fm.fat * fi.quantity),0) AS fat,
       COALESCE(SUM(fm.calcium * fi.quantity),0) AS calcium,
       COALESCE(SUM(fm.iron * fi.quantity),0) AS iron
       FROM food_intake fi JOIN food_master fm ON fi.food_id = fm.food_id WHERE fi.child_id = %s AND fi.intake_date = %s"""
   cursor.execute(query,(child_id, intake_date))
   result = cursor.fetchone()
   cursor.close()
   conn.close()
   return result