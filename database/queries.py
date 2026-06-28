from db_connection import connect_db

# Insert Parent
def insert_parent(name, phone, password):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO parents(name, phone, password)
    VALUES(%s, %s, %s)
    """

    values = (name, phone, password)

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


# Fetch Parent
def get_parent(phone, password):

    conn = connect_db()
    cursor = conn.cursor()

    query = """
    SELECT * FROM parents
    WHERE phone=%s AND password=%s
    """

    values = (phone, password)

    cursor.execute(query, values)

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data