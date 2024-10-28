# Here, we learn how Python interacts with database file 
import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

# Inserting new rows
# cursor.execute("INSERT INTO events VALUES('Agnee','Mumbai','2024.11.06')")
new_rows = [('Fossils', 'Kolkata', '2024.11.05'), 
            ('Parikrama', 'Pune', '2024.11.05')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()