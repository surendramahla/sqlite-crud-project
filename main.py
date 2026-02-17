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

#name = "Tom"
# web app form or sink
# sqllit3 dosn't allow multiple sql statements to run. that's why it's safe
"""name = "Tom); DROP TABLE students; --"
cursor.execute(f"INSERT INTO students (name) VALUES  ('{name}')")

conn.commit()"""

# parameterised query that prevent sql injectio attack
"""cursor.execute("insert into students (name, age, grade) values (?, ?, ?)",
                ("BOB", 22, "B++"))

conn.commit()"""

"""cursor.execute("UPDATE students SET grade = ? WHERE id = ?", ("A++",2))
conn.commit()"""

"""student_l = [
    ("abc", 55, "B"),
    ("BotTheDog", 33, "A"),
    ("abcdfas", 26, "C")
]

cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                   student_l)
conn.commit()"""

## DELETE DATA

"""cursor.execute("DELETE FROM students WHERE id = ?", (4,))
conn.commit()"""

## ORDER by
#cursor.execute("SELECT * FROM students ORDER BY age")
#cursor.execute("SELECT * FROM students ORDER BY age DESC")
#cursor.execute("SELECT * FROM students ORDER BY age DESC LIMIT 2")
#####


# Find data by patern like find all the name which has "om"

#cursor.execute("SELECT * FROM students WHERE name LIKE ?", ("%om%",))

#
#rows = cursor.fetchall()

# Transection and roleback
# Prevent the database curption
try:
    cursor.execute('INSERT INTO students (name, age, grade) VALUE (?, ?, ?)', 
                   ('raju', 55, 'B+'))
    raise Exception("error")
except:
    conn.rollback()
    print("roleback cancle the error query")



def add_details(name,age,grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("DATA inserted")

def data_del(id):
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    print(f"The row which has {id} deleted")
def show_tab():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:       
        print(row)

#add_details("BOBTHEDOG", 11, "A")

"""cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)"""

show_tab()