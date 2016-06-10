import sqlite3	
import SQLExceptions

#retorna id da nova ordem
def insertOrder(table_no,status):
	table_no = int(table_no)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	sql_string = """INSERT INTO restaurantOrder VALUES 
		        (NULL,%d,'%s')"""%(table_no,status)
	try:
		row = c.execute(sql_string)
		conn.commit()
		conn.close()
		return c.lastrowid
	except:
		conn.close()
		raise SQLExceptions.SQLTableInserionError
	conn.close()
	pass


def changeOrderStatus(order_id,status):

	order_id = int(order_id)
	print order_id
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	found = False
	for a_id in c.execute("""SELECT order_id FROM restaurantOrder
                                     WHERE %d==order_id"""%(order_id)):
		if order_id in a_id:
			found = True
	if found == True:
		#	raise SQLExceptions.SQLTableAlterationError("id not found")
		c.execute("""UPDATE restaurantOrder SET status = '%s' WHERE
				  order_id = order_id """)
		conn.commit()
	else:
		conn.close()
		raise SQLExceptions.SQLTableAlterationError("INVALID ID")
	conn.close()


def addDishToOrder(order_id,dish,quantity,half_portion):
	order_id = int(order_id)
	quantity = int(quantity)
	half_portion = int(half_portion)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	if type(half_portion) == type(True):
		half_portion = int(half_portion)
	try:
		c.execute("""INSERT INTO orderedDishes VALUES(%d,'%s',%d,%d)"""
			  %(order_id,dish,quantity,half_portion))
	except:
		conn.close()
		raise SQLExceptions.SQLTableInserionError
	conn.close()
	pass


def deleteAllDishesFromOrder(order_id):

	order_id = int(order_id)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	c.execute("""DELETE FROM orderedDishes WHERE %d==order_id"""%(order_id))
	##Se requisitado no futuro eu do raise em algo
	conn.close()
	pass







