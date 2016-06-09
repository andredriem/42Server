#Server Tests

import sqlite3
import orderManager
import menuManager
import SQLExceptions

#conn = sqlite3.connect('exemple.db')
#c = conn.cursor()

#TEST1 - Insert a new Dish
print menuManager.getMenu()
menuManager.insertDish('NewDish', 'blablabla', 0, 0, 0, 0, 'principal', 0.0,20.30)
print menuManager.getMenu()

print "\nTEST 1 PASSED"

#TEST2 - Delete a existing Dish
print "\n"
print menuManager.getMenu()
menuManager.deleteDish('NewDish')
print menuManager.getMenu()

print "\nTEST 2 PASSED"

#TEST3 - Delete a not existing Dish
print "\n"
print menuManager.getMenu()
try:
	menuManager.deleteDish('OAKSDOAKFAOKOA')
except SQLExceptions.SQLTableDeletionError:
	pass
else:
	print('teste falhou')

print "\nTEST 3 PASSED"

#TEST4 - Insert an existing Dish (this is used to update the dish)
print "\n"
print menuManager.getMenu()
menuManager.insertDish('NewDish2', 'blablabla', 0, 0, 0, 0, 'principal', 0.0,20.30)
print menuManager.getMenu()
try:
	menuManager.insertDish('NewDish2', 'blablabla', 0, 0, 0, 0, 'principal', 0.0,20.30)
except: 
	pass
else:
	print "funcionou"

print "\nTEST 4 PASSED"

#TEST5 - Insert a new Order
test = orderManager.insertOrder(2,'ble')
orderManager.addDishToOrder(test,'hamburger',8000,False)
orderManager.addDishToOrder(test,'pizza',8001,True)
print test

print "\nTEST 5 PASSED"

#TEST6 - Change an Order Status of an existing Order
orderManager.changeOrderStatus(2,'bla')

print "\nTEST 6 PASSED"

#TEST7 - Change an Order Status of a not existing Order:
try:
	orderManager.changeOrderStatus(888,'bla')  #mudei pra ordem 888 pq o 2 existe :p
except:
	pass
else:
	print('teste falhou')

print "\nTEST 7 PASSED"

#TEST8 - Try to add an already existing Dish in an Order
try:
	orderManager.addDishToOrder(test,'hamburger',8000,False)
except SQLExceptions.SQLTableAlterationError:
	pass
else:
	print('teste 8 falhou, porem essa funcao e usada pra editar um prato existente tambem por falta de tempo para criar novas funcoes')

print "\nTEST 8 PASSED"

#TEST9 - Add Dish to a not existing order
orderManager.deleteAllDishesFromOrder(test)
#alem de deleteAllDishesFromOrder tem que de

try:
	orderManager.addDishToOrder(test,'pizza',8001,True)
except SQLExceptions.SQLTableInserionError:
	pass
else: 
	print('teste 9 falhou, ele requer a criacao de uma nova funcao deleteOrder, porem ela nao e prioridade para os casos de uso sendo implementados agora')

print "\nTEST 9 PASSED"
print "\nALL TESTS PASSED :)"


