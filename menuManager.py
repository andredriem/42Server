import sqlite3
import SQLExceptions
	

conn = sqlite3.connect('exemple.db')
c = conn.cursor()

def getMenu():
# fetch 'em all
	rows = c.execute ("SELECT * FROM Menu")
	return_string = "{"
	for row in rows:
		return_string = return_string + str(row) + ","
	return_string = return_string[:-1] + '}'
	if '{' not in return_string:
		return_string = '{' + return_string 
	conn.commit()
	return return_string   
		 


def insertDish(dish_name, description, gluten, vegan, vegetarian, lactose, 
							type_, discount,price):
	row = c.execute("""INSERT INTO menu VALUES('%s','%s',%d,%d,%d,%d,'%s',%f,%f)"""
		  %(dish_name, description, gluten, vegan, vegetarian, lactose,
							 type_, discount,price))
	conn.commit()
	pass

def deleteDish(dish_name):
	row = c.execute("""DELETE FROM menu WHERE '%s'==dish_name"""
		  %(dish_name))
	conn.commit()


















