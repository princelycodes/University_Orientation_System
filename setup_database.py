# setup_database.py
import sqlite3
import data # We will still use the data.py file just to get the initial info

# 1. Connect to the database (this creates the file 'university.db' if it doesn't exist)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# 2. Create the table (like designing the Excel columns)
# We use TEXT and INTEGER to define the data types
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id TEXT PRIMARY KEY,
        name TEXT,
        math INTEGER,
        prog INTEGER,
        interest TEXT
    )
''')

# 3. Insert the data from our old dictionary into the database
# We clear the table first just in case we run this multiple times
cursor.execute('DELETE FROM students')

for student_id, info in data.STUDENT_PROFILES.items():
    cursor.execute('''
        INSERT INTO students (id, name, math, prog, interest)
        VALUES (?, ?, ?, ?, ?)
    ''', (student_id, info["name"], info["math"], info["prog"], info["interest"]))

# 4. Save (commit) changes and close
conn.commit()
conn.close()

print("Database 'university.db' created and populated successfully!")