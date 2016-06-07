import sqlite3
import SQLExceptions
import unittest
	

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
	found = False
	for a_id in c.execute("""SELECT dish_name FROM menu
                                     WHERE '%s'==dish_name"""%(dish_name)):
		if dish_name in a_id:
			found = True
	if found == True:
		row = c.execute("""DELETE FROM menu WHERE '%s'==dish_name"""
			  %(dish_name))
		conn.commit()
	else:
		raise SQLExceptions.SQLTableDeletionError("Dish was not in table")
	pass

















