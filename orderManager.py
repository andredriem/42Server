import sqlite3	
import SQLExceptions





conn = sqlite3.connect('exemple.db')
c = conn.cursor()


#retorna id da nova ordem
def insertOrder(table_no,status):
	sql_string = """INSERT INTO restaurantOrder VALUES 
		        (NULL,%d,'%s')"""%(table_no,status)
	try:
		row = c.execute(sql_string)
		conn.commit()
		return c.lastrowid
	except:
		raise SQLExceptions.SQLTableInserionError
	pass


def changeOrderStatus(order_id,status):
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
		raise SQLExceptions.SQLTableAlterationError("INVALID ID")


def addDishToOrder(order_id,dish,quantity,half_portion):
	if type(half_portion) == type(True):
		half_portion = int(half_portion)
	try:
		c.execute("""INSERT INTO orderedDishes VALUES(%d,'%s',%d,%d)"""
			  %(order_id,dish,quantity,half_portion))
	except:
		raise SQLExceptions.SQLTableInserionError
	pass


def deleteAllDishesFromOrder(order_id):
	c.execute("""DELETE FROM orderedDishes WHERE %d==order_id"""%(order_id))
	##Se requisitado no futuro eu do raise em algo
	pass

		
	

test = insertOrder(2,'ble')
addDishToOrder(test,'hamburger',8000,False)
addDishToOrder(test,'pizza',8001,True)
print test
deleteAllDishesFromOrder(test)


