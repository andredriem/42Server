import sqlite3
conn = sqlite3.connect('exemple.db')

c = conn.cursor()



##INICIA ESTRUTUR DE DAOS MENU


c.execute("""CREATE TABLE menu(name varchar unique primary key,
				description varchar,
				glutem integer,
				vegan integer,
				vegetarian integer,
				lactose integer,
				tipo string,
				float desconto)""")

#exemplos
c.execute("""INSERT INTO menu VALUES ('pizza','uma pizza hmmm...',1,1,1,1,'principal',50)""")
c.execute("""INSERT INTO menu VALUES ('hamburger','uma pizza hmmm...',1,0,0,1,'principal',50)""")






#c.execute ("""SELECT * FROM menu""")
#print c.fetchone()
