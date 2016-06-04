import sqlite3
conn = sqlite3.connect('exemple.db')

c = conn.cursor()



##INICIA ESTRUTUR DE DADOS MENU: Contem dados de todos os pratos


c.execute("""CREATE TABLE menu(dish_name varchar primary key,
			       description varchar,
			       gluten integer,
			       vegan integer,
			       vegetarian integer,
			       lactose integer,
			       type string,
			       discount float)
                               """)

#exemplos / dados iniciais
c.execute("""INSERT INTO menu VALUES ('pizza','uma pizza hmmm...',1,1,1,1,'principal',50)""")
c.execute("""INSERT INTO menu VALUES ('hamburger','uma pizza hmmm...',1,0,0,1,'principal',50)""")

##INICIA ESTRUTURA DE DADOS PEDIDO: Contem ID de Pedido e Status

c.execute("""CREATE TABLE restaurantOrder(order_id integer primary key,
                                tableNo integer,
                                status varchar
                                )""")


#exemplos / dados iniciais
c.execute("""INSERT INTO restaurantOrder VALUES (0,1,'solicitado')""")


##INICIA ESTRUTURA DE DADOS PRATOS-PEDIDOS: RELACIONA PRATO COM PEDIDO

c.execute("""CREATE TABLE orderedDishes(
          PRIMARY KEY (order_id integer REFERENCES restaurantOrder(order_id),
          dish_name varchar REFERENCES menu(dish_name)),
          quantity integer,
          halfportion integer
          )""")


#exemplos / dados iniciais
c.execute("""INSERT INTO orderedDishes VALUES (0,'pizza',2,0)""")
c.execute("""INSERT INTO orderedDishes VALUES (0,'hamburger',2,1)""")





#c.execute ("""SELECT * FROM menu""")
#print c.fetchone()
