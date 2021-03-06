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
				  order_id = order_id """%(status))
		conn.commit()
	else:
		conn.close()
		raise SQLExceptions.SQLTableAlterationError("INVALID ID")
	conn.close()


def addDishToOrder(order_id,dish,quantity,half_portion):
	order_id = int(order_id)
	quantity = int(quantity)
	half_portion = int(half_portion)
	print order_id
	print dish
	print quantity
	print half_portion



	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	if type(half_portion) == type(True):
		half_portion = int(half_portion)
	try:
		c.execute("""INSERT INTO orderedDishes VALUES(%d,'%s',%d,%d)"""
			  %(order_id,dish,quantity,half_portion))
		conn.commit()
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
	conn.commit()
	conn.close()
	pass

def getOrder(order_id):
	order_id = int(order_id)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	rows = c.execute ("""SELECT dish_name,quantity,halfportion FROM orderedDishes
			     WHERE order_id == %d"""%(order_id))
	return_string = "{"
	for row in rows:
		return_string = return_string + str(row) + ","
	return_string = return_string[:-1] + '}'
	if '{' not in return_string:
		return_string = '{' + return_string 
	conn.commit()
	conn.close()
	return return_string

def getOrderPrice(order_id):
	order_id = int(order_id)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	rows = c.execute ("""SELECT sum(quantity*price) FROM orderedDishes,menu
			     WHERE order_id == %d and orderedDishes.dish_name == menu.dish_name"""%(order_id))
	return_string = ""
	for row in rows:
		return_string = return_string + str(row) 
	conn.commit()
	conn.close()
	return "["+return_string[1:-2]+"]"


def getOrderInfo(order_id):
	order_id = int(order_id)
	conn = sqlite3.connect('exemple.db')
	c = conn.cursor()
	rows = c.execute("""SELECT * FROM restaurantOrder
                                     WHERE %d==order_id"""%(order_id))
	return_string = ""
	for row in rows:
		return_string+= str(row)
	conn.commit()
	conn.close()
	return ('['+ return_string[1:-1] + ']')






















