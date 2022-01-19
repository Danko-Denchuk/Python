import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('First Post', 'Content of the first post'))
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Second Post', 'Content of the second post'))

connection.commit()
connection.close()
