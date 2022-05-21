import sqlite3


conn = sqlite3.connect("main/database.db")
cur = conn.cursor()

schema_banco = open("main/schema.sql", "rt")

cur.executescript(schema_banco.read())

conn.commit()
conn.close()