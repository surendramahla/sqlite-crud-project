import sqlite3

conn = sqlite3.connect("abc.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
grade TEXT)
""")

# Insert one valid record
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    ("BOB", 22, "B++")
)
conn.commit()   # Important!

print("Before rollback test:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Now test rollback
try:
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        ("Alice", 20, "A")
    )
    raise Exception("Simulated error")
except:
    conn.rollback()
    print("\nRollback cancelled the error query")

print("\nAfter rollback test:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)



def add_details():
    conn = sqlite3.connect("abc.db")
    cursor = conn.cursor()

    # 5-7 students sample data
    students = [
        {"name": "Rahul", "age": 21, "grade": "A"},
        {"name": "Amit", "age": 22, "grade": "B+"},
        {"name": "Sneha", "age": 20, "grade": "A+"},
        {"name": "Priya", "age": 23, "grade": "B"},
        {"name": "Rohan", "age": 21, "grade": "C"},
        {"name": "Anjali", "age": 22, "grade": "A"},
        {"name": "Karan", "age": 24, "grade": "B"}
    ]

    cursor.executemany(
        "INSERT INTO students (name, age, grade) VALUES (:name, :age, :grade)",
        students
    )

    conn.commit()
    conn.close()

    print("7 Students added successfully ✅")


add_details()

conn.close()

