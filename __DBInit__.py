import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute("CREATE TABLE Menu(name CHAR(150),price FLOAT,tag CHAR(250),description CHAR(600),soyUse INT,lactoUse INT,glutUse INT)")
