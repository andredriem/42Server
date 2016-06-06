import sqlite3	
import SQLExceptions





conn = sqlite3.connect('exemple.db')
c = conn.cursor()

def insertOrder(table_no,status):
	sql_string = """INSERT INTO restaurantOrder VALUES 
		        (NULL,%d,'%s')"""%(table_no,status)
	try:
		c.execute(sql_string)
		conn.commit()
	except:
		raise SQLTableInserionError
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
		raise SQLTableAlterationError("INVALID ID")
		
	

insertOrder(1,'bla')
changeOrderStatus(88,'hue')
