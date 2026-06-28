from database.db_connection import connect_db

#save BMI
def save_bmi(child_id,height,weight,bmi,record_date):
    conn=connect_db()
    cursor=conn.cursor()
    query="""INSERT INTO BMI(child_id,height,weight,bmi,record_date)
    VALUES(%s,%s,%s,%s,%s)"""
    values=(child_id,height,weight,bmi,record_date)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

#fetch Bmi  records
def get_bmi(child_id):
    conn= connect_db()
    cursor=conn.cursor(dictionary=True)
    query=""" SELECT * FROM bmi WHERE child_id=%s"""
    cursor.execute(query,(child_id,))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data
