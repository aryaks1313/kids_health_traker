from database.db_connection import connect_db

def get_nearest_vaccine(parent_id):
    conn=connect_db()
    cursor=conn.cursor(dictionary=True)
    query=""" select c.child_name,vm.vaccine_name,date_add(c.dob,interval vm.due_days day) as due_date,
    datediff(date_add(c.dob,interval vm.due_days day),curdate()) as days_left from children c
    cross join vaccination_master vm where c.parent_id =%s and vm.vaccine_id not in (select vaccine_id from child_vaccination cv where cv.child_id=c.child_id)
    order by due_date limit 1"""
    cursor.execute(query,(parent_id,))
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    return  result
def get_all_upcoming_vaccines(parent_id):
     conn=connect_db()
     cursor = conn.cursor(dictionary=True)
     query="""select c.child_name,vm.vaccine_name,date_add(c.dob,interval vm.due_days day) as due_date,
    datediff(date_add(c.dob,interval vm.due_days day),curdate()) as days_left from children c
    cross join vaccination_master vm where c.parent_id =%s and vm.vaccine_id not in (select vaccine_id from child_vaccination cv where cv.child_id=c.child_id)
    order by due_date limit 1 """
     cursor.execute(query,(parent_id,))
     data=cursor.fetchall()
     cursor.close()
     conn.close()
     return data