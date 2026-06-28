from database.db_connection import connect_db

# add child
def add_child(parent_id,child_name,dob,blood_group,gender):
    conn = connect_db()
    cursor=conn.cursor()

    query = """ 
    INSERT INTO children (parent_id,child_name,dob,blood_group,gender)
    VALUES(%s,%s,%s,%s,%s)"""
    values = (parent_id,child_name,dob,blood_group,gender)
    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()

#fetch children
def get_children(parent_id):
    conn=connect_db()
    cursor=conn.cursor(dictionary=True)
    query="""
    SELECT * FROM children WHERE parent_id=%s"""
    cursor.execute(query,(parent_id,))
    data=cursor.fetchall()
    cursor.close()
    conn.close()
    return data