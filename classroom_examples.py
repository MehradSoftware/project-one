import sqlite3
connection = sqlite3.connect("school.db")
print("connection successfully")
# ----------------------------------------
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        field TEXT
    )
""")
connection.commit()
print("table created")
# ----------------------------------------
students = [
    ('neda', 20, 'computer') , ('ali', 23, 'electric')
]
cursor.executemany("""
    INSERT INTO students (name, age, field) 
    VALUES (?, ?, ?)
""", students)
connection.commit()
print("students added")
# ----------------------------------------
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)