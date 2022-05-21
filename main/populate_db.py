import sqlite3

exemplos = """
insert into posts (título, conteúdo)
values
("1º post", "conteúdo muito importante"),
("2º post", "conteúdo muito importante"),
("3º post", "conteúdo muito importante"),
("4º post", "conteúdo muito importante")
;
"""

conn = sqlite3.connect("main/database.db")
cur = conn.cursor()

cur.execute(exemplos)

conn.commit()
conn.close()