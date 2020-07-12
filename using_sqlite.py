import sqlite3

#conn = sqlite3.connect('employees.db')
conn = sqlite3.connect(':memory:')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        years INTEGER DEFAULT 0
    )
""")

cur.executemany("""
    INSERT INTO employees (first_name, last_name, email, years) VALUES (?,?,?,?)
""", [
    ('Kevin','Bacon', 'kbacon@exa.com',2),
    ('Josh','Brolin', 'jbrolin@exa.com',1),
    ('Kim','Dickens', 'kdickens@exa.com',0)
])

conn.commit()

cur.execute("select * from employees")
print(cur.fetchall())

#for row in cur.execute("SELECT * FROM employees WHERE years >= 1"):
#    print(row[1], "has worked for", row[4], "years")

for row in cur.execute("SELECT * FROM employees WHERE years >= 1"):
    print(row["first_name"], "has worked for", row["years"], "years")

cur.close()
conn.close()
