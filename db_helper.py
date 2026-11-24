# db_helper.py
import sqlite3

def get_all_students():
    # Connect to the database
    conn = sqlite3.connect('university.db')
    # row_factory makes it so we can access columns by name (like a dictionary)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    
    # Convert the SQL rows into a standard Python dictionary for our logic files
    students_dict = {}
    for row in rows:
        students_dict[row["id"]] = {
            "id": row["id"],
            "name": row["name"],
            "math": row["math"],
            "prog": row["prog"],
            "interest": row["interest"]
        }
        
    conn.close()
    return students_dict