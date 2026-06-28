from database.db_connection import connect_db

#register parent
def insert_parent(name,phone,password):
    conn=connect_db()
    cursor = conn.cursor()
    query=""" INSERT INTO parents(parent_name,phone,password) VALUES(%s,%s,%s)"""
    values=(name,phone,password)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

#parent login
def login_parent(phone,password):
    conn=connect_db()
    cursor=conn.cursor(dictionary=True)
    query=""" select * from parents where phone=%s and password=%s"""
    values=(phone,password)
    cursor.execute(query,values)
    data=cursor.fetchone()
    cursor.close()
    conn.close()
    return data